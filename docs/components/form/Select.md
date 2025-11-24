# Select

The Select component enables users to choose a single item from a dropdown list of options.

## Import

```jsx
import { Select } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Select } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicSelect() {
  const [selectedOption, setSelectedOption] = useState(null);
  
  return (
    <Select
      selectedOption={selectedOption}
      onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
      options={[
        { label: 'Option 1', value: '1' },
        { label: 'Option 2', value: '2' },
        { label: 'Option 3', value: '3' }
      ]}
      placeholder="Choose an option"
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `options` | Array<{label, value, ...}> | Array of options to choose from |
| `selectedOption` | { label, value, ... } | Currently selected option |
| `onChange` | ({ detail }) => void | Called when selection changes |
| `placeholder` | string | Text displayed when no option is selected |
| `disabled` | boolean | Whether the control is disabled |
| `invalid` | boolean | Indicates that the field has an error |
| `triggerVariant` | 'normal' \| 'option' | Visual style of the trigger |
| `expandToViewport` | boolean | Whether the dropdown expands to the viewport |
| `filteringType` | 'auto' \| 'manual' | Whether filtering is automatic or manual |
| `filteringPlaceholder` | string | Placeholder for the filtering input |
| `filteringAriaLabel` | string | ARIA label for the filtering input |
| `statusType` | 'pending' \| 'loading' \| 'error' \| 'success' | Status of the select |
| `loadingText` | string | Text to display when loading options |
| `errorText` | string | Text to display when loading options failed |
| `recoveryText` | string | Text for the recovery button when loading failed |
| `finishedText` | string | Text to display when loading is finished |

## Examples

### Select with Option Groups

```jsx
import { Select, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function SelectWithGroups() {
  const [selectedOption, setSelectedOption] = useState(null);
  
  return (
    <FormField label="Select a fruit">
      <Select
        selectedOption={selectedOption}
        onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
        options={[
          {
            label: 'Citrus',
            options: [
              { label: 'Orange', value: 'orange' },
              { label: 'Lemon', value: 'lemon' },
              { label: 'Lime', value: 'lime' }
            ]
          },
          {
            label: 'Berries',
            options: [
              { label: 'Strawberry', value: 'strawberry' },
              { label: 'Blueberry', value: 'blueberry' },
              { label: 'Raspberry', value: 'raspberry' }
            ]
          },
          {
            label: 'Other',
            options: [
              { label: 'Apple', value: 'apple' },
              { label: 'Banana', value: 'banana' },
              { label: 'Pear', value: 'pear' }
            ]
          }
        ]}
        placeholder="Choose a fruit"
      />
    </FormField>
  );
}
```

### Select with Filtering

```jsx
import { Select, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function FilterableSelect() {
  const [selectedOption, setSelectedOption] = useState(null);
  
  const options = [
    { label: 'Alabama', value: 'AL' },
    { label: 'Alaska', value: 'AK' },
    { label: 'Arizona', value: 'AZ' },
    { label: 'Arkansas', value: 'AR' },
    { label: 'California', value: 'CA' },
    { label: 'Colorado', value: 'CO' },
    { label: 'Connecticut', value: 'CT' },
    // ... more states
    { label: 'Wisconsin', value: 'WI' },
    { label: 'Wyoming', value: 'WY' }
  ];
  
  return (
    <FormField label="Select a state">
      <Select
        selectedOption={selectedOption}
        onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
        options={options}
        placeholder="Choose a state"
        filteringType="auto"
        filteringPlaceholder="Find a state"
        filteringAriaLabel="Filter states"
      />
    </FormField>
  );
}
```

### Select with Custom Filtering

```jsx
import { Select, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function CustomFilteringSelect() {
  const [selectedOption, setSelectedOption] = useState(null);
  const [filteringText, setFilteringText] = useState('');
  
  const allOptions = [
    { label: 'Alabama', value: 'AL' },
    { label: 'Alaska', value: 'AK' },
    { label: 'Arizona', value: 'AZ' },
    // ... more states
  ];
  
  // Custom filtering logic
  const filteredOptions = allOptions.filter(option => 
    option.label.toLowerCase().includes(filteringText.toLowerCase()) ||
    option.value.toLowerCase().includes(filteringText.toLowerCase())
  );
  
  return (
    <FormField label="Select a state">
      <Select
        selectedOption={selectedOption}
        onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
        options={filteredOptions}
        placeholder="Choose a state"
        filteringType="manual"
        filteringPlaceholder="Find a state"
        filteringAriaLabel="Filter states"
        filteringText={filteringText}
        onFilteringChange={({ detail }) => setFilteringText(detail.filteringText)}
      />
    </FormField>
  );
}
```

### Select with Async Loading

```jsx
import { Select, FormField } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function AsyncSelect() {
  const [selectedOption, setSelectedOption] = useState(null);
  const [options, setOptions] = useState([]);
  const [status, setStatus] = useState('loading');
  
  useEffect(() => {
    // Simulate API call
    const fetchOptions = async () => {
      setStatus('loading');
      
      try {
        // In a real app, this would be an API call
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        setOptions([
          { label: 'Option 1', value: '1' },
          { label: 'Option 2', value: '2' },
          { label: 'Option 3', value: '3' },
          { label: 'Option 4', value: '4' },
          { label: 'Option 5', value: '5' }
        ]);
        
        setStatus('finished');
      } catch (error) {
        setStatus('error');
      }
    };
    
    fetchOptions();
  }, []);
  
  const handleRecoveryClick = () => {
    // Retry loading options
    setOptions([]);
    setStatus('loading');
    
    // Simulate API call again
    setTimeout(() => {
      setOptions([
        { label: 'Option 1', value: '1' },
        { label: 'Option 2', value: '2' },
        { label: 'Option 3', value: '3' }
      ]);
      setStatus('finished');
    }, 1500);
  };
  
  return (
    <FormField label="Select an option">
      <Select
        selectedOption={selectedOption}
        onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
        options={options}
        placeholder="Choose an option"
        statusType={status}
        loadingText="Loading options..."
        errorText="Error loading options."
        recoveryText="Retry"
        finishedText="Options loaded."
        onRecoveryClick={handleRecoveryClick}
      />
    </FormField>
  );
}
```

### Select with Validation

```jsx
import { Select, FormField, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function ValidatedSelect() {
  const [selectedOption, setSelectedOption] = useState(null);
  const [error, setError] = useState('');
  
  const handleSubmit = () => {
    if (!selectedOption) {
      setError('Please select an option');
      return;
    }
    
    // Clear error and submit form
    setError('');
    console.log('Selected option:', selectedOption);
  };
  
  return (
    <SpaceBetween size="m">
      <FormField
        label="Select an option"
        errorText={error}
      >
        <Select
          selectedOption={selectedOption}
          onChange={({ detail }) => {
            setSelectedOption(detail.selectedOption);
            // Clear error when user makes a selection
            if (error) setError('');
          }}
          options={[
            { label: 'Option 1', value: '1' },
            { label: 'Option 2', value: '2' },
            { label: 'Option 3', value: '3' }
          ]}
          placeholder="Choose an option"
          invalid={Boolean(error)}
        />
      </FormField>
      
      <Button onClick={handleSubmit}>Submit</Button>
    </SpaceBetween>
  );
}
```

### Select with Description and Tags

```jsx
import { Select, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function SelectWithDescriptions() {
  const [selectedOption, setSelectedOption] = useState(null);
  
  return (
    <FormField label="Select an instance type">
      <Select
        selectedOption={selectedOption}
        onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
        options={[
          {
            label: 't2.micro',
            value: 't2.micro',
            description: '1 vCPU, 1 GiB RAM',
            tags: [{ label: 'Free Tier Eligible', color: 'green' }]
          },
          {
            label: 't2.small',
            value: 't2.small',
            description: '1 vCPU, 2 GiB RAM'
          },
          {
            label: 't2.medium',
            value: 't2.medium',
            description: '2 vCPU, 4 GiB RAM'
          },
          {
            label: 't2.large',
            value: 't2.large',
            description: '2 vCPU, 8 GiB RAM'
          }
        ]}
        placeholder="Choose an instance type"
        selectedAriaLabel="Selected"
      />
    </FormField>
  );
}
```

## Accessibility

- Implements WAI-ARIA combobox pattern
- Keyboard navigation for selecting options
- ARIA labels for assistive technologies
- Focus management within the dropdown
- Visual indication for selected and focused options

## Best Practices

1. Always provide meaningful labels through the FormField component
2. Include a clear placeholder when no option is selected
3. Group related options using the option group structure
4. Enable filtering for dropdowns with many options
5. Display descriptive text for complex options
6. Implement validation to ensure a selection is made when required
7. Use expandToViewport for select components in modals or containers with overflow constraints
8. Provide appropriate loading and error states for asynchronously loaded options
9. Use the triggerVariant property to match the visual style with your design
10. Ensure enough space for the dropdown to expand without cutting off options
