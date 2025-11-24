---
title: "Side navigation - Cloudscape Design System"
source: "https://cloudscape.design/components/side-navigation/?tabId=playground&example=with-sections"
created: 2025-11-21
description: "A list of navigational links that point to the pages within an application."
---
- [Playground](https://cloudscape.design/components/side-navigation/?tabId=playground)
- [API](https://cloudscape.design/components/side-navigation/?tabId=api)
- [Testing](https://cloudscape.design/components/side-navigation/?tabId=testing)
- [Usage](https://cloudscape.design/components/side-navigation/?tabId=usage)

## Configurator

### Configuration

## Code

```jsx
import * as React from "react";

export default () => {
  const [activeHref, setActiveHref] = React.useState(
    "#/page2"
  );
  return (
    <SideNavigation
      activeHref={activeHref}
      onFollow={event => {
        if (!event.detail.external) {
          event.preventDefault();
          setActiveHref(event.detail.href);
        }
      }}
      items={[
        { type: "link", text: "Page 1", href: "#/page1" },
        { type: "link", text: "Page 2", href: "#/page2" },
        {
          type: "section",
          text: "Section 1",
          items: [
            {
              type: "link",
              text: "Page 4",
              href: "#/page4"
            },
            {
              type: "link",
              text: "Page 5",
              href: "#/page5"
            },
            {
              type: "link",
              text: "Page 6",
              href: "#/page6"
            }
          ]
        },
        {
          type: "section",
          text: "Section 2",
          items: [
            {
              type: "link",
              text: "Page 7",
              href: "#/page7"
            },
            {
              type: "link",
              text: "Page 8",
              href: "#/page8"
            },
            {
              type: "link",
              text: "Page 9",
              href: "#/page9"
            }
          ]
        }
      ]}
    />
  );
}
```