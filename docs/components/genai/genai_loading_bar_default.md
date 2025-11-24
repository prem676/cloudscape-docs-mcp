---
title: "Loading bar - Cloudscape Design System"
source: "https://cloudscape.design/components/loading-bar/?tabId=playground"
created: 2025-10-07
description: "A linear loading indicator that informs the user about an ongoing operation with unknown duration."
---
- [Playground](https://cloudscape.design/components/loading-bar/?tabId=playground)
- [Usage](https://cloudscape.design/components/loading-bar/?tabId=usage)

## Configurator

### Examples

[Default](https://cloudscape.design/components/loading-bar/?tabId=playground&example=default)

[With mask](https://cloudscape.design/components/loading-bar/?tabId=playground&example=with-mask)

### Configuration

## Code

```jsx
import * as React from "react";
import LoadingBar from "@cloudscape-design/chat-components/loading-bar";
import LiveRegion from "@cloudscape-design/components/live-region";
import Box from "@cloudscape-design/components/box";

export default () => {
  return (
    <LiveRegion>
      <Box
        margin={{ bottom: "xs", left: "l" }}
        color="text-body-secondary"
      >
        Generating a response
      </Box>
      <LoadingBar variant="gen-ai" />
    </LiveRegion>
  );
}
```
