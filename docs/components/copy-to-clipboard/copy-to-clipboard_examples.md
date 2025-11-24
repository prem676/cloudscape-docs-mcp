---
title: "Copy to clipboard - Cloudscape Design System"
source: "https://cloudscape.design/components/copy-to-clipboard/?tabId=playground&example=icon-variant"
created: 2025-10-13
description: "With copy to clipboard, users can copy content to their clipboard."
---

## Copy to clipboard Icon Variant

```jsx
import * as React from "react";
import CopyToClipboard from "@cloudscape-design/components/copy-to-clipboard";

export default () => {
  return (
    <CopyToClipboard
      copyButtonAriaLabel="Copy ARN"
      copyErrorText="ARN failed to copy"
      copySuccessText="ARN copied"
      textToCopy="SLCCSMWOHOFUY0"
      variant="icon"
    />
  );
}
```

## Copy to clipboard Inline Variant

```jsx
import * as React from "react";
import CopyToClipboard from "@cloudscape-design/components/copy-to-clipboard";

export default () => {
  return (
    <CopyToClipboard
      copyButtonAriaLabel="Copy ARN"
      copyErrorText="ARN failed to copy"
      copySuccessText="ARN copied"
      textToCopy="SLCCSMWOHOFUY0"
      variant="inline"
    />
  );
}
```

## Copy to clipboard Button Variant

```jsx
import * as React from "react";
import CopyToClipboard from "@cloudscape-design/components/copy-to-clipboard";

export default () => {
  return (
    <CopyToClipboard
      copyButtonText="Copy"
      copyErrorText="ARN failed to copy"
      copySuccessText="ARN copied"
      textToCopy="SLCCSMWOHOFUY0"
    />
  );
}
```
