# TextContent

The TextContent component is used for displaying properly formatted text content with appropriate spacing, font sizes, and line heights. It ensures consistent typographic styling across the application.

## Import

```jsx
import { TextContent } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { TextContent } from '@cloudscape-design/components';

function BasicTextContent() {
  return (
    <TextContent>
      <h1>Heading 1</h1>
      <h2>Heading 2</h2>
      <h3>Heading 3</h3>
      <p>This is a paragraph of text. TextContent component ensures proper spacing and typography throughout the content.</p>
      <ul>
        <li>First item in an unordered list</li>
        <li>Second item in an unordered list</li>
      </ul>
      <p>Another paragraph with <a href="#">a link</a> included.</p>
    </TextContent>
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `children` | ReactNode | Content to be displayed with the appropriate styling |

## Examples

### Report Introduction with TextContent

```jsx
import { TextContent, Box, Container, Header } from '@cloudscape-design/components';

function ReportIntroduction() {
  return (
    <Container header={<Header variant="h2">Monthly Analysis Report</Header>}>
      <Box padding="l">
        <TextContent>
          <h2>Executive Summary</h2>
          <p>
            This report provides a comprehensive analysis of our cloud resource usage and performance
            metrics for the month of May 2023. The data presented covers all major service
            categories and highlights key trends and anomalies observed during this period.
          </p>
          
          <h3>Key Findings</h3>
          <ul>
            <li>Overall compute usage increased by 15% compared to the previous month.</li>
            <li>Storage costs decreased by 7% due to optimization efforts.</li>
            <li>Three performance incidents were recorded, all resolved within SLA timeframes.</li>
            <li>New machine learning workloads contributed to 20% of the total compute hours.</li>
          </ul>
          
          <h3>Recommendations</h3>
          <ol>
            <li>Consider rightsizing instances in the development environment.</li>
            <li>Implement lifecycle policies for object storage to reduce costs further.</li>
            <li>Scale up database capacity before the anticipated traffic increase next month.</li>
          </ol>
          
          <p>
            <strong>Note:</strong> The data presented in this report is based on actual usage
            metrics collected from our monitoring systems. For detailed methodology, please refer
            to the appendix.
          </p>
        </TextContent>
      </Box>
    </Container>
  );
}
```

### Combining TextContent with Data Visualizations

```jsx
import { 
  TextContent, 
  Box, 
  SpaceBetween, 
  Container, 
  Header, 
  ColumnLayout,
  PieChart
} from '@cloudscape-design/components';

function DataReportWithText() {
  // Sample data for chart
  const data = [
    { title: 'Compute', value: 45 },
    { title: 'Storage', value: 30 },
    { title: 'Database', value: 15 },
    { title: 'Networking', value: 10 }
  ];

  return (
    <Container header={<Header variant="h2">Cloud Resource Allocation</Header>}>
      <SpaceBetween size="l">
        <TextContent>
          <p>
            The following visualization shows the distribution of cloud resources across different
            service categories. Compute resources continue to dominate our usage, accounting for
            nearly half of all allocated resources.
          </p>
        </TextContent>
        
        <ColumnLayout columns={2} variant="text-grid">
          <div>
            <PieChart
              data={data}
              variant="donut"
              size="medium"
              hideFilter={true}
              innerMetricValue="100%"
              innerMetricDescription="Total"
              ariaLabel="Resource allocation pie chart"
              i18nStrings={{
                detailPopoverDismissAriaLabel: 'Dismiss',
                legendAriaLabel: 'Legend',
                chartAriaRoleDescription: 'pie chart'
              }}
            />
          </div>
          
          <TextContent>
            <h3>Analysis</h3>
            <p>
              The resource distribution reflects our current architectural focus on compute-intensive
              workloads. With 45% of resources allocated to compute services, we're well-positioned
              to handle the processing demands of our applications.
            </p>
            <p>
              Storage represents 30% of our resource allocation, which is consistent with our data-driven
              approach. Database and networking services make up the remaining 25%, providing essential
              infrastructure for our applications.
            </p>
            <h4>Key Observations</h4>
            <ul>
              <li>Compute allocation increased by 5% since last quarter</li>
              <li>Storage needs are growing steadily with our expanding datasets</li>
              <li>Database resources may need expansion in the next quarter</li>
            </ul>
          </TextContent>
        </ColumnLayout>
        
        <TextContent>
          <h3>Recommendations</h3>
          <p>
            Based on the current resource allocation and projected needs, we recommend the following
            actions:
          </p>
          <ol>
            <li>Evaluate compute auto-scaling policies to optimize resource usage during peak hours</li>
            <li>Implement tiered storage solutions to reduce costs for infrequently accessed data</li>
            <li>Monitor database performance closely as usage approaches allocated capacity</li>
          </ol>
        </TextContent>
      </SpaceBetween>
    </Container>
  );
}
```

### TextContent with Code Samples

```jsx
import { TextContent, Box, Container, Header, Code } from '@cloudscape-design/components';

function DocumentationWithCode() {
  return (
    <Container header={<Header variant="h2">Implementation Guide</Header>}>
      <Box padding="l">
        <TextContent>
          <h2>Data Visualization Integration</h2>
          
          <p>
            This guide provides instructions for integrating data visualizations into your CloudScape
            application. Follow the steps below to incorporate charts and graphs that effectively
            communicate your data insights.
          </p>
          
          <h3>1. Basic Chart Implementation</h3>
          
          <p>
            Start by importing the necessary components from the CloudScape design system:
          </p>
          
          <Code>{`import { PieChart, LineChart, BarChart } from '@cloudscape-design/components';`}</Code>
          
          <p>
            Then, structure your data according to the chart type you're using. Here's an example
            for a PieChart:
          </p>
          
          <Code>{`
// Data format for PieChart
const data = [
  { title: 'Category A', value: 45 },
  { title: 'Category B', value: 30 },
  { title: 'Category C', value: 15 },
  { title: 'Category D', value: 10 }
];

// Basic PieChart implementation
function MyPieChart() {
  return (
    <PieChart
      data={data}
      variant="donut"
      size="medium"
      hideFilter={true}
      innerMetricValue="100%"
      innerMetricDescription="Total"
    />
  );
}`}</Code>
          
          <h3>2. Adding Interactivity</h3>
          
          <p>
            Enhance your charts with interactive elements to provide users with a more engaging
            experience:
          </p>
          
          <Code>{`
function InteractivePieChart() {
  const [highlightedSegment, setHighlightedSegment] = useState(null);
  
  return (
    <PieChart
      data={data}
      variant="donut"
      size="medium"
      highlightedSegment={highlightedSegment}
      onHighlightChange={({ detail }) => setHighlightedSegment(detail.highlightedSegment)}
      // Other props...
    />
  );
}`}</Code>
          
          <h3>3. Responsive Layouts</h3>
          
          <p>
            Use the ColumnLayout component to create responsive layouts for your visualizations:
          </p>
          
          <Code>{`
<ColumnLayout columns={2} variant="text-grid">
  <div>
    <PieChart data={pieData} />
  </div>
  <div>
    <BarChart data={barData} />
  </div>
</ColumnLayout>
`}</Code>
          
          <p>
            For more detailed information, refer to the component-specific documentation or reach out
            to the design system team.
          </p>
        </TextContent>
      </Box>
    </Container>
  );
}
```

### Dynamic TextContent with Markdown

```jsx
import { TextContent, Box, Container, Header, SpaceBetween, Button } from '@cloudscape-design/components';
import { useState } from 'react';
import ReactMarkdown from 'react-markdown';

function DynamicTextContent() {
  const [showDetails, setShowDetails] = useState(false);
  
  // Sample markdown content
  const markdownContent = `
## Detailed Analysis

This section provides an in-depth analysis of the collected metrics.

### Performance Indicators

* **Response Time**: Average response time decreased by 15% this month
* **Throughput**: System throughput increased to 1,200 requests/second
* **Error Rate**: Error rate remains stable at 0.02%

### Regional Distribution

| Region | Traffic | Growth |
|--------|---------|--------|
| US East | 45% | +5% |
| Europe | 30% | +2% |
| Asia | 20% | +8% |
| Other | 5% | -1% |

For more information, contact the performance team.
  `;
  
  return (
    <Container header={<Header variant="h2">System Performance Report</Header>}>
      <SpaceBetween size="l">
        <TextContent>
          <h2>Performance Summary</h2>
          <p>
            Overall system performance has improved significantly over the past month. Key metrics
            show positive trends across all major service categories, with particularly strong
            improvements in response time and throughput.
          </p>
        </TextContent>
        
        <Button onClick={() => setShowDetails(!showDetails)}>
          {showDetails ? 'Hide Details' : 'Show Details'}
        </Button>
        
        {showDetails && (
          <Box padding="m" bgcolor="background.container">
            <TextContent>
              <ReactMarkdown>{markdownContent}</ReactMarkdown>
            </TextContent>
          </Box>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### TextContent with Data-Driven Text

```jsx
import { TextContent, Box, Container, Header, SpaceBetween, StatusIndicator } from '@cloudscape-design/components';

function DataDrivenTextContent() {
  // Sample data that would typically come from an API or state
  const metrics = {
    usagePercent: 72,
    costTrend: -5.2,
    performance: 'good',
    availabilityPercent: 99.98,
    incidents: 1,
    recommendations: [
      'Optimize instance sizes in development environment',
      'Consider reserved instances for stable workloads',
      'Implement automated scaling for batch processing jobs'
    ]
  };
  
  // Determine status indicators based on data
  const getUsageStatus = (percent) => {
    if (percent > 90) return 'error';
    if (percent > 70) return 'warning';
    return 'success';
  };
  
  const getCostTrendStatus = (percent) => {
    if (percent < 0) return 'success';
    if (percent < 10) return 'info';
    return 'warning';
  };
  
  return (
    <Container header={<Header variant="h2">Resource Utilization Report</Header>}>
      <Box padding="l">
        <TextContent>
          <h2>Current Status</h2>
          
          <p>
            Your cloud resources are currently at{' '}
            <StatusIndicator type={getUsageStatus(metrics.usagePercent)}>
              {metrics.usagePercent}% utilization
            </StatusIndicator>
            {' '}with a monthly cost trend of{' '}
            <StatusIndicator type={getCostTrendStatus(metrics.costTrend)}>
              {metrics.costTrend > 0 ? '+' : ''}{metrics.costTrend}%
            </StatusIndicator>
            {' '}compared to last month.
          </p>
          
          <p>
            System performance is rated as{' '}
            <strong>{metrics.performance}</strong>{' '}
            with an availability of {metrics.availabilityPercent}% this month.
            {metrics.incidents > 0 ? (
              <> There {metrics.incidents === 1 ? 'was' : 'were'} {metrics.incidents} incident{metrics.incidents > 1 ? 's' : ''} reported.</>
            ) : (
              <> No incidents were reported.</>
            )}
          </p>
          
          <h3>Cost Optimization Recommendations</h3>
          
          {metrics.recommendations.length > 0 ? (
            <ul>
              {metrics.recommendations.map((rec, index) => (
                <li key={index}>{rec}</li>
              ))}
            </ul>
          ) : (
            <p>No recommendations available at this time.</p>
          )}
          
          <p>
            <strong>Note:</strong> This report is generated based on data collected over the past 30 days.
            For real-time metrics, please refer to the monitoring dashboard.
          </p>
        </TextContent>
      </Box>
    </Container>
  );
}
```

## Styling Typography

TextContent applies the following styling to elements:

| Element | Styling |
|---------|---------|
| `h1` | Large heading with appropriate margins |
| `h2` | Medium heading with appropriate margins |
| `h3` - `h5` | Smaller headings with appropriate scaling |
| `p` | Standard paragraph with proper line height and margins |
| `a` | Styled links with appropriate hover states |
| `ul`, `ol` | Lists with proper indentation and bullet/number styling |
| `li` | List items with appropriate spacing |
| `blockquote` | Quoted text with distinctive styling |
| `code`, `pre` | Monospaced text for code samples |
| `hr` | Horizontal rule with subtle styling |
| `table` | Basic table styling with borders and spacing |
| `strong`, `b` | Bold text |
| `em`, `i` | Italic text |

## Accessibility

- Uses semantic HTML elements for proper document structure
- Maintains proper heading hierarchy for screen readers
- Ensures adequate color contrast for text readability
- Preserves proper focus states for interactive elements
- Maintains consistent text sizing and spacing for readability
- Supports responsive text that scales appropriately across devices

## Best Practices

1. Use TextContent to wrap all complex text content in your application
2. Maintain proper heading hierarchy (h1 → h2 → h3) for good document structure
3. Use appropriate semantic elements (`<p>` for paragraphs, `<ul>` or `<ol>` for lists)
4. Keep paragraphs concise and focused on a single idea
5. Use lists to break down complex information into digestible chunks
6. Include proper spacing between sections for improved readability
7. Integrate TextContent with other components like Container for proper visual hierarchy
8. Use semantic HTML within TextContent for better accessibility
9. Consider using ColumnLayout for text-heavy sections to improve readability
10. Include visual cues like StatusIndicator to highlight important information
11. Maintain consistent styling across all text content in your application
12. Consider responsive behavior for text-heavy sections on smaller screens
13. Use Code component for displaying code samples within TextContent
14. Combine TextContent with Box for additional padding and background styling
15. Keep font sizes and line heights consistent for a professional appearance
