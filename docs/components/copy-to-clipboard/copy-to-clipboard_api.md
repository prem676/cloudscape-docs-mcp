---
title: "Copy to clipboard - Cloudscape Design System"
source: "https://cloudscape.design/components/copy-to-clipboard/?tabId=api"
created: 2025-10-13
description: "With copy to clipboard, users can copy content to their clipboard."
---
- [Playground](https://cloudscape.design/components/copy-to-clipboard/?tabId=playground)
- [Usage](https://cloudscape.design/components/copy-to-clipboard/?tabId=usage)

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| className (deprecated) | ``` string ``` | Adds the specified classes to the root element of the component.  **Deprecated**. Custom CSS is not supported. For testing and other use cases, use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). | \- | \- | ``` false ``` |
| copyButtonAriaLabel | ``` string ``` | Adds `aria-label` to the copy button. Use this to provide an accessible name for buttons that don't have visible text,and to distinguish between multiple buttons with identical visible text. The text will also be added to the `title` attribute of the button. | \- | \- | ``` false ``` |
| copyButtonText | ``` string ``` | The text of the copy button (for variant="button"). | \- | \- | ``` false ``` |
| copyErrorText | ``` string ``` | The message shown when the text is not copied due to an error, see [https://w3c.github.io/clipboard-apis/#dom-clipboard-writetext](https://w3c.github.io/clipboard-apis/#dom-clipboard-writetext). | \- | \- | ``` true ``` |
| copySuccessText | ``` string ``` | The message shown when the text is copied successfully. | \- | \- | ``` true ``` |
| disabled | ``` boolean ``` | Renders the copy to clipboard button as disabled and prevents clicks. | \- | ``` false ``` | ``` false ``` |
| disabledReason | ``` string ``` | Provides a reason why the copy to clipboard button is disabled (only when `disabled` is `true`).If provided, the copy to clipboard button becomes focusable.Applicable for all variants except inline. | \- | \- | ``` false ``` |
| id (deprecated) | ``` string ``` | Adds the specified ID to the root element of the component.  **Deprecated**. The usage of the `id` attribute is reserved for internal use cases. For testing and other use cases,use [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). If you mustuse the `id` attribute, consider setting it on a parent element instead. | \- | \- | ``` false ``` |
| popoverRenderWithPortal | ``` boolean ``` | By default, the popover is constrained to fit inside its parent [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).Enabling this property will allow the popover to be rendered in the root stack context using [React Portals](https://reactjs.org/docs/portals.html).Enable this setting if you need the popover to ignore its parent stacking context. | \- | ``` false ``` | ``` false ``` |
| textToCopy | ``` string ``` | The text content to be copied. It is displayed next to the copy button when `variant="inline"` unless when `content` is specified, and is not shown otherwise. | \- | \- | ``` true ``` |
| textToDisplay | ``` string ``` | The text content to display next to the copy button when `variant="inline"`. If not provided, `textToCopy` will be displayed instead. | \- | \- | ``` false ``` |
| variant | ``` string ``` | Determines the general styling of the copy button as follows:  - `button` to display a standalone secondary button with an icon, and `copyButtonText` as text. - `icon` to display a standalone icon-only (no text) button. - `inline` to display an icon-only (no text) button within a text context.  Defaults to `button`. | ``` inline \| button \| icon ``` | ``` 'button' ``` | ``` false ``` |
