---
title: "Cartesian charts - Cloudscape Design System"
source: "https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart%3A-with-sub-items"
created: 2025-10-03
description: "Cartesian charts display information along horizontal and vertical axes to clearly show patterns, comparisons, and relationships between values. It includes line, bar, area, scatter, and mixed charts."
---
## Cartesian charts

Published: September 10, 2025 | Last updated: September 8, 2025

[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/chart-components/tree/main/src/cartesian-chart "Browse code (opens new tab)")

[View in demo](https://cloudscape.design/examples/react/dashboard.html "View in demo (opens new tab)")

These new chart components are built on top of Highcharts, which is a [commercial third-party library](https://www.highcharts.com/). Refer to the [licensing section on Charts](https://cloudscape.design/components/charts/#licensing) for more details.

- [Playground](https://cloudscape.design/components/cartesian-chart/?tabId=playground)
- [Usage](https://cloudscape.design/components/cartesian-chart/?tabId=usage)

## Configurator

### Examples

[Bar chart: Single data series](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart%3A-single-data-series)

[Bar chart: Multiple data series, grouped](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart%3A-multiple-data-series%2C-grouped)

[Bar chart: Multiple data series, stacked](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart%3A-multiple-data-series%2C-stacked)

[Bar chart: Multiple data series, stacked, horizontal](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart%3A-multiple-data-series%2C-stacked%2C-horizontal)

[Bar chart: With sub-items](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart%3A-with-sub-items)

[Line chart: Single data series](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=line-chart%3A-single-data-series)

[Line chart: Multiple data series and threshold](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=line-chart%3A-multiple-data-series-and-threshold)

[Bar chart with error bars](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-chart-with-error-bars)

[Bar and line chart with error bars](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=bar-and-line-chart-with-error-bars)

[Area chart: Stacked](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=area-chart%3A-stacked)

[Area chart: Stacked, multiple metrics](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=area-chart%3A-stacked%2C-multiple-metrics)

[Area chart: Stacked, with threshold](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=area-chart%3A-stacked%2C-with-threshold)

[Scatter chart](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=scatter-chart)

[Scatter chart: Multiple series, with trend lines](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=scatter-chart%3A-multiple-series%2C-with-trend-lines)

[Empty](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=empty)

[Loading](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=loading)

[Error](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=error)

[Empty with thresholds](https://cloudscape.design/components/cartesian-chart/?tabId=playground&example=empty-with-thresholds)

### Configuration

## Code

Due to limitations of the playground the highcharts import cannot be shown in the generated code below. You will find a proper example (with corresponding code) in the [code examples](https://cloudscape.design/components/cartesian-chart/?tabId=api#code-examples).

This example uses [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/) to provide common UI strings. If you don't use this feature, you should provide the following properties:`i18nStrings`.

```jsx
import * as React from "react";
import CartesianChart from "@cloudscape-design/chart-components/cartesian-chart";

export default () => {
  return (
    <CartesianChart
      stacking="normal"
      ariaLabel="Costs chart"
      chartHeight={400}
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
      series={[
        {
          name: "Amazon Simple Storage Service",
          type: "column",
          data: [56.03, 65.14, 69.8, 78.45, 84.36, 90.68]
        },
        {
          name: "Amazon Relational Database Service",
          type: "column",
          data: [null, 217.77, 35.9, 36.39, 36.39, 35.96]
        },
        {
          name: "AWS Config",
          type: "column",
          data: [39.02, 41.94, 40.06, 39.6, 48.62, 88.34]
        },
        {
          name: "AWS Key Management Service",
          type: "column",
          data: [39.48, 43.63, 43.25, 45.62, 45.12, 45.93]
        },
        {
          name: "Amazon Elastic Container Service",
          type: "column",
          data: [25.48, 45.06, 41.65, 23.42, 13.52, 64.24]
        },
        {
          name: "Others",
          type: "column",
          data: [27.31, 33.6, 41.08, 37.37, 25.49, 25.28]
        }
      ]}
      tooltip={{
        point: ({ item }) => {
          return {
            key: item.series.name,
            value:
              item.y !== null
                ? moneyFormatter(item.y)
                : null,
            expandable: item.series.name === "Others",
            subItems:
              item.series.name === "Others"
                ? [
                    {
                      key: "AWS Lambda",
                      value: moneyFormatter(
                        [
                          10.89,
                          11.25,
                          10.89,
                          11.25,
                          11.25,
                          10.89
                        ][item.x]
                      )
                    },
                    {
                      key: "CodeBuild",
                      value: moneyFormatter(
                        [
                          6.42,
                          9.52,
                          19.06,
                          17.92,
                          7.22,
                          6.08
                        ][item.x]
                      )
                    },
                    {
                      key: "Amazon GuardDuty",
                      value: moneyFormatter(
                        [
                          10,
                          12.83,
                          11.13,
                          8.2,
                          7.02,
                          8.31
                        ][item.x]
                      )
                    }
                  ]
                : undefined
          };
        },
          const total = [
            131.29,
            447.14,
            271.74,
            260.85,
            253.5,
            350.43
          ][x];
          return (
            <div
              style={{
                display: "flex",
                justifyContent: "space-between"
              }}
            >
              <span>Total</span>
              <span>{moneyFormatter(total)}</span>
            </div>
          );
        }
      }}
      xAxis={{
        type: "category",
        title: "Time",
        categories: [
          "2023-04",
          "2023-05",
          "2023-06",
          "2023-07",
          "2023-08",
          "2023-09"
        ]
      }}
      yAxis={{ title: "Costs" }}
    />
  );
}
```
