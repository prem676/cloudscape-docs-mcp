---
title: "Steps - Cloudscape Design System"
source: "https://cloudscape.design/components/steps/?tabId=usage"
created: 2025-10-07
description: "Display a list of tasks."
---
- [Playground](https://cloudscape.design/components/steps/?tabId=playground)
- [Usage](https://cloudscape.design/components/steps/?tabId=usage)

## General guidelines

## Features

- #### Status

 The status of a step conveyed via corresponding [status indicator](https://cloudscape.design/components/status-indicator/).

- #### Header

 A brief summary of the step to provide more context to users. It can be used to display the name of a task being performed, a [popover](https://cloudscape.design/components/popover/) that contains the step details, and a [link](https://cloudscape.design/components/link/) to a detail page as needed.

- #### Details - optional

 A slot to display additional information corresponding to the step. For example, a description or list of sub-tasks being performed, a [link](https://cloudscape.design/components/link/) to navigate to a detail page, or a [button](https://cloudscape.design/components/button/) to let users perform an action on that step.

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

#### Status indicator

- Follow the writing guidelines for [status indicator](https://cloudscape.design/components/status-indicator/?tabId=usage#writing-guidelines).

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### ARIA live regions

- Status updates are not automatically announced to assistive technology. For situations where the steps’ status change dynamically, the Steps component should be wrapped with live regions.
- For example: `<span aria-live="polite"><Steps steps={steps}/></span>`

#### Alternative text

- Provide a label for the Steps component using the `ariaLabelledBy` property.
- `<p id="stepsLabelId">Cloudformation deployment</p> <Steps ariaLabelledBy={"stepsLabelId"} steps={steps} />`
- Provide a description for the Steps component using the `ariaDescribedby` property.
- `<p id="stepsDescriptionId">Cloudformation deployment will affect the following resources...</p> <Steps ariaDescribedby={"stepsDescriptionId"} steps={steps} />`
- Provide alternative text for the status icon using the `statusIconAriaLabel` property.
- `<Steps steps={[status: "error", header: "Terminated process", statusIconAriaLabel="Error"]}/>`

## Did this page help you?

1000 character(s) available. Do not disclose any personal, commercially sensitive, or confidential information.
