# File Upload

The FileUpload component is a form element that allows users to select one or multiple local files to upload. Files can be uploaded upon form submission or processed further in the browser.

## Import

```jsx
import { FileUpload } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { FileUpload } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicFileUpload() {
  const [value, setValue] = useState([]);

  return (
    <FileUpload
      onChange={({ detail }) => setValue(detail.value)}
      value={value}
      i18nStrings={{
        uploadButtonText: e => 'Choose files',
        dropzoneText: e => 'Drop files to upload',
        removeFileAriaLabel: e => `Remove file ${e.name}`,
        limitShowFewer: 'Show fewer files',
        limitShowMore: 'Show more files',
        errorIconAriaLabel: 'Error'
      }}
      constraintText="Maximum of 5 files. Up to 30 MB per file."
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `value` | Array | Array of files to display |
| `onChange` | ({ detail }) => void | Called when files are added or removed |
| `multiple` | boolean | Whether to allow multiple files |
| `accept` | string | Comma-separated list of MIME types or file extensions |
| `disabled` | boolean | Whether the component is disabled |
| `showFileLastModified` | boolean | Whether to show the file's last modified date |
| `showFileSize` | boolean | Whether to show the file's size |
| `showFileType` | boolean | Whether to show the file's type |
| `tokenLimit` | number | Maximum number of file tokens to show before collapsing |
| `constraintText` | string | Text that appears below the component |
| `fileErrors` | Map | Map of file names to error messages |
| `errorText` | string | Text displayed as an error |
| `ariaRequired` | boolean | Indicates if the field is required for accessibility |
| `ariaDescribedby` | string | ID of an element containing a custom description |
| `fileTokenAlignment` | 'vertical' \| 'horizontal' | How to align file tokens |
| `i18nStrings` | object | Internationalization strings |
| `isEmpty` | (value) => boolean | Function that determines if the value is empty |

## Examples

### Single File Upload

```jsx
import { FileUpload, SpaceBetween, FormField } from '@cloudscape-design/components';
import { useState } from 'react';

function SingleFileUpload() {
  const [value, setValue] = useState([]);

  return (
    <FormField
      label="Upload profile picture"
      description="Select an image file to use as your profile picture."
    >
      <FileUpload
        onChange={({ detail }) => setValue(detail.value)}
        value={value}
        multiple={false}
        accept="image/*"
        i18nStrings={{
          uploadButtonText: e => 'Choose file',
          dropzoneText: e => 'Drop file to upload',
          removeFileAriaLabel: e => `Remove file ${e.name}`,
          errorIconAriaLabel: 'Error'
        }}
        constraintText="Maximum size: 5 MB. Supported formats: JPEG, PNG, GIF."
      />
    </FormField>
  );
}
```

### Multiple File Upload with Validation

```jsx
import { FileUpload, SpaceBetween, FormField, Alert } from '@cloudscape-design/components';
import { useState } from 'react';

function MultipleFileUploadWithValidation() {
  const [value, setValue] = useState([]);
  const [fileErrors, setFileErrors] = useState(new Map());
  const [errorText, setErrorText] = useState('');
  
  const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB
  const ALLOWED_TYPES = ['application/pdf', 'image/jpeg', 'image/png', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
  
  const handleChange = ({ detail }) => {
    const newValue = detail.value;
    setValue(newValue);
    
    // Validate files
    const errors = new Map();
    let hasErrors = false;
    
    newValue.forEach(file => {
      if (file.size > MAX_FILE_SIZE) {
        errors.set(file.name, 'File exceeds the 5 MB size limit.');
        hasErrors = true;
      } else if (!ALLOWED_TYPES.includes(file.type)) {
        errors.set(file.name, 'File type not supported.');
        hasErrors = true;
      }
    });
    
    setFileErrors(errors);
    setErrorText(hasErrors ? 'One or more files have errors.' : '');
  };

  return (
    <SpaceBetween size="m">
      <FormField
        label="Upload documents"
        description="Upload supporting documents for your application."
        errorText={errorText}
      >
        <FileUpload
          onChange={handleChange}
          value={value}
          multiple={true}
          accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"
          fileErrors={fileErrors}
          showFileSize={true}
          showFileType={true}
          showFileLastModified={true}
          constraintText="Maximum of 10 files. Accepted formats: PDF, DOC, DOCX, JPG, PNG. Maximum size per file: 5 MB."
          i18nStrings={{
            uploadButtonText: e => 'Choose files',
            dropzoneText: e => 'Drop files to upload',
            removeFileAriaLabel: e => `Remove file ${e.name}`,
            limitShowFewer: 'Show fewer files',
            limitShowMore: 'Show more files',
            errorIconAriaLabel: 'Error'
          }}
        />
      </FormField>
      
      {value.length > 0 && (
        <Alert type="info">
          {value.length} file{value.length === 1 ? '' : 's'} selected, ready to upload.
        </Alert>
      )}
    </SpaceBetween>
  );
}
```

### File Upload with Drag and Drop Emphasis

```jsx
import { FileUpload, SpaceBetween, Container, Header, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function DragAndDropFileUpload() {
  const [value, setValue] = useState([]);
  
  return (
    <Container header={<Header variant="h2">Import data</Header>}>
      <SpaceBetween size="l">
        <Box variant="p">
          Upload your data files by dragging and dropping them into the area below,
          or by selecting them from your computer.
        </Box>
        
        <FileUpload
          onChange={({ detail }) => setValue(detail.value)}
          value={value}
          multiple={true}
          accept=".csv,.xlsx,.json"
          i18nStrings={{
            uploadButtonText: e => 'Select files',
            dropzoneText: e => 'Drag and drop files here',
            removeFileAriaLabel: e => `Remove file ${e.name}`,
            limitShowFewer: 'Show fewer files',
            limitShowMore: 'Show more files',
            errorIconAriaLabel: 'Error'
          }}
          constraintText="Accepted formats: CSV, Excel, JSON. Maximum file size: 50 MB."
          showFileSize={true}
          showFileType={true}
          tokenLimit={5}
        />
        
        <Box variant="p">
          {value.length === 0 ? (
            'No files selected.'
          ) : (
            `${value.length} file${value.length === 1 ? '' : 's'} selected.`
          )}
        </Box>
      </SpaceBetween>
    </Container>
  );
}
```

### File Upload with Token Alignment Options

```jsx
import { FileUpload, SpaceBetween, Container, Header, RadioGroup } from '@cloudscape-design/components';
import { useState } from 'react';

function FileUploadWithAlignmentOptions() {
  const [value, setValue] = useState([]);
  const [alignment, setAlignment] = useState('horizontal');
  
  // Generate sample files
  const generateSampleFiles = () => {
    const sampleFiles = [];
    for (let i = 1; i <= 5; i++) {
      const fileType = i % 2 === 0 ? 'document.pdf' : 'image.jpg';
      sampleFiles.push({
        name: `Sample-${i}-${fileType}`,
        size: i * 1024 * 1024,
        type: i % 2 === 0 ? 'application/pdf' : 'image/jpeg',
        lastModified: new Date().getTime() - i * 86400000
      });
    }
    setValue(sampleFiles);
  };
  
  return (
    <Container header={<Header variant="h2">File upload with alignment options</Header>}>
      <SpaceBetween size="l">
        <RadioGroup
          items={[
            { value: 'horizontal', label: 'Horizontal alignment' },
            { value: 'vertical', label: 'Vertical alignment' }
          ]}
          value={alignment}
          onChange={({ detail }) => setAlignment(detail.value)}
        />
        
        <FileUpload
          onChange={({ detail }) => setValue(detail.value)}
          value={value}
          multiple={true}
          fileTokenAlignment={alignment}
          showFileSize={true}
          showFileType={true}
          showFileLastModified={true}
          i18nStrings={{
            uploadButtonText: e => 'Choose files',
            dropzoneText: e => 'Drop files to upload',
            removeFileAriaLabel: e => `Remove file ${e.name}`,
            limitShowFewer: 'Show fewer files',
            limitShowMore: 'Show more files',
            errorIconAriaLabel: 'Error'
          }}
        />
        
        {value.length === 0 && (
          <SpaceBetween size="s" direction="horizontal">
            <a href="#" onClick={(e) => { e.preventDefault(); generateSampleFiles(); }}>
              Add sample files
            </a>
            <span>to see alignment differences</span>
          </SpaceBetween>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### File Upload with Dynamic File Processing

```jsx
import { 
  FileUpload, 
  SpaceBetween, 
  Container, 
  Header, 
  ProgressBar, 
  StatusIndicator,
  Table,
  Box,
  Button
} from '@cloudscape-design/components';
import { useState } from 'react';

function FileUploadWithProcessing() {
  const [value, setValue] = useState([]);
  const [processedFiles, setProcessedFiles] = useState([]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentFile, setCurrentFile] = useState(null);
  const [progress, setProgress] = useState(0);
  
  // Simulate file processing
  const processFiles = () => {
    if (value.length === 0 || isProcessing) return;
    
    setIsProcessing(true);
    setProgress(0);
    setProcessedFiles([]);
    
    let currentIndex = 0;
    const results = [];
    
    const processNextFile = () => {
      if (currentIndex >= value.length) {
        setIsProcessing(false);
        setCurrentFile(null);
        return;
      }
      
      const file = value[currentIndex];
      setCurrentFile(file.name);
      
      // Simulate file processing with progress updates
      let fileProgress = 0;
      const totalProgress = (currentIndex / value.length) * 100;
      
      const fileInterval = setInterval(() => {
        fileProgress += 10;
        setProgress(totalProgress + (fileProgress / 10) * (100 / value.length));
        
        if (fileProgress >= 100) {
          clearInterval(fileInterval);
          
          // Add processed result
          results.push({
            name: file.name,
            size: file.size,
            type: file.type,
            status: Math.random() > 0.8 ? 'error' : 'success',
            message: Math.random() > 0.8 ? 'Failed to process file' : 'Successfully processed'
          });
          
          setProcessedFiles([...results]);
          currentIndex++;
          setTimeout(processNextFile, 300);
        }
      }, 300);
    };
    
    processNextFile();
  };
  
  return (
    <Container header={<Header variant="h2">File processing</Header>}>
      <SpaceBetween size="l">
        <FileUpload
          onChange={({ detail }) => setValue(detail.value)}
          value={value}
          multiple={true}
          disabled={isProcessing}
          i18nStrings={{
            uploadButtonText: e => 'Choose files',
            dropzoneText: e => 'Drop files to upload',
            removeFileAriaLabel: e => `Remove file ${e.name}`,
            limitShowFewer: 'Show fewer files',
            limitShowMore: 'Show more files',
            errorIconAriaLabel: 'Error'
          }}
          constraintText="Select files to process."
          showFileSize={true}
          showFileType={true}
        />
        
        <Button onClick={processFiles} disabled={value.length === 0 || isProcessing}>
          Process files
        </Button>
        
        {isProcessing && (
          <SpaceBetween size="s">
            <Box variant="p">Processing file: {currentFile}</Box>
            <ProgressBar
              value={progress}
              label="Processing files"
              description={`${Math.round(progress)}% complete`}
            />
          </SpaceBetween>
        )}
        
        {processedFiles.length > 0 && (
          <Table
            header={<Header variant="h3">Processing results</Header>}
            columnDefinitions={[
              {
                id: 'name',
                header: 'File name',
                cell: item => item.name
              },
              {
                id: 'size',
                header: 'Size',
                cell: item => `${Math.round(item.size / 1024)} KB`
              },
              {
                id: 'status',
                header: 'Status',
                cell: item => (
                  <StatusIndicator type={item.status === 'success' ? 'success' : 'error'}>
                    {item.status === 'success' ? 'Success' : 'Error'}
                  </StatusIndicator>
                )
              },
              {
                id: 'message',
                header: 'Message',
                cell: item => item.message
              }
            ]}
            items={processedFiles}
          />
        )}
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Form Component

The FileUpload component works seamlessly with the Form component for validation and submission:

```jsx
import { 
  Form, 
  FormField, 
  SpaceBetween, 
  Container, 
  Header, 
  Button,
  FileUpload
} from '@cloudscape-design/components';
import { useState } from 'react';

function FileUploadForm() {
  const [files, setFiles] = useState([]);
  const [fileErrors, setFileErrors] = useState(new Map());
  const [error, setError] = useState('');
  
  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (files.length === 0) {
      setError('Please select at least one file.');
      return;
    }
    
    if (fileErrors.size > 0) {
      setError('Please fix the errors before submitting.');
      return;
    }
    
    // Form is valid, process the files
    alert(`Submitting ${files.length} files`);
  };
  
  const validateFiles = (newFiles) => {
    const errors = new Map();
    
    newFiles.forEach(file => {
      if (file.size > 10 * 1024 * 1024) { // 10MB limit
        errors.set(file.name, 'File exceeds the 10 MB size limit');
      }
    });
    
    setFileErrors(errors);
    setError(errors.size > 0 ? 'One or more files have errors' : '');
    
    return errors;
  };
  
  const handleFilesChange = ({ detail }) => {
    const newFiles = detail.value;
    setFiles(newFiles);
    validateFiles(newFiles);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <Form
        header={<Header variant="h2">Submit documents</Header>}
        errorText={error}
        actions={
          <SpaceBetween direction="horizontal" size="xs">
            <Button formAction="none" variant="link">Cancel</Button>
            <Button variant="primary">Submit</Button>
          </SpaceBetween>
        }
      >
        <Container>
          <SpaceBetween size="l">
            <FormField
              label="Upload documents"
              description="Upload all required documents for processing."
              constraintText="Maximum 5 files, 10 MB per file."
              errorText={error}
            >
              <FileUpload
                onChange={handleFilesChange}
                value={files}
                multiple={true}
                fileErrors={fileErrors}
                showFileSize={true}
                showFileType={true}
                i18nStrings={{
                  uploadButtonText: e => 'Choose files',
                  dropzoneText: e => 'Drop files to upload',
                  removeFileAriaLabel: e => `Remove file ${e.name}`,
                  limitShowFewer: 'Show fewer files',
                  limitShowMore: 'Show more files',
                  errorIconAriaLabel: 'Error'
                }}
              />
            </FormField>
          </SpaceBetween>
        </Container>
      </Form>
    </form>
  );
}
```

## Accessibility

- Provides accessible labels for all interactive elements
- Includes keyboard navigation for file selection and removal
- Uses ARIA attributes for status information
- Provides descriptive error messages
- Maintains focus management during user interactions
- Supports screen readers through meaningful announcements

## Best Practices

1. Always include descriptive constraints about file types, size limits, and count
2. Show file size and type information to help users verify their selections
3. Use validation to prevent users from uploading invalid files
4. Display clear error messages for invalid files
5. Use vertical alignment for file tokens when space is limited
6. Limit the number of visible tokens and use "show more" for larger collections
7. Add progress indicators for upload or processing operations
8. Integrate with form validation and submission flows
9. Use appropriate file type restrictions to guide users
10. Consider accessibility needs for all users
11. Include meaningful feedback after upload operations
12. Combine with other components like Tables or ProgressBars for complex workflows
