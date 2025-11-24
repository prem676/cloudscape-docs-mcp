---
title: "Modal - Cloudscape Design System"
source: "https://cloudscape.design/components/modal/?tabId=api"
created: 2025-10-09
description: "A user interface element subordinate to an application's main window. It prevents interaction with the main page content, but keeps it visible with the modal as a child window in front of it."
---
## Modal

Published: May 4, 2020

[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/components/tree/main/src/modal "Browse code (opens new tab)")

- [Playground](https://cloudscape.design/components/modal/?tabId=playground)
- [Usage](https://cloudscape.design/components/modal/?tabId=usage)

## Development guidelines

#### Testing

By default, modals are rendered to the document root. To find this component using test-utils, you need to start from the document root, for example: `createWrapper(document.body).findModal()`.

#### Alternative modal roots

By default, the Modal component renders its content directly to `document.body` using [React portal API](https://react.dev/reference/react-dom/createPortal). This behavior can be customized in two ways:

- Use `modalRoot` property if you experience rendering issues, for example due to `z-index` conflicts. Then you can manually create a DOM container on your page, and style it accordingly.
- Use `getModalRoot` and `removeModalRoot` to add and remove modal root container on demand. This can be useful when rendering modals inside iframes when you would like to render it in a different frame to ensure it renders full screen. Note that `getModalRoot` is called even if the `visible` property is set to `false`. Render the whole modal conditionally if you want to avoid this.

#### footer slot

If you want to place multiple buttons in the `footer` slot, use the [space between](https://cloudscape.design/components/space-between/) component to add horizontal spacing between them.

#### State management

The Modal component is controlled. Set the `visible` property and the `onDismiss` listener to control its visibility. Learn more about the [state management](https://cloudscape.design/get-started/dev-guides/state-management/) of Cloudscape components.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| analyticsMetadata | ``` ModalProps.AnalyticsMetadata {   flowType?: string   instanceIdentifier?: string   resourceType?: string } ``` | Specifies additional analytics-related metadata.  - `instanceIdentifier` - A unique string that identifies this component instance in your application. - `flowType` - Identifies the type of flow represented by the component. - `resourceType` - Identifies the type of resource represented by the flow. **Note:** This API is currently experimental. Used internally in AWS. | \- | \- | ``` false ``` |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| closeAriaLabel | ``` string ``` | Adds an `aria-label` to the close button, for accessibility.  **Note:** The property is part of [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/).This property is automatically provided if the application uses Cloudscape's I18nProvider. | \- | \- | ``` false ``` |
| disableContentPaddings | ``` boolean ``` | Determines whether the modal content has padding. If `true`, removes the default padding from the content area. | \- | ``` false ``` | ``` false ``` |
| getModalRoot | ``` () => Promise<HTMLElement> ``` | Use this property to specify a different dynamic modal root for the dialog.The function will be called when a user clicks on the trigger button. | \- | \- | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| modalRoot | ``` HTMLElement ``` | Specifies the HTML element where the modal is rendered.If neither `modalRoot` or `getModalRoot` properties are provided, the modal willrender to an element under `document.body`. | \- | \- | ``` false ``` |
| removeModalRoot | ``` (rootElement: HTMLElement) => void ``` | Use this property when `getModalRoot` is used to clean up the modal rootelement after a user closes the dialog. The function receives the return valueof the most recent getModalRoot call as an argument. | \- | \- | ``` false ``` |
| size | ``` string ``` | Sets the width of the modal. `max` uses variable width up to thelargest size allowed by the design guidelines. Other sizes(`small` / `medium` / `large`) have fixed widths. | ``` small \| max \| medium \| large ``` | ``` 'medium' ``` | ``` false ``` |
| visible | ``` boolean ``` | Determines whether the modal is displayed on the screen. Modals are hidden by default.Set this property to `true` to show them. | \- | ``` false ``` | ``` true ``` |

## Slots

| Name | Description |
| --- | --- |
| content (default) | Body of the modal.  **Default slot:** Specify the content as a child of the component. |
| footer | Specifies a footer for the modal. If empty, the footer isn't displayed. |
| header | Specifies a title for the modal. Although this can be empty, we suggest that you always provide a title. |

## Events

| Name | Detail | Description | Cancelable |
| --- | --- | --- | --- |
| onDismiss | ``` ModalProps.DismissDetail {   reason: string } ``` | Called when a user closes the modal by using the close icon button,clicking outside of the modal, or pressing ESC.The event detail contains the `reason`, which can be any of the following:`['closeButton', 'overlay', 'keyboard']`. | ``` false ``` |
