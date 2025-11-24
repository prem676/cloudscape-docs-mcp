# Modal

The Modal component is a dialog window that appears on top of the main application content, preventing interaction with the underlying page until closed. It's used for focused interactions that require immediate attention.

## Import

```jsx
import { Modal } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Modal, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicModal() {
  const [visible, setVisible] = useState(false);
  
  return (
    <>
      <Button onClick={() => setVisible(true)}>Open modal</Button>
      
      <Modal
        visible={visible}
        onDismiss={() => setVisible(false)}
        header="Modal title"
      >
        <Box padding="l">This is the modal content.</Box>
      </Modal>
    </>
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `children` | ReactNode | Content of the modal |
| `header` | ReactNode | Title displayed at the top of the modal |
| `visible` | boolean | Determines whether the modal is displayed |
| `size` | 'small' \| 'medium' \| 'large' \| 'max' | Controls the width of the modal |
| `footer` | ReactNode | Content displayed at the bottom of the modal (typically action buttons) |
| `onDismiss` | () => void | Called when the user dismisses the modal |
| `closeAriaLabel` | string | ARIA label for the close button |
| `modalRoot` | HTMLElement | DOM node where the modal should be rendered |
| `disableContentPaddings` | boolean | Removes the default padding from the content area |

## Examples

### Confirmation Modal

```jsx
import { Modal, Box, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function ConfirmationModal() {
  const [visible, setVisible] = useState(false);
  
  const handleDelete = () => {
    // Perform delete operation
    console.log('Item deleted');
    setVisible(false);
  };
  
  return (
    <>
      <Button variant="primary" onClick={() => setVisible(true)}>
        Delete item
      </Button>
      
      <Modal
        visible={visible}
        onDismiss={() => setVisible(false)}
        header="Confirm deletion"
        size="small"
        footer={
          <Box float="right">
            <SpaceBetween direction="horizontal" size="xs">
              <Button variant="link" onClick={() => setVisible(false)}>
                Cancel
              </Button>
              <Button variant="primary" onClick={handleDelete}>
                Delete
              </Button>
            </SpaceBetween>
          </Box>
        }
      >
        <Box variant="span">
          Are you sure you want to delete this item?
          This action cannot be undone.
        </Box>
      </Modal>
    </>
  );
}
```

### Form Modal

```jsx
import { 
  Modal, 
  Box, 
  Button, 
  SpaceBetween,
  Form,
  FormField,
  Input,
  Select
} from '@cloudscape-design/components';
import { useState } from 'react';

function FormModal() {
  const [visible, setVisible] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    type: null
  });
  const [formError, setFormError] = useState('');
  
  const handleSubmit = () => {
    // Validate form
    if (!formData.name) {
      setFormError('Name is required');
      return;
    }
    
    if (!formData.type) {
      setFormError('Type is required');
      return;
    }
    
    // Submit form data
    console.log('Form submitted:', formData);
    setVisible(false);
    
    // Reset form
    setFormData({
      name: '',
      type: null
    });
    setFormError('');
  };
  
  const handleCancel = () => {
    setVisible(false);
    setFormError('');
  };
  
  return (
    <>
      <Button variant="primary" onClick={() => setVisible(true)}>
        Create new item
      </Button>
      
      <Modal
        visible={visible}
        onDismiss={handleCancel}
        header="Create new item"
        size="medium"
        footer={
          <Box float="right">
            <SpaceBetween direction="horizontal" size="xs">
              <Button variant="link" onClick={handleCancel}>
                Cancel
              </Button>
              <Button variant="primary" onClick={handleSubmit}>
                Create
              </Button>
            </SpaceBetween>
          </Box>
        }
      >
        <Form errorText={formError}>
          <SpaceBetween direction="vertical" size="l">
            <FormField
              label="Name"
              description="Enter a name for the item"
              constraintText="Required"
            >
              <Input
                value={formData.name}
                onChange={({ detail }) => 
                  setFormData(prev => ({ ...prev, name: detail.value }))
                }
              />
            </FormField>
            
            <FormField
              label="Type"
              description="Select the item type"
              constraintText="Required"
            >
              <Select
                options={[
                  { label: 'Type A', value: 'a' },
                  { label: 'Type B', value: 'b' },
                  { label: 'Type C', value: 'c' }
                ]}
                selectedOption={formData.type}
                onChange={({ detail }) => 
                  setFormData(prev => ({ ...prev, type: detail.selectedOption }))
                }
              />
            </FormField>
          </SpaceBetween>
        </Form>
      </Modal>
    </>
  );
}
```

### Large Content Modal

```jsx
import { 
  Modal, 
  Box, 
  Button, 
  Tabs,
  Container,
  Header,
  Table
} from '@cloudscape-design/components';
import { useState } from 'react';

function LargeContentModal() {
  const [visible, setVisible] = useState(false);
  const [activeTabId, setActiveTabId] = useState('details');
  
  // Sample data for table
  const items = [
    { id: '1', name: 'Item 1', description: 'Description 1' },
    { id: '2', name: 'Item 2', description: 'Description 2' },
    { id: '3', name: 'Item 3', description: 'Description 3' }
  ];
  
  return (
    <>
      <Button onClick={() => setVisible(true)}>
        View details
      </Button>
      
      <Modal
        visible={visible}
        onDismiss={() => setVisible(false)}
        header="Resource details"
        size="large"
        footer={
          <Box float="right">
            <Button variant="primary" onClick={() => setVisible(false)}>
              Close
            </Button>
          </Box>
        }
      >
        <Tabs
          tabs={[
            {
              id: 'details',
              label: 'Details',
              content: (
                <Container
                  header={<Header variant="h2">Resource information</Header>}
                >
                  <p>
                    This is detailed information about the resource.
                    You can add any content here, such as descriptions,
                    properties, or other information.
                  </p>
                </Container>
              )
            },
            {
              id: 'related',
              label: 'Related items',
              content: (
                <Table
                  columnDefinitions={[
                    { id: 'id', header: 'ID', cell: item => item.id },
                    { id: 'name', header: 'Name', cell: item => item.name },
                    { id: 'description', header: 'Description', cell: item => item.description }
                  ]}
                  items={items}
                  header={<Header variant="h2">Related items</Header>}
                />
              )
            },
            {
              id: 'settings',
              label: 'Settings',
              content: (
                <Container
                  header={<Header variant="h2">Resource settings</Header>}
                >
                  <p>Configure settings for this resource here.</p>
                </Container>
              )
            }
          ]}
          activeTabId={activeTabId}
          onChange={({ detail }) => setActiveTabId(detail.activeTabId)}
        />
      </Modal>
    </>
  );
}
```

### Modal with Loading State

```jsx
import { 
  Modal, 
  Box, 
  Button, 
  SpaceBetween,
  Spinner
} from '@cloudscape-design/components';
import { useState } from 'react';

function LoadingModal() {
  const [visible, setVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  
  const handleAction = () => {
    setLoading(true);
    
    // Simulate API call
    setTimeout(() => {
      setLoading(false);
      setVisible(false);
    }, 2000);
  };
  
  return (
    <>
      <Button onClick={() => setVisible(true)}>
        Perform action
      </Button>
      
      <Modal
        visible={visible}
        onDismiss={() => !loading && setVisible(false)}
        header="Confirmation"
        closeAriaLabel="Close modal"
        footer={
          <Box float="right">
            <SpaceBetween direction="horizontal" size="xs">
              <Button 
                variant="link" 
                onClick={() => setVisible(false)}
                disabled={loading}
              >
                Cancel
              </Button>
              <Button 
                variant="primary" 
                onClick={handleAction}
                loading={loading}
                loadingText="Processing..."
              >
                Continue
              </Button>
            </SpaceBetween>
          </Box>
        }
      >
        {loading ? (
          <Box textAlign="center" padding="l">
            <SpaceBetween size="m" direction="vertical">
              <Spinner size="large" />
              <Box variant="p">Processing your request...</Box>
            </SpaceBetween>
          </Box>
        ) : (
          <Box variant="span">
            Are you sure you want to continue with this action?
          </Box>
        )}
      </Modal>
    </>
  );
}
```

## Accessibility

- Traps focus within the modal when open
- Provides keyboard navigation (Tab, Escape to close)
- Returns focus to the trigger element when closed
- Uses appropriate ARIA roles and properties
- Close button has an accessible label

## Best Practices

1. Use modals sparingly - they interrupt user workflow
2. Keep modal content focused on a single task or topic
3. Provide clear headers that explain the modal's purpose
4. Include action buttons in the footer for common actions
5. Allow dismissal both through a close button and by clicking outside (via onDismiss)
6. Disable the underlying page to prevent interaction when modal is open
7. Choose an appropriate size based on content needs:
   - `small` for confirmations or simple messages
   - `medium` for forms or content with moderate complexity
   - `large` for complex forms or data displays
   - `max` for content that needs maximum screen space
8. Consider using a form inside the modal for data collection
9. Provide loading states for actions that take time
10. Return focus to the triggering element when the modal closes
