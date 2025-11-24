---
title: "Progress bar - Cloudscape Design System"
source: "https://cloudscape.design/components/progress-bar/?tabId=playground"
created: 2025-10-07
description: "Informs the user about the progress of an operation with a known duration."
---
- [Playground](https://cloudscape.design/components/progress-bar/?tabId=playground)
- [Usage](https://cloudscape.design/components/progress-bar/?tabId=usage)

## Configurator

### Examples

[Standalone in progress](https://cloudscape.design/components/progress-bar/?tabId=playground&example=standalone-in-progress)

[Standalone in success state](https://cloudscape.design/components/progress-bar/?tabId=playground&example=standalone-in-success-state)

[Standalone in error state](https://cloudscape.design/components/progress-bar/?tabId=playground&example=standalone-in-error-state)

[Within flash component](https://cloudscape.design/components/progress-bar/?tabId=playground&example=within-flash-component)

[Within key/value pairs pattern](https://cloudscape.design/components/progress-bar/?tabId=playground&example=within-key%2Fvalue-pairs-pattern)

### Configuration

## Code

```jsx
import * as React from "react";
import ProgressBar from "@cloudscape-design/components/progress-bar";

export default () => {
  return (
    <ProgressBar
      value={36}
      additionalInfo="Additional information"
      description="Progress bar description"
      label="Progress bar label"
    />
  );
}
```
