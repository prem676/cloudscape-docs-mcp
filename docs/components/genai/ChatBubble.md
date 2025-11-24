# Chat Bubble

The ChatBubble component displays individual messages in a conversation interface, designed specifically for AI chat experiences. It supports different message types, rich content, and various visual customizations.

## Import

```jsx
import { ChatBubble } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { ChatBubble } from '@cloudscape-design/components';

function BasicChatBubble() {
  return (
    <>
      <ChatBubble
        type="ai"
        content="Hello! I'm an AI assistant. How can I help you today?"
      />
      
      <ChatBubble
        type="user"
        content="I'd like to know more about cloud computing architecture."
      />
      
      <ChatBubble
        type="ai"
        content="Cloud computing architecture refers to the components and subcomponents required for cloud computing. These components typically consist of a front-end platform (client or device), back-end platforms (servers, storage), a cloud-based delivery model, and a network (Internet, Intranet)."
      />
    </>
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `type` | 'ai' \| 'user' | Type of the chat bubble (AI or user) |
| `content` | ReactNode | Content to display in the chat bubble |
| `header` | ReactNode | Optional header content for the chat bubble |
| `footer` | ReactNode | Optional footer content for the chat bubble |
| `variant` | 'default' \| 'emphasized' | Visual variant of the chat bubble |
| `loading` | boolean | Whether the chat bubble is in a loading state |
| `media` | ReactNode | Optional media content displayed above the text |

## Examples

### Chat Bubbles with Headers and Footers

```jsx
import { ChatBubble, Avatar, Box, SpaceBetween } from '@cloudscape-design/components';

function ChatBubblesWithHeadersAndFooters() {
  return (
    <SpaceBetween size="m">
      <ChatBubble
        type="ai"
        content="Hello! I'm Claude, an AI assistant built by Anthropic. I can help answer questions, generate content, and assist with a variety of tasks."
        header={
          <SpaceBetween direction="horizontal" size="xs">
            <Avatar
              name="Claude"
              variant="default"
              size="medium"
            />
            <span>Claude</span>
          </SpaceBetween>
        }
        footer={
          <Box fontSize="body-s" color="text-body-secondary">
            Sent at 10:32 AM
          </Box>
        }
      />
      
      <ChatBubble
        type="user"
        content="Thanks for the introduction! Can you help me understand the difference between various cloud service models like IaaS, PaaS, and SaaS?"
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
        footer={
          <Box fontSize="body-s" color="text-body-secondary">
            Sent at 10:33 AM
          </Box>
        }
      />
      
      <ChatBubble
        type="ai"
        content={
          <div>
            <p>Certainly! Here's a breakdown of the main cloud service models:</p>
            <ul>
              <li><strong>IaaS (Infrastructure as a Service)</strong>: Provides virtualized computing resources over the internet. You rent IT infrastructure—servers, storage, networks, operating systems—from a cloud provider on a pay-as-you-go basis.</li>
              <li><strong>PaaS (Platform as a Service)</strong>: Provides a platform allowing customers to develop, run, and manage applications without dealing with the complexity of building and maintaining the infrastructure.</li>
              <li><strong>SaaS (Software as a Service)</strong>: Delivers software applications over the internet, on-demand and typically on a subscription basis. With SaaS, cloud providers host and manage the software application and underlying infrastructure.</li>
            </ul>
            <p>Each model offers different levels of control, flexibility, and management responsibility.</p>
          </div>
        }
        header={
          <SpaceBetween direction="horizontal" size="xs">
            <Avatar
              name="Claude"
              variant="default"
              size="medium"
            />
            <span>Claude</span>
          </SpaceBetween>
        }
        footer={
          <Box fontSize="body-s" color="text-body-secondary">
            Sent at 10:35 AM
          </Box>
        }
      />
    </SpaceBetween>
  );
}
```

### Chat Bubbles with Loading State

```jsx
import { ChatBubble, Avatar, SpaceBetween, LoadingBar } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function ChatBubblesWithLoadingState() {
  const [isLoading, setIsLoading] = useState(true);
  const [content, setContent] = useState('');
  
  useEffect(() => {
    // Simulate loading and content generation
    const response = "I'm analyzing your question about cloud architecture. Cloud architecture refers to how components that make up cloud services, including hardware and software, are integrated to create the cloud. The key components include:\n\n1. Frontend Platform\n2. Backend Platform\n3. Cloud-based Delivery\n4. Network";
    
    const timer = setTimeout(() => {
      setIsLoading(false);
      setContent(response);
    }, 3000);
    
    return () => clearTimeout(timer);
  }, []);
  
  return (
    <SpaceBetween size="m">
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
        content={isLoading ? <LoadingBar /> : content}
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
  );
}
```

### Chat Bubbles with Different Variants

```jsx
import { ChatBubble, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function ChatBubblesWithVariants() {
  return (
    <Container header={<Header variant="h2">Chat Bubble Variants</Header>}>
      <SpaceBetween size="l">
        <div>
          <h3>Default Variant</h3>
          <SpaceBetween size="m">
            <ChatBubble
              type="ai"
              content="This is a default AI chat bubble."
              variant="default"
            />
            
            <ChatBubble
              type="user"
              content="This is a default user chat bubble."
              variant="default"
            />
          </SpaceBetween>
        </div>
        
        <div>
          <h3>Emphasized Variant</h3>
          <SpaceBetween size="m">
            <ChatBubble
              type="ai"
              content="This is an emphasized AI chat bubble, which can be used to highlight important messages or responses."
              variant="emphasized"
            />
            
            <ChatBubble
              type="user"
              content="This is an emphasized user chat bubble, which can be used to highlight important questions or inputs."
              variant="emphasized"
            />
          </SpaceBetween>
        </div>
      </SpaceBetween>
    </Container>
  );
}
```

### Chat Bubbles with Media Content

```jsx
import { ChatBubble, Avatar, SpaceBetween, Box, ColumnLayout, Container, Header } from '@cloudscape-design/components';

function ChatBubblesWithMedia() {
  // Mock chart or image component
  const ChartComponent = () => (
    <Box
      padding="m"
      textAlign="center"
      bgcolor="background.container"
      borderRadius="default"
      border="divider-standard"
    >
      [Cloud Services Comparison Chart]
      <div style={{ height: '200px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div>Mock Chart Visualization</div>
      </div>
    </Box>
  );
  
  return (
    <Container header={<Header variant="h2">Data Visualization in Chat</Header>}>
      <SpaceBetween size="l">
        <ChatBubble
          type="user"
          content="Can you show me a comparison of different cloud service models?"
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
          content={
            <SpaceBetween size="m">
              <p>Here's a comparison of the different cloud service models:</p>
              <ColumnLayout columns={1}>
                <Box>
                  <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                    <thead>
                      <tr>
                        <th style={{ border: '1px solid #ddd', padding: '8px', textAlign: 'left' }}>Service Model</th>
                        <th style={{ border: '1px solid #ddd', padding: '8px', textAlign: 'left' }}>Control Level</th>
                        <th style={{ border: '1px solid #ddd', padding: '8px', textAlign: 'left' }}>Management Responsibility</th>
                        <th style={{ border: '1px solid #ddd', padding: '8px', textAlign: 'left' }}>Use Case</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>IaaS</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>High</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>User manages OS, middleware, apps</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>Test environments, website hosting</td>
                      </tr>
                      <tr>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>PaaS</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>Medium</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>User manages apps only</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>App development, API development</td>
                      </tr>
                      <tr>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>SaaS</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>Low</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>Provider manages everything</td>
                        <td style={{ border: '1px solid #ddd', padding: '8px' }}>Email, CRM, productivity apps</td>
                      </tr>
                    </tbody>
                  </table>
                </Box>
              </ColumnLayout>
              <p>This comparison shows the key differences in terms of control, responsibility, and typical use cases.</p>
            </SpaceBetween>
          }
          media={<ChartComponent />}
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

### Complete Chat Interface with ChatBubble

```jsx
import { 
  ChatBubble, 
  Avatar, 
  SpaceBetween, 
  Container, 
  Header, 
  PromptInput,
  Box,
  LoadingBar
} from '@cloudscape-design/components';
import { useState, useRef, useEffect } from 'react';

function ChatInterface() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'ai',
      content: 'Hello! I\'m an AI assistant. How can I help you today?',
      timestamp: new Date(Date.now() - 60000)
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
      let aiResponse;
      
      // Generate different responses based on user input
      if (inputValue.toLowerCase().includes('hello') || inputValue.toLowerCase().includes('hi')) {
        aiResponse = 'Hello there! How can I assist you today?';
      } else if (inputValue.toLowerCase().includes('help')) {
        aiResponse = 'I\'m here to help! You can ask me questions about cloud computing, architecture, services, or any other technical topics.';
      } else if (inputValue.toLowerCase().includes('cloud')) {
        aiResponse = 'Cloud computing is a technology that allows access to computing resources (like servers, storage, databases, networking, software) over the internet ("the cloud") instead of owning and maintaining physical infrastructure.';
      } else {
        aiResponse = 'That\'s an interesting question. I\'ll do my best to provide a helpful response based on my knowledge and capabilities.';
      }
      
      const aiMessage = {
        id: Date.now(),
        type: 'ai',
        content: aiResponse,
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, aiMessage]);
      setIsLoading(false);
    }, 1500);
  };
  
  const formatTime = (date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };
  
  return (
    <Container header={<Header variant="h2">AI Chat Assistant</Header>}>
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
                    name={message.type === 'user' ? 'You' : 'AI Assistant'}
                    variant={message.type === 'user' ? 'user' : 'default'}
                    size="medium"
                  />
                  <span>{message.type === 'user' ? 'You' : 'AI Assistant'}</span>
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
              content={<LoadingBar />}
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
            inputPlaceholder: 'Type your message...',
            submitButtonText: 'Send'
          }}
        />
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Other Components

The ChatBubble component works well with these related components:

1. **PromptInput** - For accepting user input in chat interfaces
2. **Avatar** - For representing users and AI in message headers
3. **LoadingBar** - For indicating loading states in AI responses
4. **Container** - For wrapping chat interfaces with proper styling

## Accessibility

- Uses semantic HTML to ensure proper screen reader interpretation
- Provides clear visual differentiation between user and AI messages
- Includes appropriate ARIA roles for interactive elements
- Maintains focus management for keyboard navigation
- Supports high contrast modes for better visibility
- Uses proper color contrast for text readability

## Best Practices

1. Use consistent styling for all chat bubbles in an interface
2. Include avatars and names in headers for clear identification of message sources
3. Display timestamps in footers to provide context about message timing
4. Use loading states to indicate when the AI is generating a response
5. Implement auto-scrolling to keep the most recent messages visible
6. Use the emphasized variant for important messages or information
7. Consider adding media support for rich content like charts or images
8. Ensure the chat interface is fully accessible to all users
9. Maintain proper spacing between chat bubbles for readability
10. Use animation sparingly to avoid distracting users
11. Include error states and recovery options for failed messages
12. Consider responsive design for various screen sizes and devices
13. Test with screen readers to ensure accessibility compliance
14. Use semantic HTML within chat bubble content for proper structure
