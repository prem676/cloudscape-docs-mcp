# Side Navigation

The SideNavigation component provides a list of navigational links that point to the pages within an application. It's typically used as the primary navigation in the AppLayout component.

## Import

```jsx
import { SideNavigation } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { SideNavigation } from '@cloudscape-design/components';

function BasicSideNavigation() {
  return (
    <SideNavigation
      activeHref="#/home"
      header={{ text: 'My Application', href: '#/home' }}
      items={[
        { type: 'link', text: 'Home', href: '#/home' },
        { type: 'link', text: 'Dashboard', href: '#/dashboard' },
        { type: 'link', text: 'Settings', href: '#/settings' }
      ]}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `items` | Array | Array of navigation items |
| `header` | { text, href } | Header displayed at the top of the navigation |
| `activeHref` | string | URL of the currently active page |
| `onFollow` | (event: CustomEvent) => void | Called when a navigation link is clicked |
| `ariaLabel` | string | ARIA label for the navigation |

## Item Types

- **Link** - A simple navigational link to a page
- **Section** - A collapsible group of navigation items
- **ExpandableLink** - A link that can be expanded to show related links
- **Divider** - A horizontal line to separate navigation items
- **Section group** - A non-collapsible group of sections, used for organizing complex navigation

## Examples

### Side Navigation with Sections

```jsx
import { SideNavigation } from '@cloudscape-design/components';

function NavigationWithSections() {
  return (
    <SideNavigation
      activeHref="#/dashboard/overview"
      header={{ text: 'Service Console', href: '#/' }}
      items={[
        {
          type: 'section',
          text: 'Dashboard',
          items: [
            { type: 'link', text: 'Overview', href: '#/dashboard/overview' },
            { type: 'link', text: 'Analytics', href: '#/dashboard/analytics' },
            { type: 'link', text: 'Reports', href: '#/dashboard/reports' }
          ]
        },
        {
          type: 'section',
          text: 'Resources',
          items: [
            { type: 'link', text: 'Instances', href: '#/resources/instances' },
            { type: 'link', text: 'Storage', href: '#/resources/storage' },
            { type: 'link', text: 'Networking', href: '#/resources/networking' }
          ]
        },
        { type: 'divider' },
        { type: 'link', text: 'Settings', href: '#/settings' },
        { type: 'link', text: 'Help', href: '#/help' }
      ]}
    />
  );
}
```

### Side Navigation with Expandable Links

```jsx
import { SideNavigation } from '@cloudscape-design/components';

function NavigationWithExpandableLinks() {
  return (
    <SideNavigation
      activeHref="#/resources/instances/i-1234"
      header={{ text: 'Service Console', href: '#/' }}
      items={[
        { type: 'link', text: 'Dashboard', href: '#/dashboard' },
        {
          type: 'expandable-link',
          text: 'Resources',
          href: '#/resources',
          items: [
            { type: 'link', text: 'Instances', href: '#/resources/instances' },
            { type: 'link', text: 'Storage', href: '#/resources/storage' },
            { type: 'link', text: 'Networking', href: '#/resources/networking' }
          ]
        },
        {
          type: 'expandable-link',
          text: 'Instances',
          href: '#/resources/instances',
          items: [
            { type: 'link', text: 'Instance i-1234', href: '#/resources/instances/i-1234' },
            { type: 'link', text: 'Instance i-5678', href: '#/resources/instances/i-5678' }
          ]
        },
        { type: 'link', text: 'Settings', href: '#/settings' }
      ]}
    />
  );
}
```

### Side Navigation with Section Groups

```jsx
import { SideNavigation } from '@cloudscape-design/components';

function NavigationWithSectionGroups() {
  return (
    <SideNavigation
      activeHref="#/compute/instances"
      header={{ text: 'AWS Console', href: '#/' }}
      items={[
        { type: 'link', text: 'Home', href: '#/' },
        { type: 'divider' },
        {
          type: 'section-group',
          title: 'Recently visited',
          items: [
            {
              type: 'section',
              text: 'Compute',
              items: [
                { type: 'link', text: 'EC2 Instances', href: '#/compute/instances' },
                { type: 'link', text: 'Lambda Functions', href: '#/compute/lambda' }
              ]
            },
            {
              type: 'section',
              text: 'Storage',
              items: [
                { type: 'link', text: 'S3 Buckets', href: '#/storage/s3' },
                { type: 'link', text: 'EBS Volumes', href: '#/storage/ebs' }
              ]
            }
          ]
        },
        { type: 'divider' },
        {
          type: 'section-group',
          title: 'All services',
          items: [
            {
              type: 'section',
              text: 'Compute',
              items: [
                { type: 'link', text: 'EC2', href: '#/compute/ec2' },
                { type: 'link', text: 'Lambda', href: '#/compute/lambda' },
                { type: 'link', text: 'ECS', href: '#/compute/ecs' },
                { type: 'link', text: 'EKS', href: '#/compute/eks' }
              ]
            },
            {
              type: 'section',
              text: 'Storage',
              items: [
                { type: 'link', text: 'S3', href: '#/storage/s3' },
                { type: 'link', text: 'EBS', href: '#/storage/ebs' },
                { type: 'link', text: 'EFS', href: '#/storage/efs' },
                { type: 'link', text: 'Glacier', href: '#/storage/glacier' }
              ]
            },
            {
              type: 'section',
              text: 'Database',
              items: [
                { type: 'link', text: 'RDS', href: '#/database/rds' },
                { type: 'link', text: 'DynamoDB', href: '#/database/dynamodb' },
                { type: 'link', text: 'ElastiCache', href: '#/database/elasticache' }
              ]
            }
          ]
        }
      ]}
    />
  );
}
```

### Side Navigation with Badges and Icons

```jsx
import { SideNavigation } from '@cloudscape-design/components';

function NavigationWithBadgesAndIcons() {
  return (
    <SideNavigation
      activeHref="#/notifications"
      header={{ text: 'My Application', href: '#/' }}
      items={[
        { 
          type: 'link', 
          text: 'Dashboard', 
          href: '#/dashboard',
          iconName: 'dashboard' 
        },
        { 
          type: 'link', 
          text: 'Notifications', 
          href: '#/notifications',
          iconName: 'notification', 
          badge: { content: '4', color: 'red' } 
        },
        {
          type: 'section',
          text: 'Resources',
          iconName: 'folder',
          items: [
            { 
              type: 'link', 
              text: 'Instances', 
              href: '#/resources/instances',
              badge: { content: 'New', color: 'blue' }
            },
            { type: 'link', text: 'Storage', href: '#/resources/storage' }
          ]
        },
        { 
          type: 'link', 
          text: 'Settings', 
          href: '#/settings',
          iconName: 'settings' 
        }
      ]}
    />
  );
}
```

### Side Navigation with Custom Handling

```jsx
import { SideNavigation } from '@cloudscape-design/components';
import { useState } from 'react';

function NavigationWithCustomHandling() {
  const [activeHref, setActiveHref] = useState('#/dashboard');
  
  const handleFollow = (event) => {
    // Prevent default navigation
    event.preventDefault();
    
    const href = event.detail.href;
    setActiveHref(href);
    
    // Custom navigation logic
    console.log(`Navigating to: ${href}`);
    
    // In a real application, you might use a router:
    // router.push(href);
  };
  
  return (
    <SideNavigation
      activeHref={activeHref}
      header={{ text: 'My Application', href: '#/' }}
      items={[
        { type: 'link', text: 'Dashboard', href: '#/dashboard' },
        { type: 'link', text: 'Resources', href: '#/resources' },
        { type: 'link', text: 'Settings', href: '#/settings' }
      ]}
      onFollow={handleFollow}
    />
  );
}
```

## Integration with AppLayout

```jsx
import { AppLayout, SideNavigation } from '@cloudscape-design/components';
import { useState } from 'react';

function AppWithNavigation() {
  const [navigationOpen, setNavigationOpen] = useState(true);
  
  return (
    <AppLayout
      navigation={
        <SideNavigation
          activeHref="#/dashboard"
          header={{ text: 'My Application', href: '#/' }}
          items={[
            { type: 'link', text: 'Dashboard', href: '#/dashboard' },
            { type: 'link', text: 'Resources', href: '#/resources' },
            { type: 'link', text: 'Settings', href: '#/settings' }
          ]}
        />
      }
      navigationOpen={navigationOpen}
      onNavigationChange={({ detail }) => setNavigationOpen(detail.open)}
      content={<div>Main content goes here</div>}
    />
  );
}
```

## Accessibility

- Uses appropriate ARIA roles for navigation
- Supports keyboard navigation
- Provides focus management for navigation items
- ARIA labels for screen readers
- Proper contrast for different visual modes

## Best Practices

1. Keep the navigation structure simple and intuitive
2. Use consistent naming conventions for navigation items
3. Highlight the current page with the activeHref property
4. Group related items using sections or expandable links
5. Use dividers to separate logical groups of navigation items
6. Include a header with a link to the home page
7. Consider using icons to enhance visual recognition
8. Use badges sparingly to highlight important information
9. Implement custom onFollow handling for advanced navigation needs
10. Always integrate SideNavigation with AppLayout for a consistent user experience
11. Ensure navigation items clearly describe their destination
12. Limit the depth of nested navigation to avoid complexity
