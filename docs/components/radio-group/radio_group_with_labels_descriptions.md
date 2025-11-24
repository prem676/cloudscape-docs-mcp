---
title: "Radio group - Cloudscape Design System"
source: "https://cloudscape.design/components/radio-group/?tabId=playground&example=with-labels-and-descriptions"
created: 2025-10-04
description: "Radio group enable users to choose one option from a predefined set."
---
- [Playground](https://cloudscape.design/components/radio-group/?tabId=playground)
- [Usage](https://cloudscape.design/components/radio-group/?tabId=usage)

## Configurator

### Configuration

#### Properties

 ariaRequired  readOnly

'second'

\[{ value:"first",

label:"First choice",

description:"This is the first option." },

{ value:"second",

label:"Second choice",

description:"This is the second option." },

{ value:"third",

label:"Third choice",

## Preview

First choice This is the first option.Second choice This is the second option.Third choice This is the third option.

## Code

```jsx
import * as React from "react";
import RadioGroup from "@cloudscape-design/components/radio-group";

export default () => {
  const [value, setValue] = React.useState("second");
  return (
    <RadioGroup
      onChange={({ detail }) => setValue(detail.value)}
      value={value}
      items={[
        {
          value: "first",
          label: "First choice",
          description: "This is the first option."
        },
        {
          value: "second",
          label: "Second choice",
          description: "This is the second option."
        },
        {
          value: "third",
          label: "Third choice",
          description: "This is the third option."
        }
      ]}
    />
  );
}
```
