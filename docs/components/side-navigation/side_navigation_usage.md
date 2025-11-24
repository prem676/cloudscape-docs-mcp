---
title: "Side navigation - Cloudscape Design System"
source: "https://cloudscape.design/components/side-navigation/?tabId=usage"
created: 2025-11-21
description: "A list of navigational links that point to the pages within an application."
---
- [Playground](https://cloudscape.design/components/side-navigation/?tabId=playground)
- [API](https://cloudscape.design/components/side-navigation/?tabId=api)
- [Testing](https://cloudscape.design/components/side-navigation/?tabId=testing)
- [Usage](https://cloudscape.design/components/side-navigation/?tabId=usage)

## General guidelines

### Do

- Avoid linking outside of your application from the side navigation. If you need to do that, add the flag *external* to navigation links.
- Sparingly use dividers to separate sets of links that are fundamentally not related to each other.
- Follow the guidelines for [service navigation](https://cloudscape.design/patterns/general/service-navigation/) on how to structure your navigation information architecture and map it to breadcrumbs.
- Use *New* labels in the side navigation to mark new pages. See the guidance for [announcing new features](https://cloudscape.design/patterns/general/announcing-new-features/).
- If needing to place both a badge, such as a notifications badge, and a *New* label next to the same navigational link, place the *New* label to the right of the badge.
- Use SVG format for logos.

## Features

- #### Header
	The application name is displayed at the top of the navigation panel, so the user can see which application they’re using.
- #### Items control - optional
	The side navigation provides an area below the header and above the items, where a custom item control can be added.  
	For example, adding a [select](https://cloudscape.design/components/select/) or [segmented control](https://cloudscape.design/components/segmented-control/) to let users toggle the content of the side navigation.
- #### Link structure
	The first link listed in the side navigation, below the header, should correspond with the default landing page for a returning user of the application. Often, this may be a dashboard or an item list. This differs with the landing page for either a first-time user or when items don’t exist within the application. In such cases, the landing page should be the application homepage.
- #### Sections
	Sets of links can be grouped together under a single header. The header itself is not a link to a page but provides the ability to expand and collapse the section.
- #### Section groups
	Set of items that are conceptually related to each other, and can be displayed under a single heading to provide further organization. You can nest sections, links, link groups and expandable link groups within a section group depending on your information architecture needs.
- #### Expandable link groups
	Link groups support nested page information architectures. Set the group of child links as hidden by default until either a user has navigated to a page within the link group, including the parent, or has explicitly expanded the group into view.
- #### Link groups
	Only to be used when the information for an existing item must be split between multiple detail pages. This link grouping should only appear after an existing item is selected by the user.
- #### Dividers
	Dividers provides the ability to organize the side panel by separating major sets of links that are fundamentally not related to each other.
- #### Badges
	Use badges in the navigation to flag actionable areas. For example, you can use them for notifications.
- #### New labels
	Place New labels next to newly launched pages in the application, and keep them for 30 days. Follow the guidelines for [announcing new features](https://cloudscape.design/patterns/general/announcing-new-features/).
- #### App layout
	Place the side navigation in the `navigation` region of [app layout](https://cloudscape.design/components/app-layout/).

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

- Use sentence case (not title case).
- Use nouns representing objects or features, don't use verbs.
- Keep link names and section headers as short as possible while maintaining clarity, and avoid jargon or abbreviations the user may not know.
- Avoid articles (*a, an, the*) in headings to keep content short and actionable.

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.

### Component-specific guidelines

#### Roles and landmarks

- Side navigation does not come with its own `navigation` role, because this is already provided by an enclosing [app layout component](https://cloudscape.design/components/app-layout/).
- If you wish to use side navigation outside of app layout, make sure that you wrap it inside a properly labelled `<nav>` block.
