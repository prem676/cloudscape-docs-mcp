---
title: "Global styles - Cloudscape Design System"
source: "https://cloudscape.design/get-started/integration/global-styles/"
author:
published:
created: 2025-06-07
description: "Use the Cloudscape global styles package to apply foundational CSS to pages."
tags:
  - "clippings"
---
## Overview

The Cloudscape global styles package (`@cloudscape-design/global-styles`) offers:

- [Global CSS styles](https://cloudscape.design/get-started/integration/global-styles/#apply-global-styles) (`@font-face` for Open Sans font)
- [JavaScript utilities to set visual and content density modes](https://cloudscape.design/get-started/integration/global-styles/#manipulate-global-styles-using-js-helpers)
- [Global CSS utility classes for dark mode](https://cloudscape.design/get-started/integration/global-styles/#dark-mode-global-utility-classes)

## Installation

This package is provided with the npm module: `@cloudscape-design/global-styles`

For more information, see the [package installation guide](https://cloudscape.design/get-started/integration/using-cloudscape-components/).

```
npm install @cloudscape-design/global-styles
```

The global styles package offers global CSS styles, including [normalize](https://www.npmjs.com/package/normalize.css?activeTab=versions) and [Open Sans font](https://fonts.google.com/specimen/Open+Sans) files. To have Cloudscape components display correctly, import the global CSS file:

```
import '@cloudscape-design/global-styles/index.css';
```

To avoid duplication of assets, make sure you have only one import of this module in your project.

The global styles package exposes a JavaScript module (global-styles.js) with helpers that allow to set visual and content density modes, as well as a function to disable motion.

### Visual modes

| Name | Type | Description | Accepted values | Default |
| --- | --- | --- | --- | --- |
| applyMode | ``` (mode: Mode) => void ``` | Sets the color [mode](https://cloudscape.design/foundation/visual-foundation/visual-modes/). | ``` Mode.Light, Mode.Dark ``` | ``` Mode.Light ``` |
| applyDensity | ``` (density: Density) => void ``` | Sets the [content density](https://cloudscape.design/foundation/visual-foundation/content-density/). | ``` Density.Comfortable, Density.Compact ``` | ``` Density.Comfortable ``` |
| Density | ``` enum ``` | Definition for content densities. | ``` Comfortable, Compact ``` | ``` Comfortable ``` |
| Mode | ``` enum ``` | Definition for color modes. | ``` Light, Dark ``` | ``` Light ``` |

#### Code example

```
import { applyMode, applyDensity, Density, Mode } from '@cloudscape-design/global-styles';

// apply a color mode
applyMode(Mode.Dark);
applyMode(Mode.Light);

// apply a content density mode
applyDensity(Density.Compact);
applyDensity(Density.Comfortable);
```

### Motion

| Name | Type | Description | Accepted values | Default |
| --- | --- | --- | --- | --- |
| disableMotion | ``` (isDisabled: boolean) => void ``` | Turns off [motion effects](https://cloudscape.design/foundation/visual-foundation/motion/). | \- | false |

#### Code example

```
import { disableMotion } from '@cloudscape-design/global-styles';

disableMotion(true);
```

To [implement dark mode](https://cloudscape.design/foundation/visual-foundation/visual-modes/#implementation-and-demos) in your application, you might need to adjust some visual content. For example, you might want to display two different versions of an image depending on the mode.

To do that, you can use the following global CSS classes provided by the `dark-mode-utils.css` artifact in `@cloudscape-design/global-styles`.

| Class | Description |
| --- | --- |
| ``` awsui-util-show-in-dark-mode ``` | Makes the content visible in the dark mode. |
| ``` awsui-util-hide-in-dark-mode ``` | Makes the content hidden in the dark mode. |

### Usage example

```
import '@cloudscape-design/global-styles/dark-mode-utils.css';
...
<div>
  <img className="awsui-util-hide-in-dark-mode" src="./light-image.png" />
  <img className="awsui-util-show-in-dark-mode" src="./dark-image.png" />
</div>
```

In the previous example, there are two images, where the image with `awsui-util-hide-in-dark-mode` class name will be hidden when the dark mode is on and visible in the light mode. The image with `awsui-util-show-in-dark-mode` class name becomes visible in the dark mode and hidden in the light mode.
