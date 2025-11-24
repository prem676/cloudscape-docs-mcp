---
title: "Container - Cloudscape Design System"
source: "https://cloudscape.design/components/container/?tabId=playground&example=key-value-pairs-in-a-container-with-a-table"
author:
published:
created: 2025-10-01
description: "With the container, you can present a group of pieces of content, indicating that the items are related. For example, a table is a type of container."
tags:
  - "clippings"
---
[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/components/tree/main/src/container "Browse code (opens new tab)")

- [Playground](https://cloudscape.design/components/container/?tabId=playground)
- [API](https://cloudscape.design/components/container/?tabId=api)
- [Testing](https://cloudscape.design/components/container/?tabId=testing)
- [Usage](https://cloudscape.design/components/container/?tabId=usage)

## Code

```jsx
import * as React from "react";
import Container from "@cloudscape-design/components/container";
import KeyValuePairs from "@cloudscape-design/components/key-value-pairs";
import Header from "@cloudscape-design/components/header";

export default () => {
  return (
    <Container
      variant="stacked"
      header={
        <Header headingTagOverride="h3" counter="(5)">
          Header
        </Header>
      }
    >
      <KeyValuePairs
        columns={4}
        items={[
          { label: "Label for key", value: "Value" },
          { label: "Label for key", value: "Value" },
          { label: "Label for key", value: "Value" },
          { label: "Label for key", value: "Value" }
        ]}
      />
    </Container>
  );
}
```
