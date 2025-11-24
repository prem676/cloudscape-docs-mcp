---
title: "Select - Cloudscape Design System"
source: "https://cloudscape.design/components/select/?tabId=playground&example=loading-state"
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

null

\[\]

#### Slots

Use React and JSX syntax only.

## Preview

## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`errorIconAriaLabel`, `filteringClearAriaLabel`, `recoveryText`, `selectedAriaLabel`.

```jsx
import * as React from "react";
import Select from "@cloudscape-design/components/select";

export default () => {
  const [
    selectedOption,
    setSelectedOption
  ] = React.useState(null);
  return (
    <Select
      selectedOption={selectedOption}
      onChange={({ detail }) =>
        setSelectedOption(detail.selectedOption)
      }
      options={[]}
      loadingText="Loading instances"
      placeholder="Choose an option"
      statusType="loading"
    />
  );
}
```