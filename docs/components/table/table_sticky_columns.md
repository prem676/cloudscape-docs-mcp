---
title: "Table - Cloudscape Design System"
source: "https://cloudscape.design/components/table/?tabId=playground&example=sticky-columns"
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
import CollectionPreferences from "@cloudscape-design/components/collection-preferences";

export default () => {
  const [
    selectedItems,
    setSelectedItems
  ] = React.useState([{ name: "Item 2" }]);
  return (
    <Table
      renderAriaLive={({
        firstIndex,
        lastIndex,
        totalItemsCount
      }) =>
        \`Displaying items ${firstIndex} to ${lastIndex} of ${totalItemsCount}\`
      }
      onSelectionChange={({ detail }) =>
        setSelectedItems(detail.selectedItems)
      }
      selectedItems={selectedItems}
      ariaLabels={{
        selectionGroupLabel: "Items selection",
        allItemsSelectionLabel: () => "select all",
        itemSelectionLabel: ({ selectedItems }, item) =>
          item.name
      }}
      columnDefinitions={[
        {
          id: "variable",
          cell: e => e.name,
          sortingField: "name",
        },
        {
          id: "value",
          cell: e => e.alt,
          sortingField: "alt"
        },
        {
          id: "description",
          cell: e => e.description
        },
        {
          id: "description-2",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-3",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-4",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-5",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-6",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-7",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-8",
          cell: e => e.description || "-",
          width: 200
        },
        {
          id: "description-9",
          cell: e => e.description || "-",
          width: 200
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
      selectionType="multi"
      stickyColumns={{ first: 1, last: 0 }}
      trackBy="name"
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
      pagination={
        <Pagination currentPageIndex={1} pagesCount={1} />
      }
      preferences={
        <CollectionPreferences
          title="Preferences"
          confirmLabel="Confirm"
          cancelLabel="Cancel"
          preferences={{
            pageSize: 10,
            contentDisplay: [
              { id: "variable", visible: true },
              { id: "value", visible: true },
              { id: "type", visible: true },
              { id: "description", visible: true }
            ]
          }}
          pageSizePreference={{
            title: "Page size",
            options: [
              { value: 10, label: "10 resources" },
              { value: 20, label: "20 resources" }
            ]
          }}
          wrapLinesPreference={{}}
          stripedRowsPreference={{}}
          contentDensityPreference={{}}
          contentDisplayPreference={{
            options: [
              {
                id: "variable",
                label: "Variable name",
                alwaysVisible: true
              },
              { id: "value", label: "Text value" },
              { id: "type", label: "Type" },
              { id: "description", label: "Description" }
            ]
          }}
          stickyColumnsPreference={{
            firstColumns: {
              title: "Stick first column(s)",
              description:
                "Keep the first column(s) visible while horizontally scrolling the table content.",
              options: [
                { label: "None", value: 0 },
                { label: "First column", value: 1 },
                { label: "First two columns", value: 2 }
              ]
            },
            lastColumns: {
              title: "Stick last column",
              description:
                "Keep the last column visible while horizontally scrolling the table content.",
              options: [
                { label: "None", value: 0 },
                { label: "Last column", value: 1 }
              ]
            }
          }}
        />
      }
    />
  );
}
```

