---
title: "Drawer - Cloudscape Design System"
source: "https://cloudscape.design/components/drawer/?tabId=api"
created: 2025-10-23
description: "A panel that displays supplementary content on a page, which supports task completion or feature access."
---
- [Playground](https://cloudscape.design/components/drawer/?tabId=playground)
- [Usage](https://cloudscape.design/components/drawer/?tabId=usage)

## Development guidelines

#### App layout

- Place drawer content in the content slot of the `drawers` property of the [app layout](https://cloudscape.design/components/app-layout/) component. The app layout will provide the dismiss icon and toggle functionality.
- To allow users to adjust the size of the drawer, set the `resizable` value to true on the `drawers` property of the app layout. The component will set the maximum and minimum size when resizing the drawer and remembers the adjusted size when users close and reopen the drawer. If you need to override the default drawer width provided by the app layout, modify the `defaultSize` value on the `drawers` property of the app layout.
- Don’t disable the functionality to close the drawer, even when there is only one state of content.
- When the user closes the drawer and later reopens it within the same page view, the content should remain the same as what was previously shown. The content should not automatically switch back to the default content.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| disableContentPaddings | ``` boolean ``` | Determines whether the drawer content has padding. If `true`, removes the default padding from the content area. | \- | ``` false ``` | ``` false ``` |
| i18nStrings | ``` I18nStrings {   loadingText?: string } ``` | An object containing all the necessary localized strings required by the component.  **Note:** The property is part of [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/).This property is automatically provided if the application uses Cloudscape's I18nProvider. | \- | \- | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| loading | ``` boolean ``` | Renders the drawer in a loading state. We recommend that you also set a `loadingText`. | \- | ``` false ``` | ``` false ``` |

## Slots

| Name | Description |
| --- | --- |
| content (default) | Main content of the drawer.  **Default slot:** Specify the content as a child of the component. |
| header | Header of the drawer.  It should contain the only `h2` used in the drawer. |
| headerActions | Actions for the header. Available only if you specify the `header` property. |
