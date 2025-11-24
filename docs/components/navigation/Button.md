# Button

The Button component allows users to initiate actions in the user interface.

## Import

```jsx
import { Button } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
<Button>Click me</Button>
```

## Variants

```jsx
// Primary button (high emphasis)
<Button variant="primary">Primary action</Button>

// Normal button (medium emphasis)
<Button variant="normal">Secondary action</Button>

// Link button (low emphasis)
<Button variant="link">Tertiary action</Button>

// Icon button
<Button iconName="settings">Settings</Button>

// Icon-only button
<Button iconName="settings" iconAlign="icon-only" ariaLabel="Settings" />
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `children` | ReactNode | Label shown on the button |
| `variant` | 'normal' \| 'primary' \| 'link' \| 'icon' \| 'inline-icon' | Visual style of the button |
| `disabled` | boolean | Determines whether the button is disabled |
| `loading` | boolean | Renders the button in a loading state |
| `loadingText` | string | Text that replaces the button's content when in the loading state |
| `iconName` | string | Name of the icon to display |
| `iconAlign` | 'left' \| 'right' \| 'icon-only' | Determines the icon alignment |
| `formAction` | 'none' \| 'submit' \| 'reset' | Button's form action when used inside a form |
| `href` | string | URL that the link button points to |
| `target` | string | Specifies where to open the linked URL |
| `onClick` | (event: CustomEvent) => void | Called when the user clicks the button |

## Examples

### Button with Loading State

```jsx
import { Button } from '@cloudscape-design/components';
import { useState } from 'react';

function LoadingButtonExample() {
  const [loading, setLoading] = useState(false);
  
  const handleClick = () => {
    setLoading(true);
    // Simulate API call
    setTimeout(() => setLoading(false), 2000);
  };
  
  return (
    <Button 
      variant="primary"
      loading={loading}
      loadingText="Processing..."
      onClick={handleClick}
    >
      Save changes
    </Button>
  );
}
```

### Button with Icon

```jsx
import { Button } from '@cloudscape-design/components';

function IconButtonExample() {
  return (
    <>
      {/* Icon on the left (default) */}
      <Button iconName="add-plus">Add item</Button>
      
      {/* Icon on the right */}
      <Button iconName="external" iconAlign="right">
        View documentation
      </Button>
      
      {/* Icon-only button */}
      <Button 
        iconName="refresh"
        iconAlign="icon-only"
        ariaLabel="Refresh content"
        onClick={() => console.log('Refreshing...')}
      />
    </>
  );
}
```

### Button Group Example

```jsx
import { Button, SpaceBetween } from '@cloudscape-design/components';

function ButtonGroupExample() {
  return (
    <SpaceBetween direction="horizontal" size="xs">
      <Button variant="link">Cancel</Button>
      <Button variant="normal">Reset</Button>
      <Button variant="primary">Submit</Button>
    </SpaceBetween>
  );
}
```

## Accessibility

- Ensure icon-only buttons have an `ariaLabel` property for screen readers
- Focus order follows visual layout
- When using link buttons with `href`, proper ARIA roles are automatically applied
- Tab navigation is supported out of the box

## Best Practices

1. Use `primary` variant for the main action in a section
2. Limit the use of primary buttons to one per visual section
3. Use `normal` variant for secondary actions
4. Use `link` variant for tertiary actions
5. Group related buttons together using SpaceBetween component
6. Maintain consistent button sizes in your application
7. Use loading state for actions that take time to complete
8. Keep button labels concise and action-oriented (e.g., "Save" instead of "Save the form")
