---
title: "Code view - Cloudscape Design System"
source: "https://cloudscape.design/components/code-view/?tabId=api"
created: 2025-10-04
description: "Allow users to read and copy a code snippet."
---
- [Playground](https://cloudscape.design/components/code-view/?tabId=playground)
- [Usage](https://cloudscape.design/components/code-view/?tabId=usage)

## Development guidelines

#### Syntax highlighting

The component supports several languages with predefined highlighting rules.

To utilize the built-in syntax highlighting with the languages supported by the component, pass one of the available highlight functions to the `highlight` property of the `CodeView` component. The following code example demonstrates how to import and use the JavaScript and PHP highlight functions for syntax highlighting in your code view. You can follow the same steps to highlight other supported languages.

```
import CodeView from "@cloudscape-design/code-view";
import javascriptHighlight from "@cloudscape-design/code-view/highlight/javascript";
import phpHighlight from "@cloudscape-design/code-view/highlight/php";

<CodeView content={\`const hello = "world"\`} highlight={javascriptHighlight} />

<CodeView content={\`<?php echo 'Hello, world!'; ?>\`} highlight={phpHighlight} />
```

If your desired programming language isn't supported out-of-the-box, you can still add syntax highlighting for it. The `createHighlight` utility let's you create a highlighting function based on an [ace-code](https://www.npmjs.com/package/ace-code) rule, which you can then pass to the `highlight` property of the `CodeView` component. This allows you to integrate syntax highlighting for any language supported by `ace-code` that isn't included by default in our component.

```
import { TerraformHighlightRules } from "ace-code/src/mode/terraform_highlight_rules";
import { createHighlight } from "@cloudscape-design/code-view/highlight";

const terraformHighlight = createHighlight(new TerraformHighlightRules());

<CodeView content={\`resource "aws_s3_bucket" "example" { bucket = "example-bucket" }\`} highlight={terraformHighlight} />
```

Alternatively, you can use a custom highlighting function for more flexibility. You can pass a function to the `highlight` property of the component that takes the source code content as a string argument and returns a React node representing the highlighted code.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| ariaLabel | ``` string ``` | Adds an `aria-label` to the component. Use this label when there is not enough context around the code snippet to describe its purpose or content. | \- | \- | ``` false ``` |
| ariaLabelledby | ``` string ``` | Adds `aria-labelledby` to the component. Use this property to reference the ID of an existing element that provides a descriptive label for the code snippet. | \- | \- | ``` false ``` |
| content | ``` string ``` | The code content to be displayed. | \- | \- | ``` true ``` |
| highlight | ``` (code: string) => React.ReactNode ``` | A function to perform custom syntax highlighting. | \- | \- | ``` false ``` |
| i18nStrings | ``` CodeViewProps.I18nStrings {   codeLabel?: string   lineNumberLabel?: string } ``` | An object containing all the necessary localized strings required by the component. The object should contain:  - `lineNumberLabel` - Label for the column that displays line numbers (when line numbers are visible) - `codeLabel` - Label for the column that displays the code content (when line numbers are visible) | \- | \- | ``` false ``` |
| lineNumbers | ``` boolean ``` | Controls the display of line numbers.  Defaults to `false`. | \- | ``` false ``` | ``` false ``` |
| wrapLines | ``` boolean ``` | Controls whether line-wrapping is enabled when content would overflow the component.  Defaults to `false`. | \- | ``` false ``` | ``` false ``` |

## Slots

| Name | Description |
| --- | --- |
| actions | An optional slot to display a button to enable users to perform actions, such as copy or download the code snippet. |
