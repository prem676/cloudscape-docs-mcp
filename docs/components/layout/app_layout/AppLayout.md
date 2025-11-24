# App Layout

The AppLayout component provides page structure for applications, offering collapsible side navigation, tools panel, drawers, and split panel support.

## Import

```jsx
import { AppLayout } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { AppLayout, SideNavigation, TopNavigation } from '@cloudscape-design/components';

function BasicAppLayout() {
  return (
    <AppLayout
      navigation={<SideNavigation items={[/* navigation items */]} />}
      content={<div>Main content goes here</div>}
      toolsHide={true}
    />
  );
}
```

## Key Properties

| Property | Type | Description |
|----------|------|-------------|
| `content` | ReactNode | Main content area of the application |
| `contentType` | 'default' \| 'table' \| 'form' \| 'cards' \| 'wizard' \| 'dashboard' | Type of content displayed |
| `navigation` | ReactNode | Side navigation content (typically SideNavigation component) |
| `navigationHide` | boolean | Determines if navigation should be hidden |
| `navigationOpen` | boolean | Controls whether the navigation pane is open in narrow viewports |
| `onNavigationChange` | ({ detail }) => void | Called when navigation open state changes |
| `tools` | ReactNode | Tools panel content (typically HelpPanel component) |
| `toolsHide` | boolean | Determines if tools should be hidden |
| `toolsOpen` | boolean | Controls whether the tools pane is open |
| `onToolsChange` | ({ detail }) => void | Called when tools open state changes |
| `notifications` | ReactNode | Notification content (typically Flashbar component) |
| `breadcrumbs` | ReactNode | Breadcrumb navigation (typically BreadcrumbGroup component) |
| `stickyNotifications` | boolean | Determines if notifications should be sticky |
| `headerSelector` | string | CSS selector of the page header (for navigation) |
| `footerSelector` | string | CSS selector of the page footer |
| `ariaLabels` | object | ARIA labels for accessibility |
| `drawers` | Drawer[] | Array of drawer objects to be displayed at the bottom of the page |

## Examples

### Complete Application Layout

```jsx
import { 
  AppLayout,
  SideNavigation,
  TopNavigation,
  BreadcrumbGroup,
  HelpPanel,
  ContentLayout,
  Container,
  Header,
  Button,
  Flashbar
} from '@cloudscape-design/components';
import { useState } from 'react';

function CompleteAppLayout() {
  // Navigation state
  const [navigationOpen, setNavigationOpen] = useState(true);
  
  // Tools state
  const [toolsOpen, setToolsOpen] = useState(false);
  
  // Notifications state
  const [notifications, setNotifications] = useState([
    {
      type: 'success',
      content: 'Resource was successfully created.',
      dismissible: true,
      dismissLabel: 'Dismiss message',
      onDismiss: () => setNotifications([])
    }
  ]);
  
  // Navigation items
  const navItems = [
    {
      type: 'section',
      text: 'Dashboard',
      items: [
        { type: 'link', text: 'Overview', href: '#' },
        { type: 'link', text: 'Analytics', href: '#' },
      ]
    },
    {
      type: 'section',
      text: 'Resources',
      items: [
        { type: 'link', text: 'Instances', href: '#' },
        { type: 'link', text: 'Storage', href: '#' },
        { type: 'link', text: 'Network', href: '#' }
      ]
    }
  ];
  
  // Breadcrumb items
  const breadcrumbItems = [
    { text: 'Home', href: '#' },
    { text: 'Resources', href: '#' },
    { text: 'Instances', href: '#' }
  ];
  
  return (
    <>
      <TopNavigation
        identity={{ href: '#', title: 'My Application' }}
        utilities={[
          {
            type: 'button',
            text: 'Help',
            onClick: () => setToolsOpen(true)
          },
          {
            type: 'menu-dropdown',
            text: 'User',
            iconName: 'user-profile',
            items: [
              { id: 'profile', text: 'Profile' },
              { id: 'preferences', text: 'Preferences' },
              { id: 'security', text: 'Security' },
              { id: 'signout', text: 'Sign out' }
            ]
          }
        ]}
      />
      
      <AppLayout
        navigation={
          <SideNavigation
            activeHref="#"
            header={{ text: 'My Application', href: '#' }}
            items={navItems}
          />
        }
        navigationOpen={navigationOpen}
        onNavigationChange={({ detail }) => setNavigationOpen(detail.open)}
        
        content={
          <ContentLayout
            header={
              <Header
                variant="h1"
                actions={
                  <Button variant="primary">Create resource</Button>
                }
              >
                Instances
              </Header>
            }
          >
            <Container>
              <p>Main content area where your application's primary interface would go.</p>
            </Container>
          </ContentLayout>
        }
        
        breadcrumbs={
          <BreadcrumbGroup items={breadcrumbItems} />
        }
        
        tools={
          <HelpPanel
            header={<h2>Help panel</h2>}
            footer={
              <div>
                <h3>Looking for more help?</h3>
                <p>
                  <a href="#">Contact support</a>
                </p>
              </div>
            }
          >
            <p>
              This is a help panel that provides contextual help information
              for the current page or task.
            </p>
            <h3>Learn more</h3>
            <ul>
              <li><a href="#">Documentation</a></li>
              <li><a href="#">Tutorials</a></li>
              <li><a href="#">Developer guide</a></li>
            </ul>
          </HelpPanel>
        }
        toolsOpen={toolsOpen}
        onToolsChange={({ detail }) => setToolsOpen(detail.open)}
        
        notifications={
          <Flashbar items={notifications} />
        }
        
        contentType="default"
        
        ariaLabels={{
          navigation: 'Side navigation',
          navigationClose: 'Close side navigation',
          navigationToggle: 'Open side navigation',
          tools: 'Help panel',
          toolsClose: 'Close help panel',
          toolsToggle: 'Open help panel'
        }}
      />
    </>
  );
}
```

### AppLayout with Split Panel

```jsx
import { 
  AppLayout, 
  SideNavigation, 
  Container, 
  Table, 
  SplitPanel,
  Box,
  ColumnLayout
} from '@cloudscape-design/components';
import { useState } from 'react';

function AppLayoutWithSplitPanel() {
  const [navigationOpen, setNavigationOpen] = useState(true);
  const [toolsOpen, setToolsOpen] = useState(false);
  const [splitPanelOpen, setSplitPanelOpen] = useState(false);
  const [splitPanelSize, setSplitPanelSize] = useState(300);
  const [selectedItem, setSelectedItem] = useState(null);
  
  // Sample data
  const items = [
    { id: 'i-1234', name: 'Instance 1', type: 't2.micro', state: 'Running' },
    { id: 'i-5678', name: 'Instance 2', type: 't2.small', state: 'Stopped' },
    { id: 'i-9012', name: 'Instance 3', type: 't3.medium', state: 'Running' }
  ];
  
  // Column definitions for the table
  const columnDefinitions = [
    { id: 'id', header: 'ID', cell: item => item.id },
    { id: 'name', header: 'Name', cell: item => item.name },
    { id: 'type', header: 'Type', cell: item => item.type },
    { id: 'state', header: 'State', cell: item => item.state }
  ];
  
  // Handle item selection
  const handleSelectionChange = ({ detail }) => {
    if (detail.selectedItems.length > 0) {
      setSelectedItem(detail.selectedItems[0]);
      setSplitPanelOpen(true);
    } else {
      setSelectedItem(null);
      setSplitPanelOpen(false);
    }
  };
  
  return (
    <AppLayout
      navigation={
        <SideNavigation
          activeHref="#"
          header={{ text: 'My Application', href: '#' }}
          items={[
            { type: 'link', text: 'Instances', href: '#' },
            { type: 'link', text: 'Volumes', href: '#' }
          ]}
        />
      }
      navigationOpen={navigationOpen}
      onNavigationChange={({ detail }) => setNavigationOpen(detail.open)}
      
      content={
        <Container>
          <Table
            columnDefinitions={columnDefinitions}
            items={items}
            selectionType="single"
            selectedItems={selectedItem ? [selectedItem] : []}
            onSelectionChange={handleSelectionChange}
            header={<h2>Instances</h2>}
            variant="container"
          />
        </Container>
      }
      
      toolsHide={true}
      
      splitPanel={
        <SplitPanel
          header={selectedItem ? `Instance details: ${selectedItem.name}` : 'Details'}
          i18nStrings={{
            preferencesTitle: 'Split panel preferences',
            preferencesPositionLabel: 'Split panel position',
            preferencesPositionBottom: 'Bottom',
            preferencesPositionSide: 'Side',
            preferencesConfirm: 'Confirm',
            preferencesCancel: 'Cancel',
            closeButtonAriaLabel: 'Close panel',
            openButtonAriaLabel: 'Open panel',
            resizeHandleAriaLabel: 'Resize split panel'
          }}
        >
          {selectedItem && (
            <ColumnLayout columns={2} variant="text-grid">
              <Box variant="awsui-key-label">ID</Box>
              <Box>{selectedItem.id}</Box>
              
              <Box variant="awsui-key-label">Name</Box>
              <Box>{selectedItem.name}</Box>
              
              <Box variant="awsui-key-label">Type</Box>
              <Box>{selectedItem.type}</Box>
              
              <Box variant="awsui-key-label">State</Box>
              <Box>{selectedItem.state}</Box>
            </ColumnLayout>
          )}
        </SplitPanel>
      }
      splitPanelOpen={splitPanelOpen}
      onSplitPanelToggle={({ detail }) => setSplitPanelOpen(detail.open)}
      splitPanelSize={splitPanelSize}
      onSplitPanelResize={({ detail }) => setSplitPanelSize(detail.size)}
    />
  );
}
```

### AppLayout with Drawers

```jsx
import { 
  AppLayout, 
  SideNavigation,
  Container, 
  Button, 
  Header, 
  ContentLayout,
  SpaceBetween
} from '@cloudscape-design/components';
import { useState } from 'react';

function AppLayoutWithDrawers() {
  const [navigationOpen, setNavigationOpen] = useState(true);
  const [activeDrawer, setActiveDrawer] = useState(null);
  
  // Drawer definitions
  const drawers = [
    {
      id: 'drawer1',
      content: (
        <Container header={<Header variant="h2">First drawer</Header>}>
          <p>This is the content of the first drawer.</p>
          <p>You can put any content here, such as forms, tables, or custom components.</p>
          <Button onClick={() => setActiveDrawer(null)}>Close drawer</Button>
        </Container>
      ),
      ariaLabels: {
        closeButton: 'Close first drawer',
        drawerName: 'First drawer'
      }
    },
    {
      id: 'drawer2',
      content: (
        <Container header={<Header variant="h2">Second drawer</Header>}>
          <p>This is the content of the second drawer.</p>
          <p>Drawers are useful for supplementary tasks that don't require a full page.</p>
          <Button onClick={() => setActiveDrawer(null)}>Close drawer</Button>
        </Container>
      ),
      ariaLabels: {
        closeButton: 'Close second drawer',
        drawerName: 'Second drawer'
      }
    }
  ];
  
  return (
    <AppLayout
      navigation={
        <SideNavigation
          activeHref="#"
          header={{ text: 'My Application', href: '#' }}
          items={[
            { type: 'link', text: 'Dashboard', href: '#' },
            { type: 'link', text: 'Resources', href: '#' }
          ]}
        />
      }
      navigationOpen={navigationOpen}
      onNavigationChange={({ detail }) => setNavigationOpen(detail.open)}
      
      content={
        <ContentLayout
          header={<Header variant="h1">Dashboard</Header>}
        >
          <Container>
            <SpaceBetween size="l">
              <h2>Drawer examples</h2>
              
              <SpaceBetween direction="horizontal" size="xs">
                <Button onClick={() => setActiveDrawer('drawer1')}>
                  Open first drawer
                </Button>
                
                <Button onClick={() => setActiveDrawer('drawer2')}>
                  Open second drawer
                </Button>
              </SpaceBetween>
              
              <p>
                Drawers provide a way to display supplementary content without
                navigating away from the current page. They appear at the bottom
                of the page and can be dismissed by the user.
              </p>
            </SpaceBetween>
          </Container>
        </ContentLayout>
      }
      
      toolsHide={true}
      
      drawers={drawers}
      activeDrawerId={activeDrawer}
      onDrawerChange={({ detail }) => setActiveDrawer(detail.activeDrawerId)}
    />
  );
}
```

## Accessibility

- Provides proper ARIA labels for navigation toggle buttons
- Keyboard navigation support between main regions
- Proper focus management when panels open/close
- Screen reader announcements for state changes

## Best Practices

1. Use the appropriate contentType property to optimize layout for specific content patterns
2. Implement responsive behavior by handling navigationOpen state
3. Provide helpful content in the tools panel (typically using HelpPanel component)
4. Keep side navigation concise and well-organized
5. Use split panel for displaying details about selected items
6. Use drawers for supplementary tasks that don't require full-page navigation
7. Include proper breadcrumbs for navigation hierarchy
8. Display relevant notifications with the Flashbar component
9. Set appropriate ARIA labels for accessibility
10. Consider using AppLayoutToolbar for productivity-focused applications
