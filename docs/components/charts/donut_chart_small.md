---
title: "Pie and donut charts - Cloudscape Design System"
source: "https://cloudscape.design/components/pie-chart/?tabId=playground&example=small-donut-chart"
created: 2025-10-03
description: "Pie and donut charts visualize the relationship or correlation between data metrics in a dataset."
---
## Pie and donut charts

Published: September 10, 2025 | Last updated: September 8, 2025

[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/chart-components/tree/main/src/pie-chart "Browse code (opens new tab)")

[View in demo](https://cloudscape.design/examples/react/dashboard.html "View in demo (opens new tab)")

These new chart components are built on top of Highcharts, which is a [commercial third-party library](https://www.highcharts.com/). Refer to the [licensing section on Charts](https://cloudscape.design/components/charts/#licensing) for more details.

- [Playground](https://cloudscape.design/components/pie-chart/?tabId=playground)
- [Usage](https://cloudscape.design/components/pie-chart/?tabId=usage)

## Configurator

### Configuration

#### Properties

 fitHeight

{

statusType:"finished",

empty:(

< div \>

< Box fontWeight \= "bold" textAlign \= "center" color \= "inherit" \>

No data available

</ Box \>

< Box textAlign \= "center" color \= "inherit" \>

({ segmentValue,totalValue }) \=>

\` ${ segmentValue } units, ${ ((segmentValue / totalValue) \* 100).toFixed (0) } % \`

{ name:"Units",

type:"donut",

data:\[{ name:"Complete",

y:160 },

{ name:"Incomplete",

y:40 }\] }

{

details:({ segmentValue,totalValue }) \=> \[

{ key:"Units",value:segmentValue },

{ key:"Percentage",value:\` ${ ((segmentValue / totalValue) \* 100).toFixed (0) } % \` },

\],

}

## Code

Due to limitations of the playground the highcharts import cannot be shown in the generated code below. You will find a proper example (with corresponding code) in the [code examples](https://cloudscape.design/components/cartesian-chart/?tabId=api#code-examples).

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`i18nStrings`.

```jsx
import * as React from "react";
import PieChart from "@cloudscape-design/chart-components/pie-chart";

export default () => {
  return (
    <PieChart
      ariaDescription="Donut chart showing generic progress."
      ariaLabel="Small donut chart"
      chartHeight={200}
      innerAreaTitle="80%"
      noData={{
        statusType: "finished",
        empty: (
          <div>
            <Box
              fontWeight="bold"
              textAlign="center"
              color="inherit"
            >
              No data available
            </Box>
            <Box textAlign="center" color="inherit">
              There is no data available
            </Box>
          </div>
        ),
        noMatch: (
          <SpaceBetween size="xs" alignItems="center">
            <div>
              <Box
                fontWeight="bold"
                textAlign="center"
                color="inherit"
              >
                No matching data
              </Box>
              <Box color="inherit">
                There is no matching data to display
              </Box>
            </div>
            <Button>Clear filter</Button>
          </SpaceBetween>
        ),
        onRecoveryClick: () => {}
      }}
      series={{
        name: "Units",
        type: "donut",
        data: [
          { name: "Complete", y: 160 },
          { name: "Incomplete", y: 40 }
        ]
      }}
      tooltip={{
        details: ({ segmentValue, totalValue }) => [
          { key: "Units", value: segmentValue },
          {
            key: "Percentage",
            value: \`${(
              (segmentValue / totalValue) *
              100
            ).toFixed(0)}%\`
          }
        ]
      }}
    />
  );
}
```
