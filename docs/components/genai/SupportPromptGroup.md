# Support Prompt Group

The SupportPromptGroup component provides a user-friendly interface for suggesting predefined prompts or questions to help users interact with AI assistants. It offers a collection of clickable prompts that can be used to quickly populate the input field with common or suggested queries.

## Import

```jsx
import { SupportPromptGroup } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { SupportPromptGroup } from '@cloudscape-design/components';

function BasicSupportPromptGroup() {
  return (
    <SupportPromptGroup
      header="Suggested prompts"
      items={[
        { text: "How do I set up an S3 bucket?" },
        { text: "What is Lambda function?" },
        { text: "Explain EC2 instance types" }
      ]}
      onItemClick={(e) => console.log('Selected:', e.detail.text)}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `header` | ReactNode | Text or component to display as the header |
| `items` | Array<{ text: string, iconName?: string, iconUrl?: string, iconAlt?: string, description?: string, disabled?: boolean }> | Array of prompt items to display |
| `onItemClick` | (event: { detail: { text: string } }) => void | Event handler that fires when a prompt item is clicked |
| `maxHeight` | string | Maximum height of the prompt group container |
| `variant` | 'default' \| 'embedded' | Visual variant of the support prompt group |
| `i18nStrings` | object | Internationalization strings |

## Examples

### Support Prompt Group with Icons

```jsx
import { SupportPromptGroup, Container, Header } from '@cloudscape-design/components';

function SupportPromptGroupWithIcons() {
  const handlePromptClick = (e) => {
    console.log('Selected prompt:', e.detail.text);
    // You would typically set this text in your PromptInput component
  };
  
  return (
    <Container header={<Header variant="h2">AI Assistant Help</Header>}>
      <SupportPromptGroup
        header="Things you can ask me"
        items={[
          { 
            text: "How do I set up an S3 bucket?", 
            iconName: "storage",
            description: "Learn about creating and configuring Amazon S3 buckets"
          },
          { 
            text: "What are Lambda functions?", 
            iconName: "code",
            description: "Understand serverless computing with AWS Lambda"
          },
          { 
            text: "Explain EC2 instance types", 
            iconName: "server",
            description: "Compare different Amazon EC2 compute instances"
          },
          { 
            text: "How to set up a VPC?", 
            iconName: "network",
            description: "Create and configure Virtual Private Cloud networks"
          }
        ]}
        onItemClick={handlePromptClick}
      />
    </Container>
  );
}
```

### Support Prompt Group with Categories

```jsx
import { SupportPromptGroup, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function SupportPromptGroupWithCategories() {
  const handlePromptClick = (e) => {
    console.log('Selected prompt:', e.detail.text);
  };
  
  return (
    <Container header={<Header variant="h2">Explore AWS Services</Header>}>
      <SpaceBetween size="l">
        <SupportPromptGroup
          header="Compute Services"
          items={[
            { text: "Tell me about EC2" },
            { text: "How does AWS Lambda work?" },
            { text: "What is Amazon ECS?" },
            { text: "Compare EC2 vs. Fargate" }
          ]}
          onItemClick={handlePromptClick}
        />
        
        <SupportPromptGroup
          header="Storage Services"
          items={[
            { text: "Explain S3 storage classes" },
            { text: "What is EBS used for?" },
            { text: "Tell me about Amazon EFS" },
            { text: "How does S3 Glacier work?" }
          ]}
          onItemClick={handlePromptClick}
        />
        
        <SupportPromptGroup
          header="Database Services"
          items={[
            { text: "What is Amazon RDS?" },
            { text: "Explain DynamoDB" },
            { text: "How does Aurora compare to RDS?" },
            { text: "Tell me about Amazon Redshift" }
          ]}
          onItemClick={handlePromptClick}
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Embedded Support Prompt Group

```jsx
import { SupportPromptGroup, PromptInput, Container, Header, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function EmbeddedSupportPromptGroup() {
  const [inputValue, setInputValue] = useState('');
  
  const handlePromptClick = (e) => {
    setInputValue(e.detail.text);
  };
  
  return (
    <Container header={<Header variant="h2">AI Chat Assistant</Header>}>
      <SpaceBetween size="l">
        <div style={{ height: "300px", backgroundColor: "#f2f3f3", padding: "16px" }}>
          {/* Chat messages would appear here */}
          <div style={{ textAlign: "center", padding: "32px" }}>
            Start a conversation with the AI assistant
          </div>
        </div>
        
        <PromptInput
          value={inputValue}
          onChange={({ detail }) => setInputValue(detail.value)}
          onSubmit={() => console.log('Submitted:', inputValue)}
          expandable={true}
          stickyBottom={true}
        />
        
        <SupportPromptGroup
          variant="embedded"
          header="Try asking"
          items={[
            { text: "What AWS services should I use for a serverless application?" },
            { text: "How can I optimize my AWS costs?" },
            { text: "Explain the AWS Well-Architected Framework" },
            { text: "What are best practices for AWS security?" }
          ]}
          onItemClick={handlePromptClick}
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Support Prompt Group with Max Height

```jsx
import { SupportPromptGroup, Container, Header } from '@cloudscape-design/components';

function SupportPromptGroupWithMaxHeight() {
  // Generate a lot of items to demonstrate scrolling
  const generateItems = () => {
    const items = [];
    for (let i = 1; i <= 20; i++) {
      items.push({ 
        text: `Sample prompt question ${i}`,
        description: `This is a description for prompt ${i}`
      });
    }
    return items;
  };
  
  return (
    <Container header={<Header variant="h2">Support Prompts with Scrolling</Header>}>
      <SupportPromptGroup
        header="Frequently asked questions"
        items={generateItems()}
        maxHeight="300px"
        onItemClick={(e) => console.log('Selected:', e.detail.text)}
      />
    </Container>
  );
}
```

### Disabled Support Prompt Items

```jsx
import { SupportPromptGroup, Container, Header } from '@cloudscape-design/components';

function SupportPromptGroupWithDisabledItems() {
  return (
    <Container header={<Header variant="h2">Available Features</Header>}>
      <SupportPromptGroup
        header="What would you like to do?"
        items={[
          { text: "Create a new bucket", iconName: "add-plus" },
          { text: "Upload files", iconName: "upload" },
          { 
            text: "Configure replication (Premium tier only)", 
            iconName: "settings", 
            disabled: true,
            description: "Upgrade your account to access this feature"
          },
          { 
            text: "Set up cross-region backup (Premium tier only)", 
            iconName: "copy", 
            disabled: true,
            description: "Upgrade your account to access this feature"
          }
        ]}
        onItemClick={(e) => console.log('Selected:', e.detail.text)}
      />
    </Container>
  );
}
```

### Support Prompt Group with Custom Icons

```jsx
import { SupportPromptGroup, Container, Header } from '@cloudscape-design/components';

function SupportPromptGroupWithCustomIcons() {
  return (
    <Container header={<Header variant="h2">Learn About AWS Services</Header>}>
      <SupportPromptGroup
        header="Popular services"
        items={[
          { 
            text: "Amazon S3", 
            iconUrl: "https://example.com/s3-icon.png",
            iconAlt: "S3 logo"
          },
          { 
            text: "Amazon EC2", 
            iconUrl: "https://example.com/ec2-icon.png",
            iconAlt: "EC2 logo"
          },
          { 
            text: "AWS Lambda", 
            iconUrl: "https://example.com/lambda-icon.png",
            iconAlt: "Lambda logo"
          },
          { 
            text: "Amazon RDS", 
            iconUrl: "https://example.com/rds-icon.png",
            iconAlt: "RDS logo"
          }
        ]}
        onItemClick={(e) => console.log('Selected:', e.detail.text)}
      />
    </Container>
  );
}
```

### Complete Chat Interface with Support Prompt Group

```jsx
import { 
  SupportPromptGroup, 
  PromptInput, 
  ChatBubble, 
  Avatar, 
  Container, 
  Header, 
  SpaceBetween,
  Box 
} from '@cloudscape-design/components';
import { useState, useRef, useEffect } from 'react';

function ChatInterfaceWithSupportPromptGroup() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'ai',
      content: 'Hello! I\'m an AI assistant specializing in AWS services. How can I help you today?',
      timestamp: new Date()
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const chatEndRef = useRef(null);
  
  // Auto-scroll to bottom when messages change
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);
  
  const handleSendMessage = () => {
    if (!inputValue.trim()) return;
    
    // Add user message
    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: inputValue,
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    
    // Simulate AI response after a delay
    setTimeout(() => {
      const aiResponse = {
        id: Date.now(),
        type: 'ai',
        content: generateResponse(inputValue),
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, aiResponse]);
      setIsLoading(false);
    }, 1500);
  };
  
  const handlePromptClick = (e) => {
    setInputValue(e.detail.text);
  };
  
  // Simple response generator based on input
  const generateResponse = (input) => {
    const lowerInput = input.toLowerCase();
    
    if (lowerInput.includes('s3') || lowerInput.includes('bucket')) {
      return 'Amazon S3 (Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance. You can set up an S3 bucket by going to the S3 console and clicking "Create bucket". You\'ll need to provide a globally unique bucket name and configure options like region, access settings, and encryption.';
    } else if (lowerInput.includes('lambda')) {
      return 'AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. You can use Lambda to run code for virtually any type of application or backend service - all with zero administration.';
    } else if (lowerInput.includes('ec2') || lowerInput.includes('instance')) {
      return 'Amazon EC2 (Elastic Compute Cloud) provides resizable compute capacity in the cloud. EC2 offers various instance types optimized for different use cases, including general purpose, compute optimized, memory optimized, storage optimized, and accelerated computing instances. Each instance type includes different families with different CPU, memory, storage, and networking capacities.';
    } else if (lowerInput.includes('vpc')) {
      return 'Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.';
    } else {
      return 'That\'s an interesting question about AWS. Could you provide more details about what specific service or feature you\'re interested in learning about?';
    }
  };
  
  const formatTime = (date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };
  
  return (
    <Container header={<Header variant="h2">AWS Assistant</Header>}>
      <SpaceBetween size="l">
        <Box padding="m" style={{ height: '400px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {messages.map(message => (
            <ChatBubble
              key={message.id}
              type={message.type}
              content={message.content}
              header={
                <SpaceBetween direction="horizontal" size="xs">
                  <Avatar
                    name={message.type === 'user' ? 'You' : 'AWS Assistant'}
                    variant={message.type === 'user' ? 'user' : 'default'}
                    size="medium"
                  />
                  <span>{message.type === 'user' ? 'You' : 'AWS Assistant'}</span>
                </SpaceBetween>
              }
              footer={
                <Box fontSize="body-s" color="text-body-secondary">
                  {formatTime(message.timestamp)}
                </Box>
              }
            />
          ))}
          
          {isLoading && (
            <ChatBubble
              type="ai"
              content="Thinking..."
              header={
                <SpaceBetween direction="horizontal" size="xs">
                  <Avatar
                    name="AWS Assistant"
                    variant="default"
                    size="medium"
                  />
                  <span>AWS Assistant</span>
                </SpaceBetween>
              }
            />
          )}
          
          <div ref={chatEndRef} />
        </Box>
        
        <PromptInput
          value={inputValue}
          onChange={({ detail }) => setInputValue(detail.value)}
          onSubmit={handleSendMessage}
          expandable={true}
          submitting={isLoading}
          stickyBottom={true}
          i18nStrings={{
            submitAriaLabel: 'Send message',
            expandAriaLabel: 'Expand message',
            inputPlaceholder: 'Ask about AWS services...',
            submitButtonText: 'Send'
          }}
        />
        
        <SupportPromptGroup
          variant="embedded"
          header="Try asking about"
          items={[
            { 
              text: "How do I set up an S3 bucket?", 
              iconName: "storage"
            },
            { 
              text: "What are Lambda functions?", 
              iconName: "code"
            },
            { 
              text: "Explain EC2 instance types", 
              iconName: "server"
            },
            { 
              text: "How to set up a VPC?", 
              iconName: "network"
            }
          ]}
          onItemClick={handlePromptClick}
        />
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Other Components

The SupportPromptGroup component works well with these related components:

1. **PromptInput** - For integrating suggested prompts with user input
2. **ChatBubble** - For displaying AI responses to selected prompts
3. **Container** - For proper framing of the support prompt interface
4. **SpaceBetween** - For consistent spacing between prompt categories
5. **Box** - For custom styling and layout

## Accessibility

- Uses semantic HTML to ensure proper screen reader interpretation
- Provides appropriate ARIA attributes for interactive elements
- Ensures keyboard navigation support for all prompt items
- Maintains focus management when selecting prompts
- Uses proper color contrast for text readability
- Supports high contrast modes for better visibility

## Best Practices

1. Group related prompts together under clear category headers
2. Use concise, action-oriented text for prompt items
3. Add icons to provide visual cues about prompt categories or actions
4. Include brief descriptions to clarify what each prompt does
5. Limit the number of prompts to avoid overwhelming users
6. Use the embedded variant when integrating with chat interfaces
7. Set a reasonable maxHeight when displaying many prompts to keep the interface compact
8. Disable prompts that are not currently available and explain why
9. Use consistent styling for all support prompt groups in your application
10. Consider the user's context when suggesting prompts
11. Update prompt suggestions based on user interactions or conversation history
12. Test with screen readers to ensure accessibility compliance
13. Ensure prompt text is translated properly for international users
14. Consider different device sizes when designing prompt layouts
15. Use analytics to refine and improve prompt suggestions over time
