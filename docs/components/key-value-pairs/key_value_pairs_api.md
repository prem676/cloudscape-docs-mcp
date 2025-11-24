---
title: "Key-value pairs - Cloudscape Design System"
source: "https://cloudscape.design/components/key-value-pairs/?tabId=api"
created: 2025-10-03
description: "Key-value pairs are lists of properties (labels) followed by their corresponding values."
---
- [Playground](https://cloudscape.design/components/key-value-pairs/?tabId=playground)
- [Usage](https://cloudscape.design/components/key-value-pairs/?tabId=usage)

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| ariaLabel | ``` string ``` | Provides an `aria-label` to the Key-value pairs container.Don't use `ariaLabel` and `ariaLabelledby` at the same time. | \- | \- | ``` false ``` |
| ariaLabelledby | ``` string ``` | Sets the `aria-labelledby` property on the Key-value pairs container.If there's a visible label element that you can reference, use this instead of `ariaLabel`.Don't use `ariaLabel` and `ariaLabelledby` at the same time. | \- | \- | ``` false ``` |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| columns | ``` number ``` | Specifies the number of columns in each grid row.Valid values are any integer between 1 and 4. It defaults to 1. | \- | ``` 1 ``` | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| items | ``` ReadonlyArray<KeyValuePairsProps.Item> ``` | An array of either key-value pairs individual items or groups.They could be combined.Each item has `type` prop, which might be either `group` or `pair`. Defaults to `pair` if not specified.  Each key-value pair definition has the following properties:  - `type` (string) - (Optional) Item type (pair). - `label` (React.ReactNode) - The key label. - `info` (React.ReactNode) - (Optional) Area next to the key to display an info link. - `value` (React.ReactNode) - The corresponding value for the key.  Each group definition has the following properties:  - `type` (string) - Item type (group). - `title` (string) - (Optional) An optional title for this column. - `items` (ReadonlyArray<KeyValuePairProps.KeyValuePair>) - An array ofkey-value pair items. | \- | \- | ``` true ``` |
| minColumnWidth | ``` number ``` | Use to specify the desired minimum width for each column in pixels.  The number of columns is determined by the value of this property, the available space,and the maximum number of columns as defined by the `columns` property.If not set, defaults to 150. | \- | ``` 150 ``` | ``` false ``` |
