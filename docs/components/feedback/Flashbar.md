# Flashbar

The Flashbar component displays important messages that require the user's attention. It can show multiple notifications at once, each with different types, actions, and dismissal options.

## Import

```jsx
import { Flashbar } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Flashbar } from '@cloudscape-design/components';

function BasicFlashbar() {
  return (
    <Flashbar
      items={[
        {
          header: 'Success message',
          type: 'success',
          content: 'The operation completed successfully.',
          dismissible: true,
        }
      ]}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `items` | Array | Array of flashbar item objects to be displayed |
| `stackItems` | boolean | Whether to stack the items vertically |
| `i18nStrings` | object | Object containing localized strings |

## Flashbar Item Properties

| Property | Type | Description |
|----------|------|-------------|
| `header` | string | Header text for the item |
| `content` | ReactNode | Content for the item (text or JSX) |
| `type` | 'success' \| 'warning' \| 'error' \| 'info' | Type of the notification |
| `dismissible` | boolean | Whether the item can be dismissed |
| `dismissLabel` | string | Accessibility label for the dismiss button |
| `statusIconAriaLabel` | string | Accessibility label for the status icon |
| `loading` | boolean | Whether to show a loading indicator |
| `action` | ReactNode | Action component for the item |
| `buttonText` | string | Text for the button (deprecated, use action instead) |
| `onButtonClick` | () => void | Callback for button click (deprecated, use action instead) |
| `onDismiss` | () => void | Callback when the item is dismissed |
| `id` | string | Unique identifier for the item |

## Examples

### Different Types of Flash Messages

```jsx
import { Flashbar } from '@cloudscape-design/components';

function FlashbarTypes() {
  return (
    <Flashbar
      items={[
        {
          header: 'Success',
          type: 'success',
          content: 'Resource created successfully.',
          dismissible: true,
          dismissLabel: 'Dismiss success message',
          statusIconAriaLabel: 'Success'
        },
        {
          header: 'Warning',
          type: 'warning',
          content: 'This configuration might affect performance.',
          dismissible: true,
          dismissLabel: 'Dismiss warning message',
          statusIconAriaLabel: 'Warning'
        },
        {
          header: 'Error',
          type: 'error',
          content: 'Failed to save the configuration.',
          dismissible: true,
          dismissLabel: 'Dismiss error message',
          statusIconAriaLabel: 'Error'
        },
        {
          header: 'Information',
          type: 'info',
          content: 'A new version of the service is available.',
          dismissible: true,
          dismissLabel: 'Dismiss info message',
          statusIconAriaLabel: 'Information'
        }
      ]}
    />
  );
}
```

### Flashbar with Actions

```jsx
import { Flashbar, Button, Link } from '@cloudscape-design/components';

function FlashbarWithActions() {
  return (
    <Flashbar
      items={[
        {
          header: 'Update available',
          type: 'info',
          content: 'A new version of the service is available.',
          action: <Button>Update now</Button>,
          dismissible: true
        },
        {
          header: 'Configuration conflict',
          type: 'warning',
          content: 'Current configuration may cause conflicts with other resources.',
          action: (
            <Button variant="link">
              Review configuration
            </Button>
          ),
          dismissible: true
        },
        {
          header: 'Service limit approaching',
          type: 'warning',
          content: (
            <>
              You are approaching your service limit. 
              <Link href="#" external>Learn more</Link> about service limits.
            </>
          ),
          action: <Button>Request limit increase</Button>,
          dismissible: true
        }
      ]}
    />
  );
}
```

### Interactive Dismissible Flashbar

```jsx
import { Flashbar, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function DismissibleFlashbar() {
  const [items, setItems] = useState([]);
  
  // Add a success message
  const addSuccessMessage = () => {
    const id = Date.now().toString();
    setItems(prevItems => [...prevItems, {
      id,
      type: 'success',
      header: 'Success message',
      content: 'Operation completed successfully.',
      dismissible: true,
      onDismiss: () => removeItem(id)
    }]);
  };
  
  // Add a warning message
  const addWarningMessage = () => {
    const id = Date.now().toString();
    setItems(prevItems => [...prevItems, {
      id,
      type: 'warning',
      header: 'Warning message',
      content: 'This action might have unintended consequences.',
      dismissible: true,
      onDismiss: () => removeItem(id)
    }]);
  };
  
  // Add an error message
  const addErrorMessage = () => {
    const id = Date.now().toString();
    setItems(prevItems => [...prevItems, {
      id,
      type: 'error',
      header: 'Error message',
      content: 'Operation failed to complete.',
      dismissible: true,
      onDismiss: () => removeItem(id)
    }]);
  };
  
  // Add an info message
  const addInfoMessage = () => {
    const id = Date.now().toString();
    setItems(prevItems => [...prevItems, {
      id,
      type: 'info',
      header: 'Information message',
      content: 'New features are available in this version.',
      dismissible: true,
      onDismiss: () => removeItem(id)
    }]);
  };
  
  // Remove an item by id
  const removeItem = (id) => {
    setItems(prevItems => prevItems.filter(item => item.id !== id));
  };
  
  // Clear all items
  const clearAll = () => {
    setItems([]);
  };
  
  return (
    <SpaceBetween size="m">
      <Flashbar items={items} />
      
      <SpaceBetween size="xs" direction="horizontal">
        <Button onClick={addSuccessMessage}>Add success</Button>
        <Button onClick={addWarningMessage}>Add warning</Button>
        <Button onClick={addErrorMessage}>Add error</Button>
        <Button onClick={addInfoMessage}>Add info</Button>
        <Button onClick={clearAll}>Clear all</Button>
      </SpaceBetween>
    </SpaceBetween>
  );
}
```

### Flashbar with Loading State

```jsx
import { Flashbar, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function LoadingFlashbar() {
  const [items, setItems] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  
  // Start a loading operation
  const startOperation = () => {
    // Clear previous messages
    setItems([]);
    
    // Add loading message
    const loadingId = Date.now().toString();
    setItems([{
      id: loadingId,
      type: 'info',
      loading: true,
      header: 'Operation in progress',
      content: 'Please wait while the operation completes...',
      dismissible: false
    }]);
    
    setIsLoading(true);
    
    // Simulate an operation
    setTimeout(() => {
      setIsLoading(false);
      setItems(prevItems => {
        // Remove loading message
        const filteredItems = prevItems.filter(item => item.id !== loadingId);
        
        // Add success message
        const successId = Date.now().toString();
        return [...filteredItems, {
          id: successId,
          type: 'success',
          header: 'Operation completed',
          content: 'The operation completed successfully.',
          dismissible: true,
          onDismiss: () => setItems(prevItems => prevItems.filter(item => item.id !== successId))
        }];
      });
    }, 3000);
  };
  
  // Simulate an error
  const simulateError = () => {
    // Clear previous messages
    setItems([]);
    
    // Add loading message
    const loadingId = Date.now().toString();
    setItems([{
      id: loadingId,
      type: 'info',
      loading: true,
      header: 'Operation in progress',
      content: 'Please wait while the operation completes...',
      dismissible: false
    }]);
    
    setIsLoading(true);
    
    // Simulate an operation that fails
    setTimeout(() => {
      setIsLoading(false);
      setItems(prevItems => {
        // Remove loading message
        const filteredItems = prevItems.filter(item => item.id !== loadingId);
        
        // Add error message
        const errorId = Date.now().toString();
        return [...filteredItems, {
          id: errorId,
          type: 'error',
          header: 'Operation failed',
          content: 'An error occurred while processing your request.',
          dismissible: true,
          action: <Button onClick={startOperation}>Retry</Button>,
          onDismiss: () => setItems(prevItems => prevItems.filter(item => item.id !== errorId))
        }];
      });
    }, 3000);
  };
  
  return (
    <SpaceBetween size="m">
      <Flashbar items={items} />
      
      <SpaceBetween size="xs" direction="horizontal">
        <Button onClick={startOperation} disabled={isLoading}>Start operation</Button>
        <Button onClick={simulateError} disabled={isLoading}>Simulate error</Button>
      </SpaceBetween>
    </SpaceBetween>
  );
}
```

### Flashbar with Rich Content

```jsx
import { Flashbar, Link, StatusIndicator, Box, SpaceBetween } from '@cloudscape-design/components';

function RichContentFlashbar() {
  return (
    <Flashbar
      items={[
        {
          header: 'Deployment status',
          type: 'info',
          content: (
            <SpaceBetween size="m">
              <Box>
                <SpaceBetween size="xs">
                  <div>Deployment of <strong>application-v1.2</strong> is in progress.</div>
                  <StatusIndicator type="in-progress">
                    Stage 2/3: Building containers
                  </StatusIndicator>
                  <div>
                    Started at: <time>2023-05-15 14:30</time> | 
                    Estimated completion: <time>2023-05-15 15:00</time>
                  </div>
                </SpaceBetween>
              </Box>
              <Box>
                <Link href="#" external>View deployment logs</Link> | 
                <Link href="#" external>Deployment documentation</Link>
              </Box>
            </SpaceBetween>
          ),
          dismissible: true
        },
        {
          header: 'Service health report',
          type: 'success',
          content: (
            <Box>
              <div>All services are operating normally.</div>
              <ul>
                <li><StatusIndicator type="success">API Gateway: 100% uptime</StatusIndicator></li>
                <li><StatusIndicator type="success">Database: 99.99% uptime</StatusIndicator></li>
                <li><StatusIndicator type="success">Authentication: 100% uptime</StatusIndicator></li>
                <li><StatusIndicator type="success">Storage: 99.95% uptime</StatusIndicator></li>
              </ul>
              <div>Last updated: <time>2023-05-15 15:00</time></div>
            </Box>
          ),
          dismissible: true
        }
      ]}
    />
  );
}
```

### Stacked Flashbar

```jsx
import { Flashbar, Button, SpaceBetween } from '@cloudscape-design/components';

function StackedFlashbar() {
  return (
    <Flashbar
      stackItems={true}
      items={[
        {
          header: 'Account verification required',
          type: 'warning',
          content: 'Please verify your email address to ensure account security.',
          action: <Button>Verify now</Button>,
          dismissible: true
        },
        {
          header: 'New features available',
          type: 'info',
          content: 'Check out the new features in this version.',
          action: <Button variant="link">Learn more</Button>,
          dismissible: true
        },
        {
          header: 'Service maintenance',
          type: 'warning',
          content: 'Scheduled maintenance on June 15, 2023, from 2:00 AM to 4:00 AM UTC.',
          dismissible: true
        }
      ]}
    />
  );
}
```

### Auto-dismissible Flashbar

```jsx
import { Flashbar, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function AutoDismissibleFlashbar() {
  const [items, setItems] = useState([]);
  
  // Add a message that auto-dismisses after a specified duration
  const addMessage = (type, header, content, duration = 5000) => {
    const id = Date.now().toString();
    const newItem = {
      id,
      type,
      header,
      content,
      dismissible: true,
      onDismiss: () => removeItem(id)
    };
    
    setItems(prevItems => [...prevItems, newItem]);
    
    // Auto-dismiss after duration
    setTimeout(() => {
      removeItem(id);
    }, duration);
  };
  
  // Remove an item by id
  const removeItem = (id) => {
    setItems(prevItems => prevItems.filter(item => item.id !== id));
  };
  
  return (
    <SpaceBetween size="m">
      <Flashbar items={items} />
      
      <SpaceBetween size="xs" direction="horizontal">
        <Button onClick={() => addMessage('success', 'Success', 'This message will auto-dismiss after 5 seconds', 5000)}>
          5s success message
        </Button>
        <Button onClick={() => addMessage('warning', 'Warning', 'This message will auto-dismiss after 8 seconds', 8000)}>
          8s warning message
        </Button>
        <Button onClick={() => addMessage('info', 'Info', 'This message will auto-dismiss after 10 seconds', 10000)}>
          10s info message
        </Button>
      </SpaceBetween>
    </SpaceBetween>
  );
}
```

## Accessibility

- Uses ARIA attributes for screen reader announcements
- Provides keyboard navigation for interactive elements
- Includes proper labeling for status icons and dismiss buttons
- Maintains focus management for actions and dismissal
- Provides descriptive message types for different notification categories
- Clear visual differentiation between message types

## Best Practices

1. Use the appropriate type for each message (success, warning, error, info)
2. Keep headers and content concise and informative
3. Provide clear actions when users need to respond to a message
4. Make messages dismissible when appropriate
5. Use loading state for operations in progress
6. Limit the number of simultaneous messages to avoid overwhelming users
7. Consider auto-dismissing success messages after a few seconds
8. Order messages by priority (errors, warnings, success, info)
9. Use stacked format when displaying multiple messages that need attention
10. Provide clear instructions for resolving warnings and errors
11. Include timestamps for time-sensitive notifications
12. Ensure the content is accessible and properly formatted
13. Test with screen readers to ensure accessibility
14. Use icons consistently for each message type
15. Consider using actions instead of text links within content for better accessibility
