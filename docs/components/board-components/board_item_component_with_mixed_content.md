---
title: "Board item - Cloudscape Design System"
source: "https://cloudscape.design/components/board-item/?tabId=playground&example=with-mixed-content"
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

## Code

```jsx
import * as React from "react";
import BoardItem from "@cloudscape-design/board-components/board-item";
import FormField from "@cloudscape-design/components/form-field";
import Select from "@cloudscape-design/components/select";
import ColumnLayout from "@cloudscape-design/components/column-layout";
import SpaceBetween from "@cloudscape-design/components/space-between";
import KeyValuePairs from "@cloudscape-design/components/key-value-pairs";
import StatusIndicator from "@cloudscape-design/components/status-indicator";
import BarChart from "@cloudscape-design/components/bar-chart";
import Box from "@cloudscape-design/components/box";
import Link from "@cloudscape-design/components/link";
import ButtonDropdown from "@cloudscape-design/components/button-dropdown";
import Board from "@cloudscape-design/board-components/board";

export default () => {
  return (
    <Board
      items={[
        { id: "1", rowSpan: 5, columnSpan: 4, data: {} }
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
          header={
            <Header>
              Board item with mixed content types
            </Header>
          }
          settings={
            <ButtonDropdown
              items={[{ id: "remove", text: "Remove" }]}
              ariaLabel="Board item settings"
              variant="icon"
            />
          }
        >
          <div style={{ maxWidth: 280 }}>
            <FormField label="Filter displayed data">
              <Select
                selectedOption={{ value: "October 2025" }}
                empty="Not supported in this demo"
              />
            </FormField>
          </div>
          <ColumnLayout columns={2} variant="text-grid">
            <div>
              <SpaceBetween size="s">
                <KeyValuePairs
                  columns={1}
                  items={[
                    {
                      label: "Status",
                      value: (
                        <StatusIndicator type="success">
                          Service is operating normally
                        </StatusIndicator>
                      )
                    },
                    {
                      label: "Enabled Regions",
                      value: "10"
                    },
                    {
                      label: "Instances",
                      value: "18 in 10 regions"
                    },
                    {
                      label: "Security groups",
                      value: "11 in 10 regions"
                    },
                    {
                      label: "Volumes",
                      value: "34 in 10 regions"
                    }
                  ]}
                />
              </SpaceBetween>
            </div>
            <div>
              <BarChart
                hideFilter={true}
                hideLegend={true}
                xScaleType="categorical"
                xTitle="Chars"
                yTitle="Numbers"
                series={[
                  {
                    type: "bar",
                    title: "Value",
                    data: [
                      { x: "A", y: 170.25 },
                      { x: "B", y: 116.07 },
                      { x: "C", y: 54.19 },
                      { x: "D", y: 15.18 },
                      { x: "E", y: 15.03 },
                      { x: "F", y: 49.85 }
                    ]
                  }
                ]}
                height={230}
              />
            </div>
          </ColumnLayout>
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
