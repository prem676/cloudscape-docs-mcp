---
title: "Board item - Cloudscape Design System"
source: "https://cloudscape.design/components/board-item/?tabId=playground&example=with-table"
author:
published:
created: 2025-10-01
description: "A board item is a self-contained user interface (UI) element living within a board."
tags:
  - "clippings"
---
- [Playground](https://cloudscape.design/components/board-item/?tabId=playground)
- [API](https://cloudscape.design/components/board-item/?tabId=api)
- [Testing](https://cloudscape.design/components/board-item/?tabId=testing)
- [Usage](https://cloudscape.design/components/board-item/?tabId=usage)

## Configurator

## Code

```jsx
import * as React from "react";
import BoardItem from "@cloudscape-design/board-components/board-item";
import Table from "@cloudscape-design/components/table";
import Link from "@cloudscape-design/components/link";
import StatusIndicator from "@cloudscape-design/components/status-indicator";
import Box from "@cloudscape-design/components/box";
import ButtonDropdown from "@cloudscape-design/components/button-dropdown";
import Board from "@cloudscape-design/board-components/board";

export default () => {
  return (
    <Board
      items={[
        { id: "1", rowSpan: 4, columnSpan: 4, data: {} }
      ]}
      renderItem={() => (
        <BoardItem
          i18nStrings={{
            dragHandleAriaLabel: "Drag handle",
            dragHandleAriaDescription:
            resizeHandleAriaLabel: "Resize handle",
            resizeHandleAriaDescription:
          }}
          footer={
            <Box textAlign="center">
              <Link>View all</Link>
            </Box>
          }
          settings={
            <ButtonDropdown
              items={[
                {
                  id: "preferences",
                  text: "Preferences"
                },
                { id: "remove", text: "Remove" }
              ]}
              ariaLabel="Board item settings"
              variant="icon"
            />
          }
        >
          <div style={{ overflow: "hidden" }}>
            <Table
              variant="embedded"
              columnDefinitions={[
                {
                  cell: item => (
                    <Link href="#">{item.id}</Link>
                  )
                },
                {
                  cell: item => (
                    <StatusIndicator
                      type={item.status.toLowerCase()}
                    >
                      {item.status}
                    </StatusIndicator>
                  )
                }
              ]}
              items={[
                {
                  id:
                    "6f80c977-ca20-4563-8007-6387581f9a34",
                  status: "Success"
                },
                {
                  id:
                    "4345032a-e270-4e6f-a187-60bf7ddd4ba3",
                  status: "Success"
                },
                {
                  id:
                    "54dc6682-26d0-4c70-a42a-1772d443dd0d",
                  status: "Success"
                },
                {
                  id:
                    "bcd939ad-2203-4585-8e93-d944632872ef",
                  status: "Error"
                },
                {
                  id:
                    "244d0a59-c18d-4c18-90c2-deba14535d51",
                  status: "Success"
                },
                {
                  id:
                    "bcd939ad-2203-4585-8e93-d944632872ef",
                  status: "Pending"
                }
              ]}
            />
          </div>
        </BoardItem>
      )}
      i18nStrings={(() => {
        function createAnnouncement(
          operationAnnouncement,
          conflicts,
          disturbed
        ) {
          const conflictsAnnouncement =
            conflicts.length > 0
              ? \`Conflicts with ${conflicts
                  .map(c => c.data.title)
                  .join(", ")}.\`
              : "";
          const disturbedAnnouncement =
            disturbed.length > 0
              ? \`Disturbed ${disturbed.length} items.\`
              : "";
          return [
            operationAnnouncement,
            conflictsAnnouncement,
            disturbedAnnouncement
          ]
            .filter(Boolean)
            .join(" ");
        }
        return {
          liveAnnouncementDndStarted: operationType =>
            operationType === "resize"
              ? "Resizing"
              : "Dragging",
          liveAnnouncementDndItemReordered: operation => {
            const columns = \`column ${operation.placement
              .x + 1}\`;
            const rows = \`row ${operation.placement.y +
              1}\`;
            return createAnnouncement(
              \`Item moved to ${
                operation.direction === "horizontal"
                  ? columns
                  : rows
              }.\`,
              operation.conflicts,
              operation.disturbed
            );
          },
          liveAnnouncementDndItemResized: operation => {
            const columnsConstraint = operation.isMinimalColumnsReached
              ? " (minimal)"
              : "";
            const rowsConstraint = operation.isMinimalRowsReached
              ? " (minimal)"
              : "";
            const sizeAnnouncement =
              operation.direction === "horizontal"
                ? \`columns ${operation.placement.width}${columnsConstraint}\`
                : \`rows ${operation.placement.height}${rowsConstraint}\`;
            return createAnnouncement(
              \`Item resized to ${sizeAnnouncement}.\`,
              operation.conflicts,
              operation.disturbed
            );
          },
          liveAnnouncementDndItemInserted: operation => {
            const columns = \`column ${operation.placement
              .x + 1}\`;
            const rows = \`row ${operation.placement.y +
              1}\`;
            return createAnnouncement(
              \`Item inserted to ${columns}, ${rows}.\`,
              operation.conflicts,
              operation.disturbed
            );
          },
          liveAnnouncementDndCommitted: operationType =>
            \`${operationType} committed\`,
          liveAnnouncementDndDiscarded: operationType =>
            \`${operationType} discarded\`,
          liveAnnouncementItemRemoved: op =>
            createAnnouncement(
              \`Removed item ${op.item.data.title}.\`,
              [],
              op.disturbed
            ),
          navigationAriaDescription:
            "Click on non-empty item to move focus over",
            item ? item.data.title : "Empty"
        };
      })()}
      onItemsChange={() => {}}
    />
  );
}
```
