---
title: "Pagination - Cloudscape Design System"
source: "https://cloudscape.design/components/pagination/?tabId=usage"
created: 2025-10-01
description: "Provides horizontal navigation between pages of a collection."
---
- [Playground](https://cloudscape.design/components/pagination/?tabId=playground)
- [Usage](https://cloudscape.design/components/pagination/?tabId=usage)

## General guidelines

## Features

- #### Basic controls

 Pagination includes several mechanisms to move between pages:
 **Left arrow**

- Navigates backward one page.
- Inactive when the first page is selected.
 **Numbers**
- Redirect directly to a certain collection page.
- The number of pages changes based on the filter results.
 **Right arrow**
- Navigates forward one page.
- Inactive when the last page is selected.
 **Ellipsis**
- Ellipsis is included at the end of the pagination element when the total amount of items is unknown (see *Open end pagination*).

- #### Open end pagination

 Open end pagination is a pagination variant for cases when it’s impossible to determine the full size of the data set. This can happen when, for example, the API does not return the total number of items, or it’s not paginated. The open end variant always displays ellipsis before the next page icon. The next button is always active so that users can load the next page of items.

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### Alternative text

- Define labels for the pagination buttons through the `labels` property according to the alternative text guidelines.
- When using multiple `Pagination` on a page, define `paginationLabel` to help users with context setting.
- State where the icon takes the user to.
- For example: Previous page or even page numbers (such as *Page 6*) rather than *left* or *right*.
