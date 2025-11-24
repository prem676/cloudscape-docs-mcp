---
title: "Select - Cloudscape Design System"
source: "https://cloudscape.design/components/select/?tabId=playground&example=with-features"
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

value:"1",

iconName:"settings",

description:"sub value",

tags:\["CPU-v2",

"2Gb RAM"\],

labelTag:"128Gb" }

\[{ label:"Option 1",

value:"1",

iconName:"settings",

description:"sub value",

tags:\["CPU-v2",

"2Gb RAM"\],

labelTag:"128Gb" },

{ label:"Option 2",

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
  ] = React.useState({
    label: "Option 1",
    value: "1",
    iconName: "settings",
    description: "sub value",
    tags: ["CPU-v2", "2Gb RAM"],
    labelTag: "128Gb"
  });
  return (
    <Select
      selectedOption={selectedOption}
      onChange={({ detail }) =>
        setSelectedOption(detail.selectedOption)
      }
      options={[
        {
          label: "Option 1",
          value: "1",
          iconName: "settings",
          description: "sub value",
          tags: ["CPU-v2", "2Gb RAM"],
          labelTag: "128Gb"
        },
        {
          label: "Option 2",
          value: "2",
          iconName: "settings",
          description: "sub value",
          tags: ["CPU-v2", "2Gb RAM"],
          labelTag: "128Gb"
        },
        {
          label: "Option 3",
          value: "3",
          iconName: "settings",
          description: "sub value",
          tags: ["CPU-v2", "2Gb RAM"],
          labelTag: "128Gb"
        }
      ]}
      triggerVariant="option"
    />
  );
}
```