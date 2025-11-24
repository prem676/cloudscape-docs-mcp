---
title: "Progress bar - Cloudscape Design System"
source: "https://cloudscape.design/components/progress-bar/?tabId=playground&example=within-key%2Fvalue-pairs-pattern"
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
import Container from "@cloudscape-design/components/container";
import KeyValuePairs from "@cloudscape-design/components/key-value-pairs";
import StatusIndicator from "@cloudscape-design/components/status-indicator";
import Link from "@cloudscape-design/components/link";

export default () => {
  return (
    <Container
    >
      <KeyValuePairs
        columns={2}
        items={[
          { label: "Label for key", value: "Value" },
          {
            label: "Progress bar label",
            id: "progress-bar-id",
            value: (
              <ProgressBar
                ariaLabelledby="progress-bar-id"
                value={36}
                variant="key-value"
                additionalInfo="Additional information"
                description="Progress bar description"
              />
            )
          },
          {
            label: "Label for key",
            value: (
              <StatusIndicator>
                Value for positive status
              </StatusIndicator>
            )
          },
          {
            label: "Label for key",
            value: (
              <Link
                href="/"
                target="_blank"
                rel="noopener noreferrer"
                external={true}
                variant="primary"
                ariaLabel="Label for key"
              >
                Value with external link
              </Link>
            )
          }
        ]}
      />
    </Container>
  );
}
```
