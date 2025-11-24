---
title: "Code view - Cloudscape Design System"
source: "https://cloudscape.design/components/code-view/?tabId=playground&example=simple"
created: 2025-10-04
description: "Allow users to read and copy a code snippet."
---
- [Playground](https://cloudscape.design/components/code-view/?tabId=playground)
- [Usage](https://cloudscape.design/components/code-view/?tabId=usage)

## Configurator

### Examples

[Simple](https://cloudscape.design/components/code-view/?tabId=playground&example=simple)

[With line numbers and copy button](https://cloudscape.design/components/code-view/?tabId=playground&example=with-line-numbers-and-copy-button)

### Configuration

#### Properties

 lineNumbers  wrapLines

typescriptHighlight

#### Slots

Use React and JSX syntax only.

## Preview

| `const hello: string = "world"; ` |
| --- |
| `console.log(hello); ` |

## Code

```jsx
import * as React from "react";
import typescriptHighlight from "@cloudscape-design/code-view/highlight/typescript";
import CodeView from "@cloudscape-design/code-view/code-view";

export default () => {
  return (
    <CodeView
      content='const hello: string = "world";
console.log(hello);'
    />
  );
}
```
