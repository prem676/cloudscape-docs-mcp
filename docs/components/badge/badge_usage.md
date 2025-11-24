---
title: "Badge - Cloudscape Design System"
source: "https://cloudscape.design/components/badge/?tabId=usage"
created: 2025-10-01
description: "A small, color-coded visual element that contains letters or numbers, that is used to label, categorize, organize, or indicate severity of items."
---

## General guidelines

### Do

- Use badges for items that you want to label, categorize, or organize using text or numbers.
- Place the badge in proximity to the item that it relates to.
- Use badges to provide additional context or to call attention to a component.
- Use multiple badges in a row if needed.
- Use badge color coding consistently.
- Use the same severity palette for all items (badges and charts) across the application to consistently show its severity level. See [severity data visualization](https://cloudscape.design/foundation/visual-foundation/data-vis-colors/#status-and-severity-palette) for more details.

### Don't

- Don’t include icons or imagery on badges, only letters and numbers.
- Keep in mind that badges are not interactive.
- Avoid using badges, including severity badges, to indicate status. Follow the guidelines for [status indicator](https://cloudscape.design/components/status-indicator/).
- Don't use color only to indicate severity or category. Supplement color with text to let user know what this badge is indicating.
- Don't use badges for labeling features as new.

## Features

- #### Values
	Badge text is limited to alphanumeric characters.
- #### Types
	Basic badge colors are limited to the following:
	- `grey (default)`
	- `blue`
	- `green`
	- `red`
	In addition to basic badges, there are five severity badges. Severity badge types are limited to the following:
	- `severity-critical`
	- `severity-high`
	- `severity-medium`
	- `severity-low`
	- `severity-neutral`

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

Don't use color only to indicate severity or category. Supplement color with text to let user know what this badge is indicating. For example, use the word “Critical” in critical-severity badges.
