---
title: "Container - Cloudscape Design System"
source: "https://cloudscape.design/components/container/?tabId=playground&example=with-footer"
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
- [Usage](https://cloudscape.design/components/container/?tabId=usage)

## Code

```jsx
import * as React from "react";
import Container from "@cloudscape-design/components/container";
import Header from "@cloudscape-design/components/header";

export default () => {
  return (
    <Container
      footer="Container footer"
      header={
        <Header
          variant="h2"
          description="Container description"
        >
          Container title
        </Header>
      }
    >
      Container content
    </Container>
  );
}
```
