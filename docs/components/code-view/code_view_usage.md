---
title: "Code view - Cloudscape Design System"
source: "https://cloudscape.design/components/code-view/?tabId=usage"
created: 2025-10-04
description: "Allow users to read and copy a code snippet."
---
- [Playground](https://cloudscape.design/components/code-view/?tabId=playground)
- [Usage](https://cloudscape.design/components/code-view/?tabId=usage)

## General guidelines

### Do

- Use to display read-only code snippets. For code editing use [code editor](https://cloudscape.design/components/code-editor/?tabId=usage) instead.

## Features

- #### Action buttons - optional
	Enables users to perform actions, such as copy or download the code snippet. Follow the guidelines for [copy to clipboard](https://cloudscape.design/components/copy-to-clipboard/).
- #### Syntax highlight - optional
	Syntax highlighting determines the color and style of source code displayed in the code view.
	- For example, it’s responsible for colorizing keywords in JavaScript like `for`, `if`, or `const` differently than strings, comments, and numbers.
- #### Line numbers - optional
	Line numbers are displayed preceding each line of code to support lines reference.
- #### Line wrapping - optional
	With line wrapping, users can have visibility over the source code content within the code view area by wrapping long lines of code onto new lines. When line wrapping is active, the maximum row width is the width of the code editing area in the component. Line wrapping is off by default.

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
	- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
	- For example: use *choose* or *select* not *click*.

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### Button

- Follow the accessibility guidelines for [buttons](https://cloudscape.design/components/button/).
- Follow the accessibility guidelines for [copy to clipboard.](https://cloudscape.design/components/copy-to-clipboard/)

