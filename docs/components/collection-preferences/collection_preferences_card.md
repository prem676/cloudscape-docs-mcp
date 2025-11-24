---
title: "Collection preferences - Cloudscape Design System"
source: "https://cloudscape.design/components/collection-preferences/?tabId=playground&example=cards-preferences"
created: 2025-11-21
description: "With collection preferences, users can manage their display preferences within a collection."
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

visibleContent:\['id','domainName','deliveryMethod'\]

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

title:'Select visible content',

options:\[

{

label:'Main distribution properties',

options:\[

{ id:'id',label:'Distribution ID',editable:false },

{ id:'domainName',label:'Domain name' },

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

() \=> (

< FormField label \= "View as" \>

< RadioGroup

value \= "cards"

items \= { \[

{ value:'table',label:'Table' },

{ value:'cards',label:'Cards' },

\] }

#### Slots

Use React and JSX syntax only.

## Code

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`cancelLabel`, `closeAriaLabel`, `confirmLabel`, `contentDensityPreference`, `contentDisplayPreference`, `pageSizePreference`, `stripedRowsPreference`, `title`, `wrapLinesPreference`.

```jsx
import * as React from "react";
import CollectionPreferences from "@cloudscape-design/components/collection-preferences";

export default () => {
  const [preferences, setPreferences] = React.useState({
    pageSize: 10,
    visibleContent: ["id", "domainName", "deliveryMethod"]
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
      visibleContentPreference={{
        title: "Select visible content",
        options: [
          {
            label: "Main distribution properties",
            options: [
              {
                id: "id",
                label: "Distribution ID",
                editable: false
              },
              { id: "domainName", label: "Domain name" },
              {
                id: "deliveryMethod",
                label: "Delivery method"
              }
            ]
          },
          {
            label: "Secondary distribution properties",
            options: [
              { id: "priceClass", label: "Price class" },
              {
                id: "sslCertificate",
                label: "SSL certificate"
              },
              { id: "origin", label: "Origin" }
            ]
          }
        ]
      }}
      customPreference={() => (
        <FormField label="View as">
          <RadioGroup
            value="cards"
            items={[
              { value: "table", label: "Table" },
              { value: "cards", label: "Cards" }
            ]}
          />
        </FormField>
      )}
    />
  );
}
```
