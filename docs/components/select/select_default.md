---
title: "Select - Cloudscape Design System"
source: "https://cloudscape.design/components/select/?tabId=playground"
description: "Selects enable users to choose a single item from a list of items."
---
- [Playground](https://cloudscape.design/components/select/?tabId=playground)
- [API](https://cloudscape.design/components/select/?tabId=api)
- [Testing](https://cloudscape.design/components/select/?tabId=testing)
- [Usage](https://cloudscape.design/components/select/?tabId=usage)

## Configurator

#### Properties

 ariaRequired  autoFocus  disabled  expandToViewport  invalid  readOnly  virtualScroll  warning

{ label:"Option 1",

value:"1" }

\[{ label:"Option 1",

value:"1" },

{ label:"Option 2",

value:"2" },

{ label:"Option 3",

value:"3" },

{ label:"Option 4",

value:"4" },

#### Slots

Use React and JSX syntax only.


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
        { label: "Option 1", value: "1" },
        { label: "Option 2", value: "2" },
        { label: "Option 3", value: "3" },
        { label: "Option 4", value: "4" },
        { label: "Option 5", value: "5" }
      ]}
    />
  );
}
```
