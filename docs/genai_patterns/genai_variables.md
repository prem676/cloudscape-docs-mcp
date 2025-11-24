---
title: "Variables - Cloudscape Design System"
source: "https://cloudscape.design/patterns/genai/variables/"
created: 2025-10-07
description: "A pattern for using variables within structured content such as prompt templates, code snippets, and text with predefined formats."
---
### Variables

Variables are bits of information displayed inline within structured content like text or prompt templates. They can be plain text variables, interactive variables, or read-only variables.

### Displaying variables

Variables are visually distinguished from their surrounding content by visual style, consistent syntax, or both. They can be displayed in read only or interactive states. Interactive variables should use clear, descriptive names to help users determine the type of input that is expected. For more about writing and displaying variables, see [writing guidelines](https://cloudscape.design/patterns/genai/variables/#writing-guidelines).

Variables are essential building blocks of templates, enabling customization while preserving the template's structure. For example, templates used in generative AI workflows, where models are sensitive to word order and phrasing, variables allow users to modify specific elements without compromising the template's effectiveness. This controlled customization ensures consistent outputs, reduces errors, and enables templates to be reused across different contexts.

There are three distinct types of variables: Plain text variables, interactive variables, and read-only variables. Each type serves a specific purpose and offers unique characteristics in how they are represented and interacted with in an interface. Understanding these variable types helps create dynamic, interactive content effectively.

Plain text variables are stateless variables that can be edited directly through standard text editing, denoted by angle brackets <>. In contexts where angle brackets might be confusing, [use alternative syntax](https://cloudscape.design/patterns/genai/variables/#component-specific-guidelines). They enable users to edit text associated with the variable directly within the form field they are displayed in. For example, in [generative AI chat](https://cloudscape.design/patterns/genai/generative-AI-chat/), a user can take advantage of a prompt template and quickly edit the variable to help generate their intended output before sending the prompt.

![](https://cloudscape.design/__images/yvlrib0vb3vb/2NwXzrlAcgfRNHOx2xRViT/9de8b9dd49c0188a49ca2ab4e7d0f283/Plain-variables-light.png) ![](https://cloudscape.design/__images/yvlrib0vb3vb/3vMPPqyvoLppaYYorYZuF5/b075a6a02ff58050ebae09c866698610/Plain-variables-dark.png)

### Interactive variables

Interactive variables utilize the inline variant of Token component to provide distinct visual style and interactions when placed in context of surrounding content.

#### Popover interaction

This kind of interactive variable triggers a [popover](https://cloudscape.design/components/popover/) where users can edit the variables through a simple [form field](https://cloudscape.design/components/form-field/) or [selection](https://cloudscape.design/patterns/general/selection/) without navigating to a separate area within the UI. This kind of interaction is best suited for variables where a single form field or selection are required.

![](https://cloudscape.design/__images/yvlrib0vb3vb/3rNCqP01AIW4AaiSXS1Dn6/e17ee5c383f692227c5909f843f11b3e/Popover-configured-light.png) ![](https://cloudscape.design/__images/yvlrib0vb3vb/2oI0EDd9TCAuEwvQyj4T21/e40815714a3032690cca629005a81b2a/Popover-configured-dark.png)

### Read-only variables

Read-only variables are used to highlight bits of information from surrounding content. For example, in a code snippet, highlighting the key parameters show users where specific values can be edited when using the snippet.

![](https://cloudscape.design/__images/yvlrib0vb3vb/78UQn4fN5nGcjyUFAUz0ik/761c663d2f1f38955e159eb1d1f34bdb/Read-only-light.png) ![](https://cloudscape.design/__images/yvlrib0vb3vb/2CsTRDrWhWdt1FDj5llKUi/0c6232f7c78f65fc7bc6e3948308677a/Read-only-dark.png)

## Guidelines

### Do

- Use variables to enable customization within structured content such as prompt templates, code snippets, or text with predefined formats. For example, in AI prompt templates, variables allow users to modify specific elements without altering the overall structure that ensures consistent outputs.
- Match placeholder variable text with input field labels when using interactive variables to help users easily identify which variable they're editing.

## Writing guidelines

### Component-specific guidelines

#### Syntax

By default inline token variables should use angle brackets <> and italic text to indicate placeholder within variable text. Use alternative syntax when angle brackets could cause confusion, such as in code snippets.

- Use angle brackets: *<variable-name>*
- Use descriptive, hyphenated names: *<service-name>*, *<region-name>*
- Do not use spaces within variable names: *<database-name>* not *<database name>*
- For example, "List EC2 instances in *<region>* created before *<date>* "

#### Alternative syntax

When working with code snippets or contexts where angle brackets might be confusing, use the appropriate syntax for that context. For example, View metrics for *${service}* in *${region}*.

- Follow the syntax required by the code or template language
- Common formats include: *${variable}*, *$variable*, or other language-specific syntax

#### Placeholder variable text

- When an inline variable has not yet been edited by a user, it should be displayed as italic text. This formatting communicates a familiar pattern to users that there is placeholder text within a variable. For example, "Analyze potential cost savings for my *<service-name>* in region *<region>*."

#### User-edited variable text

- Once a user selects or enters a value for an inline variable, the value should be displayed as regular styled text. For example, "Analyze potential cost savings for my EC2 in region us-east-2."
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
