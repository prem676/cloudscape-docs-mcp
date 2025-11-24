---
title: "Cards - Cloudscape Design System"
source: "https://cloudscape.design/components/cards/?tabId=playground&example=simple"
created: 2025-10-01
description: "Represents a collection of items."
---
- [Playground](https://cloudscape.design/components/cards/?tabId=playground)
- [Usage](https://cloudscape.design/components/cards/?tabId=usage)

## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`ariaLabels`.

```jsx
import * as React from "react";
import Cards from "@cloudscape-design/components/cards";
import Box from "@cloudscape-design/components/box";
import SpaceBetween from "@cloudscape-design/components/space-between";
import Button from "@cloudscape-design/components/button";

export default () => {
  return (
    <Cards
      ariaLabels={{
        itemSelectionLabel: (e, i) => \`select ${i.name}\`,
        selectionGroupLabel: "Item selection"
      }}
      cardDefinition={{
          <Link href="#" fontSize="heading-m">
            {item.name}
          </Link>
        ),
        sections: [
          {
            id: "description",
            content: item => item.description
          },
          {
            id: "type",
            content: item => item.type
          },
          {
            id: "size",
            content: item => item.size
          }
        ]
      }}
      cardsPerRow={[
        { cards: 1 },
        { minWidth: 500, cards: 2 }
      ]}
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
          description: "This is the third item",
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
          alt: "Fifth",
          description: "This is the fifth item",
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
