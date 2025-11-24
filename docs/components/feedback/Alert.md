# Alert

The Alert component provides a brief message that gives information or instructs users to take a specific action.

## Import

```jsx
import { Alert } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
<Alert>This is a basic alert message.</Alert>
```

## Variants

```jsx
// Info alert (default)
<Alert>This is an informational message.</Alert>

// Success alert
<Alert type="success">Operation completed successfully.</Alert>

// Warning alert
<Alert type="warning">This action cannot be undone.</Alert>

// Error alert
<Alert type="error">An error occurred during the operation.</Alert>
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `children` | ReactNode | Alert message content |
| `type` | 'success' \| 'error' \| 'warning' \| 'info' | Determines the color and icon of the alert |
| `header` | ReactNode | Header text or element displayed at the top of the alert |
| `action` | ReactNode | Button or link that gives the user a relevant action |
| `dismissible` | boolean | Determines whether the alert can be dismissed |
| `dismissAriaLabel` | string | ARIA label for the dismiss button |
| `onDismiss` | () => void | Called when the user clicks the dismiss button |
| `visible` | boolean | Determines whether the alert is visible |

## Examples

### Alert with Header and Action

```jsx
import { Alert, Button } from '@cloudscape-design/components';

function AlertWithHeaderAndAction() {
  return (
    <Alert
      type="warning"
      header="Resource limit reached"
      action={<Button>Increase limit</Button>}
    >
      You have reached the maximum number of resources allowed for your account.
      Upgrade your plan to create more resources.
    </Alert>
  );
}
```

### Dismissible Alert

```jsx
import { Alert } from '@cloudscape-design/components';
import { useState } from 'react';

function DismissibleAlert() {
  const [visible, setVisible] = useState(true);
  
  return (
    <>
      {visible && (
        <Alert
          type="success"
          dismissible
          dismissAriaLabel="Close message"
          onDismiss={() => setVisible(false)}
        >
          Your changes have been saved successfully.
        </Alert>
      )}
    </>
  );
}
```

### Multiple Alert Types

```jsx
import { Alert, SpaceBetween } from '@cloudscape-design/components';

function MultipleAlerts() {
  return (
    <SpaceBetween size="m">
      <Alert type="info" header="Information">
        Your account is being set up. This may take a few minutes.
      </Alert>
      
      <Alert type="success" header="Success">
        The resource was created successfully.
      </Alert>
      
      <Alert type="warning" header="Warning">
        This action will restart all instances in your account.
      </Alert>
      
      <Alert type="error" header="Error">
        Failed to delete the resource. Please try again later.
      </Alert>
    </SpaceBetween>
  );
}
```

### Conditional Alert

```jsx
import { Alert, FormField, Input, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function ConditionalAlert() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  
  const validateEmail = () => {
    // Reset states
    setError('');
    setSuccess(false);
    
    // Simple email validation
    if (!email) {
      setError('Email is required');
      return false;
    }
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Please enter a valid email address');
      return false;
    }
    
    return true;
  };
  
  const handleSubmit = () => {
    if (validateEmail()) {
      // Simulate API call
      setTimeout(() => {
        setSuccess(true);
      }, 500);
    }
  };
  
  return (
    <SpaceBetween size="m">
      {error && (
        <Alert type="error" dismissible onDismiss={() => setError('')}>
          {error}
        </Alert>
      )}
      
      {success && (
        <Alert 
          type="success" 
          dismissible 
          onDismiss={() => setSuccess(false)}
        >
          Subscription confirmed! Check your email for next steps.
        </Alert>
      )}
      
      <FormField label="Email address">
        <Input
          value={email}
          onChange={({ detail }) => setEmail(detail.value)}
        />
      </FormField>
      
      <Button onClick={handleSubmit}>Subscribe</Button>
    </SpaceBetween>
  );
}
```

## Accessibility

- Uses semantic HTML with appropriate ARIA roles
- Type-specific icons have proper accessibility descriptions
- Dismiss button includes ARIA label for screen readers
- Focus management when alert appears or is dismissed

## Best Practices

1. Use the appropriate alert type to match the message severity:
   - `info` for general information
   - `success` for successful operations
   - `warning` for potentially unwanted outcomes
   - `error` for failed operations or problems
2. Include a clear, concise header that summarizes the message
3. Keep alert content brief and actionable
4. Provide an action button for alerts that require user response
5. Make alerts dismissible for non-critical information
6. Position alerts contextually near the related content
7. Use multiple alerts sparingly to avoid overwhelming users
8. Consider using Flashbar for application-level messages
9. Animate appearance/disappearance for better user experience
10. Use alerts to provide immediate feedback on user actions
