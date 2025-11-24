---
title: "Loading bar - Cloudscape Design System"
source: "https://cloudscape.design/components/loading-bar/?tabId=usage"
created: 2025-10-07
description: "A linear loading indicator that informs the user about an ongoing operation with unknown duration."
---

- [Playground](https://cloudscape.design/components/loading-bar/?tabId=playground)
- [Usage](https://cloudscape.design/components/loading-bar/?tabId=usage)

## General guidelines

### Do

- Show loading text next to the loading bar to inform users about the ongoing operation. Refer to [generative AI loading states](https://cloudscape.design/patterns/genai/genai-loading-states/) for more guidelines.

### Don't

- Avoid using the loading bar for non-generative AI use cases. The loading bar is currently styled for usage in generative AI use cases only.

## Features

- #### Variant
  - **Generative AI -** Use when bar is placed inside an element. For example, center of a [container](https://cloudscape.design/components/container/).
  - **Generative AI with mask -** Use when bar is placed next to the edge of elements that have rounded corners. For example, bottom of a chat bubble.

## Writing guidelines

Follow the writing guidelines for [generative AI loading states](https://cloudscape.design/patterns/genai/genai-loading-states/).

## Accessibility guidelines

You can ensure status changes are announced to users by wrapping a [live region component](https://cloudscape.design/components/live-region/).

### Preview

Generating a response

### Code

The following code uses React and JSX syntax.

```jsx
import React from 'react';
import { Box, LiveRegion } from '@cloudscape-design/components';
import LoadingBar from '@cloudscape-design/chat-components/loading-bar';

const GenAILoading = () => {
  return (
    <LiveRegion>
      <Box margin={{ bottom: 'xs', left: 'l' }} color="text-body-secondary">
        Generating a response
      </Box>
      <LoadingBar variant="gen-ai" />
    </LiveRegion>
  );
};

export default GenAILoading;
```
