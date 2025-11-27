"""
Ingestion script for Cloudscape documentation.

Indexes Markdown and TSX files into a local LanceDB instance using semantic vectors.
Uses 'rich' for UI and Python 3.13 features.
"""

import logging
import sys
from pathlib import Path
from typing import Any

import lancedb
import torch
from lancedb.pydantic import LanceModel, Vector
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
)
from sentence_transformers import SentenceTransformer

# --- Configuration ---
DOCS_DIR = Path("./docs")
DB_URI = Path("./data/lancedb")
MODEL_NAME = "Alibaba-NLP/gte-multilingual-base"
VECTOR_DIM = 768
EXTENSIONS = {".md", ".txt", ".tsx", ".ts"}

# --- Setup Rich Console & Logging ---
console = Console()
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)],
)
logger = logging.getLogger("ingest")


# --- Database Schema ---
class DocChunk(LanceModel):
    """Database schema definition for a documentation chunk."""

    path: str
    filename: str
    content: str
    vector: Vector(VECTOR_DIM)  # type: ignore[assignment]


def get_file_list(root: Path, extensions: set[str]) -> list[Path]:
    """Scan directory using Python 3.12+ Path.walk and return a list of files."""
    file_list = []
    try:
        for root_dir, _, files in root.walk():
            for file in files:
                file_path = root_dir / file
                if file_path.suffix in extensions:
                    file_list.append(file_path)
    except OSError:
        logger.exception("Error accessing directory %s", root)
        sys.exit(1)
    return file_list


def chunk_content(text: str, max_chars: int = 2000) -> list[str]:
    """Split text into chunks ~2000 characters long, preserving paragraph integrity."""
    raw_chunks = text.split("\n\n")
    merged_chunks = []
    current_chunk = []
    current_len = 0

    for chunk in raw_chunks:
        chunk_len = len(chunk)
        if current_len + chunk_len > max_chars and current_chunk:
            merged_chunks.append("\n\n".join(current_chunk))
            current_chunk = []
            current_len = 0

        current_chunk.append(chunk)
        current_len += chunk_len

    if current_chunk:
        merged_chunks.append("\n\n".join(current_chunk))

    return merged_chunks


def _gather_files() -> list[Path]:
    """Gather files from documentation directory."""
    with console.status("[bold green]Scanning files...", spinner="dots"):
        files = get_file_list(DOCS_DIR, EXTENSIONS)
        if not files:
            logger.error("No documentation files found in %s", DOCS_DIR)
            sys.exit(1)
        console.print(f"[green]✓[/green] Found {len(files)} files to process.")
    return files


def _determine_device() -> str:
    """Check for MPS (Apple Silicon) support."""
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def _load_resources() -> tuple[SentenceTransformer, Any]:
    """Load embedding model and database."""
    device = _determine_device()

    try:
        with console.status(
            f"[bold green]Loading {MODEL_NAME} on {device.upper()}...",
            spinner="bouncingBall",
        ):
            # Mac Optimization Notes:
            # 1. We removed 'flash_attention_2' (CUDA only).
            # 2. We removed 'device_map'. We pass 'device' directly to SentenceTransformer.
            # 3. Using float16 for faster inference on MPS.

            model = SentenceTransformer(
                MODEL_NAME,
                device=device,
                model_kwargs={"torch_dtype": torch.float16},
                trust_remote_code=True,
            )

            # Explicitly compile the model for potentially faster inference on Mac
            # (Optional, sometimes speeds up slightly on M-series chips)
            # if device == "mps":
            #     model = torch.compile(model)

            db = lancedb.connect(DB_URI)
            table = db.create_table("docs", schema=DocChunk, mode="overwrite")

    except (OSError, RuntimeError) as e:
        logger.critical("Failed to initialize resources: %s", e)
        sys.exit(1)
    else:
        console.print(f"[green]✓[/green] Model loaded & Database connected at {DB_URI}")
        return model, table


def _process_files(
    files: list[Path],
    model: SentenceTransformer,
) -> tuple[list[DocChunk], int]:
    """Process files and generate embeddings."""
    data_buffer: list[DocChunk] = []
    failed_files = 0

    progress_layout = [
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeRemainingColumn(),
    ]

    with Progress(*progress_layout, console=console) as progress:
        task = progress.add_task("[cyan]Indexing documents...", total=len(files))

        for file_path in files:
            try:
                content = file_path.read_text(encoding="utf-8")
                chunks = chunk_content(content)

                for chunk_text in chunks:
                    if not chunk_text.strip():
                        continue

                    # show_progress_bar=False disables the internal tqdm of SentenceTransformer
                    vec = model.encode(
                        chunk_text,
                        normalize_embeddings=True,
                        show_progress_bar=False,
                    ).tolist()

                    data_buffer.append(
                        DocChunk(
                            path=str(file_path),
                            filename=file_path.name,
                            content=chunk_text,
                            vector=vec,
                        ),
                    )

            except UnicodeDecodeError:
                logger.warning("Skipping binary file: %s", file_path.name)
                failed_files += 1
            except OSError:
                logger.exception("Failed to process %s", file_path.name)
                failed_files += 1
            finally:
                progress.advance(task)

    return data_buffer, failed_files


def _write_to_database(table: Any, data_buffer: list[DocChunk]) -> None:
    """Write processed chunks to database."""
    if data_buffer:
        with console.status(
            f"[bold green]Writing {len(data_buffer)} chunks to disk...",
            spinner="dots",
        ):
            try:
                table.add(data_buffer)
                console.print(
                    f"[green]✓[/green] Successfully indexed {len(data_buffer)} chunks.",
                )
            except (OSError, RuntimeError) as e:
                logger.critical("Failed to write to database: %s", e)
                sys.exit(1)
    else:
        logger.warning("No valid chunks found to index.")


def _print_summary(failed_files: int) -> None:
    """Print final summary."""
    console.rule("[bold blue]Done[/bold blue]")
    if failed_files > 0:
        console.print(
            f"[bold red]Warning:[/bold red] {failed_files} files could not be processed.",
        )
    console.print("Ready to serve.")


def main() -> None:
    console.rule("[bold blue]Cloudscape Docs Ingestion[/bold blue]")
    files = _gather_files()
    model, table = _load_resources()
    data_buffer, failed_files = _process_files(files, model)
    _write_to_database(table, data_buffer)
    _print_summary(failed_files)


if __name__ == "__main__":
    main()
