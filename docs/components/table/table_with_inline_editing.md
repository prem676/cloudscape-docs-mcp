---
title: "Table - Cloudscape Design System"
source: "https://cloudscape.design/components/table/?tabId=playground&example=with-inline-editing"
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
      ariaLabels={{
        activateEditLabel: (column, item) =>
        cancelEditLabel: column =>
        submitEditLabel: column =>
        tableLabel: "Table with inline editing"
      }}
      columnDefinitions={[
        {
          id: "variable",
          minWidth: 176,
          cell: item => {
            return item.name;
          },
          editConfig: {
            ariaLabel: "Name",
            editIconAriaLabel: "editable",
            errorIconAriaLabel: "Name Error",
            editingCell: (
              item,
              { currentValue, setValue }
            ) => {
              return (
                <Input
                  autoFocus={true}
                  value={currentValue ?? item.name}
                  onChange={event =>
                    setValue(event.detail.value)
                  }
                />
              );
            },
            disabledReason: item => {
              if (item.type === "1A") {
                return "You cannot change the name of Type 1A variables.";
              }
              return undefined;
            }
          }
        },
        {
          id: "type",
          minWidth: 176,
          editConfig: {
            ariaLabel: "Type",
            editIconAriaLabel: "editable",
            editingCell: (
              item,
              { currentValue, setValue }
            ) => {
              const value = currentValue ?? item.type;
              return (
                <Select
                  autoFocus={true}
                  expandToViewport={true}
                  selectedOption={
                    [
                      { label: "1A", value: "1A" },
                      { label: "1B", value: "1B" },
                      { label: "2A", value: "2A" },
                      { label: "2B", value: "2B" }
                    ].find(
                      option => option.value === value
                    ) ?? null
                  }
                  onChange={event => {
                    setValue(
                      event.detail.selectedOption.value ??
                        item.type
                    );
                  }}
                  options={[
                    { label: "1A", value: "1A" },
                    { label: "1B", value: "1B" },
                    { label: "2A", value: "2A" },
                    { label: "2B", value: "2B" }
                  ]}
                />
              );
            }
          },
          cell: item => {
            return item.type;
          }
        },
        {
          id: "description",
          cell: e => e.description
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
      submitEdit={async () => {
        await new Promise(e => setTimeout(e, 1e3));
      }}
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
    />
  );
}
```

