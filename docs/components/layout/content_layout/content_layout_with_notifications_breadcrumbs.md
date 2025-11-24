---
title: "Content layout - Cloudscape Design System"
source: "https://cloudscape.design/components/content-layout/?tabId=playground&example=with-notifications-and-breadcrumbs"
created: 2025-10-01
description: "Provides page structure for expressive use cases."
---

- [Playground](https://cloudscape.design/components/content-layout/?tabId=playground)
- [Usage](https://cloudscape.design/components/content-layout/?tabId=usage)

## Code

```jsx
import * as React from "react";
import ContentLayout from "@cloudscape-design/components/content-layout";
import BreadcrumbGroup from "@cloudscape-design/components/breadcrumb-group";
import Container from "@cloudscape-design/components/container";
import Header from "@cloudscape-design/components/header";
import Link from "@cloudscape-design/components/link";
import Flashbar from "@cloudscape-design/components/flashbar";
import Button from "@cloudscape-design/components/button";

export default () => {
  return (
    <ContentLayout
      defaultPadding
      disableOverlap
      breadcrumbs={
        <BreadcrumbGroup
          items={[
            { text: "System", href: "#" },
            { text: "Components", href: "#components" },
            {
              text: "Breadcrumb group",
              href: "#components/breadcrumb-group"
            }
          ]}
          ariaLabel="Breadcrumbs"
        />
      }
      header={
        <Header
          variant="h1"
          info={<Link variant="info">Info</Link>}
          description="This is a generic description used in the header."
        >
          Header
        </Header>
      }
      notifications={
        <Flashbar
          items={[
            {
              type: "success",
              content: "This is a success flash message.",
              action: <Button>View instance</Button>,
              dismissible: true,
              dismissLabel: "Dismiss message",
              id: "message_1"
            }
          ]}
        />
      }
    >
      <Container
        header={
          <Header
            variant="h2"
            description="Container description"
          >
            Container header
          </Header>
        }
      >
        Container content
      </Container>
    </ContentLayout>
  );
}
```
