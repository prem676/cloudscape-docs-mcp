---
title: "Cards - Cloudscape Design System"
source: "https://cloudscape.design/components/cards/?tabId=usage"
created: 2025-10-01
description: "Represents a collection of items."
---
- [Playground](https://cloudscape.design/components/cards/?tabId=playground)
- [Usage](https://cloudscape.design/components/cards/?tabId=usage)

## General guidelines

### Do

- Use icons in cards only to show status. Avoid using other icons in cards where possible.
- Ensure data symmetry. For example, the order of the key-value pairs after the unique identifier and status should match the order of the inputs in the create flow.
- Only use filtering and pagination if there are more than five cards in the collection.
- Use - (hyphen) for any empty values.
- Consider using sticky header in your card collection if users need to take an action on item(s) upon selection.
- Use a sticky header only in card views and table views.
- Always show the total number of items next to the cards collection title.
- Use [header](https://cloudscape.design/components/header/?tabId=playground) component to display additional information, such as item counter, info link, action buttons, or description text.
- Only use selection if the user can take action on the items in the collection.
- Disabled items should not be selected. A user should always be able to deselect an item.
- Always provide information on why inactive items are unselectable. For example: show the status of an item as *Pending.*
- Reset item selection across pagination, sorting, filtering, and page size changes to prevent users from performing actions on items they may not know are selected.
- Store all the card preferences when the user leaves the page and restore them when the user comes back to the same page.
- Always include the number of selected items in the header item counter.
- When used within the [app layout](https://cloudscape.design/components/app-layout/), `full-page` cards must be the first component in the  `content` slot.
- Cards are dedicated to collections only. Use the [container](https://cloudscape.design/components/container/) component with media to present a card-like container with an image.
- Use the [primary link](https://cloudscape.design/components/link/?tabId=playground&example=primary-link)  variant instead of the  [secondary link](https://cloudscape.design/components/link/?tabId=playground) variant in cards to help users distinguish links from other surrounding text content.
- Make sure that the cards per row property includes a single column breakpoint for mobile viewports.

## Features

- #### Variant
	There are two types of cards available:
	- **Default**
		- The default variant renders the cards header within a container.
	- **Full page**
		- This variant takes up the full page. Use for presenting and managing cards on a standalone page. We also suggest enabling the sticky header and using the "awsui-h1-sticky" `variant` of the [header](https://cloudscape.design/components/header/?example=page-header&tabId=api) with this variant, so the title reduces its size on scroll. For further context, see the [card view demo](https://cloudscape.design/examples/react/cards.html) and the [card view](https://cloudscape.design/patterns/resource-management/view/card-view/) pattern.
- #### Header
	The header is an area to place descriptive content and actions applicable to the entire items collection. These can include a title, item counter, and action stripe.
	- **Collection title**
		- The collection title is a short noun phrase describing the contents of the collection.
		- Use the h1 variant of the [header](https://cloudscape.design/components/header/?example=page-header) component to display the title of full page collection in card view.
			- For example: When used as a [full page card view](https://cloudscape.design/examples/react/cards.html).
		- Use the h2 variant of the [header](https://cloudscape.design/components/header/?example=with-info-link-and-counter) component in the container header of the default cards variant.
	- **Item counter**
		- The item counter is a number next to the title that shows the total number of items in a collection, in parentheses.
			- For example: *(150)*
		- If the total number of items is unknown, include a plus sign (+) after the known number, indicating that more items exist.
		- If the table is in loading state, don't display the item counter.
		- The number of selected items are listed before number of total items, using a forward slash (/) to separate the two values. Use the format: (\[number of selected items\]/\[number of total items\])
			- For example: *(1/150)*
		- The counter slot in the header component is designed to provide counter functionality in this component.
- #### Sticky header - optional
	A sticky header keeps the collection header and features at the top of the page when a user scrolls down the page. Enabling this property lets users perform actions in context, such as using the action stripe, selecting items, filtering, and using pagination. Use the [awsui-h1-sticky](https://cloudscape.design/components/header/?example=with-info-link-and-counter&tabId=api) header variant when the full page cards header is set to sticky. The title size is then automatically reduced on scroll to conserve space.
	If users need to take an action on items upon selection, consider using a sticky header in your card collection.
	Sticky header is not supported on mobile viewport sizes.
- #### Features
	Features are additional attributes that can be added to support more complex collections, such as those with many items. Features include:
	- **Filtering:** Filtering allows users to find a specific item, or a subset of items, using one of three [filtering mechanisms](https://cloudscape.design/patterns/general/filter-patterns/): [text filtering](https://cloudscape.design/components/text-filter/), [collection select filter](https://cloudscape.design/components/collection-select-filter/), or [property filter](https://cloudscape.design/components/property-filter/).
	- **Pagination:**[Pagination](https://cloudscape.design/components/pagination/) allows users to paginate through a collection.
	- **Preferences:**[Preferences](https://cloudscape.design/components/collection-preferences/?tabId=playground&example=cards-preferences) allow users to manage the display of the cards for properties like visible sections and page size.
- #### Cards per row
	Use this property to specify the number of cards per row for any interval of container width. You can set the maximum number of cards in each row for very wide screens. The maximum number of cards per row is 20.
- #### Selection types - optional
	- **None** - default
		- Prevents users from selecting any items from the collection.
	- **Multi**
		- Allows multiple items to be selected at a time, by using checkboxes in each card item.
		- Includes the ability for users to select groups of items by using `shift + click` or `shift + space` to select items between ranges.
		- Use for collections that support bulk actions.
	- **Single**
		- Allows a single item to be selected, by using a radio button in each card item.
		- Use for collections that don't support bulk actions.
	- **Full card selection**
		- Enables the entire card to be selectable when there are no interactive elements within a card. This makes the selection easier by increasing the selection target area. Full card selection can be used with Multi or Single card selection.
- #### Disabled items - optional
	The selection on any item can be inactive. When an item is inactive, a user won't be able to select it.

### States

- #### Loading
	The state of the component while the dataset is being loaded before being displayed. Follow the guidelines for [loading states](https://cloudscape.design/patterns/general/loading-and-refreshing/) in table and cards.
- #### No match
	The state of the collection of items after a user applies a filter that doesn’t return any results. Follow the guidelines for [empty states](https://cloudscape.design/patterns/general/empty-states/) zero results.
- #### Empty
	The state of the component when there are no items to display. Follow the guidelines for [empty states](https://cloudscape.design/patterns/general/empty-states/) in table and cards.

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
	- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
	- For example: use *choose* or *select* not *click*.

### Component-specific guidelines

#### Cards title

- Use nouns to describe what the table contains.
	- For example: *Resources* or *Distributions*

#### Cards description

- Follow the writing guidelines for [table description](https://cloudscape.design/components/table/?tabId=usage#writing-guidelines).

#### Item counter

- When no items are selected, use the format: *(\[number of items in the collection\])*
	- For example: *(340)*
- If the total number of items is unknown and you only know a subset, use the format: *(\[number of known items in the collection\]+)*
	- For example: *(1000+)*
- When at least one item is selected, use the format: *(\[number of selected items\]/\[number of total items\])*
	- For example: *(1* / *500)*

#### Loading state

- When the table is in a loading state, make sure to add a loading text as well.
- Follow the guidelines for [loading and refreshing](https://cloudscape.design/patterns/general/loading-and-refreshing/).

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

