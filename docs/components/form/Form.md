# Form

The Form component is a section of a page with interactive controls that allows users to submit information.

## Import

```jsx
import { Form } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Form, Button, SpaceBetween } from '@cloudscape-design/components';

function BasicForm() {
  return (
    <Form
      header={<h2>User Information</h2>}
      actions={
        <SpaceBetween direction="horizontal" size="xs">
          <Button formAction="none" variant="link">Cancel</Button>
          <Button variant="primary">Submit</Button>
        </SpaceBetween>
      }
    >
      {/* Form content goes here */}
    </Form>
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `children` | ReactNode | Content of the form |
| `header` | ReactNode | Title displayed at the top of the form |
| `actions` | ReactNode | Container for action buttons (typically at the bottom) |
| `secondaryActions` | ReactNode | Container for secondary action buttons |
| `variant` | 'full-page' \| 'embedded' \| 'modal' | Determines the form's padding and margin |
| `errorText` | string | Text displayed as an error message |
| `errorIconAriaLabel` | string | ARIA label for the error icon |
| `loading` | boolean | Determines whether form is in loading state |
| `loadingText` | string | Text to display when form is loading |
| `onSubmit` | (event: CustomEvent<FormDetail>) => void | Called when the form is submitted |

## Examples

### Complete Form with Fields

```jsx
import {
  Form,
  Container,
  Header,
  SpaceBetween,
  Button,
  FormField,
  Input,
  Select,
  Checkbox
} from '@cloudscape-design/components';
import { useState } from 'react';

function CompleteForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    role: { label: 'User', value: 'user' },
    agreeToTerms: false
  });
  const [error, setError] = useState('');
  
  const handleSubmit = event => {
    event.preventDefault();
    
    // Validate form data
    if (!formData.name) {
      setError('Name is required');
      return;
    }
    
    if (!formData.email) {
      setError('Email is required');
      return;
    }
    
    if (!formData.agreeToTerms) {
      setError('You must agree to the terms and conditions');
      return;
    }
    
    // Clear error and submit form data
    setError('');
    console.log('Form submitted with:', formData);
    
    // In a real application, you would submit the data to a server here
  };
  
  return (
    <Form
      header={<Header variant="h1">User Registration</Header>}
      actions={
        <SpaceBetween direction="horizontal" size="xs">
          <Button formAction="none" variant="link">
            Cancel
          </Button>
          <Button variant="primary" onClick={handleSubmit}>
            Create user
          </Button>
        </SpaceBetween>
      }
      errorText={error}
    >
      <Container>
        <SpaceBetween direction="vertical" size="l">
          <FormField
            label="Name"
            description="Enter your full name"
            constraintText="Required"
          >
            <Input
              value={formData.name}
              onChange={({ detail }) => 
                setFormData(prev => ({ ...prev, name: detail.value }))}
            />
          </FormField>
          
          <FormField
            label="Email"
            description="Enter your email address"
            constraintText="Required"
          >
            <Input
              type="email"
              value={formData.email}
              onChange={({ detail }) => 
                setFormData(prev => ({ ...prev, email: detail.value }))}
            />
          </FormField>
          
          <FormField
            label="Role"
            description="Select your role"
          >
            <Select
              options={[
                { label: 'User', value: 'user' },
                { label: 'Admin', value: 'admin' },
                { label: 'Guest', value: 'guest' }
              ]}
              selectedOption={formData.role}
              onChange={({ detail }) => 
                setFormData(prev => ({ ...prev, role: detail.selectedOption }))}
            />
          </FormField>
          
          <FormField>
            <Checkbox
              checked={formData.agreeToTerms}
              onChange={({ detail }) => 
                setFormData(prev => ({ ...prev, agreeToTerms: detail.checked }))}
            >
              I agree to the terms and conditions
            </Checkbox>
          </FormField>
        </SpaceBetween>
      </Container>
    </Form>
  );
}
```

### Form with Validation

```jsx
import {
  Form,
  Container,
  SpaceBetween,
  Button,
  FormField,
  Input
} from '@cloudscape-design/components';
import { useState } from 'react';

function ValidationForm() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    confirmPassword: ''
  });
  
  const [errors, setErrors] = useState({
    username: '',
    password: '',
    confirmPassword: '',
    form: ''
  });
  
  const validate = () => {
    const newErrors = {
      username: '',
      password: '',
      confirmPassword: '',
      form: ''
    };
    
    // Username validation
    if (!formData.username) {
      newErrors.username = 'Username is required';
    } else if (formData.username.length < 3) {
      newErrors.username = 'Username must be at least 3 characters';
    }
    
    // Password validation
    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }
    
    // Confirm password validation
    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }
    
    setErrors(newErrors);
    
    // Check if there are any errors
    return !Object.values(newErrors).some(error => error);
  };
  
  const handleSubmit = event => {
    event.preventDefault();
    
    if (validate()) {
      console.log('Form is valid, submitting:', formData);
      // In a real application, you would submit the data to a server here
    } else {
      setErrors(prev => ({
        ...prev,
        form: 'Please fix the errors above before submitting'
      }));
    }
  };
  
  return (
    <Form
      header={<h2>Create Account</h2>}
      actions={
        <Button variant="primary" onClick={handleSubmit}>
          Create account
        </Button>
      }
      errorText={errors.form}
    >
      <Container>
        <SpaceBetween direction="vertical" size="l">
          <FormField
            label="Username"
            errorText={errors.username}
          >
            <Input
              value={formData.username}
              onChange={({ detail }) => {
                setFormData(prev => ({ ...prev, username: detail.value }));
                // Clear error when user starts typing
                if (errors.username) {
                  setErrors(prev => ({ ...prev, username: '', form: '' }));
                }
              }}
            />
          </FormField>
          
          <FormField
            label="Password"
            errorText={errors.password}
          >
            <Input
              type="password"
              value={formData.password}
              onChange={({ detail }) => {
                setFormData(prev => ({ ...prev, password: detail.value }));
                if (errors.password) {
                  setErrors(prev => ({ ...prev, password: '', form: '' }));
                }
              }}
            />
          </FormField>
          
          <FormField
            label="Confirm password"
            errorText={errors.confirmPassword}
          >
            <Input
              type="password"
              value={formData.confirmPassword}
              onChange={({ detail }) => {
                setFormData(prev => ({ ...prev, confirmPassword: detail.value }));
                if (errors.confirmPassword) {
                  setErrors(prev => ({ ...prev, confirmPassword: '', form: '' }));
                }
              }}
            />
          </FormField>
        </SpaceBetween>
      </Container>
    </Form>
  );
}
```

### Form with Loading State

```jsx
import {
  Form,
  Container,
  SpaceBetween,
  Button,
  FormField,
  Input
} from '@cloudscape-design/components';
import { useState } from 'react';

function LoadingForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: ''
  });
  
  const [loading, setLoading] = useState(false);
  
  const handleSubmit = event => {
    event.preventDefault();
    
    setLoading(true);
    
    // Simulate API call
    setTimeout(() => {
      console.log('Form submitted with:', formData);
      setLoading(false);
    }, 2000);
  };
  
  return (
    <Form
      header={<h2>Contact Form</h2>}
      actions={
        <Button 
          variant="primary" 
          onClick={handleSubmit}
          disabled={loading}
        >
          Submit
        </Button>
      }
      loading={loading}
      loadingText="Submitting form..."
    >
      <Container>
        <SpaceBetween direction="vertical" size="l">
          <FormField label="Name">
            <Input
              value={formData.name}
              onChange={({ detail }) => 
                setFormData(prev => ({ ...prev, name: detail.value }))}
              disabled={loading}
            />
          </FormField>
          
          <FormField label="Email">
            <Input
              type="email"
              value={formData.email}
              onChange={({ detail }) => 
                setFormData(prev => ({ ...prev, email: detail.value }))}
              disabled={loading}
            />
          </FormField>
        </SpaceBetween>
      </Container>
    </Form>
  );
}
```

## Accessibility

- When using form controls, ensure all FormField components have proper labels
- Provide descriptive error messages
- Use constraintText to indicate required fields
- Ensure logical tab order of form controls
- Use proper HTML5 input types (email, number, etc.)

## Best Practices

1. Group related form fields together using Container or SpaceBetween
2. Provide clear labels and descriptions for all form fields
3. Use constraintText to indicate any input requirements
4. Display validation errors inline with form fields
5. Include a submit button in the actions slot
6. Add a cancel button for forms that modify existing data
7. Disable form controls during the loading state
8. Use client-side validation before submission
9. Provide clear error messages for validation failures
10. Consider using the Form variant that matches your page layout (full-page, embedded, or modal)
