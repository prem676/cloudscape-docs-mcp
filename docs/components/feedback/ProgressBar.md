# Progress Bar

The Progress Bar component provides visual feedback about the progress of an operation, especially for long-running tasks. It helps users understand the status of processes like file uploads, data loading, or multi-step operations.

## Import

```jsx
import { ProgressBar } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { ProgressBar } from '@cloudscape-design/components';

function BasicProgressBar() {
  return (
    <ProgressBar
      value={30}
      label="File upload"
      description="Uploading file to storage"
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `value` | number | Current progress value between 0 and 100 |
| `label` | ReactNode | Text label displayed above the progress bar |
| `description` | ReactNode | Additional description displayed below the progress bar |
| `status` | 'in-progress' \| 'success' \| 'error' | Status of the operation |
| `additionalInfo` | ReactNode | Additional information displayed next to the label |
| `variant` | 'standalone' \| 'flash' \| 'key-value' | Visual variant of the progress bar |
| `resultButtonText` | string | Text for the result button when operation completes |
| `onResultButtonClick` | () => void | Callback fired when the result button is clicked |

## Examples

### Progress Bar with Different Statuses

```jsx
import { ProgressBar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function ProgressBarStatuses() {
  return (
    <Container header={<Header variant="h2">Progress Bar Statuses</Header>}>
      <SpaceBetween size="l">
        <ProgressBar
          value={30}
          label="In Progress"
          description="Operation is currently running"
          status="in-progress"
        />
        
        <ProgressBar
          value={100}
          label="Completed"
          description="Operation completed successfully"
          status="success"
        />
        
        <ProgressBar
          value={45}
          label="Failed"
          description="Operation encountered an error"
          status="error"
        />
      </SpaceBetween>
    </Container>
  );
}
```

### Indeterminate Progress Bar

```jsx
import { ProgressBar, Box } from '@cloudscape-design/components';

function IndeterminateProgressBar() {
  return (
    <Box padding="m">
      <ProgressBar
        label="Loading data"
        description="Please wait while we load your data"
        value={undefined} // Using undefined makes it indeterminate
      />
    </Box>
  );
}
```

### Progress Bar with Result Button

```jsx
import { ProgressBar, Container, Header } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function ProgressBarWithResult() {
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState('in-progress');
  
  useEffect(() => {
    // Simulate progress
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval);
          setStatus('success');
          return 100;
        }
        return prev + 10;
      });
    }, 1000);
    
    return () => clearInterval(interval);
  }, []);
  
  const handleResultClick = () => {
    alert('View results clicked');
    // Navigate to results or show results modal
  };
  
  return (
    <Container header={<Header variant="h2">File Conversion</Header>}>
      <ProgressBar
        value={progress}
        label="Converting file"
        description={progress < 100 ? "Please wait while your file is being converted" : "Your file has been converted successfully"}
        status={status}
        resultButtonText={status === 'success' ? "View converted file" : undefined}
        onResultButtonClick={handleResultClick}
      />
    </Container>
  );
}
```

### Progress Bar with Additional Info

```jsx
import { ProgressBar, Box } from '@cloudscape-design/components';

function ProgressBarWithAdditionalInfo() {
  return (
    <Box padding="m">
      <ProgressBar
        value={75}
        label="Database backup"
        description="Backing up your database"
        additionalInfo="75 of 100 tables"
      />
    </Box>
  );
}
```

### Progress Bar in Different Variants

```jsx
import { ProgressBar, Container, Header, SpaceBetween } from '@cloudscape-design/components';

function ProgressBarVariants() {
  return (
    <Container header={<Header variant="h2">Progress Bar Variants</Header>}>
      <SpaceBetween size="l">
        <div>
          <h3>Standalone Variant</h3>
          <ProgressBar
            value={60}
            label="Standard progress bar"
            description="Used in most contexts"
            variant="standalone"
          />
        </div>
        
        <div>
          <h3>Flash Variant</h3>
          <ProgressBar
            value={60}
            label="Flash progress bar"
            description="Used in notification contexts"
            variant="flash"
          />
        </div>
        
        <div>
          <h3>Key-Value Variant</h3>
          <ProgressBar
            value={60}
            label="Key-value progress bar"
            description="Used in property lists"
            variant="key-value"
          />
        </div>
      </SpaceBetween>
    </Container>
  );
}
```

### Animated Progress Bar

```jsx
import { ProgressBar, Container, Header, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState, useEffect, useRef } from 'react';

function AnimatedProgressBar() {
  const [isRunning, setIsRunning] = useState(false);
  const [progress, setProgress] = useState(0);
  const intervalRef = useRef(null);
  
  useEffect(() => {
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, []);
  
  const startProgress = () => {
    setIsRunning(true);
    setProgress(0);
    
    intervalRef.current = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(intervalRef.current);
          setIsRunning(false);
          return 100;
        }
        return prev + 5;
      });
    }, 300);
  };
  
  const stopProgress = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      setIsRunning(false);
    }
  };
  
  const resetProgress = () => {
    stopProgress();
    setProgress(0);
  };
  
  return (
    <Container header={<Header variant="h2">Animated Progress</Header>}>
      <SpaceBetween size="m">
        <ProgressBar
          value={progress}
          label="Operation progress"
          description={isRunning ? "Operation in progress..." : progress === 100 ? "Operation complete!" : "Ready to start"}
          status={progress === 100 ? 'success' : 'in-progress'}
        />
        
        <SpaceBetween direction="horizontal" size="xs">
          <Button onClick={startProgress} disabled={isRunning}>Start</Button>
          <Button onClick={stopProgress} disabled={!isRunning}>Pause</Button>
          <Button onClick={resetProgress}>Reset</Button>
        </SpaceBetween>
      </SpaceBetween>
    </Container>
  );
}
```

### Progress Bar with Time Estimation

```jsx
import { ProgressBar, Container, Header, Box } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function ProgressBarWithTimeEstimation() {
  const [progress, setProgress] = useState(0);
  const [startTime, setStartTime] = useState(null);
  const [estimatedTime, setEstimatedTime] = useState('Calculating...');
  
  useEffect(() => {
    setStartTime(Date.now());
    
    const interval = setInterval(() => {
      setProgress(prev => {
        const newValue = prev + 2;
        
        if (newValue >= 100) {
          clearInterval(interval);
          setEstimatedTime('Complete');
          return 100;
        }
        
        // Calculate estimated time remaining
        if (newValue > 0 && startTime) {
          const elapsedMs = Date.now() - startTime;
          const msPerPercent = elapsedMs / newValue;
          const remainingPercent = 100 - newValue;
          const remainingMs = msPerPercent * remainingPercent;
          
          let timeString = 'Calculating...';
          
          if (remainingMs > 0) {
            const remainingSec = Math.round(remainingMs / 1000);
            if (remainingSec < 60) {
              timeString = `About ${remainingSec} second${remainingSec !== 1 ? 's' : ''} remaining`;
            } else {
              const remainingMin = Math.round(remainingSec / 60);
              timeString = `About ${remainingMin} minute${remainingMin !== 1 ? 's' : ''} remaining`;
            }
          }
          
          setEstimatedTime(timeString);
        }
        
        return newValue;
      });
    }, 500);
    
    return () => clearInterval(interval);
  }, []);
  
  return (
    <Container header={<Header variant="h2">Download Progress</Header>}>
      <Box padding="m">
        <ProgressBar
          value={progress}
          label="Downloading file"
          description={progress < 100 ? `Downloaded ${progress}%` : "Download complete"}
          additionalInfo={estimatedTime}
        />
      </Box>
    </Container>
  );
}
```

### File Upload with Progress Bar

```jsx
import { ProgressBar, FileUpload, Container, Header, SpaceBetween, Button } from '@cloudscape-design/components';
import { useState } from 'react';

function FileUploadWithProgressBar() {
  const [files, setFiles] = useState([]);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploadStatus, setUploadStatus] = useState('in-progress');
  
  const handleFilesChange = ({ detail }) => {
    setFiles(detail.value);
    // Reset progress when files change
    setUploadProgress(0);
    setIsUploading(false);
    setUploadStatus('in-progress');
  };
  
  const simulateUpload = () => {
    if (files.length === 0) return;
    
    setIsUploading(true);
    setUploadProgress(0);
    
    // Simulate upload progress
    const interval = setInterval(() => {
      setUploadProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval);
          setIsUploading(false);
          setUploadStatus('success');
          return 100;
        }
        return prev + 5;
      });
    }, 300);
  };
  
  return (
    <Container header={<Header variant="h2">File Upload with Progress</Header>}>
      <SpaceBetween size="l">
        <FileUpload
          onChange={handleFilesChange}
          value={files}
          multiple={true}
          accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
          constraintText="Accepted file types: .jpg, .jpeg, .png, .pdf, .doc, .docx"
        />
        
        <Button 
          onClick={simulateUpload} 
          disabled={files.length === 0 || isUploading}
        >
          Upload Files
        </Button>
        
        {(isUploading || uploadProgress > 0) && (
          <ProgressBar
            value={uploadProgress}
            label="File upload"
            description={`Uploading ${files.length} file${files.length !== 1 ? 's' : ''}`}
            status={uploadStatus}
            additionalInfo={`${uploadProgress}%`}
          />
        )}
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Other Components

The ProgressBar component works well with these related components:

1. **FileUpload** - For showing upload progress
2. **Container** - For proper framing of the progress context
3. **Alert** - For showing error states when progress fails
4. **Spinner** - For complementary loading states
5. **Button** - For actions related to the process

## Accessibility

- Includes ARIA attributes to ensure progress is communicated to screen readers
- Uses appropriate color contrast for visibility
- Provides text alternatives for visual indicators
- Ensures keyboard focus management for interactive elements
- Announces status changes to screen readers via aria-live regions

## Best Practices

1. Always include descriptive labels and descriptions to explain what is happening
2. Use appropriate status values to communicate success, error, or in-progress states
3. Consider using indeterminate progress bars when progress cannot be calculated
4. Add time estimates for longer operations when possible
5. Provide a way for users to cancel long-running operations
6. Use consistent styling for all progress bars in your application
7. Place progress bars near the content they relate to
8. For file uploads, show both percentage and file size information
9. Consider adding animation to make progress feel more dynamic
10. Keep users informed about what to expect next after completion
11. Ensure the progress bar is visible and prominent during long operations
12. Test with screen readers to ensure accessibility compliance
13. Use appropriate width based on the context and importance
14. Consider the appropriate variant based on where the progress bar appears in your UI
15. Add result buttons for quick actions after completion
