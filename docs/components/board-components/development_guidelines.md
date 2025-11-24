---
title: "Board - Cloudscape Design System"
source: "https://cloudscape.design/components/board/?tabId=api"
author:
published:
created: 2025-10-01
description: "Provides the base for a configurable layout, including drag and drop, responsiveness and grid."
---
- [Playground](https://cloudscape.design/components/board/?tabId=playground)
- [API](https://cloudscape.design/components/board/?tabId=api)
- [Testing](https://cloudscape.design/components/board/?tabId=testing)
- [Usage](https://cloudscape.design/components/board/?tabId=usage)

## Development guidelines

This component comes from the new `@cloudscape-design/board-components` NPM module. Make sure to add this module to your dependencies.

#### Usage

This component is a part of configurable dashboards pattern. For more details on the expected usage, see the [pattern article](https://cloudscape.design/patterns/general/service-dashboard/configurable-dashboard/).

#### State management

The board component is controlled. Set the `items` property and the `onItemsChange` listener to store its value in the state of your application. Refer to [state management guidelines](https://cloudscape.design/get-started/dev-guides/state-management/) for components.

It is recommended to persist items layout as a user preference and apply on page reload.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| i18nStrings | ``` BoardProps.I18nStrings<D> {   liveAnnouncementDndCommitted: (     operationType: BoardProps.DndOperationType   ) => string   liveAnnouncementDndDiscarded: (     operationType: BoardProps.DndOperationType   ) => string   liveAnnouncementDndItemInserted: (     operation: BoardProps.DndInsertState<D>   ) => string   liveAnnouncementDndItemReordered: (     operation: BoardProps.DndReorderState<D>   ) => string   liveAnnouncementDndItemResized: (     operation: BoardProps.DndResizeState<D>   ) => string   liveAnnouncementDndStarted: (     operationType: BoardProps.DndOperationType   ) => string   liveAnnouncementItemRemoved: (     operation: BoardProps.ItemRemovedState<D>   ) => string   navigationAriaDescription?: string   navigationAriaLabel: string   navigationItemAriaLabel: (     item: BoardProps.Item<D> \| null   ) => string } ``` | An object containing all the necessary localized strings required by the component.  Live announcements:  - `liveAnnouncementDndStarted(BoardProps.DndOperationType): string` - the function to create a live announcement string to indicate start of DnD ("reorder", "resize" or "insert"). - `liveAnnouncementDndItemReordered(BoardProps.DndReorderState<D>): string` - the function to create a live announcement string to indicate when DnD reorder is performed. - `liveAnnouncementDndItemResized(BoardProps.DndResizeState<D>): string` - the function to create a live announcement string to indicate when DnD resize is performed. - `liveAnnouncementDndItemInserted(BoardProps.DndInsertState<D>): string` - the function to create a live announcement string to indicate when DnD insert is performed. - `liveAnnouncementDndDiscarded(BoardProps.DndOperationType): string` - the function to create a live announcement string to indicate commit of DnD ("reorder", "resize" or "insert"). - `liveAnnouncementDndCommitted(BoardProps.DndOperationType): string` - the function to create a live announcement string to indicate discard of DnD ("reorder", "resize" or "insert"). - `liveAnnouncementItemRemoved(BoardProps.OperationStateRemove<D>): string` - the function to create a live announcement string to indicate when item is removed. | \- | \- | ``` true ``` |
| items | ``` ReadonlyArray<BoardProps.Item<D>> ``` | Specifies the items displayed in the board. Each item includes its position on the board andoptional data. The content of an item is controlled by the `renderItem` property.  The BoardProps.Item includes:  - `id` (string) - the unique item identifier. The IDs of any two items in a page must be different. - `definition.minRowSpan` (number, optional) - the minimal number of rows the item is allowed to take. It can't be less than two. Defaults to two. - `definition.minColumnSpan` (number, optional) - the minimal number of columns the item is allowed to take. It can't be less than one. Defaults to one. - `definition.defaultRowSpan` (number, optional) - the number or rows the item will take when inserted to the board. It can't be less than `definition.minRowSpan`. - `definition.defaultColumnSpan` (number, optional) - the number or columns the item will take when inserted in the board. It can't be less than `definition.minColumnSpan`. - `columnOffset` (mapping, optional) - the item's offset from the first column (per layout) starting from zero. The value is updated by `onItemsChange` after an update is committed. - `rowSpan` (number, optional) - the item's vertical size starting from two. The value is updated by `onItemsChange` after an update is committed. - `columnSpan` (number, optional) - the item's horizontal size starting from one. The value is updated by `onItemsChange` after an update is committed. - `data` (D) - optional item data which can include the specific configurations of an item, such as its title. | \- | \- | ``` true ``` |
| renderItem | ``` (   item: BoardProps.Item<D>,   actions: BoardProps.ItemActions ) => JSX.Element ``` | Specifies a function to render content for board items. The return value must include board item component.  The function takes the item and its associated actions (BoardProps.ItemActions) that include:  - `removeItem(): void` - the callback to issue the item's removal. Once issued, the `onItemsChange` will fire to update the state. | \- | \- | ``` true ``` |

## Slots

| Name | Description |
| --- | --- |
| empty | Rendered when the `items` array is empty.  When items are loading the slot can be used to render the loading indicator. |

## Events

| Name | Detail | Description | Cancelable |
| --- | --- | --- | --- |
| onItemsChange | ``` BoardProps.ItemsChangeDetail<D> {   addedItem?: BoardProps.Item<D>   items: ReadonlyArray<BoardProps.Item<D>>   movedItem?: BoardProps.Item<D>   removedItem?: BoardProps.Item<D>   resizedItem?: BoardProps.Item<D> } ``` | Called when a user modifies the size or position of board items.  The change detail has the following properties:  - `items`: (readonly Item<D>\[\]) - the updated items array. - `addedItem`: (Item<D>, optional) - the item that was added as part of the update, if applicable. - `removedItem`: (Item<D>, optional) - the item that was removed as part of the update, if applicable. - `resizedItem`: (Item<D>, optional) - the item that was resized as part of the update, if applicable. - `movedItem`: (Item<D>, optional) - the item that was moved as part of the update, if applicable. | ``` false ``` |
