---
title: "Select - Cloudscape Design System"
source: "https://cloudscape.design/components/select/?tabId=playground&example=with-groups"
created: 2025-11-21
description: "Selects enable users to choose a single item from a list of items."
---
- [Playground](https://cloudscape.design/components/select/?tabId=playground)
- [API](https://cloudscape.design/components/select/?tabId=api)
- [Testing](https://cloudscape.design/components/select/?tabId=testing)
- [Usage](https://cloudscape.design/components/select/?tabId=usage)

## Configurator

### Configuration

#### Properties

 ariaRequired  autoFocus  disabled  expandToViewport  invalid  readOnly  virtualScroll  warning

{ label:"Option 1",

value:"1" }

\[{ label:"Group 1",

options:\[{ label:"Option 1",

value:"1" },

{ label:"Option 2",

value:"2" },

{ label:"Option 3",

value:"3" }\] },

{ label:"Group 2 (disabled)",

#### Slots

Use React and JSX syntax only.


## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`errorIconAriaLabel`, `filteringClearAriaLabel`, `recoveryText`, `selectedAriaLabel`.

```jsx
import * as React from "react";
import Select from "@cloudscape-design/components/select";

export default () => {
  const [
    selectedOption,
    setSelectedOption
  ] = React.useState({ label: "Option 1", value: "1" });
  return (
    <Select
      selectedOption={selectedOption}
      onChange={({ detail }) =>
        setSelectedOption(detail.selectedOption)
      }
      options={[
        {
          label: "Group 1",
          options: [
            { label: "Option 1", value: "1" },
            { label: "Option 2", value: "2" },
            { label: "Option 3", value: "3" }
          ]
        },
        {
          label: "Group 2 (disabled)",
          disabled: true,
          options: [
            { label: "Option 4", value: "4" },
            { label: "Option 5", value: "5" }
          ]
        }
      ]}
    />
  );
}
```