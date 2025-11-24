# Loading Bar

The LoadingBar component provides a visual indication that content is being generated or loaded, designed specifically for generative AI contexts. It features a subtle animation to indicate processing activity without drawing excessive attention.

## Import

```jsx
import { LoadingBar } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { LoadingBar } from '@cloudscape-design/components';

function BasicLoadingBar() {
  return <LoadingBar />;
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `size` | 'small' \| 'medium' \| 'large' | Size of the loading bar |
| `variant` | 'default' \| 'subtle' | Visual variant of the loading bar |
| `label` | ReactNode | Optional text label for the loading bar |
| `additionalInfo` | ReactNode | Optional additional information about the loading process |

## Examples

### Loading Bar Sizes

```jsx
import { LoadingBar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function LoadingBarSizes() {
  return (
    <Container header={<Header variant="h2">Loading Bar Sizes</Header>}>
      <SpaceBetween size="l">
        <div>
          <h3>Small Loading Bar</h3>
          <LoadingBar size="small" />
        </div>
        
        <div>
          <h3>Medium Loading Bar</h3>
          <LoadingBar size="medium" />
        </div>
        
        <div>
          <h3>Large Loading Bar</h3>
          <LoadingBar size="large" />
        </div>
      </SpaceBetween>
    </Container>
  );
}
```

### Loading Bar Variants

```jsx
import { LoadingBar, Container, Header, SpaceBetween, Box } from '@cloudscape-design/components';

function LoadingBarVariants() {
  return (
    <Container header={<Header variant="h2">Loading Bar Variants</Header>}>
      <SpaceBetween size="l">
        <div>
          <h3>Default Variant</h3>
          <LoadingBar variant="default" />
        </div>
        
        <div>
          <h3>Subtle Variant</h3>
          <Box padding="m" bgcolor="background.container">
            <LoadingBar variant="subtle" />
          </Box>
        </div>
      </SpaceBetween>
    </Container>
  );
}
```

### Loading Bar with Label and Additional Info

```jsx
import { LoadingBar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function LoadingBarWithLabel() {
  return (
    <Container header={<Header variant="h2">Loading Bar with Context</Header>}>
      <SpaceBetween size="l">
        <LoadingBar 
          label="Generating response" 
          additionalInfo="This may take a few seconds"
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Loading Bar in Chat Interface

```jsx
import { LoadingBar, ChatBubble, Container, Header, SpaceBetween, Avatar } from '@cloudscape-design/components';

function LoadingBarInChat() {
  return (
    <Container header={<Header variant="h2">AI Chat</Header>}>
      <SpaceBetween size="l">
        <ChatBubble
          type="user"
          content="Can you explain cloud architecture to me?"
          header={
            <SpaceBetween direction="horizontal" size="xs">
              <Avatar
                name="User"
                variant="user"
                size="medium"
              />
              <span>You</span>
            </SpaceBetween>
          }
        />
        
        <ChatBubble
          type="ai"
          content={<LoadingBar size="medium" />}
          header={
            <SpaceBetween direction="horizontal" size="xs">
              <Avatar
                name="AI Assistant"
                variant="default"
                size="medium"
              />
              <span>AI Assistant</span>
            </SpaceBetween>
          }
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Loading Bar with State Management

```jsx
import { LoadingBar, Container, Header, Button, Box } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function LoadingBarWithStateManagement() {
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState('');
  
  useEffect(() => {
    let timer;
    if (isLoading) {
      timer = setTimeout(() => {
        setIsLoading(false);
        setResult('AI response has been generated successfully.');
      }, 3000);
    }
    
    return () => clearTimeout(timer);
  }, [isLoading]);
  
  const handleStartLoading = () => {
    setIsLoading(true);
    setResult('');
  };
  
  return (
    <Container header={<Header variant="h2">AI Generation Process</Header>}>
      <Box padding="m">
        <Button onClick={handleStartLoading} disabled={isLoading}>
          Generate AI Response
        </Button>
        
        <Box padding={{ top: 'l' }}>
          {isLoading ? (
            <LoadingBar 
              label="Generating AI response" 
              additionalInfo="Please wait while we process your request" 
              size="medium"
            />
          ) : (
            result && <Box>{result}</Box>
          )}
        </Box>
      </Box>
    </Container>
  );
}
```

### Loading Bar with Progress Indication

```jsx
import { LoadingBar, Container, Header, Box, SpaceBetween } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function LoadingBarWithProgress() {
  const [isLoading, setIsLoading] = useState(true);
  const [step, setStep] = useState(1);
  const totalSteps = 3;
  
  useEffect(() => {
    if (isLoading) {
      const timer = setTimeout(() => {
        if (step < totalSteps) {
          setStep(step + 1);
        } else {
          setIsLoading(false);
        }
      }, 2000);
      
      return () => clearTimeout(timer);
    }
  }, [isLoading, step]);
  
  const getStepInfo = () => {
    switch (step) {
      case 1:
        return "Analyzing your question...";
      case 2:
        return "Retrieving relevant information...";
      case 3:
        return "Formulating response...";
      default:
        return "";
    }
  };
  
  return (
    <Container header={<Header variant="h2">AI Processing Steps</Header>}>
      <Box padding="m">
        {isLoading ? (
          <SpaceBetween size="s">
            <LoadingBar 
              label={`Step ${step} of ${totalSteps}`} 
              additionalInfo={getStepInfo()} 
            />
          </SpaceBetween>
        ) : (
          <Box>Response generation complete!</Box>
        )}
      </Box>
    </Container>
  );
}
```

### Custom Styled Loading Bar

```jsx
import { LoadingBar, Container, Header, Box } from '@cloudscape-design/components';

function CustomStyledLoadingBar() {
  return (
    <Container header={<Header variant="h2">Custom Styled Loading</Header>}>
      <Box
        padding="l"
        bgcolor="background.paper"
        color="text.primary"
        borderRadius="default"
        textAlign="center"
      >
        <Box 
          fontSize="heading-xl" 
          fontWeight="bold" 
          padding={{ bottom: 'm' }}
        >
          Processing Your Request
        </Box>
        
        <LoadingBar size="large" />
        
        <Box 
          fontSize="body-m" 
          color="text.secondary"
          padding={{ top: 'm' }}
        >
          Our AI system is analyzing your complex query. This may take a few moments.
        </Box>
      </Box>
    </Container>
  );
}
```

## Integration with Other Components

The LoadingBar component works well with these related components:

1. **ChatBubble** - For indicating AI response generation in chat interfaces
2. **PromptInput** - For showing submission and processing states
3. **Container** - For properly framing the loading context
4. **Box** - For custom styling and layout
5. **Avatar** - For identifying the source in chat interfaces

## Accessibility

- Uses ARIA attributes to ensure loading state is communicated to screen readers
- Provides appropriate contrast for visibility
- Includes text alternatives for the loading animation
- Supports both light and dark mode themes
- Maintains focus management during loading processes

## Best Practices

1. Use LoadingBar when generating AI content or loading data in AI contexts
2. Include descriptive labels to explain what is happening during loading
3. Consider adding time estimates or step indicators for longer operations
4. Use consistent sizing across your application
5. Select the appropriate variant based on the background color
6. Position the LoadingBar in a prominent location related to the content being loaded
7. Use the subtle variant when you want a less prominent loading indicator
8. Consider adding animation to make the waiting experience more engaging
9. Keep loading states visually consistent with other components
10. Provide clear feedback when loading completes
11. For extended loading times, consider showing progressive updates
12. Test with screen readers to ensure accessibility compliance
13. Use appropriate size based on the context and importance of the loading operation
14. Avoid using multiple LoadingBar components in close proximity
15. Consider using skeletal loaders for complex content structures
