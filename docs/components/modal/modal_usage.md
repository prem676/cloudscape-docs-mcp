---
title: "Modal - Cloudscape Design System"
source: "https://cloudscape.design/components/modal/?tabId=usage"
created: 2025-10-09
description: "A user interface element subordinate to an application's main window. It prevents interaction with the main page content, but keeps it visible with the modal as a child window in front of it."
---
## Modal

Published: May 4, 2020

[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/components/tree/main/src/modal "Browse code (opens new tab)")

- [Playground](https://cloudscape.design/components/modal/?tabId=playground)
- [Usage](https://cloudscape.design/components/modal/?tabId=usage)

## General guidelines

### Do

- Use an action button to act on the entire contents of a modal. For example: *Save*, *OK*, *Done*, *Canceled*. Use a [flash message](https://cloudscape.design/components/flashbar/) to confirm the result of committing modal data.
- Use a modal primarily to confirm or cancel a choice For example: *Delete instance*.
- Keep the text short and interactions to a minimum. Try to avoid scrolling content.

### Don't

- Avoid tabs, or expanded sections in modal which overload the interface.
- Never launch another modal from within a modal.
- Do not chain together a sequence of modals. Instead of using a sequence of modals with multiple steps over multiple pages, use the [multipage create flow](https://cloudscape.design/patterns/resource-management/create/multi-page-create/).

## Features

- #### Overlay

 A modal will tint the outlying content areas to indicate that they are blocked from user interaction.

- #### Header

 Provides a short summary of the requested user action.

- #### Content

 The area for modal content. Common content types of a modal are:

- [Alert](https://cloudscape.design/components/alert/?tabId=playground)  and description to inform the consequences of the user actions, for example, in  [delete](https://cloudscape.design/patterns/resource-management/delete/)  pattern to provide details of a delete action and in  [communicating unsaved changes](https://cloudscape.design/patterns/general/unsaved-changes/) to communicate unsaved changes.
- [Input fields](https://cloudscape.design/components/input/?tabId=playground)  and simple  [selects](https://cloudscape.design/components/select/?tabId=playground)  to create resource, for example, in  [create resource flow](https://cloudscape.design/patterns/resource-management/create/).
- [Tiles](https://cloudscape.design/components/tiles/?tabId=playground) and description to facilitate comparison, for example, in [density settings](https://cloudscape.design/patterns/general/density-settings/)  to compare content density modes and in  [split panel](https://cloudscape.design/components/split-panel/?tabId=api) to compare display modes.
- [Checkboxes](https://cloudscape.design/components/checkbox/?tabId=playground), [radio groups](https://cloudscape.design/components/radio-group/?tabId=playground), and  [toggles](https://cloudscape.design/components/toggle/?tabId=playground)  to change preference settings, for example, in  [collection preferences](https://cloudscape.design/components/collection-preferences/?tabId=playground) for table and cards.

- #### Dismiss button

 Always allows the user to dismiss the modal. Dismissing via the *X* icon is the same as canceling when more than one input or action is present in the dialog box.

- #### Scrolling content area

 A scrolling viewport for content that overflows the visible area.

- #### Footer

 An area at the bottom of the dialog box for actions, such as *Cancel, Create, Delete, or Save.*
 While form controls may be placed within the content area, actions that commit or cancel an operation should always be placed in the footer area.

- #### Size

 Sets the width of the modal. The default is **medium**. **Max** varies to fit the largest size. Other sizes (small/medium/large) are fixed width.

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

#### Header

- Start with an active verb, where possible.
- Don’t use terminal punctuation (period, colon, or similar).
- For example: *Delete channel*

#### Description

- Use one or two short sentences that describe the task. Use active voice instead of passive voice.
- Keep text concise and to the point, because text can grow by as much as three times its size when it is translated into other languages.

#### Button

- Don’t include *Yes* for buttons that confirm an action
- For example: in a modal that prompts users to confirm a system reboot, use *Reboot*
- Follow the writing guidelines for [button](https://cloudscape.design/components/button/?tabId=usage#writing-guidelines).

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### Roles and landmarks

- The modal component comes with its own `role` attribute set to `alert` in order to announce it to screen readers. Don't add any additional roles yourself.

#### Alternative text

- Provide alternative text for the X close icon according to the alternative text guidelines using `closeLabel` property.
- For example: *Close*

#### Keyboard interaction

- The default keyboard functionality is to focus the modal *Close* button when the modal is opened.
