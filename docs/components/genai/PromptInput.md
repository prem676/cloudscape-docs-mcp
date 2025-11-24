# Prompt Input

The PromptInput component allows users to interact with generative AI capabilities through a specialized text input interface. It supports various features such as file attachments, voice input, and expandable text areas to accommodate different use cases.

## Import

```jsx
import { PromptInput } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { PromptInput } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicPromptInput() {
  const [value, setValue] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleSubmit = () => {
    if (!value.trim()) return;
    
    setIsProcessing(true);
    
    // Simulate processing
    setTimeout(() => {
      console.log('Processing prompt:', value);
      setIsProcessing(false);
      setValue('');
    }, 2000);
  };

  return (
    <PromptInput
      value={value}
      onChange={({ detail }) => setValue(detail.value)}
      onSubmit={handleSubmit}
      expandable={true}
      placeholder="Ask me anything..."
      submitting={isProcessing}
      i18nStrings={{
        submitAriaLabel: 'Submit prompt',
        expandAriaLabel: 'Expand prompt',
        inputPlaceholder: 'Ask me anything...',
        voiceInputTooltip: 'Voice input',
        voiceInputErrorText: 'Voice input is not supported',
        microphoneActiveAriaLabel: 'Microphone active',
        submitButtonText: 'Submit'
      }}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `value` | string | Current value of the input |
| `onChange` | ({ detail }) => void | Called when the value changes |
| `onSubmit` | () => void | Called when the user submits the input |
| `placeholder` | string | Placeholder text for the input (deprecated, use i18nStrings) |
| `disabled` | boolean | Whether the component is disabled |
| `disableSubmit` | boolean | Whether to disable the submit button |
| `expandable` | boolean | Whether the input can be expanded |
| `expanded` | boolean | Whether the input is expanded (controlled mode) |
| `defaultExpanded` | boolean | Whether the input is expanded by default |
| `onExpandedChange` | ({ detail }) => void | Called when expanded state changes |
| `submitting` | boolean | Whether the input is in a submitting state |
| `ariaLabel` | string | ARIA label for the input |
| `i18nStrings` | object | Internationalization strings |
| `controlId` | string | ID for the input element |
| `inputRef` | RefObject | Reference to the internal input element |
| `showVoiceInput` | boolean | Whether to show voice input option |
| `fileAttachmentOptions` | object | Options for file attachments |
| `stickyBottom` | boolean | Whether to stick to the bottom of the container |

## Examples

### Prompt Input with File Attachments

```jsx
import { PromptInput, Container, Header, SpaceBetween, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function PromptInputWithFileAttachments() {
  const [value, setValue] = useState('');
  const [files, setFiles] = useState([]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [conversation, setConversation] = useState([]);

  const handleSubmit = () => {
    if (!value.trim() && files.length === 0) return;
    
    setIsProcessing(true);
    
    // Add user message to conversation
    const userMessage = {
      type: 'user',
      content: value,
      files: [...files],
      timestamp: new Date()
    };
    
    setConversation(prev => [...prev, userMessage]);
    
    // Simulate AI response
    setTimeout(() => {
      const aiResponse = {
        type: 'ai',
        content: `I received your message${files.length > 0 ? ` and ${files.length} file(s)` : ''}. How can I help you with this?`,
        timestamp: new Date()
      };
      
      setConversation(prev => [...prev, aiResponse]);
      setIsProcessing(false);
      setValue('');
      setFiles([]);
    }, 2000);
  };

  const handleFilesChange = ({ detail }) => {
    setFiles(detail.value);
  };

  return (
    <Container header={<Header variant="h2">AI Assistant</Header>}>
      <SpaceBetween size="l">
        <Box>
          {conversation.map((message, index) => (
            <Box 
              key={index}
              padding="s"
              margin="s"
              textAlign={message.type === 'user' ? 'right' : 'left'}
            >
              <strong>{message.type === 'user' ? 'You' : 'AI Assistant'}:</strong>
              <p>{message.content}</p>
              {message.files && message.files.length > 0 && (
                <Box variant="small">
                  Attached files: {message.files.map(file => file.name).join(', ')}
                </Box>
              )}
            </Box>
          ))}
        </Box>
        
        <PromptInput
          value={value}
          onChange={({ detail }) => setValue(detail.value)}
          onSubmit={handleSubmit}
          expandable={true}
          submitting={isProcessing}
          fileAttachmentOptions={{
            accept: '.jpg,.jpeg,.png,.pdf,.doc,.docx,.txt',
            maxFileSize: 5 * 1024 * 1024, // 5MB
            maxFilesCount: 3,
            value: files,
            onChange: handleFilesChange,
            i18nStrings: {
              uploadButtonText: e => 'Attach files',
              dropzoneText: e => 'Drop files to attach',
              removeFileAriaLabel: e => `Remove file ${e.name}`,
              limitShowFewer: 'Show fewer files',
              limitShowMore: 'Show more files',
              errorIconAriaLabel: 'Error',
              attachButtonText: 'Attach',
              attachButtonLoadingAnnouncement: 'Attaching file',
              errorMessages: {
                maxFileSize: 'File is too large. Maximum file size is 5MB.',
                maxFilesCount: 'Too many files. Maximum number of files is 3.',
                acceptedFormats: 'File format is not supported.',
                default: 'Error attaching file.'
              }
            }
          }}
          i18nStrings={{
            submitAriaLabel: 'Submit prompt',
            expandAriaLabel: 'Expand prompt',
            inputPlaceholder: 'Ask me anything or attach files...',
            voiceInputTooltip: 'Voice input',
            voiceInputErrorText: 'Voice input is not supported',
            microphoneActiveAriaLabel: 'Microphone active',
            submitButtonText: 'Submit'
          }}
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Prompt Input with Voice Input

```jsx
import { PromptInput, Container, Header, SpaceBetween, StatusIndicator } from '@cloudscape-design/components';
import { useState } from 'react';

function PromptInputWithVoiceInput() {
  const [value, setValue] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const [voiceSupported, setVoiceSupported] = useState(true);

  const handleSubmit = () => {
    if (!value.trim()) return;
    
    setIsProcessing(true);
    
    // Simulate processing
    setTimeout(() => {
      console.log('Processing voice prompt:', value);
      setIsProcessing(false);
      setValue('');
    }, 2000);
  };

  const handleVoiceInputStart = () => {
    setIsListening(true);
    
    // Simulate voice recognition
    setTimeout(() => {
      setValue(prev => prev + 'This text was added via voice input. ');
      setIsListening(false);
    }, 3000);
  };

  return (
    <Container header={<Header variant="h2">Voice-Enabled AI Assistant</Header>}>
      <SpaceBetween size="l">
        <StatusIndicator type={isListening ? 'in-progress' : 'stopped'}>
          {isListening ? 'Listening...' : 'Ready for voice input'}
        </StatusIndicator>
        
        <PromptInput
          value={value}
          onChange={({ detail }) => setValue(detail.value)}
          onSubmit={handleSubmit}
          expandable={true}
          submitting={isProcessing}
          showVoiceInput={true}
          onVoiceInputStarted={handleVoiceInputStart}
          onVoiceInputError={() => setVoiceSupported(false)}
          i18nStrings={{
            submitAriaLabel: 'Submit prompt',
            expandAriaLabel: 'Expand prompt',
            inputPlaceholder: 'Type or speak your question...',
            voiceInputTooltip: 'Voice input',
            voiceInputErrorText: 'Voice input is not supported in your browser',
            microphoneActiveAriaLabel: 'Microphone active',
            submitButtonText: 'Submit'
          }}
        />
        
        {!voiceSupported && (
          <StatusIndicator type="error">
            Voice input is not supported in your browser.
          </StatusIndicator>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### Expandable Prompt Input

```jsx
import { PromptInput, Container, Header, SpaceBetween, Button, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function ExpandablePromptInput() {
  const [value, setValue] = useState('');
  const [expanded, setExpanded] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  
  const handleSubmit = () => {
    if (!value.trim()) return;
    
    setIsProcessing(true);
    
    // Simulate processing
    setTimeout(() => {
      console.log('Processing expanded prompt:', value);
      setIsProcessing(false);
      setValue('');
      setExpanded(false);
    }, 2000);
  };

  return (
    <Container header={<Header variant="h2">Advanced Query Interface</Header>}>
      <SpaceBetween size="l">
        <Box>
          <p>Use the expandable input below for longer, more detailed queries. Click the expand button to enter multi-line text.</p>
        </Box>
        
        <PromptInput
          value={value}
          onChange={({ detail }) => setValue(detail.value)}
          onSubmit={handleSubmit}
          expanded={expanded}
          onExpandedChange={({ detail }) => setExpanded(detail.expanded)}
          expandable={true}
          submitting={isProcessing}
          i18nStrings={{
            submitAriaLabel: 'Submit prompt',
            expandAriaLabel: 'Expand prompt',
            inputPlaceholder: 'Enter your detailed query...',
            submitButtonText: 'Submit'
          }}
        />
        
        <SpaceBetween direction="horizontal" size="xs">
          <Button onClick={() => setExpanded(!expanded)}>
            {expanded ? 'Collapse' : 'Expand'} input
          </Button>
          <Button variant="primary" disabled={!value.trim() || isProcessing} onClick={handleSubmit}>
            {isProcessing ? 'Processing...' : 'Process query'}
          </Button>
        </SpaceBetween>
      </SpaceBetween>
    </Container>
  );
}
```

### Prompt Input with Response Streaming

```jsx
import { PromptInput, Container, Header, SpaceBetween, Box, LoadingBar } from '@cloudscape-design/components';
import { useState, useEffect, useRef } from 'react';

function PromptInputWithStreaming() {
  const [value, setValue] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [response, setResponse] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const streamIntervalRef = useRef(null);
  
  // Cleanup interval on unmount
  useEffect(() => {
    return () => {
      if (streamIntervalRef.current) {
        clearInterval(streamIntervalRef.current);
      }
    };
  }, []);
  
  const handleSubmit = () => {
    if (!value.trim()) return;
    
    setIsProcessing(true);
    setIsStreaming(true);
    setResponse('');
    
    // Sample response to stream
    const fullResponse = 
      `Thank you for your question about "${value}". Let me provide a detailed response.\n\n` +
      `First, it's important to understand the context. The question relates to advanced AI techniques and their applications. ` +
      `There are several approaches we can consider when addressing this topic.\n\n` +
      `The most relevant factors include model architecture, training data quality, and evaluation methods. ` +
      `When implementing solutions in this area, best practices suggest starting with well-established baselines before exploring more novel approaches.\n\n` +
      `In conclusion, the answer depends on your specific use case, but the principles I've outlined should provide a solid foundation.`;
    
    let currentIndex = 0;
    
    // Simulate streaming response
    streamIntervalRef.current = setInterval(() => {
      if (currentIndex < fullResponse.length) {
        // Stream the next few characters
        const nextChunk = fullResponse.substring(currentIndex, currentIndex + 10);
        setResponse(prev => prev + nextChunk);
        currentIndex += 10;
      } else {
        // End streaming
        clearInterval(streamIntervalRef.current);
        setIsProcessing(false);
        setIsStreaming(false);
        setValue('');
      }
    }, 100);
  };

  return (
    <Container header={<Header variant="h2">AI Assistant with Streaming Response</Header>}>
      <SpaceBetween size="l">
        {response && (
          <Box
            padding="m"
            bgcolor="background.container"
            borderRadius="default"
          >
            <pre style={{ whiteSpace: 'pre-wrap', fontFamily: 'inherit', margin: 0 }}>
              {response}
            </pre>
            {isStreaming && <LoadingBar />}
          </Box>
        )}
        
        <PromptInput
          value={value}
          onChange={({ detail }) => setValue(detail.value)}
          onSubmit={handleSubmit}
          expandable={true}
          submitting={isProcessing}
          stickyBottom={true}
          i18nStrings={{
            submitAriaLabel: 'Submit prompt',
            expandAriaLabel: 'Expand prompt',
            inputPlaceholder: 'Ask a question...',
            submitButtonText: 'Submit'
          }}
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Complete Chat Interface

```jsx
import { 
  PromptInput, 
  Container, 
  Header, 
  SpaceBetween, 
  Box, 
  LoadingBar,
  Avatar,
  ChatBubble,
  StatusIndicator
} from '@cloudscape-design/components';
import { useState, useRef, useEffect } from 'react';

function ChatInterface() {
  const [value, setValue] = useState('');
  const [files, setFiles] = useState([]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [messages, setMessages] = useState([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const chatEndRef = useRef(null);
  const streamIntervalRef = useRef(null);
  
  // Scroll to bottom when messages change
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);
  
  // Cleanup interval on unmount
  useEffect(() => {
    return () => {
      if (streamIntervalRef.current) {
        clearInterval(streamIntervalRef.current);
      }
    };
  }, []);
  
  const handleSubmit = () => {
    if (!value.trim() && files.length === 0) return;
    
    // Add user message
    const userMessage = {
      type: 'user',
      content: value,
      files: [...files],
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setIsProcessing(true);
    setIsStreaming(true);
    
    // Start AI response with empty content
    const aiMessageId = Date.now();
    const initialAiMessage = {
      id: aiMessageId,
      type: 'ai',
      content: '',
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, initialAiMessage]);
    
    // Sample response to stream
    const fullResponse = 
      `Thank you for your question${files.length > 0 ? ' and the files you shared' : ''}.\n\n` +
      `I've analyzed ${files.length > 0 ? 'both your query and the attached documents' : 'your query'}. ` +
      `Based on the information provided, here's what I can tell you:\n\n` +
      `${value.includes('how') ? 'The process you asked about involves several steps:\n\n1. First, analyze the requirements\n2. Then, design a solution approach\n3. Implement the solution\n4. Finally, evaluate and refine the results' : 
        value.includes('what') ? 'The concept you asked about refers to an advanced approach in this domain. It combines several key techniques to achieve optimal results.' :
        'This is an interesting topic with many applications in the field. The key considerations include technical feasibility, resource requirements, and expected outcomes.'}`;
    
    let currentIndex = 0;
    
    // Simulate streaming response
    streamIntervalRef.current = setInterval(() => {
      if (currentIndex < fullResponse.length) {
        // Stream the next few characters
        const nextChunk = fullResponse.substring(currentIndex, currentIndex + 8);
        setMessages(prev => 
          prev.map(msg => 
            msg.id === aiMessageId 
              ? { ...msg, content: msg.content + nextChunk } 
              : msg
          )
        );
        currentIndex += 8;
      } else {
        // End streaming
        clearInterval(streamIntervalRef.current);
        setIsProcessing(false);
        setIsStreaming(false);
        setValue('');
        setFiles([]);
      }
    }, 50);
  };
  
  const handleFilesChange = ({ detail }) => {
    setFiles(detail.value);
  };

  return (
    <Container header={<Header variant="h2">AI Chat Assistant</Header>}>
      <SpaceBetween size="l">
        <Box padding="m" style={{ height: '400px', overflowY: 'auto' }}>
          {messages.length === 0 ? (
            <Box textAlign="center" color="text-body-secondary" padding="xl">
              <p>No messages yet. Start a conversation with the AI assistant.</p>
            </Box>
          ) : (
            messages.map((message, index) => (
              <ChatBubble
                key={index}
                type={message.type === 'user' ? 'user' : 'ai'}
                content={message.content || (isStreaming && index === messages.length - 1 ? <LoadingBar /> : 'Processing...')}
                header={
                  <SpaceBetween direction="horizontal" size="xs">
                    <Avatar
                      size="medium"
                      name={message.type === 'user' ? 'You' : 'AI Assistant'}
                      variant={message.type === 'user' ? 'user' : 'default'}
                    />
                    <span>{message.type === 'user' ? 'You' : 'AI Assistant'}</span>
                  </SpaceBetween>
                }
                footer={
                  message.files && message.files.length > 0 ? (
                    <Box fontSize="body-s" color="text-body-secondary">
                      Attached: {message.files.map(file => file.name).join(', ')}
                    </Box>
                  ) : null
                }
              />
            ))
          )}
          <div ref={chatEndRef} />
        </Box>
        
        {isProcessing && (
          <StatusIndicator type="in-progress">
            AI is responding...
          </StatusIndicator>
        )}
        
        <PromptInput
          value={value}
          onChange={({ detail }) => setValue(detail.value)}
          onSubmit={handleSubmit}
          expandable={true}
          submitting={isProcessing}
          stickyBottom={true}
          fileAttachmentOptions={{
            accept: '.jpg,.jpeg,.png,.pdf,.doc,.docx,.txt',
            maxFileSize: 5 * 1024 * 1024, // 5MB
            maxFilesCount: 3,
            value: files,
            onChange: handleFilesChange,
            i18nStrings: {
              uploadButtonText: e => 'Attach files',
              dropzoneText: e => 'Drop files to attach',
              removeFileAriaLabel: e => `Remove file ${e.name}`,
              limitShowFewer: 'Show fewer files',
              limitShowMore: 'Show more files',
              errorIconAriaLabel: 'Error',
              attachButtonText: 'Attach',
              attachButtonLoadingAnnouncement: 'Attaching file',
              errorMessages: {
                maxFileSize: 'File is too large. Maximum file size is 5MB.',
                maxFilesCount: 'Too many files. Maximum number of files is 3.',
                acceptedFormats: 'File format is not supported.',
                default: 'Error attaching file.'
              }
            }
          }}
          i18nStrings={{
            submitAriaLabel: 'Send message',
            expandAriaLabel: 'Expand message',
            inputPlaceholder: 'Message AI assistant...',
            voiceInputTooltip: 'Voice input',
            voiceInputErrorText: 'Voice input is not supported',
            microphoneActiveAriaLabel: 'Microphone active',
            submitButtonText: 'Send'
          }}
        />
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with other GenAI Components

The PromptInput component works seamlessly with other GenAI components:

1. **ChatBubble** - For displaying messages in a conversation interface
2. **Avatar** - For representing users and AI in conversations
3. **LoadingBar** - For indicating streaming text responses
4. **File uploading components** - For attaching files to prompts

## Accessibility

- Uses ARIA attributes for better screen reader support
- Provides keyboard navigation for all interactive elements
- Includes focus management for expandable input and buttons
- Offers voice input options for alternative interaction methods
- Includes clear labeling for all interactive elements
- Supports notification announcements for status changes

## Best Practices

1. Use clear placeholder text to guide users on expected input
2. Implement appropriate validation to prevent empty submissions
3. Show loading states during processing to provide feedback
4. Use expandable input for scenarios where users might need to enter longer text
5. Consider adding file attachment options for more complex use cases
6. Combine with ChatBubble for conversational interfaces
7. Use the voice input feature with appropriate error handling
8. Implement streaming responses for more engaging interactions
9. Ensure the component is accessible to all users
10. Provide clear feedback for errors and processing states
11. Use stickyBottom for chat interfaces where the input should stay visible
12. Consider performance optimizations for large conversation histories
