# Avatar

The Avatar component displays a visual representation of a user, AI assistant, or entity within the interface. It's commonly used in chat interfaces, user profiles, and comment sections to provide visual identification.

## Import

```jsx
import { Avatar } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { Avatar } from '@cloudscape-design/components';

function BasicAvatar() {
  return (
    <Avatar
      name="John Doe"
      variant="user"
      size="medium"
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Name of the entity represented by the avatar (used for accessibility and generating initials) |
| `variant` | 'user' \| 'default' \| 'system' | Visual variant of the avatar |
| `size` | 'small' \| 'medium' \| 'large' | Size of the avatar |
| `src` | string | Optional URL for a custom avatar image |
| `alt` | string | Alternative text for the avatar image (defaults to name if not provided) |
| `color` | string | Optional color override for the avatar background |
| `ariaLabel` | string | Accessible label for screen readers |

## Examples

### Avatar Variants

```jsx
import { Avatar, Container, Header, SpaceBetween, Box } from '@cloudscape-design/components';

function AvatarVariants() {
  return (
    <Container header={<Header variant="h2">Avatar Variants</Header>}>
      <SpaceBetween size="l">
        <div>
          <h3>User Avatar</h3>
          <Avatar
            name="Jane Smith"
            variant="user"
            size="medium"
          />
        </div>
        
        <div>
          <h3>Default Avatar (AI)</h3>
          <Avatar
            name="Claude"
            variant="default"
            size="medium"
          />
        </div>
        
        <div>
          <h3>System Avatar</h3>
          <Avatar
            name="System"
            variant="system"
            size="medium"
          />
        </div>
      </SpaceBetween>
    </Container>
  );
}
```

### Avatar Sizes

```jsx
import { Avatar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function AvatarSizes() {
  return (
    <Container header={<Header variant="h2">Avatar Sizes</Header>}>
      <SpaceBetween size="l">
        <div>
          <h3>Small Avatar</h3>
          <Avatar
            name="John Doe"
            variant="user"
            size="small"
          />
        </div>
        
        <div>
          <h3>Medium Avatar</h3>
          <Avatar
            name="John Doe"
            variant="user"
            size="medium"
          />
        </div>
        
        <div>
          <h3>Large Avatar</h3>
          <Avatar
            name="John Doe"
            variant="user"
            size="large"
          />
        </div>
      </SpaceBetween>
    </Container>
  );
}
```

### Avatars with Custom Images

```jsx
import { Avatar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function AvatarsWithCustomImages() {
  return (
    <Container header={<Header variant="h2">Avatars with Custom Images</Header>}>
      <SpaceBetween size="l">
        <Avatar
          name="Jane Smith"
          variant="user"
          size="large"
          src="https://example.com/avatar1.jpg"
          alt="Jane Smith profile picture"
        />
        
        <Avatar
          name="John Doe"
          variant="user"
          size="large"
          src="https://example.com/avatar2.jpg"
          alt="John Doe profile picture"
        />
        
        <Avatar
          name="Claude AI"
          variant="default"
          size="large"
          src="https://example.com/claude-avatar.jpg"
          alt="Claude AI logo"
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Avatars with Custom Colors

```jsx
import { Avatar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function AvatarsWithCustomColors() {
  return (
    <Container header={<Header variant="h2">Avatars with Custom Colors</Header>}>
      <SpaceBetween size="l">
        <Avatar
          name="Marketing Team"
          variant="user"
          size="medium"
          color="#FF5733"
        />
        
        <Avatar
          name="Development Team"
          variant="user"
          size="medium"
          color="#33A1FF"
        />
        
        <Avatar
          name="Sales Team"
          variant="user"
          size="medium"
          color="#33FF57"
        />
        
        <Avatar
          name="Support Team"
          variant="user"
          size="medium"
          color="#D133FF"
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Avatars in Chat Interface

```jsx
import { Avatar, ChatBubble, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function AvatarsInChatInterface() {
  return (
    <Container header={<Header variant="h2">Chat Interface with Avatars</Header>}>
      <SpaceBetween size="l">
        <ChatBubble
          type="ai"
          content="Hello! I'm Claude, an AI assistant. How can I help you today?"
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
        />
        
        <ChatBubble
          type="user"
          content="I'd like to know more about AWS Lambda functions."
          header={
            <SpaceBetween direction="horizontal" size="xs">
              <Avatar
                name="Jane Smith"
                variant="user"
                size="medium"
              />
              <span>Jane</span>
            </SpaceBetween>
          }
        />
        
        <ChatBubble
          type="ai"
          content="AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. You pay only for the compute time that you consume—there's no charge when your code isn't running. With Lambda, you can run code for virtually any type of application or backend service—all with zero administration."
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
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Avatar Group

```jsx
import { Avatar, Container, Header, SpaceBetween, Box } from '@cloudscape-design/components';

function AvatarGroup() {
  return (
    <Container header={<Header variant="h2">Avatar Group</Header>}>
      <Box padding="m">
        <Box
          display="flex"
          marginLeft="-8px" // Negative margin for overlapping effect
        >
          <Box
            style={{
              marginLeft: "0px",
              zIndex: 5,
              border: "2px solid white",
              borderRadius: "50%"
            }}
          >
            <Avatar
              name="John Doe"
              variant="user"
              size="medium"
            />
          </Box>
          
          <Box
            style={{
              marginLeft: "-8px",
              zIndex: 4,
              border: "2px solid white",
              borderRadius: "50%"
            }}
          >
            <Avatar
              name="Jane Smith"
              variant="user"
              size="medium"
            />
          </Box>
          
          <Box
            style={{
              marginLeft: "-8px",
              zIndex: 3,
              border: "2px solid white",
              borderRadius: "50%"
            }}
          >
            <Avatar
              name="Michael Johnson"
              variant="user"
              size="medium"
            />
          </Box>
          
          <Box
            style={{
              marginLeft: "-8px",
              zIndex: 2,
              border: "2px solid white",
              borderRadius: "50%"
            }}
          >
            <Avatar
              name="Sarah Williams"
              variant="user"
              size="medium"
            />
          </Box>
          
          <Box
            style={{
              marginLeft: "-8px",
              zIndex: 1,
              border: "2px solid white",
              borderRadius: "50%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              width: "40px",
              height: "40px",
              backgroundColor: "#f0f0f0",
              fontWeight: "bold"
            }}
          >
            +3
          </Box>
        </Box>
      </Box>
    </Container>
  );
}
```

### User Profile with Avatar

```jsx
import { Avatar, Container, Header, SpaceBetween, Box, Button } from '@cloudscape-design/components';

function UserProfileWithAvatar() {
  return (
    <Container header={<Header variant="h2">User Profile</Header>}>
      <SpaceBetween size="l">
        <Box
          padding="l"
          textAlign="center"
        >
          <Box padding={{ bottom: 'm' }}>
            <Avatar
              name="Jane Smith"
              variant="user"
              size="large"
              src="https://example.com/jane-smith.jpg"
            />
          </Box>
          
          <Box fontSize="heading-m" fontWeight="bold">
            Jane Smith
          </Box>
          
          <Box fontSize="body-m" color="text-body-secondary">
            Senior Cloud Architect
          </Box>
          
          <Box padding={{ top: 'm', bottom: 'm' }}>
            <Button variant="primary">Edit Profile</Button>
          </Box>
          
          <SpaceBetween size="s" direction="horizontal">
            <Box>
              <Box fontSize="heading-s">127</Box>
              <Box fontSize="body-s">Projects</Box>
            </Box>
            
            <Box>
              <Box fontSize="heading-s">452</Box>
              <Box fontSize="body-s">Followers</Box>
            </Box>
            
            <Box>
              <Box fontSize="heading-s">89</Box>
              <Box fontSize="body-s">Following</Box>
            </Box>
          </SpaceBetween>
        </Box>
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Other Components

The Avatar component works well with these related components:

1. **ChatBubble** - For identifying message senders in chat interfaces
2. **PromptInput** - For showing user representation in chat input areas
3. **Container** - For framing avatar groups or profiles
4. **SpaceBetween** - For proper spacing in avatar arrangements
5. **Box** - For custom styling and layout of avatars

## Accessibility

- Uses appropriate ARIA attributes to ensure proper screen reader interpretation
- Provides alternative text for avatar images
- Generates initials from name when no image is available
- Maintains proper color contrast for text and background
- Ensures focus states are visible for interactive avatars
- Supports high contrast modes for better visibility

## Best Practices

1. Always provide a meaningful name for the avatar, which will be used for accessibility and generating initials
2. Use consistent avatar sizes throughout your application
3. Choose the appropriate variant based on the entity type (user, AI, system)
4. Consider using custom images for personalization when available
5. Provide proper alt text for custom avatar images
6. Use avatar groups to represent teams or multiple participants
7. Maintain proper spacing between avatars in groups
8. Consider using custom colors to differentiate between different teams or departments
9. Ensure avatars are properly sized for mobile interfaces
10. Use the appropriate avatar size based on the context and importance
11. Consider adding tooltips for additional information on hover
12. Use the same avatar consistently across the application for the same entity
13. Optimize avatar images for performance
14. Test avatar displays with various name lengths
15. Ensure avatar displays properly in both light and dark themes
