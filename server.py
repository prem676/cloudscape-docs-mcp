"""
MCP Server for Cloudscape Design System Documentation.

Designed for high token efficiency and agentic workflows.
"""

import re
from pathlib import Path
from typing import Any

import lancedb
import torch
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
from loguru import logger

# --- Configuration ---
DB_URI = Path("./data/lancedb")
MODEL_NAME = "Alibaba-NLP/gte-multilingual-base"
DOCS_ROOT = Path("docs")  # Used for path validation
MAX_UNIQUE_RESULTS = 5

# --- Initialize Server ---
mcp = FastMCP(
    "CloudscapeDocs",
    dependencies=["lancedb", "sentence-transformers", "torch"],
)

# --- Global Resources (Lazy Loaded) ---
_db: Any = None
_model: Any = None
_table: Any = None


def _determine_device() -> str:
    """Check for MPS (Apple Silicon) or CUDA support."""
    if torch.backends.mps.is_available():
        logger.debug("MPS is available")
        return "mps"
    if torch.cuda.is_available():
        logger.debug("CUDA is available")
        return "cuda"
    logger.debug("CPU is available")
    return "cpu"


def get_resources():
    """Lazy initialization of DB and Model."""
    global _db, _model, _table  # noqa: PLW0603

    if _table is None:
        device = _determine_device()
        logger.debug(f"Initializing LanceDB and Embedding Model on {device.upper()}...")

        _db = lancedb.connect(DB_URI)
        _table = _db.open_table("docs")

        # Load model with Mac-optimized settings (float16)
        _model = SentenceTransformer(
            MODEL_NAME,
            device=device,
            model_kwargs={"torch_dtype": torch.float16},
            trust_remote_code=True,
        )

    return _table, _model


def _extract_title(content: str, filename: str) -> str:
    """
    Extract YAML frontmatter title from a chunk.

    Falls back to the filename if not found.
    """
    # Regex to find 'title: "Something"' inside --- blocks
    match = re.search(r'title:\s*"([^"]+)"', content)
    if match:
        return match.group(1)

    # Fallback: Clean up filename (e.g., "collection_preferences.md" -> "Collection Preferences")
    return filename.replace(".md", "").replace("_", " ").title()


@mcp.tool()
def cloudscape_search_docs(query: str) -> str:
    """
    Search the Cloudscape documentation index for relevant files.

    Use this tool FIRST to find the correct file paths.
    It returns a list of files with their relevance scores.
    It does NOT return the full content.

    Args:
        query: The search term (e.g., "collection preferences", "table sorting props").

    Returns:
        A concise list of relevant files and their paths.

    """
    table, model = get_resources()

    query_vec = model.encode(
        query,
        normalize_embeddings=True,
    ).tolist()

    # Fetch more candidates than we need to allow for deduplication
    # (Because one file might have 10 matching chunks)
    candidates = table.search(query_vec).limit(25).to_list()

    if not candidates:
        return "No relevant documentation found."

    # Deduplicate results by file path
    seen_paths = set()
    unique_results = []

    for r in candidates:
        path = r["path"]
        if path not in seen_paths:
            seen_paths.add(path)

            # Extract a friendly title from content or filename
            title = _extract_title(r["content"], r["filename"])

            unique_results.append(
                {
                    "title": title,
                    "path": path,
                    "filename": r["filename"],
                    "score": r.get(
                        "_distance",
                        0.0,
                    ),  # Lower distance = better match usually, or similarity
                },
            )

            # Stop after MAX_UNIQUE_RESULTS to save tokens
            if len(unique_results) >= MAX_UNIQUE_RESULTS:
                break

    # Format output as a concise list for the agent
    output = ["Found the following relevant documentation files:\n"]

    for i, res in enumerate(unique_results, 1):
        output.append(f"{i}. [Title: {res['title']}]\n   Path: {res['path']}\n")

    output.append("\nUse 'cloudscape_read' with a specific 'Path' to view content.")

    return "\n".join(output)


@mcp.tool()
def cloudscape_read_doc(file_path: str) -> str:
    """
    Read the FULL content of a documentation file.

    Use this tool SECOND, after finding the correct path via 'cloudscape_search_docs'.

    Args:
        file_path: The exact path provided by the search tool (e.g., "docs/components/button.md").

    """
    target_path = Path(file_path)

    # 1. Security Check: Block directory traversal
    # Ensure the path contains no ".." and is relative to our current execution or docs folder
    try:
        # Resolve to absolute path
        abs_path = target_path.resolve()
        # Verify it exists
        if not abs_path.exists():
            return f"Error: File not found at {file_path}. Please check the path."

        # Optional: Check if it's within expected directory (if you want strict confinement)
        # root = Path.cwd().resolve()
        # if root not in abs_path.parents:
        #     return "Error: Access denied. Path is outside allowed directories."

    except OSError as e:
        return f"Error validating path: {e!s}"

    if not target_path.is_file():
        return f"Error: {file_path} is not a file."

    try:
        content = target_path.read_text(encoding="utf-8")
    except OSError as e:
        return f"Error reading file: {e!s}"
    else:
        return (
            f"--- BEGIN FILE: {file_path} ---\n{content}\n--- END FILE: {file_path} ---"
        )


if __name__ == "__main__":
    # Resources are lazy-loaded on first tool call to avoid startup timeout
    mcp.run()
