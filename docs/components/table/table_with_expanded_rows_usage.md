---
title: "Table with expandable rows - Cloudscape Design System"
source: "https://cloudscape.design/patterns/resource-management/view/table-with-expandable-rows/"
created: 2025-10-16
description: "Use a table with expandable rows when a data set has multiple levels of hierarchy."
---
### Hierarchical data


One way to visualize hierarchical resources is in a table with expandable rows. Consider using expandable rows when information has multiple levels of hierarchy and it is beneficial to have in-page context for comparing and viewing multiple items at once. See the [expandable rows feature](https://cloudscape.design/components/table/?tabId=usage#features) of the table for implementation details.

In cases of extreme nesting, there may be a negative customer impact on performance or legibility. In these cases, consider alternative solutions like a [details page](https://cloudscape.design/patterns/resource-management/details/details-page/), or separating the data into multiple tables.

### Filtering


When filtering on a table with expandable rows, both parent and child rows that match the filter query will be returned. If a row with both children and parents matches the query, its parent rows will be shown, but its siblings (rows on the same level) and children will not be shown. A counter with match results should be added to expandable tables with filters applied. For example, searching for `X` in the table `A B (Y X (1 2 3) Z) C` will return `B (X)`.

### Sorting


Sorting will sort both the parent rows and child rows. For example, in a table with parent rows A B C, where B has child rows Y X Z, sorting by “descending” will update the table to look like this: `A B (Y X Z) C` → `C B (Z Y X) A`. Updating this to “ascending” will result in this: `A B (Y X Z) C` → `A B (X Y Z) C`.

### Selecting


When using a table with multi-selection, the total number of items selected should be displayed in the table header’s resource counter. If actions can be taken on both parent and child rows, show the selection state on all rows. Alternatively, if actions can only be taken on parent rows, disable the selection state on child rows.

When using a table with selection, if selecting and performing an action on the parent will also affect its children, indicate this with a [confirmation modal](https://cloudscape.design/patterns/resource-management/delete/delete-with-simple-confirmation/). For example, “Delete `B` and its child rows `X Y Z`? This action cannot be undone.”

### Pagination


The table’s default pagination will only apply to the parent rows. For example, if the table is set to show 10 rows per page, 10 parent rows will be shown per page regardless of the number of children of the parent row. Use pagination for organizing large datasets into manageable chunks, making it easier to navigate to specific sections. Pagination provides the ability to jump to specific pages making it easier to keep track of where they are, return to a specific section, and provide an accurate representation of the size of the data set.

### Progressive loading

When expanding a parent with many child rows, consider using progressive loading. This will render a set number of rows first, along with a button to load additional rows.

## Building blocks

![Expandable table example, desktop view](https://cloudscape.design/__images/yvlrib0vb3vb/4vkdPN6cage9dvte7p3wXq/bbc463c6467c3d24dff3e843e9eeba2f/automated--example--table-expandable-external-light-desktop.png.png) ![Expandable table example, desktop view](https://cloudscape.design/__images/yvlrib0vb3vb/3RZ5UdrOaOB8hTrQXI1Omo/8936359ac8d144d5b2dd0d4f04a5c857/automated--example--table-expandable-external-dark-desktop.png.png) ![Expandable table example, Mobile view](https://cloudscape.design/__images/yvlrib0vb3vb/5BnGxi5QqpYM7p3zIWTPD1/87a95f33c3f656d2ea9a9478ab9b69ff/automated--example--table-expandable-external-light-mobile.png.png) ![Expandable table example, Mobile view](https://cloudscape.design/__images/yvlrib0vb3vb/yGeMfltE9KjpDHrzzf2h3/c9731c9648ee2b2d11e7ce8d64bdcddc/automated--example--table-expandable-external-dark-mobile.png.png)

#### A. Expand toggle

This toggle marks a row as expandable. Interact with it to expand or collapse the row.

#### B. Collapsed row

A collapsed row does not show any of its children.

#### C. Expanded row

An expanded row shows its children, indicated with an indent.

#### D. Child row

A child row is indented. Child rows can also include an expand toggle, and have children of their own.

#### E. Table

Use the table component for this pattern. See the [table view](https://cloudscape.design/patterns/resource-management/view/table-view/) pattern for more details about tables in general.

#### F. Filtering - optional

Both parent and child rows that match the filter query will be returned. Here, searching for `cluster-c6a5dd09` will return only its parent (`global-57f5713c`) and itself.

#### G. Sorting - optional

Sorting will sort both the parent rows and child rows.

#### H. Selecting - optional

If selecting and performing an action on the parent will also affect its children, indicate this with a [confirmation modal](https://cloudscape.design/patterns/resource-management/delete/delete-with-simple-confirmation/) when taking an action.

## General guidelines

### Don't

- Don’t use a table with expandable rows with extremely large and complex data sets. Instead, consider [details page as a hub](https://cloudscape.design/patterns/resource-management/details/details-page-as-hub/) or separating the data into multiple tables.

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

#### Error text

- Use complete sentences and terminal punctuation.

#### Constraint text

- If there are constraints on the value that users enter into an input field, describe them under the field. Constraints can include password requirements, a URL format for a specific service, or the maximum number of characters that a user can enter into a field.
- Use complete sentences with periods except when listing valid characters, as shown previously. If space is limited, you can use a sentence fragment without a period.
- Keep constraint text brief. Two lines is the limit.

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.
