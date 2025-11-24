---
title: "Board components - Cloudscape Design System"
source: "https://cloudscape.design/components/board-components/#guidance-on-creating-a-configurable-dashboard"
author:
published:
created: 2025-10-01
description: "Made up of three components that work together to allow users to interact with, move, and configure a board layout."
---
## Related components

### Board

Provides the base for a configurable layout, including drag and drop, responsiveness and grid.

### Board item

A board item is a self-contained user interface (UI) element living within a board.

### Items palette

Provides the ability to add board items to a board layout when combined with discreet split panel.

For information about how to design and build a configurable dashboard experience using board components, see [Service dashboard](https://cloudscape.design/patterns/general/service-dashboard/), [Configurable dashboard](https://cloudscape.design/patterns/general/service-dashboard/configurable-dashboard/) and [Dashboard items](https://cloudscape.design/patterns/general/service-dashboard/dashboard-items/) patterns.

Configurable dashboard pattern consists of three components, [board](https://cloudscape.design/components/board/), [board item](https://cloudscape.design/components/board-item/) and [items palette](https://cloudscape.design/components/items-palette/).

Essentially, this pattern is a board component that contains board items within it. Individual board item components should be used for each content type you want to display on the board. These board item components are configurable (resizable and draggable).

The items palette component provides the ability to add new content types to the board via drag-and-drop. Items palette content should also be featured in the board item component. For the best experience, we recommend using the [split panel](https://cloudscape.design/components/split-panel/) component, in [discreet mode](https://cloudscape.design/components/split-panel/?tabId=usage#features).

For an example of a configurable dashboard built using board items, see [this demo](https://cloudscape.design/examples/react/configurable-dashboard.html).

![How the components work together. Board item inside a board, followed by a item palette inside a discreet split panel](https://cloudscape.design/__images/yvlrib0vb3vb/5eOmNjlJ0hto5bkXSFKltD/0de01d1fdcef5291eb3c8181bbe35885/components--board-components--vr-light.png) ![How the components work together. Board item inside a board, followed by a item palette inside a discreet split panel](https://cloudscape.design/__images/yvlrib0vb3vb/6jrxVQzS1aIM4IMj6hhv9k/c94eecce3b1b947f7d7d89a3941212ac/components--board-components--vr-dark.png)

