---
title: "Table - Cloudscape Design System"
source: "https://cloudscape.design/components/table/?tabId=playground&example=resizable-columns"
created: 2025-10-01
description: "Presents data in a two-dimensional table format, arranged in columns and rows in a rectangular form."
---
- [Playground](https://cloudscape.design/components/table/?tabId=playground)
- [Usage](https://cloudscape.design/components/table/?tabId=usage)

## Configurator

## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`ariaLabels`.

```jsx
import * as React from "react";
import Table from "@cloudscape-design/components/table";
import Box from "@cloudscape-design/components/box";
import SpaceBetween from "@cloudscape-design/components/space-between";
import Button from "@cloudscape-design/components/button";
import TextFilter from "@cloudscape-design/components/text-filter";
import Pagination from "@cloudscape-design/components/pagination";

export default () => {
  return (
    <Table
      renderAriaLive={({
        firstIndex,
        lastIndex,
        totalItemsCount
      }) =>
        \`Displaying items ${firstIndex} to ${lastIndex} of ${totalItemsCount}\`
      }
      columnDefinitions={[
        {
          id: "variable",
          cell: e => e.name,
          width: 170,
          minWidth: 165,
          sortingField: "name",
        },
        {
          id: "type",
          cell: e => e.type,
          width: 110,
          minWidth: 110,
          sortingField: "type"
        },
        {
          id: "size",
          cell: e => e.size,
          width: 110,
          minWidth: 90
        },
        {
          id: "description",
          cell: e => e.description,
          width: 200,
          minWidth: 170
        }
      ]}
      enableKeyboardNavigation
      items={[
        {
          name: "Item 1",
          alt: "First",
          description: "This is the first item",
          type: "1A",
          size: "Small"
        },
        {
          name: "Item 2",
          alt: "Second",
          description: "This is the second item",
          type: "1B",
          size: "Large"
        },
        {
          name: "Item 3",
          alt: "Third",
          description: "-",
          type: "1A",
          size: "Large"
        },
        {
          name: "Item 4",
          alt: "Fourth",
          description: "This is the fourth item",
          type: "2A",
          size: "Small"
        },
        {
          name: "Item 5",
          alt: "-",
          description:
            "This is the fifth item with a longer description",
          type: "2A",
          size: "Large"
        },
        {
          name: "Item 6",
          alt: "Sixth",
          description: "This is the sixth item",
          type: "1A",
          size: "Small"
        }
      ]}
      loadingText="Loading resources"
      resizableColumns
      selectedItems={[{ name: "Item 2" }]}
      empty={
        <Box
          margin={{ vertical: "xs" }}
          textAlign="center"
          color="inherit"
        >
          <SpaceBetween size="m">
            <b>No resources</b>
            <Button>Create resource</Button>
          </SpaceBetween>
        </Box>
      }
      filter={
        <TextFilter
          filteringPlaceholder="Find resources"
          filteringText=""
          countText="0 matches"
        />
      }
      header={
      }
      pagination={
        <Pagination currentPageIndex={1} pagesCount={1} />
      }
    />
  );
}
```
