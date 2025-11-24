---
title: "Container - Cloudscape Design System"
source: "https://cloudscape.design/components/container/?tabId=usage"
created: 2025-10-01
description: "With the container, you can present a group of pieces of content, indicating that the items are related. For example, a table is a type of container."
---
[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/components/tree/main/src/container "Browse code (opens new tab)")

- [Playground](https://cloudscape.design/components/container/?tabId=playground)
- [Usage](https://cloudscape.design/components/container/?tabId=usage)

## General guidelines

### Do

- Use vertical and horizontal lines to separate pieces of content, if necessary.
- Use a container to group similar items or display a list of attributes for a single item.
- When a container includes media and text, provide enough space for the text content, to ensure readability. Optimal ratios are 2/3 text and 1/3 media, or half text and half media.
- In a collection view where containers are displayed next to each other, use the same height for media.
- For optimal display of media elements within narrow containers, position the media at the top. This arrangement allows more room for text content, enhancing readability.

## Features

- #### Header - optional
	Use the header to display the title of the container. Additionally, you can include information and actions that apply to the entire content of the container, such as description, action stripe, counter, or an info link.

	The h2 variant of the [header](https://cloudscape.design/components/header/?example=container-header) component is designed to be used in this component.
- #### Content
	The area for primary container content. Common content types of a container are:
	- [Form fields](https://cloudscape.design/components/form-field/?example=default) for [creation](https://cloudscape.design/patterns/resource-management/create/) and [edit](https://cloudscape.design/patterns/resource-management/edit/) flows. Use the main content of a container for primary and required fields of a single item's configuration.
	- [Key-value pairs](https://cloudscape.design/components/key-value-pairs/) for [detail](https://cloudscape.design/patterns/resource-management/details/) pages. Use the main content area to display key-value pairs that describe a single item's configuration.
	- [Charts](https://cloudscape.design/components/charts/) for [dashboard](https://cloudscape.design/patterns/general/service-dashboard/) pages. Use the main content area to display the visualization.
	- [Tables](https://cloudscape.design/components/table/?example=common-table) that are displayed with other content, such as [key-value pairs](https://cloudscape.design/components/key-value-pairs/) and supporting text. Use the `embedded variant` of the table in this case.
- #### Footer - optional
	Use a footer for secondary content. For example, in a [creation flow](https://cloudscape.design/patterns/resource-management/create/), this area often contains an [expandable section](https://cloudscape.design/components/expandable-section/?example=footer) with advanced configuration options. Alternatively, the [details as a hub](https://cloudscape.design/patterns/resource-management/details/details-page-as-hub/) pattern uses this area for a *View all* link that takes the user to a new page with the complete items list.
	The footer can also contain elements like [button icons](https://cloudscape.design/components/button/?tabId=playground&example=icon-button) (for example, share or download).
- #### Media - optional
	- Optimized for content-oriented containers. Using the media feature allows displaying integrated images like photos and video thumbnails. You can define different placements and sizes of integrated images:
	- The dimensions and position of media content, such as images, can be tailored within a container. You can specify the height, width, position (top or side).
	- By default, an image stretches to fill the full width of the container when positioned at the top, or the full height when positioned on the side. To crop images, you can set a custom value for height or width as needed. However, ensure that essential elements remain visible to users and aren't unintentionally cropped out of the view.
	- For best results consider using 16:9 and 4:3 formats for large images, and 1:1 format for icons. The image will be cropped if the height/width specified don't match the aspect ratio of the image.
	- Video thumbnails can be linked to the video player page or trigger a custom action (e.g.: open a modal).
- #### Variant
	- **Default**: used in standalone context.
	- **Stacked**: optimized to be displayed adjacent to other stacked components, see an example of [key-value pairs in a container with a table](https://cloudscape.design/components/key-value-pairs/).

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
	- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
	- For example: use *choose* or *interact* not *click*.

## Accessibility guidelines

- Follow the guidelines on alternative text and Accessible Rich Internet Applications (ARIA) regions for each component.
- Make sure to define ARIA labels aligned with the language context of your application.
- Don't add unnecessary markup for roles and landmarks. Follow the guidelines for each component.
- Provide keyboard functionality to all available content in a logical and predictable order. The flow of information should make sense.
- Provide alternative text that describes the function or purpose of the image. Ideally, the alternative text should provide instructive information that would be missed if a person cannot see the image. If the image is purely decorative, use the respective ARIA presentation role instead.
	- If the image is accompanied by text in the container that describes it sufficiently, there is no need to add alternative text to the image itself.
	- When providing alternative text, make sure to follow the [alternative text guidelines.](https://cloudscape.design/foundation/core-principles/accessibility/#alternative-text)
- If the image has important visual cues or content that needs to be exposed to the user (such as text) make sure it’s not cropped when the screen size changes.

