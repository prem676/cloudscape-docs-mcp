# Tabs

The Tabs component helps organize content into multiple sections, allowing users to navigate between them without leaving the page. It's particularly useful for grouping related information in data reports.

## Import

```jsx
import { Tabs } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Tabs } from '@cloudscape-design/components';

function BasicTabs() {
  return (
    <Tabs
      tabs={[
        {
          label: 'First tab',
          id: 'first',
          content: 'First tab content'
        },
        {
          label: 'Second tab',
          id: 'second',
          content: 'Second tab content'
        },
        {
          label: 'Third tab',
          id: 'third',
          content: 'Third tab content'
        }
      ]}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `tabs` | Array | Array of tab items |
| `activeTabId` | string | ID of the active tab (controlled mode) |
| `onChange` | ({ detail }) => void | Called when a tab is selected |
| `variant` | 'default' \| 'container' | Tab appearance variant |
| `disableContentPaddings` | boolean | Removes default paddings from the content area |
| `ariaLabel` | string | ARIA label for the tabs component |
| `i18nStrings` | object | Internationalization strings |

## Tab Item Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier for the tab |
| `label` | ReactNode | Label for the tab |
| `content` | ReactNode | Content for the tab |
| `disabled` | boolean | Whether the tab is disabled |
| `href` | string | URL for the tab to navigate to |

## Examples

### Controlled Tabs

```jsx
import { Tabs, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function ControlledTabs() {
  const [activeTabId, setActiveTabId] = useState('first');
  
  return (
    <Tabs
      activeTabId={activeTabId}
      onChange={({ detail }) => setActiveTabId(detail.activeTabId)}
      tabs={[
        {
          label: 'Overview',
          id: 'first',
          content: (
            <Box padding="l">
              <h3>Overview Content</h3>
              <p>This is the overview section of the report.</p>
            </Box>
          )
        },
        {
          label: 'Details',
          id: 'second',
          content: (
            <Box padding="l">
              <h3>Details Content</h3>
              <p>This section contains detailed information.</p>
            </Box>
          )
        },
        {
          label: 'Documentation',
          id: 'third',
          content: (
            <Box padding="l">
              <h3>Documentation Content</h3>
              <p>This section contains documentation and help.</p>
            </Box>
          )
        }
      ]}
    />
  );
}
```

### Tabs with Container Variant

```jsx
import { Tabs, Container, Header, Box } from '@cloudscape-design/components';

function ContainerTabs() {
  return (
    <Tabs
      variant="container"
      tabs={[
        {
          label: 'Raw data',
          id: 'raw',
          content: (
            <Container header={<Header variant="h2">Raw Data</Header>}>
              <Box padding="l">
                <p>This tab displays the raw data of the report.</p>
              </Box>
            </Container>
          )
        },
        {
          label: 'Visualizations',
          id: 'visualizations',
          content: (
            <Container header={<Header variant="h2">Data Visualizations</Header>}>
              <Box padding="l">
                <p>This tab contains various visualizations of the data.</p>
              </Box>
            </Container>
          )
        },
        {
          label: 'Analytics',
          id: 'analytics',
          content: (
            <Container header={<Header variant="h2">Analytics</Header>}>
              <Box padding="l">
                <p>This tab presents analytical insights derived from the data.</p>
              </Box>
            </Container>
          )
        }
      ]}
    />
  );
}
```

### Tabs with Data Visualizations

```jsx
import { Tabs, Box, PieChart, LineChart, BarChart, SpaceBetween, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function DataVisualizationTabs() {
  const [activeTabId, setActiveTabId] = useState('summary');
  
  // Sample data for charts
  const pieData = [
    { title: 'Documents', value: 35 },
    { title: 'Images', value: 25 },
    { title: 'Videos', value: 15 },
    { title: 'Audio', value: 10 },
    { title: 'Other', value: 15 }
  ];
  
  const lineData = {
    series: [
      {
        title: 'Site Traffic',
        type: 'line',
        data: [
          { x: new Date(2022, 0, 1), y: 1200 },
          { x: new Date(2022, 1, 1), y: 1400 },
          { x: new Date(2022, 2, 1), y: 1800 },
          { x: new Date(2022, 3, 1), y: 2200 },
          { x: new Date(2022, 4, 1), y: 2000 },
          { x: new Date(2022, 5, 1), y: 2400 }
        ]
      }
    ]
  };
  
  const barData = [
    { title: 'Item 1', value: 30 },
    { title: 'Item 2', value: 60 },
    { title: 'Item 3', value: 45 },
    { title: 'Item 4', value: 80 },
    { title: 'Item 5', value: 25 }
  ];
  
  return (
    <Tabs
      activeTabId={activeTabId}
      onChange={({ detail }) => setActiveTabId(detail.activeTabId)}
      tabs={[
        {
          label: 'Summary',
          id: 'summary',
          content: (
            <Container header={<Header variant="h2">Data Summary</Header>}>
              <Box padding="l">
                <SpaceBetween size="l">
                  <h3>Storage Distribution</h3>
                  <PieChart
                    data={pieData}
                    variant="donut"
                    size="medium"
                    hideFilter={true}
                    innerMetricValue="100 GB"
                    innerMetricDescription="Total Storage"
                  />
                </SpaceBetween>
              </Box>
            </Container>
          )
        },
        {
          label: 'Trends',
          id: 'trends',
          content: (
            <Container header={<Header variant="h2">Time-based Trends</Header>}>
              <Box padding="l">
                <SpaceBetween size="l">
                  <h3>Monthly Traffic</h3>
                  <LineChart
                    series={lineData.series}
                    xDomain={[new Date(2022, 0, 1), new Date(2022, 5, 1)]}
                    yDomain={[0, 3000]}
                    xScaleType="time"
                    height={300}
                    xTitle="Month"
                    yTitle="Visitors"
                    i18nStrings={{
                      xTickFormatter: e => e.toLocaleDateString('en-US', { month: 'short' })
                    }}
                  />
                </SpaceBetween>
              </Box>
            </Container>
          )
        },
        {
          label: 'Comparison',
          id: 'comparison',
          content: (
            <Container header={<Header variant="h2">Data Comparison</Header>}>
              <Box padding="l">
                <SpaceBetween size="l">
                  <h3>Performance Metrics</h3>
                  <BarChart
                    series={[{ title: 'Value', type: 'bar', data: barData }]}
                    height={300}
                    xTitle="Item"
                    yTitle="Value"
                    hideFilter={true}
                    horizontalBars
                    i18nStrings={{
                      xTickFormatter: datum => datum.title
                    }}
                  />
                </SpaceBetween>
              </Box>
            </Container>
          )
        }
      ]}
    />
  );
}
```

### Tabs with Dynamic Content Loading

```jsx
import { Tabs, Box, Spinner, Container, Header, Button } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function DynamicContentTabs() {
  const [activeTabId, setActiveTabId] = useState('tab1');
  const [content, setContent] = useState({});
  const [loading, setLoading] = useState({});
  
  // Simulate loading content for a tab
  const loadContent = (tabId) => {
    if (content[tabId] || loading[tabId]) {
      return;
    }
    
    setLoading(prev => ({ ...prev, [tabId]: true }));
    
    // Simulate API call
    setTimeout(() => {
      setContent(prev => ({
        ...prev,
        [tabId]: `This is the dynamically loaded content for ${tabId}.`
      }));
      setLoading(prev => ({ ...prev, [tabId]: false }));
    }, 1500);
  };
  
  // Load content when tab changes
  useEffect(() => {
    loadContent(activeTabId);
  }, [activeTabId]);
  
  const renderTabContent = (tabId) => {
    if (loading[tabId]) {
      return (
        <Box textAlign="center" padding="l">
          <Spinner size="large" />
          <div>Loading content...</div>
        </Box>
      );
    }
    
    if (content[tabId]) {
      return (
        <Box padding="l">
          <h3>{`${tabId.charAt(0).toUpperCase() + tabId.slice(1)} Content`}</h3>
          <p>{content[tabId]}</p>
        </Box>
      );
    }
    
    return (
      <Box textAlign="center" padding="l">
        <Button onClick={() => loadContent(tabId)}>Load content</Button>
      </Box>
    );
  };
  
  return (
    <Tabs
      activeTabId={activeTabId}
      onChange={({ detail }) => setActiveTabId(detail.activeTabId)}
      tabs={[
        {
          label: 'First Tab',
          id: 'tab1',
          content: renderTabContent('tab1')
        },
        {
          label: 'Second Tab',
          id: 'tab2',
          content: renderTabContent('tab2')
        },
        {
          label: 'Third Tab',
          id: 'tab3',
          content: renderTabContent('tab3')
        }
      ]}
    />
  );
}
```

### Tabs with Notifications

```jsx
import { Tabs, Box, Badge, SpaceBetween, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function TabsWithNotifications() {
  const [activeTabId, setActiveTabId] = useState('inbox');
  
  return (
    <Tabs
      activeTabId={activeTabId}
      onChange={({ detail }) => setActiveTabId(detail.activeTabId)}
      tabs={[
        {
          label: (
            <SpaceBetween direction="horizontal" size="xs">
              <span>Inbox</span>
              <Badge color="red">3</Badge>
            </SpaceBetween>
          ),
          id: 'inbox',
          content: (
            <Container header={<Header variant="h2">Inbox</Header>}>
              <Box padding="l">
                <p>You have 3 unread messages.</p>
              </Box>
            </Container>
          )
        },
        {
          label: (
            <SpaceBetween direction="horizontal" size="xs">
              <span>Alerts</span>
              <Badge color="blue">5</Badge>
            </SpaceBetween>
          ),
          id: 'alerts',
          content: (
            <Container header={<Header variant="h2">Alerts</Header>}>
              <Box padding="l">
                <p>You have 5 active alerts.</p>
              </Box>
            </Container>
          )
        },
        {
          label: 'Archive',
          id: 'archive',
          content: (
            <Container header={<Header variant="h2">Archive</Header>}>
              <Box padding="l">
                <p>Previously processed items.</p>
              </Box>
            </Container>
          )
        }
      ]}
    />
  );
}
```

### Tabs with Conditional Rendering

```jsx
import { Tabs, Box, Button, SpaceBetween, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function ConditionalTabs() {
  const [activeTabId, setActiveTabId] = useState('tab1');
  const [showOptionalTab, setShowOptionalTab] = useState(false);
  
  // Create tabs array dynamically
  const getTabs = () => {
    const tabs = [
      {
        label: 'Tab 1',
        id: 'tab1',
        content: (
          <Container header={<Header variant="h2">Tab 1 Content</Header>}>
            <Box padding="l">
              <p>This is the content for Tab 1.</p>
            </Box>
          </Container>
        )
      },
      {
        label: 'Tab 2',
        id: 'tab2',
        content: (
          <Container header={<Header variant="h2">Tab 2 Content</Header>}>
            <Box padding="l">
              <p>This is the content for Tab 2.</p>
            </Box>
          </Container>
        )
      }
    ];
    
    // Add optional tab if enabled
    if (showOptionalTab) {
      tabs.push({
        label: 'Optional Tab',
        id: 'optional',
        content: (
          <Container header={<Header variant="h2">Optional Content</Header>}>
            <Box padding="l">
              <p>This is optional content that can be shown or hidden.</p>
            </Box>
          </Container>
        )
      });
    }
    
    return tabs;
  };
  
  // Update active tab if it's removed
  const handleToggleOptionalTab = () => {
    const newShowOptional = !showOptionalTab;
    setShowOptionalTab(newShowOptional);
    
    // If the active tab is the optional tab and it's being hidden, switch to the first tab
    if (activeTabId === 'optional' && !newShowOptional) {
      setActiveTabId('tab1');
    }
  };
  
  return (
    <SpaceBetween size="m">
      <Button onClick={handleToggleOptionalTab}>
        {showOptionalTab ? 'Hide Optional Tab' : 'Show Optional Tab'}
      </Button>
      
      <Tabs
        activeTabId={activeTabId}
        onChange={({ detail }) => setActiveTabId(detail.activeTabId)}
        tabs={getTabs()}
      />
    </SpaceBetween>
  );
}
```

## Accessibility

- Properly implements ARIA roles, states, and properties for tabs
- Provides keyboard navigation between tabs (arrow keys, Tab key)
- Includes proper focus management
- Supports screen readers with appropriate announcements
- Ensures tab content is properly labeled
- Maintains visible focus indicators

## Best Practices

1. Use descriptive labels for tabs to clearly indicate their contents
2. Organize tabs logically, with the most important or frequently used tabs first
3. Limit the number of tabs to avoid overwhelming users (5-7 is a good maximum)
4. Keep tab labels concise, ideally one or two words
5. Use badges sparingly to indicate notifications or updates
6. Ensure tab content is properly contained and formatted
7. Consider the container variant for more complex content
8. Use controlled mode when you need to manage the active tab state
9. Lazy-load content for tabs with heavy data or visualizations
10. Provide appropriate loading states for dynamic content
11. Consider accessibility when designing tab interactions
12. Ensure consistent content structure across different tabs
13. Use consistent tab heights to prevent layout shifts
14. Consider mobile responsiveness for tab layouts
15. Avoid nesting tabs within tabs when possible
16. Add visual cues (icons, badges) to help users identify tab content
