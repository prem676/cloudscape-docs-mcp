---
title: "Radio group - Cloudscape Design System"
source: "https://cloudscape.design/components/radio-group/?tabId=api"
created: 2025-10-04
description: "Radio group enable users to choose one option from a predefined set."
---
- [Playground](https://cloudscape.design/components/radio-group/?tabId=playground)
- [Usage](https://cloudscape.design/components/radio-group/?tabId=usage)

## Development guidelines

#### State management

The radio group component is controlled. Set the `value` property and the `onChange` listener to store its value in the state of your application. Learn more about the [state management](https://cloudscape.design/get-started/dev-guides/state-management/) of Cloudscape components.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| ariaControls | ``` string ``` | Adds `aria-controls` attribute to the radio group.If the radio group controls any secondary content (for example, another form field), use this to provide an ID referring to the secondary content. | \- | \- | ``` false ``` |
| ariaDescribedby | ``` string ``` | Adds `aria-describedby` to the component. If you're using this component within a form field,don't set this property because the form field component automatically sets it.  Use this property if the component isn't surrounded by a form field, or you want to override the valueautomatically set by the form field (for example, if you have two components within a single form field).  To use it correctly, define an ID for each element that you want to use as a descriptionand set the property to a string of each ID separated by spaces (for example, `"id1 id2 id3"`). | \- | \- | ``` false ``` |
| ariaLabel | ``` string ``` | Adds `aria-label` to the group. If you are using this form element within a form field,don't set this property because the form field component automatically sets the correct labels to make the component accessible. | \- | \- | ``` false ``` |
| ariaLabelledby | ``` string ``` | Adds `aria-labelledby` to the component. If you're using this component within a form field,don't set this property because the form field component automatically sets it.  Use this property if the component isn't surrounded by a form field, or you want to override the valueautomatically set by the form field (for example, if you have two components within a single form field).  To use it correctly, define an ID for the element you want to use as label and set the property to that ID. | \- | \- | ``` false ``` |
| ariaRequired | ``` boolean ``` | Adds `aria-required` to the group. | \- | ``` false ``` | ``` false ``` |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| controlId (deprecated) | ``` string ``` | Specifies the ID of the native form element. You can use it to relatea label element's `for` attribute to this control.  It defaults to an automatically generated ID thatis provided by its parent form field component.  **Deprecated**. Has no effect. | \- | \- | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| items | ``` ReadonlyArray<RadioGroupProps.RadioButtonDefinition> ``` | Specifies an array of radio buttons to display. Each of these objects have the following properties:  - `value` (string) - Sets the value of the radio button. Assigned to the radio group when a user selects the radio button. - `label` (ReactNode) - Specifies a label for the radio button. - `description` (ReactNode) - (Optional) Specifies descriptive text that appears below the label. - `disabled` (boolean) - (Optional) Determines whether the radio button is disabled, which prevents the user from selecting it. - `controlId` (string) - (Optional) Sets the ID of the internal input. You can use it to relate a label element's `for` attribute to this control.In general it's not recommended to set this because the ID is automatically set by the radio group component. | \- | \- | ``` false ``` |
| name | ``` string ``` | Specify a custom name for the radio buttons. If not provided, the radio group generates a random name. | \- | \- | ``` false ``` |
| readOnly | ``` boolean ``` | Specifies if the whole group is read-only, which prevents theuser from modifying the value, but does not prevent the value frombeing included in a form submission. A read-only control is still focusable. | \- | ``` false ``` | ``` false ``` |
| value | ``` string \| null ``` | Sets the value of the selected radio button.If you want to clear the selection, use `null`. | \- | \- | ``` true ``` |

## Events

| Name | Detail | Description | Cancelable |
| --- | --- | --- | --- |
| onChange | ``` RadioGroupProps.ChangeDetail {   value: string } ``` | Called when the user selects a different radio button. The event `detail` contains the current `value`. | ``` false ``` |

## Functions

| Name | Description |
| --- | --- |
| focus | Sets input focus onto the UI control. |

