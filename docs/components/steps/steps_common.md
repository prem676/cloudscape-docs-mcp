---
title: "Steps - Cloudscape Design System"
source: "https://cloudscape.design/components/steps/?tabId=playground&example=default"
created: 2025-10-07
description: "Display a list of tasks."
---

```jsx
import * as React from "react";
import Steps from "@cloudscape-design/components/steps";

export default () => {
  return (
    <Steps
      steps={[
        {
          status: "success",
          header: "Success step",
          statusIconAriaLabel: "Success"
        },
        {
          status: "warning",
          header: (
            <Popover
              content="More info about warning"
              dismissButton={false}
            >
              Warning step
            </Popover>
          ),
          statusIconAriaLabel: "Warning"
        },
        {
          status: "stopped",
          header: "Stopped step",
          statusIconAriaLabel: "Stopped"
        }
      ]}
    />
  );
}
```
