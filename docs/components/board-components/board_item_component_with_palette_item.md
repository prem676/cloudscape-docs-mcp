---
title: "Board item - Cloudscape Design System"
source: "https://cloudscape.design/components/board-item/?tabId=playground&example=palette-item"
author:
published:
created: 2025-10-01
description: "A board item is a self-contained user interface (UI) element living within a board."
---
- [Playground](https://cloudscape.design/components/board-item/?tabId=playground)
- [API](https://cloudscape.design/components/board-item/?tabId=api)
- [Testing](https://cloudscape.design/components/board-item/?tabId=testing)
- [Usage](https://cloudscape.design/components/board-item/?tabId=usage)

## Configurator

### Configuration

#### Wrapper (playground)

Use React and JSX syntax only. Use <BoardItem /> to render the BoardItem component with properties and slots from above injected.

## Preview

This example is static. Resizing and moving the item does not work in this preview. You can see it in action on the [configurable dashboard demo](https://cloudscape.design/examples/react/configurable-dashboard.html).

Palette item description

Drag handle Use Space or Enter to activate drag, arrow keys to move, Space or Enter to submit, or Escape to discard. Be sure to temporarily disable any screen reader navigation feature that may interfere with the functionality of the arrow keys.Resize handle Use Space or Enter to activate resize, arrow keys to move, Space or Enter to submit, or Escape to discard. Be sure to temporarily disable any screen reader navigation feature that may interfere with the functionality of the arrow keys.

## Code

```jsx
import * as React from "react";
import BoardItem from "@cloudscape-design/board-components/board-item";
import ItemsPalette from "@cloudscape-design/board-components/items-palette";

export default () => {
  return (
    <ItemsPalette
      items={[{ id: "1", data: {} }]}
      renderItem={() => (
        <BoardItem
          i18nStrings={{
            dragHandleAriaLabel: "Drag handle",
            dragHandleAriaDescription:
            resizeHandleAriaLabel: "Resize handle",
            resizeHandleAriaDescription:
          }}
        >
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 10
            }}
          >
            <img
              src="/preview-cube.svg"
              alt="cube icon"
            />
            <p>Palette item description</p>
          </div>
        </BoardItem>
      )}
      i18nStrings={{
        navigationAriaDescription:
          "Click on an item to move focus over",
        liveAnnouncementDndStarted: "Dragging",
        liveAnnouncementDndDiscarded:
          "Insertion discarded"
      }}
    />
  );
}
```
