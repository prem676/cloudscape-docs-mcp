# Input

The Input component allows users to input a single line of text. It's one of the most fundamental form elements in the CloudScape Design System.

## Import

```jsx
import { Input } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Input } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicInput() {
  const [value, setValue] = useState('');
  
  return (
    <Input
      value={value}
      onChange={({ detail }) => setValue(detail.value)}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `value` | string | Current input value |
| `onChange` | ({ detail }) => void | Called when the input value changes |
| `type` | 'text' \| 'password' \| 'search' \| 'number' \| 'email' \| 'url' \| 'tel' | Type of input |
| `placeholder` | string | Text displayed when the input is empty |
| `disabled` | boolean | Determines whether the input is disabled |
| `readOnly` | boolean | Makes the input read-only |
| `autoFocus` | boolean | Automatically focuses the input when mounted |
| `ariaLabel` | string | ARIA label for the input |
| `ariaRequired` | boolean | Indicates that the input is required |
| `ariaDescribedby` | string | ID of an element that describes the input |
| `invalid` | boolean | Indicates that the input has an error |
| `disableBrowserAutocorrect` | boolean | Disables browser autocorrect features |
| `spellcheck` | boolean | Enables or disables spell checking |
| `step` | string \| number | Step value for number inputs |
| `inputMode` | string | Hint for virtual keyboards on touch devices |
| `name` | string | Name of the input element |
| `clearAriaLabel` | string | ARIA label for the clear button |
| `onBlur` | () => void | Called when the input loses focus |
| `onFocus` | () => void | Called when the input gains focus |
| `onKeyDown` | (event: KeyboardEvent) => void | Called when a key is pressed while the input has focus |
| `onKeyUp` | (event: KeyboardEvent) => void | Called when a key is released while the input has focus |

## Examples

### Input with Placeholder

```jsx
import { Input } from '@cloudscape-design/components';
import { useState } from 'react';

function InputWithPlaceholder() {
  const [value, setValue] = useState('');
  
  return (
    <Input
      placeholder="Enter your name"
      value={value}
      onChange={({ detail }) => setValue(detail.value)}
    />
  );
}
```

### Input Types

```jsx
import { Input, SpaceBetween, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function InputTypes() {
  const [text, setText] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [number, setNumber] = useState('');
  const [search, setSearch] = useState('');
  
  return (
    <SpaceBetween size="m">
      <FormField label="Text input">
        <Input
          type="text"
          value={text}
          onChange={({ detail }) => setText(detail.value)}
        />
      </FormField>
      
      <FormField label="Password input">
        <Input
          type="password"
          value={password}
          onChange={({ detail }) => setPassword(detail.value)}
        />
      </FormField>
      
      <FormField label="Email input">
        <Input
          type="email"
          value={email}
          onChange={({ detail }) => setEmail(detail.value)}
        />
      </FormField>
      
      <FormField label="Number input">
        <Input
          type="number"
          value={number}
          onChange={({ detail }) => setNumber(detail.value)}
          step={1}
        />
      </FormField>
      
      <FormField label="Search input">
        <Input
          type="search"
          value={search}
          onChange={({ detail }) => setSearch(detail.value)}
        />
      </FormField>
    </SpaceBetween>
  );
}
```

### Input with Validation

```jsx
import { Input, FormField, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function InputWithValidation() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  
  const validateEmail = () => {
    if (!email) {
      setError('Email is required');
      return false;
    }
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Please enter a valid email address');
      return false;
    }
    
    setError('');
    return true;
  };
  
  const handleSubmit = () => {
    if (validateEmail()) {
      console.log('Email submitted:', email);
    }
  };
  
  return (
    <SpaceBetween size="m">
      <FormField
        label="Email address"
        errorText={error}
        constraintText="Must be a valid email address"
      >
        <Input
          type="email"
          value={email}
          onChange={({ detail }) => {
            setEmail(detail.value);
            // Clear error when user starts typing again
            if (error) setError('');
          }}
          onBlur={validateEmail}
          invalid={Boolean(error)}
        />
      </FormField>
      
      <Button onClick={handleSubmit}>Submit</Button>
    </SpaceBetween>
  );
}
```

### Input with Icon

```jsx
import { Input, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function InputWithIcon() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  
  return (
    <SpaceBetween size="m">
      <FormField label="Username">
        <Input
          value={username}
          onChange={({ detail }) => setUsername(detail.value)}
          placeholder="Enter username"
          // User icon on the left
          iconName="user-profile"
        />
      </FormField>
      
      <FormField label="Password">
        <Input
          type="password"
          value={password}
          onChange={({ detail }) => setPassword(detail.value)}
          placeholder="Enter password"
          // Lock icon on the left
          iconName="lock-private"
        />
      </FormField>
    </SpaceBetween>
  );
}
```

### Controllable Input

```jsx
import { Input, FormField, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function ControllableInput() {
  const [value, setValue] = useState('');
  
  // Force value to uppercase
  const handleChange = ({ detail }) => {
    setValue(detail.value.toUpperCase());
  };
  
  // Clear input value
  const handleClear = () => {
    setValue('');
  };
  
  // Set a predefined value
  const handleSetValue = () => {
    setValue('PREDEFINED VALUE');
  };
  
  return (
    <SpaceBetween size="m">
      <FormField
        label="Enter text (will be converted to uppercase)"
        description="This demonstrates how to control the input value"
      >
        <Input
          value={value}
          onChange={handleChange}
        />
      </FormField>
      
      <SpaceBetween direction="horizontal" size="xs">
        <Button onClick={handleClear}>Clear</Button>
        <Button onClick={handleSetValue}>Set value</Button>
      </SpaceBetween>
    </SpaceBetween>
  );
}
```

### Input with Autocomplete

```jsx
import { Input, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function InputWithAutocomplete() {
  const [value, setValue] = useState('');
  
  return (
    <FormField label="Country">
      <Input
        value={value}
        onChange={({ detail }) => setValue(detail.value)}
        placeholder="Start typing a country name"
        // Enable browser's autocomplete feature
        autoComplete="country-name"
        // Do not disable browser autocorrect
        disableBrowserAutocorrect={false}
        // Enable spell checking
        spellcheck={true}
      />
    </FormField>
  );
}
```

## Accessibility

- Supports standard HTML input attributes
- Proper ARIA attributes for screen readers
- Keyboard navigation support
- Visual indication for focus state
- Error states are properly communicated

## Best Practices

1. Always use a FormField component to wrap the Input with a proper label
2. Use the appropriate input type for the data being collected
3. Provide clear placeholder text when needed
4. Implement client-side validation with helpful error messages
5. Use constraintText in FormField to provide input requirements
6. Handle both onChange and onBlur events for proper validation
7. Consider providing feedback on input format (e.g., with icons or inline text)
8. Use the disabled state for fields that are not applicable
9. Use the readOnly state for display-only information
10. Set appropriate autoComplete attributes to help users fill forms faster
11. Validate input on submission to provide comprehensive feedback
12. Keep inputs as simple as possible - use specialized components for complex inputs
