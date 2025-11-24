---
title: "Content layout - Cloudscape Design System"
source: "https://cloudscape.design/components/content-layout/?tabId=playground&example=with-divider"
created: 2025-10-01
description: "Provides page structure for expressive use cases."
---
- [API](https://cloudscape.design/components/content-layout/?tabId=api)
- [Usage](https://cloudscape.design/components/content-layout/?tabId=usage)

## Configurator

## Code

```jsx
import * as React from "react";
import ContentLayout from "@cloudscape-design/components/content-layout";
import Box from "@cloudscape-design/components/box";
import Header from "@cloudscape-design/components/header";
import Link from "@cloudscape-design/components/link";

export default () => {
  return (
    <ContentLayout
      defaultPadding
      disableOverlap
      headerVariant="divider"
      header={
        <Header
          variant="h1"
          info={<Link variant="info">Info</Link>}
          description="This is a generic description used in the header."
        >
          Header
        </Header>
      }
    >
      <Box variant="h2" padding={{ top: "m" }}>
        Content heading
      </Box>

      <Box variant="p">This is a content paragraph.</Box>
    </ContentLayout>
  );
}
```
