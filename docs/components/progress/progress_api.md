---
title: "Progress bar - Cloudscape Design System"
source: "https://cloudscape.design/components/progress-bar/?tabId=api"
created: 2025-10-07
description: "Informs the user about the progress of an operation with a known duration."
---
- [Playground](https://cloudscape.design/components/progress-bar/?tabId=playground)
- [Usage](https://cloudscape.design/components/progress-bar/?tabId=usage)

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| ariaDescribedby | ``` string ``` | Adds `aria-describedby` to the progress bar. | \- | \- | ``` false ``` |
| ariaLabel | ``` string ``` | Adds an `aria-label` to the progress bar. | \- | \- | ``` false ``` |
| ariaLabelledby | ``` string ``` | Adds `aria-labelledby` to the progress bar. | \- | \- | ``` false ``` |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| resultButtonText | ``` string ``` | Specifies the text for the button that's displayed when the `status` is set to `error` or `success`.If `resultButtonText` is empty, the result button isn't displayed.  Note: If you use the `flash` variant, the result button isn't displayed.Add a button using the `action` property of the flashbar item instead. | \- | \- | ``` false ``` |
| status | ``` string ``` | Specifies the status of the progress bar. You can set it to one of the following:  - `"in-progress"` - Displays a progress bar. - `"success"` or `"error"` - Displays a result state and replaces the progress element with a status indicator,`resultText`, and a result button. | ``` error \| in-progress \| success ``` | ``` 'in-progress' ``` | ``` false ``` |
| value | ``` number ``` | Indicates the current progress as a percentage. The value must be between 0 and 100. Decimals are rounded. | \- | ``` 0 ``` | ``` false ``` |
| variant | ``` string ``` | Enables the correct styling of the progress bar in different contexts. You can set it to one of the following:  - `"flash"` - Use this variatn when using the progress bar within a flash component.Note that the result button isn't displayed when using this variant.Use the `buttonText` property and the `onButtonClick` event listener of the flashbar item instead of the result button provided by the progress bar. - `"key-value"` - Use this variant when using the progress bar within the key-value pairs pattern. - `"standalone"` Use in all other cases. This is the default value. | ``` flash \| standalone \| key-value ``` | ``` 'standalone' ``` | ``` false ``` |

## Slots

| Name | Description |
| --- | --- |
| additionalInfo | Information that's displayed below the progress bar or status text. |
| description | More detailed information about the operation that appears below the label. |
| label | Short description of the operation that appears at the top of the component.  Make sure that you always provide a label for accessibility. |
| resultText | Content that's displayed when `status` is set to `error` or `success`. |

## Events

| Name | Detail | Description | Cancelable |
| --- | --- | --- | --- |
| onResultButtonClick |  | Called when the user clicks the result state button.  Note: If you are using the `flash` variant, the result button isn't displayed.Use the `buttonText` property and the `onButtonClick` event listener of the flashbar item instead. | ``` false ``` |
