---
title: "Copy to clipboard - Cloudscape Design System"
source: "https://cloudscape.design/components/copy-to-clipboard/?tabId=usage"
created: 2025-10-13
description: "With copy to clipboard, users can copy content to their clipboard."
---
- [Playground](https://cloudscape.design/components/copy-to-clipboard/?tabId=playground)
- [Usage](https://cloudscape.design/components/copy-to-clipboard/?tabId=usage)

## General guidelines

### Do

- Use copy to clipboard to give users a consistent mechanism for quickly copying values or text data.

## Features

- #### Variant
- **Button:** If users need to copy a large or formatted block of content, for example a snippet of code, the content is paired with a corresponding copy action button.
- **Inline:** Enable users to quickly copy a string of text.
- For example: Copy a long URL within a table or an Amazon Resource Name (ARN) within a list of [key-value pairs](https://cloudscape.design/components/key-value-pairs/) (see live example in the [details page demo](https://cloudscape.design/examples/react/details.html)).
- **Icon:** When creating a collection of contextual and persistent triggers that enable users to perform a series of actions including copying to clipboard, use the icon variant.
- #### Copy confirmation
 A popover with a status indicator and text string confirms the success of the action, or communicates if an error occurs.

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
- For example: use *choose* or *select* not *click*.

### Component-specific guidelines

#### Button label

- For the [normal button](https://cloudscape.design/components/button/?example=normal-button) used for copying a block of content, use this text: *Copy*

#### Popover

- Provide a precise name to the content intended for copying.
- For example: *Sample code copied*
- For success text, use the format: *\[Name of the content\] copied*
- For example: *Secret ARN copied*
- For error text, use the format: *\[Name of the content\] failed to copy*
- For example: *ARN failed to copy*

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

## Did this page help you?

1000 character(s) available. Do not disclose any personal, commercially sensitive, or confidential information.
