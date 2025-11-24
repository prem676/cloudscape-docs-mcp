---
title: "Drawer - Cloudscape Design System"
source: "https://cloudscape.design/components/drawer/?tabId=playground"
created: 2025-10-23
description: "A panel that displays supplementary content on a page, which supports task completion or feature access."
---
- [Playground](https://cloudscape.design/components/drawer/?tabId=playground)
- [Usage](https://cloudscape.design/components/drawer/?tabId=usage)

## Configurator

### Examples

[With summary content](https://cloudscape.design/components/drawer/?tabId=playground&example=with-summary-content)

[Loading state](https://cloudscape.design/components/drawer/?tabId=playground&example=loading-state)


## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`i18nStrings`.

```jsx
import * as React from "react";
import Drawer from "@cloudscape-design/components/drawer";
import Box from "@cloudscape-design/components/box";
import SpaceBetween from "@cloudscape-design/components/space-between";
import ExpandableSection from "@cloudscape-design/components/expandable-section";
import KeyValuePairs from "@cloudscape-design/components/key-value-pairs";

export default () => {
  return (
    <div className="drawer-example">
        <Box margin={{ bottom: "l" }}>
          <SpaceBetween size="xxl">
            <SpaceBetween size="xs">
                Step 1: Engine type
              </Header>
              <ExpandableSection
                defaultExpanded
              >
                <KeyValuePairs
                  columns={2}
                  items={[
                    { label: "Engine", value: "Aurora" },
                    {
                      label: "License model",
                      value: "Bring your own license"
                    },
                    {
                      label: "Edition",
                      value: "MySQL 5.6-compatible"
                    }
                  ]}
                />
              </ExpandableSection>
            </SpaceBetween>
            <SpaceBetween size="xs">
                Step 2: Instance details
              </Header>
                <KeyValuePairs
                  columns={2}
                  items={[
                    {
                      label: "Class",
                      value: "db.t2.micro"
                    },
                    {
                      label: "Storage type",
                      value: "General Purpose (SSD)"
                    },
                    {
                      label: "Allocated storage",
                      value: "20 GiB"
                    }
                  ]}
                />
              </ExpandableSection>
                <KeyValuePairs
                  columns={2}
                  items={[
                    {
                      label: "DB instance identifier",
                      value: "example-instance-identifier"
                    },
                    {
                      label: "Primary username",
                      value: "example-username"
                    },
                    {
                      label: "Primary password",
                      value: "example-password"
                    }
                  ]}
                />
              </ExpandableSection>
            </SpaceBetween>
          </SpaceBetween>
        </Box>
      </Drawer>
    </div>
  );
}
```
