---
title: "Collection preferences - Cloudscape Design System"
source: "https://cloudscape.design/components/collection-preferences/?tabId=playground"
created: 2025-11-21
description: "With collection preferences, users can manage their display preferences within a collection."
tags:
  - "clippings"
---
- [Playground](https://cloudscape.design/components/collection-preferences/?tabId=playground)
- [API](https://cloudscape.design/components/collection-preferences/?tabId=api)
- [Testing](https://cloudscape.design/components/collection-preferences/?tabId=testing)
- [Usage](https://cloudscape.design/components/collection-preferences/?tabId=usage)

## Configurator

### Configuration

#### Properties

 disabled

{

pageSize:10,

wrapLines:true,

stickyColumns:{ first:1,last:0 }

}

{

options:\[

{ value:10,label:'10 resources' },

{ value:20,label:'20 resources' }

\]

}

{ }

{ }

{ }

{

options:\[

{

id:'id',

label:'Distribution ID',

alwaysVisible:true

},

{ id:'domainName',label:'Domain name' },

{

firstColumns:{

title:'Stick first column(s)',

description:'Keep the first column(s) visible while horizontally scrolling the table content.',

options:\[

{ label:'None',value:0 },

{ label:'First column',value:1 },

{ label:'First two columns',value:2 },

#### Slots

Use React and JSX syntax only.

## Preview

## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`cancelLabel`, `closeAriaLabel`, `confirmLabel`, `contentDensityPreference`, `contentDisplayPreference`, `pageSizePreference`, `stripedRowsPreference`, `title`, `wrapLinesPreference`.

```jsx
import * as React from "react";
import CollectionPreferences from "@cloudscape-design/components/collection-preferences";

export default () => {
  const [preferences, setPreferences] = React.useState({
    pageSize: 10,
    wrapLines: true,
    stickyColumns: { first: 1, last: 0 }
  });
  return (
    <CollectionPreferences
      onConfirm={({ detail }) => setPreferences(detail)}
      preferences={preferences}
      pageSizePreference={{
        options: [
          { value: 10, label: "10 resources" },
          { value: 20, label: "20 resources" }
        ]
      }}
      wrapLinesPreference={{}}
      stripedRowsPreference={{}}
      contentDensityPreference={{}}
      contentDisplayPreference={{
        options: [
          {
            id: "id",
            label: "Distribution ID",
            alwaysVisible: true
          },
          { id: "domainName", label: "Domain name" },
          {
            id: "deliveryMethod",
            label: "Delivery method"
          },
          { id: "priceClass", label: "Price class" },
          {
            id: "sslCertificate",
            label: "SSL certificate"
          },
          { id: "origin", label: "Origin" }
        ]
      }}
      stickyColumnsPreference={{
        firstColumns: {
          title: "Stick first column(s)",
          description:
            "Keep the first column(s) visible while horizontally scrolling the table content.",
          options: [
            { label: "None", value: 0 },
            { label: "First column", value: 1 },
            { label: "First two columns", value: 2 }
          ]
        },
        lastColumns: {
          title: "Stick last column",
          description:
            "Keep the last column visible while horizontally scrolling the table content.",
          options: [
            { label: "None", value: 0 },
            { label: "Last column", value: 1 }
          ]
        }
      }}
    />
  );
}
```
