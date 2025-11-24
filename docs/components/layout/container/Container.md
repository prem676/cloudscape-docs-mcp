# Container

The Container component is a fundamental layout element that presents a group of related content, clearly indicating that the items belong together. It provides visual separation and structure to your user interface.

## Import

```jsx
import { Container } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Container } from '@cloudscape-design/components';

function BasicContainer() {
  return (
    <Container>
      <p>This content is contained within a visual container.</p>
    </Container>
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `children` | ReactNode | Content to be displayed inside the container |
| `header` | ReactNode | Header displayed at the top of the container |
| `footer` | ReactNode | Footer displayed at the bottom of the container |
| `variant` | 'default' \| 'stacked' | Visual variant of the container |
| `disableContentPaddings` | boolean | Removes the default padding from the content area |
| `disableHeaderPaddings` | boolean | Removes the default padding from the header |
| `disableFooterPaddings` | boolean | Removes the default padding from the footer |

## Examples

### Container with Header and Footer

```jsx
import { Container, Header, Box, Button, SpaceBetween } from '@cloudscape-design/components';

function ContainerWithHeaderAndFooter() {
  return (
    <Container
      header={
        <Header
          variant="h2"
          description="This is a description that provides more details."
          actions={
            <Button variant="primary">Action</Button>
          }
        >
          Container title
        </Header>
      }
      footer={
        <Box textAlign="right">
          <SpaceBetween direction="horizontal" size="xs">
            <Button variant="link">Cancel</Button>
            <Button variant="primary">Submit</Button>
          </SpaceBetween>
        </Box>
      }
    >
      <p>This is the main content of the container.</p>
      <p>Container provides a visual boundary around related content.</p>
    </Container>
  );
}
```

### Stacked Containers

```jsx
import { Container, Header, SpaceBetween } from '@cloudscape-design/components';

function StackedContainers() {
  return (
    <SpaceBetween size="l">
      <Container
        header={<Header variant="h2">First container</Header>}
      >
        <p>This is the content of the first container.</p>
      </Container>
      
      <Container
        header={<Header variant="h2">Second container</Header>}
      >
        <p>This is the content of the second container.</p>
      </Container>
      
      <Container
        header={<Header variant="h2">Third container</Header>}
      >
        <p>This is the content of the third container.</p>
      </Container>
    </SpaceBetween>
  );
}
```

### Container with Form Elements

```jsx
import { 
  Container, 
  Header, 
  FormField, 
  Input,
  Select,
  SpaceBetween,
  Button
} from '@cloudscape-design/components';
import { useState } from 'react';

function ContainerWithForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    type: null
  });
  
  return (
    <Container
      header={<Header variant="h2">User information</Header>}
      footer={
        <SpaceBetween direction="horizontal" size="xs" alignItems="end">
          <Button variant="link">Cancel</Button>
          <Button variant="primary">Save</Button>
        </SpaceBetween>
      }
    >
      <SpaceBetween size="l">
        <FormField
          label="Name"
          description="Enter your full name"
        >
          <Input
            value={formData.name}
            onChange={({ detail }) => 
              setFormData(prev => ({ ...prev, name: detail.value }))
            }
          />
        </FormField>
        
        <FormField
          label="Email"
          description="Enter your email address"
        >
          <Input
            type="email"
            value={formData.email}
            onChange={({ detail }) => 
              setFormData(prev => ({ ...prev, email: detail.value }))
            }
          />
        </FormField>
        
        <FormField
          label="Account type"
          description="Select your account type"
        >
          <Select
            options={[
              { label: 'Personal', value: 'personal' },
              { label: 'Business', value: 'business' },
              { label: 'Educational', value: 'educational' }
            ]}
            selectedOption={formData.type}
            onChange={({ detail }) => 
              setFormData(prev => ({ ...prev, type: detail.selectedOption }))
            }
          />
        </FormField>
      </SpaceBetween>
    </Container>
  );
}
```

### Nested Containers

```jsx
import { Container, Header, ColumnLayout, Box } from '@cloudscape-design/components';

function NestedContainers() {
  return (
    <Container
      header={<Header variant="h1">Dashboard</Header>}
    >
      <ColumnLayout columns={2} variant="text-grid">
        <Container
          header={<Header variant="h2">System status</Header>}
        >
          <Box>
            <Box variant="awsui-key-label">CPU Utilization</Box>
            <Box variant="awsui-value-large">42%</Box>
          </Box>
          <Box>
            <Box variant="awsui-key-label">Memory Usage</Box>
            <Box variant="awsui-value-large">2.1 GB</Box>
          </Box>
          <Box>
            <Box variant="awsui-key-label">Disk Space</Box>
            <Box variant="awsui-value-large">120 GB available</Box>
          </Box>
        </Container>
        
        <Container
          header={<Header variant="h2">Recent activity</Header>}
        >
          <Box>
            <Box variant="awsui-key-label">Last login</Box>
            <Box variant="awsui-value-large">2 hours ago</Box>
          </Box>
          <Box>
            <Box variant="awsui-key-label">Last backup</Box>
            <Box variant="awsui-value-large">Yesterday, 11:20 PM</Box>
          </Box>
          <Box>
            <Box variant="awsui-key-label">Updates available</Box>
            <Box variant="awsui-value-large">3</Box>
          </Box>
        </Container>
      </ColumnLayout>
    </Container>
  );
}
```

### Container with Custom Styling

```jsx
import { Container, Header, Box } from '@cloudscape-design/components';

function CustomStyledContainer() {
  return (
    <div style={{ background: '#f2f3f3', padding: '20px' }}>
      <Container
        header={
          <Header
            variant="h2"
            description="A container with custom styling"
          >
            Custom container
          </Header>
        }
        // Remove default content padding to apply custom padding
        disableContentPaddings={true}
      >
        <Box padding="l" color="text-status-info" textAlign="center">
          <h3>Custom content area</h3>
          <p>
            This container has custom styling applied to its content area.
            The default paddings are removed to allow for custom padding.
          </p>
        </Box>
      </Container>
    </div>
  );
}
```

### Container with Expandable Sections

```jsx
import { 
  Container, 
  Header, 
  ExpandableSection,
  SpaceBetween
} from '@cloudscape-design/components';

function ContainerWithExpandableSections() {
  return (
    <Container
      header={<Header variant="h2">Documentation</Header>}
    >
      <SpaceBetween size="l">
        <ExpandableSection headerText="Getting started">
          <p>
            This section contains information about getting started with the application.
            Follow these steps to set up your environment and create your first project.
          </p>
        </ExpandableSection>
        
        <ExpandableSection headerText="Configuration options">
          <p>
            Learn about the various configuration options available in the application.
            These settings allow you to customize the behavior to suit your needs.
          </p>
        </ExpandableSection>
        
        <ExpandableSection headerText="Advanced features">
          <p>
            Discover advanced features that can help you optimize your workflow.
            These features are designed for experienced users who need more control.
          </p>
        </ExpandableSection>
      </SpaceBetween>
    </Container>
  );
}
```

## Accessibility

- Uses semantic HTML structure
- Properly associates headers with content
- Maintains proper color contrast
- Supports keyboard navigation

## Best Practices

1. Use containers to group related content and create visual hierarchy
2. Include descriptive headers to communicate the purpose of the container
3. Use the footer for action buttons, especially in form containers
4. Nest containers when organizing complex layouts, but avoid excessive nesting
5. Combine with other layout components like ColumnLayout or Grid for more complex arrangements
6. Use SpaceBetween to maintain consistent spacing between stacked containers
7. Consider using disableContentPaddings when you need custom padding control
8. Keep container content focused on a single topic or task
9. Use variant="stacked" when you need a more prominent visual separation
10. Ensure header text clearly describes the container's contents
11. Avoid overloading containers with too much information - consider splitting into multiple containers if needed
