---
title: "Collection preferences - Cloudscape Design System"
source: "https://cloudscape.design/components/collection-preferences/?tabId=usage"
created: 2025-11-21
description: "With collection preferences, users can manage their display preferences within a collection."
---
- [Playground](https://cloudscape.design/components/collection-preferences/?tabId=playground)
- [API](https://cloudscape.design/components/collection-preferences/?tabId=api)
- [Testing](https://cloudscape.design/components/collection-preferences/?tabId=testing)
- [Usage](https://cloudscape.design/components/collection-preferences/?tabId=usage)

## General guidelines

### Do

- Ensure data symmetry by aligning the order of visible content options with the order in which corresponding content appears in the collection view.
- Store all the table preferences when the user leaves the page and restore them when the user comes back to the same page.
- Use wrap lines, zebra stripes, content density, sticky columns and column reordering only in [table views](https://cloudscape.design/patterns/resource-management/view/table-view/).

### Don't

- Don't show the *View as* section in the preferences if the data set does not display properly as a card collection.

## Features

- #### Overlay modal
	Collection preferences are placed inside a modal that is invoked by a button.
- #### Page size
	The user can choose how many items are shown per page. You can set the default number of items, based on how much time it takes to load the data. Users can then choose how many items are shown per page.
- #### Column display preferences (table)
	Users can choose which columns to display in a [table view](https://cloudscape.design/patterns/resource-management/view/table-view/).
	- **Column reordering** \- optional
		- The default column order is set up from the input groups order used in the create flow. Users can reorder the columns in the column preferences list to build a customized view. Reordering is performed via [drag-and-drop](https://cloudscape.design/patterns/general/service-dashboard/configurable-dashboard/#drag-and-drop), columns can be moved up or down within the list, and a drop zone indicates the new location of the dragged item.
	- **Text filtering** - optional
		- Recommended when there are more than 12 column values in a table. When enabled, users can filter through the list of columns to more quickly access the ability to toggle individual items on or off. Note: Drag and drop to reorder is unavailable while actively filtering.
- #### Visible content preferences (cards)
	Users can choose which content to display in a [card view](https://cloudscape.design/patterns/resource-management/view/card-view/).
	The default is to show all the main properties, and hide the secondary properties. The main properties come from the input groups used in the create flow in the primary section. The secondary properties come from the inputs in the create flow, in the additional configuration expanding section.
- #### Wrap lines
	Users can choose to have long text in table cells displayed on one line and truncated, or fully displayed in multiple lines. The default is to truncate.
- #### View as - optional
	Users can choose to display the collection in different formats. For example: [table view](https://cloudscape.design/patterns/resource-management/view/table-view/) or [card view](https://cloudscape.design/patterns/resource-management/view/card-view/).
- #### Striped rows - optional
	Striped rows add a background color to alternating table rows to assist in tracking data across a row.
- #### Sticky columns - optional
	Allows users to turn on and off sticky columns. When selected, the columns are stuck to the edge of the table when users scroll horizontally. Options include:
	- **First column(s)** \- Sticks the first one or two visible columns to the left of the table. For example, to reference a unique identifier when scrolling horizontally is important to users.
	- **Last column** \- Sticks the last visible column to the right of the table. For example, if the last column of the table includes summary content such as totals cost of a bill or to persist in-context actions in view.
- #### Content density (compact mode) - optional
	When checked, it toggles the table’s `contentDensity` property to display the data in a denser, more compact mode.
- #### Preference details - optional
	An area at the top of the modal which can be used to display additional information relating to the preferences. For example, use this to display how the collection preferences are stored or to notify users if their preferences cannot be stored.

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
	- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
	- For example: use *choose* or *select* not *click*.

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### Alternative text

- The alternative text for the trigger button is automatically set to match the modal title.
	- For example: *Preferences*
