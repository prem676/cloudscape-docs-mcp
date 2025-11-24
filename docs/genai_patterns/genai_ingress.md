---
title: "Ingress - Cloudscape Design System"
source: "https://cloudscape.design/patterns/genai/ingress/"
created: 2025-10-07
description: "An interactive element such as a button that lets users engage a generative AI-powered feature."
---
As explained in the generative AI pattern abstraction, ingress is the the first time a user comes across a generative AI feature (for example, enabling a generative AI feature or entering a playground). To ensure users identify this action button amid other non-generative AI actions on a page, generative AI affordance for buttons is used.

Certain generative AI experiences leverage product-specific visual branding, such as iconography. In order to determine if your product needs to be branded with product specific iconography, work with your product managers and team leadership.

## Development guidelines

Refer to the code examples below for the primary and secondary [buttons](https://cloudscape.design/components/button/) when used in the context of generative AI.

```jsx
<Button variant="primary" iconAlign="left" iconName="gen-ai" ariaLabel="Generative AI - Primary button">
  Primary button
</Button>
```

```jsx
<Button iconAlign="left" iconName="gen-ai" ariaLabel="Generative AI - Normal button">
  Normal button
</Button>
```

## General guidelines

## Writing guidelines

- Use sentence case, but continue to capitalize proper nouns and brand names correctly in context.
- Use end punctuation, except in [headers](https://cloudscape.design/components/header/?tabId=usage) and [buttons](https://cloudscape.design/components/button/?tabId=usage). Don’t use exclamation points.
- Use present-tense verbs and active voice.
- Don't use *please*, *thank you*, ellipsis (*...*), ampersand (*&*), *e.g.*, *i.e.*, or *etc.* in writing.
- Avoid directional language.
	- For example: use *previous* not *above*, use *following* not *below*.
- Use device-independent language.
	- For example: use *choose* or *select* not *click*.

### Component-specific guidelines

#### Terminology

- **Introducing the AI:** *generative AI assistant* is the approved term for introducing and referring to the AI, and *generative AI* to refer to the experience.
- **User queries:** use *submit* as the label or reference term when a user is making a choice, query, or request.
- **AI replies:** refer to AI replies as *responses*, not *answers*.

#### Button text

- Follow the writing guidelines for [button](https://cloudscape.design/components/button/?tabId=usage#writing-guidelines).
