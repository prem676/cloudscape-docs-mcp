---
title: "Radio group - Cloudscape Design System"
source: "https://cloudscape.design/components/radio-group/?tabId=usage"
created: 2025-10-04
description: "Radio group enable users to choose one option from a predefined set."
---
- [Playground](https://cloudscape.design/components/radio-group/?tabId=playground)
- [Usage](https://cloudscape.design/components/radio-group/?tabId=usage)

## General guidelines

### Do

- Use radio group when only one selection can be made from a group of two to seven options. Use [select](https://cloudscape.design/components/select/?tabId=playground) for groups of eight or more options.
- If one item is selected and inactive, always deactivate the other items in the radio group.
- Use for a selection between two options that require visible explanation via label and description for both states. Use a [toggle](https://cloudscape.design/components/toggle/?tabId=playground)  or [checkbox](https://cloudscape.design/components/checkbox/?tabId=playground) if you need to explain only the active state of a boolean option.
- Use for options that turn a group of elements on or off, for example progressive disclosure of form elements. If the group of sub-elements contain other radio groups, use [checkbox](https://cloudscape.design/components/checkbox/?tabId=playground), [toggle](https://cloudscape.design/components/toggle/?tabId=playground), or [tiles](https://cloudscape.design/components/tiles/?tabId=playground) instead.
- Optimize form completion by pre-selecting an option, to reduce users effort.
- Follow the guidelines for [selection in forms](https://cloudscape.design/patterns/general/selection/).
- Follow the guidelines for [disabled and read-only states](https://cloudscape.design/patterns/general/disabled-and-read-only-states/).

### Don't

- Don’t use for options that take immediate effect, for example to switch between light and dark mode. Use a [toggle](https://cloudscape.design/components/toggle/?tabId=usage) instead.
- Don’t label a radio group as optional.

## Features

- #### Label
	The label of an individual radio button in the radio group. In contrast to checkboxes, use radio buttons only as part of a group, not as standalone buttons.
	Make sure to label individual radio buttons, as well as the whole group.
- #### Description - optional
	Use the description to provide a broader explanation of the label. Follow the guidelines for [form field](https://cloudscape.design/components/form-field/).
- #### Progressive disclosure
	For options that add additional complexity, consider showing users the most important options first, then show the additional options upon selection below the radio group.

### States

- #### Disabled item
	Use the disabled state when users cannot interact with one of the radio buttons in the radio group and to prevent users from modifying the value.
- #### Read-only
	Use the read-only state when radio group data is not to be modified by the user but they still need to view it.

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

#### Label

- Always include labels to specify the individual options and the whole group.
- Use parallel sentence structure.
	- For example: *A radio group labeled Edition, and the individual radio button labels MySQL 5.6, MySQL 5.7, and PostgreSQL.*
- Do not include links in individual option labels.
- Follow the guidelines for [form field](https://cloudscape.design/components/form-field/).

#### Description - optional

- Avoid directive text that states the obvious, such as *Select one option*.
- Do not include links in individual option descriptions.
- Follow the guidelines for [form field](https://cloudscape.design/components/form-field/).

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### Alternative text

- Provide a meaningful label and description for each radio button.
- Wrap the component in a [form field](https://cloudscape.design/components/form-field/) to ensure that the group of radio buttons is correctly labelled. Alternatively, explicitly set properties `ariaLabel` (or `ariaLabelledBy`) and `ariaDescribedBy`.

#### Labels and descriptions

- Radio button labels and descriptions are part of the clickable/focusable area of the control, so they should not contain interactive content (for example, links). Place links at the [form field](https://cloudscape.design/components/form-field/) level instead.
