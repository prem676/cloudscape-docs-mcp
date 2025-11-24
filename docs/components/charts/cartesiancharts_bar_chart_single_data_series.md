---
title: "Cartesian charts - Cloudscape Design System"
source: "https://cloudscape.design/components/cartesian-chart/?tabId=playground"
author:
published:
created: 2025-10-01
description: "Cartesian charts display information along horizontal and vertical axes to clearly show patterns, comparisons, and relationships between values. It includes line, bar, area, scatter, and mixed charts."
tags:
  - "clippings"
---
## Cartesian charts

Published: September 10, 2025 | Last updated: September 8, 2025

[Get design library](https://cloudscape.design/get-started/for-designers/design-resources)

[Browse code](https://github.com/cloudscape-design/chart-components/tree/main/src/cartesian-chart "Browse code (opens new tab)")

[View in demo](https://cloudscape.design/examples/react/dashboard.html "View in demo (opens new tab)")

These new chart components are built on top of Highcharts, which is a [commercial third-party library](https://www.highcharts.com/). Refer to the [licensing section on Charts](https://cloudscape.design/components/charts/#licensing) for more details.

- [Playground](https://cloudscape.design/components/cartesian-chart/?tabId=playground)
- [API](https://cloudscape.design/components/cartesian-chart/?tabId=api)
- [Testing](https://cloudscape.design/components/cartesian-chart/?tabId=testing)
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
      ariaLabel="Single data series bar chart"
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
          name: "Site 1",
          type: "column",
          data: [34503, 25832, 4012, -5602, 17839]
        },
        {
          type: "y-threshold",
          name: "Average revenue",
          value: 19104
        }
      ]}
      xAxis={{
        type: "category",
        title: "Time (UTC)",
        categories: [
          "Sep 25\n 15:00",
          "Sep 25\n 17:00",
          "Sep 25\n 19:00",
          "Sep 25\n 21:00",
          "Sep 25\n 23:00"
        ]
      }}
      yAxis={{
        title: "Revenue (USD)",
        min: -10000,
        max: 40000,
        valueFormatter: function y(e) {
          return Math.abs(e) >= 1e9
            ? (e / 1e9).toFixed(1).replace(/\.0$/, "") +
                "G"
            : Math.abs(e) >= 1e6
            ? (e / 1e6).toFixed(1).replace(/\.0$/, "") +
              "M"
            : Math.abs(e) >= 1e3
            ? (e / 1e3).toFixed(1).replace(/\.0$/, "") +
              "K"
            : e.toFixed(2);
        }
      }}
    />
  );
}
```
