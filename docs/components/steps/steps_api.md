---
title: "Steps - Cloudscape Design System"
source: "https://cloudscape.design/components/steps/?tabId=api"
created: 2025-10-07
description: "Display a list of tasks."
---
- [Playground](https://cloudscape.design/components/steps/?tabId=playground)
- [Usage](https://cloudscape.design/components/steps/?tabId=usage)

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| ariaDescribedby | ``` string ``` | Sets the `aria-describedby` property on the progress steps container. | \- | \- | ``` false ``` |
| ariaLabel | ``` string ``` | Provides an `aria-label` to the progress steps container.Don't use `ariaLabel` and `ariaLabelledby` at the same time. | \- | \- | ``` false ``` |
| ariaLabelledby | ``` string ``` | Sets the `aria-labelledby` property on the progress steps container.If there's a visible label element that you can reference, use this instead of `ariaLabel`.Don't use `ariaLabel` and `ariaLabelledby` at the same time. | \- | \- | ``` false ``` |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| steps | ``` ReadonlyArray<StepsProps.Step> ``` | An array of individual steps  Each step definition has the following properties:  - `status` (string) - Status of the step corresponding to a status indicator. - `statusIconAriaLabel` - (string) - (Optional) Alternative text for the status icon. - `header` (ReactNode) - Summary corresponding to the step. - `details` (ReactNode) - (Optional) Additional information corresponding to the step. | \- | \- | ``` true ``` |