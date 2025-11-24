---
title: "Loading bar - Cloudscape Design System"
source: "https://cloudscape.design/components/loading-bar/?tabId=api"
created: 2025-10-07
description: "A linear loading indicator that informs the user about an ongoing operation with unknown duration."
---
- [Playground](https://cloudscape.design/components/loading-bar/?tabId=playground)
- [Usage](https://cloudscape.design/components/loading-bar/?tabId=usage)

## Development guidelines

This component comes from the new `@cloudscape-design/chat-components` NPM module. Make sure to add this module to your dependencies.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| variant | ``` string ``` | Specifies the variant of the loading bar. Use `gen-ai` to indicate an ongoing generative AI process.Use `gen-ai-masked` for generative AI processes where the bar is displayed at the edge of an elementwith rounded corners. | ``` gen-ai \| gen-ai-masked ``` | \- | ``` true ``` |
