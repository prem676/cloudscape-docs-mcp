---
title: "Cartesian charts - Cloudscape Design System"
source: "https://cloudscape.design/components/cartesian-chart/?tabId=api"
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

## Development guidelines

To migrate from legacy to new charts, refer to the [migration guide](https://cloudscape.design/get-started/dev-guides/charts-migration/).

### Providing Highcharts

The Cartesian chart requires a Highcharts instance as an argument. You can resolve this instance either statically or dynamically. When Highcharts instance is null, the chart displays a fallback state that you can customize using the `fallback` property.

Load the [accessibility module](https://www.highcharts.com/docs/accessibility/accessibility-module) with the Highcharts instance to ensure proper accessibility features. When using *errorbar* series, load the `highcharts-more` module.

```js
// Loading Highcharts statically

import Highcharts from "highcharts";
import "highcharts/modules/accessibility";
import "highcharts/highcharts-more";

function MyChart(props) {
  return <CartesianChart highcharts={Highcharts} {...props} />
}

// Loading Highcharts dynamically

function MyChart(props) {
  const [highcharts, setHighcharts] = useState(null);
  useEffect(() => {
    const load = async () => {
      const Highcharts = await import("highcharts");
      await import("highcharts/modules/accessibility");
      await import("highcharts/highcharts-more");
      setHighcharts(Highcharts);
    };
    load();
  }, []);
  return <CartesianChart highcharts={highcharts} {...props} />
}
```

Supported Highcharts versions: v12.

### State management

By default, the chart component automatically filters series as you interact with the default filter, legend, and the chart itself. If you want to control the visible series, you need to explicitly set the `visibleSeries` property and the `onVisibleSeriesChange` listener.

Learn more about the [state management](https://cloudscape.design/get-started/dev-guides/state-management/) of Cloudscape components.

By default, the chart components use the Cloudscape generic categorical color palette as described in our [data visualization colors](https://cloudscape.design/foundation/visual-foundation/data-vis-colors/) article. If you want to use other colors, we recommend to use our data visualization colors as well. Custom colors are defined as part of the `data` property:

```js
import { colorChartsThresholdNegative } from '@cloudscape-design/design-tokens';

<CartesianChart
  {...otherProps}
  series={[
    { type: 'line', name: 'Site 1', data: dataSite1 },
    { type: 'line', name: 'Site 2', data: dataSite2 },
    { type: 'y-threshold', name: 'Limit', value: 10, color: colorChartsThresholdNegative },
  ]}
/>
```

Both the default color palette as well as any custom colors you pick from our data visualization colors use [design tokens](https://cloudscape.design/foundation/visual-foundation/design-tokens/). This means that they will automatically react to the current [visual mode](https://cloudscape.design/foundation/visual-foundation/visual-modes/), for example dark mode.

Ensure series data is sorted by ascending x values to avoid [Highcharts error #15](https://www.highcharts.com/forum/viewtopic.php?t=50446).

The labels of x and y axes do not automatically wrap. You can format them and add line breaks (\\n) with the `xAxis.valueFormatter` and `yAxis.valueFormatter` functions.

## Properties

| Name | Type | Description | Accepted values | Default | Required |
| --- | --- | --- | --- | --- | --- |
| ariaDescription | ``` string ``` | Defines the ARIA description of the chart container.This property corresponds to [accessibility.description](https://api.highcharts.com/highcharts/accessibility.description),and requires the [accessibility module](https://www.highcharts.com/docs/accessibility/accessibility-module). | \- | \- | ``` false ``` |
| ariaLabel | ``` string ``` | Defines the ARIA label for the chart container.This property corresponds to [lang.chartContainerLabel](https://api.highcharts.com/highcharts/lang.accessibility.chartContainerLabel),and requires the [accessibility module](https://www.highcharts.com/docs/accessibility/accessibility-module). | \- | \- | ``` false ``` |
| chartHeight | ``` number ``` | The height of the chart plot in pixels. It does not include legend and filter. | \- | \- | ``` false ``` |
| chartMinHeight | ``` number ``` | Defines the minimum allowed height of the chart plot. Use this when `fitHeight=true` toprevent the chart plot from becoming too small to display its content. When the parentcontainer is shorter than the minimum height, a vertical scrollbar appears automatically. | \- | \- | ``` false ``` |
| chartMinWidth | ``` number ``` | Defines the minimum allowed width of the chart plot. When the parent container is narrower than theminimum width, the horizontal scrollbar is automatically added. | \- | \- | ``` false ``` |
| emphasizeBaseline | ``` boolean ``` | When set to `true`, adds a visual emphasis on the zero baseline axis. | \- | ``` true ``` | ``` false ``` |
| filter | ``` BaseFilterOptions {   additionalFilters?: React.ReactNode   seriesFilter?: boolean } ``` | Defines options for filtering in the chart, including:  - `seriesFilter` (optional, boolean) - Displays default series filter at the top of the chart. - `additionalFilters` (optional, slot) - A slot for custom chart filters at the top of the chart. | \- | \- | ``` false ``` |
| fitHeight | ``` boolean ``` | The chart automatically adjusts its height to fill the parent container when this property is set. | \- | ``` false ``` | ``` false ``` |
| highcharts | ``` object \| null ``` | The Highcharts instance, which can be obtained using `import Highcharts from "highcharts"`.Supported Highcharts versions: 12. | \- | \- | ``` true ``` |
| i18nStrings | ``` CartesianI18nStrings {   chartRoleDescription?: string   detailPopoverDismissAriaLabel?: string   errorText?: string   legendAriaLabel?: string   loadingText?: string   recoveryText?: string   seriesFilterLabel?: string   seriesFilterPlaceholder?: string   seriesFilterSelectedAriaLabel?: string   xAxisRoleDescription?: string   yAxisRoleDescription?: string } ``` | An object that contains all of the localized strings required by the component.  **Note:** The property is part of [built-in internationalization](https://cloudscape.design/get-started/for-developers/internationalization/).This property is automatically provided if the application uses Cloudscape's I18nProvider. | \- | \- | ``` false ``` |
| inverted | ``` boolean ``` | Inverts X and Y axes. Use it to show horizontal columns (bars).This property corresponds to [chart.inverted](https://api.highcharts.com/highcharts/chart.inverted). | \- | ``` false ``` | ``` false ``` |
| legend | ``` BaseLegendOptions {   actions?: React.ReactNode   enabled?: boolean   title?: string } ``` | Defines chart legend options, including:  - `enabled` (optional, boolean) - Hides legend when set to `false`. - `title` (optional, string) - Visible label, shown above the legend. - `actions` (optional, slot) - A slot before the legend that can be used to render custom actions. | \- | \- | ``` false ``` |
| noData | ``` BaseNoDataOptions {   empty?: React.ReactNode   error?: React.ReactNode   loading?: React.ReactNode   noMatch?: React.ReactNode   onRecoveryClick?: NonCancelableEventHandler<{}>   statusType?: string } ``` | Defines options to represent empty, no-match, loading, and error state of the chart, including:  - `statusType` (optional, "finished" \| "loading" \| "error") - Specifies the current status of loading data. - `empty` (optional, ReactNode) - Content displayed when the chart data is empty. - `noMatch` (optional, ReactNode) - Content displayed when there is no data to display due to the built-in filtering. - `loading` (optional, ReactNode) - Content displayed when `statusType="loading"`. If omitted, the default loading stateis shown, using `i18n.loadingText` or built-in i18n. - `error` (optional, ReactNode) - Content displayed when `statusType="error"`. If omitted, the default error stateis shown, using `i18n.errorText` and `i18n.recoveryText` (when `onRecoveryClick` is provided), or built-in i18n. - `onRecoveryClick` (optional, function) - Called when the user clicks the recovery button that appears when using default errorstate, and only if `onRecoveryClick` is provided. Use this to enable the user to retry a failed request or provide another optionfor the user to recover from the error. | \- | \- | ``` false ``` |
| series | ``` ReadonlyArray<CartesianChartProps.SeriesOptions> ``` | Defines series options of the chart.This property corresponds to [series](https://api.highcharts.com/highcharts/series), and extends itwith two additional series types: "x-threshold", and "y-threshold".  Supported types:  - [area](https://api.highcharts.com/highcharts/series.area). - [areaspline](https://api.highcharts.com/highcharts/series.areaspline). - [column](https://api.highcharts.com/highcharts/series.column). - [errorbar](https://api.highcharts.com/highcharts/series.errorbar) - requires "highcharts/highcharts-more" module. - [line](https://api.highcharts.com/highcharts/series.line). - [scatter](https://api.highcharts.com/highcharts/series.scatter). - [spline](https://api.highcharts.com/highcharts/series.spline). - x-threshold - The line-like series to represent x-axis threshold (vertical, when `inverted=false`). - y-threshold - The line-like series to represent y-axis threshold (horizontal, when `inverted=false`). | \- | \- | ``` true ``` |
| stacking | ``` "normal" ``` | Enables series stacking behavior. Use it for column- or area- series.This property corresponds to "normal" stacking type in Highcharts ([plotOptions.series.stacking](https://api.highcharts.com/highcharts/plotOptions.series.stacking)). | \- | ``` undefined ``` | ``` false ``` |
| tooltip | ``` CartesianChartProps.TooltipOptions {   body?: (     props: CartesianChartProps.TooltipSlotRenderProps   ) => React.ReactNode   enabled?: boolean   footer?: (     props: CartesianChartProps.TooltipSlotRenderProps   ) => React.ReactNode   header?: (     props: CartesianChartProps.TooltipSlotRenderProps   ) => React.ReactNode   placement?: string   point?: (     props: CartesianChartProps.TooltipPointRenderProps   ) => BaseTooltipPointFormatted   size?: string } ``` | Defines tooltip options of the chart, including:  - `enabled` - (optional, boolean) - Hides the tooltip when set to false. - `size` - (optional, "small" \| "medium" \| "large") - Specifies max tooltip size. - `placement` - (optional, "middle" \| "outside") - Specifies preferred tooltip placement. - `point` - (optional, function) - Customizes tooltip series point rendering. - `header` - (optional, function) - Renders a custom tooltip header. - `body` - (optional, function) - Renders a custom tooltip body. - `footer` - (optional, function) - Renders a custom tooltip footer. | \- | \- | ``` false ``` |
| verticalAxisTitlePlacement | ``` string ``` | Controls the placement of the vertical axis title.When set to "side", displays the title along the axis line. | ``` top \| side ``` | ``` "top" ``` | ``` false ``` |
| visibleSeries | ``` ReadonlyArray<string> ``` | Specifies which series to show using their IDs. By default, all series are visible and managed by the component.If a series doesn't have an ID, its name is used. When using this property, manage state updates with `onVisibleSeriesChange`. | \- | \- | ``` false ``` |
| xAxis | ``` AxisOptions {   categories?: Array<string>   max?: number   min?: number   tickInterval?: number   title?: string   type?: string   valueFormatter?: (     value: number \| null   ) => string } ``` | Defines options of the chart's x axis.This property corresponds to [xAxis](https://api.highcharts.com/highcharts/xAxis), and extends itwith a custom value formatter.  Supported options:  - `title` (optional, string) - Axis title. - `type` (optional, "linear" \| "datetime" \| "category" \| "logarithmic") - Axis type. - - "linear" - Uses continuous proportional values scale. - - "datetime" - Similar to linear, but takes epoch time as values. - - "category" - Uses discrete scale, requires `categories` to be set. - - "logarithmic" - Uses continuous logarithmic values scale. - `min` (optional, number) - Axis min value boundary. - `max` (optional, number) - Axis max value boundary. - `tickInterval` (optional, number) - Distance between axis ticks. - `categories` (optional, Array<string>) - Predefined list of values, used for categorical axis type. - `valueFormatter` (optional, function) - Takes axis tick as input and returns a formatted string. This formatter alsoapplies to the tooltip header. | \- | \- | ``` false ``` |
| yAxis | ``` CartesianChartProps.YAxisOptions {   categories?: Array<string>   max?: number   min?: number   reversedStacks?: boolean   tickInterval?: number   title?: string   type?: string   valueFormatter?: (     value: number \| null   ) => string } ``` | Defines options of the chart's y axis.This property corresponds to [xAxis](https://api.highcharts.com/highcharts/yAxis), and extends itwith a custom value formatter.  Supported options:  - `title` (optional, string) - Axis title. - `type` (optional, "linear" \| "datetime" \| "category" \| "logarithmic") - Axis type. - - "linear" - Uses continuous proportional values scale. - - "datetime" - Similar to linear, but takes epoch time as values. - - "category" - Uses discrete scale, requires `categories` to be set. - - "logarithmic" - Uses continuous logarithmic values scale. - `min` (optional, number) - Axis min value boundary. - `max` (optional, number) - Axis max value boundary. - `tickInterval` (optional, number) - Distance between axis ticks. - `categories` (optional, Array<string>) - Predefined list of values, used for categorical axis type. - `reversedStacks` (optional, boolean) - Reverts series order in stacked series. - `valueFormatter` (optional, function) - Takes axis tick as input and returns a formatted string. This formatter alsoapplies to the tooltip points values. | \- | \- | ``` false ``` |

## Slots

| Name | Description |
| --- | --- |
| fallback | Custom content that renders when `highcharts=null`. It renders a spinner if not defined. |

## Events

| Name | Detail | Description | Cancelable |
| --- | --- | --- | --- |
| onVisibleSeriesChange | ``` { visibleSeries: Array<string>; } {   visibleSeries: Array<string> } ``` | A callback function, triggered when series visibility changes as a result of user interaction with the legend or filter. | ``` false ``` |

## Functions

| Name | Description |
| --- | --- |
| setVisibleSeries | Controls series visibility and works with both controlled and uncontrolled visibility modes. |
| showAllSeries | Functions similarly to `setVisibleSeries`, but applies to all series and doesn't require series IDs as input.Use this when implementing clear-filter actions in no-match states. |
