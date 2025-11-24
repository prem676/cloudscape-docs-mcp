# File Input

The FileInput component provides a simple interface for selecting files from a user's device. It acts as an enhanced version of the standard HTML file input, styled to match the CloudScape design system.

## Import

```jsx
import { FileInput } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { FileInput } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicFileInput() {
  const [value, setValue] = useState(null);
  
  const handleChange = ({ detail }) => {
    setValue(detail.value);
  };

  return (
    <FileInput
      onChange={handleChange}
      value={value}
      ariaLabel="Select a file"
      accept=".jpg,.jpeg,.png,.pdf"
      i18nStrings={{
        browseButtonText: 'Choose file',
        removeButtonText: 'Remove',
        dropzoneText: 'Drag and drop a file',
        selectedFileText: data => data.name,
        constraintText: 'Supported formats: JPG, PNG, PDF'
      }}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `value` | File | The currently selected file |
| `onChange` | (event: { detail: { value: File } }) => void | Event handler called when the file selection changes |
| `accept` | string | File types that the input accepts (comma-separated MIME types or extensions) |
| `multiple` | boolean | Whether multiple files can be selected (default: false) |
| `disabled` | boolean | Whether the file input is disabled |
| `constraintText` | string | Text that describes file constraints |
| `ariaLabel` | string | Accessible label for the file input |
| `i18nStrings` | object | Internationalization strings |
| `tokenLimit` | number | Maximum number of tokens to display when multiple files are selected |
| `showFileLastModified` | boolean | Whether to show the last modified timestamp for selected files |
| `showFileSize` | boolean | Whether to show file size information |
| `inputMode` | 'input' \| 'filedrop' | Visual mode of the file input |

## Examples

### Single File Input

```jsx
import { FileInput, Container, Header, SpaceBetween, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function SingleFileInput() {
  const [file, setFile] = useState(null);
  
  const handleChange = ({ detail }) => {
    setFile(detail.value);
  };
  
  const formatFileSize = (bytes) => {
    if (!bytes) return '';
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">Upload Profile Picture</Header>}>
      <SpaceBetween size="m">
        <FileInput
          onChange={handleChange}
          value={file}
          ariaLabel="Select profile picture"
          accept="image/*"
          i18nStrings={{
            browseButtonText: 'Choose image',
            removeButtonText: 'Remove',
            dropzoneText: 'Drag and drop an image',
            selectedFileText: data => data.name,
            constraintText: 'Only image files are supported. Maximum size: 5 MB.'
          }}
        />
        
        {file && (
          <Box padding="m">
            <SpaceBetween size="s">
              <h3>Selected file:</h3>
              <div>
                <div><strong>Name:</strong> {file.name}</div>
                <div><strong>Type:</strong> {file.type}</div>
                <div><strong>Size:</strong> {formatFileSize(file.size)}</div>
                <div><strong>Last modified:</strong> {new Date(file.lastModified).toLocaleString()}</div>
              </div>
            </SpaceBetween>
          </Box>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### Multiple File Input

```jsx
import { FileInput, Container, Header, SpaceBetween, Table } from '@cloudscape-design/components';
import { useState } from 'react';

function MultipleFileInput() {
  const [files, setFiles] = useState([]);
  
  const handleChange = ({ detail }) => {
    setFiles(detail.value);
  };
  
  const formatFileSize = (bytes) => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">Document Upload</Header>}>
      <SpaceBetween size="l">
        <FileInput
          onChange={handleChange}
          value={files}
          multiple={true}
          ariaLabel="Select documents"
          accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
          showFileSize={true}
          showFileLastModified={true}
          i18nStrings={{
            browseButtonText: 'Choose files',
            removeButtonText: 'Remove',
            dropzoneText: 'Drag and drop files',
            limitShowFewer: 'Show fewer files',
            limitShowMore: 'Show more files',
            selectedFileText: (data, index) => `${index + 1}: ${data.name}`,
            constraintText: 'Supported formats: JPG, PNG, PDF, DOC, DOCX'
          }}
        />
        
        {files.length > 0 && (
          <div>
            <h3>Selected files ({files.length}):</h3>
            <Table
              columnDefinitions={[
                {
                  id: 'name',
                  header: 'File name',
                  cell: item => item.name
                },
                {
                  id: 'type',
                  header: 'Type',
                  cell: item => item.type || 'Unknown'
                },
                {
                  id: 'size',
                  header: 'Size',
                  cell: item => formatFileSize(item.size)
                },
                {
                  id: 'lastModified',
                  header: 'Last modified',
                  cell: item => new Date(item.lastModified).toLocaleString()
                }
              ]}
              items={files}
              loadingText="Loading files"
              empty={
                <Box textAlign="center" color="inherit">
                  <b>No files</b>
                  <Box padding={{ bottom: 's' }} variant="p" color="inherit">
                    No files selected.
                  </Box>
                </Box>
              }
              header={<Header>Files detail</Header>}
            />
          </div>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### File Input with Validation

```jsx
import { FileInput, Container, Header, Alert, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function FileInputWithValidation() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);
  
  // Set maximum file size: 5 MB
  const MAX_FILE_SIZE = 5 * 1024 * 1024;
  
  // Set allowed file types
  const ALLOWED_TYPES = ['application/pdf', 'image/jpeg', 'image/jpg', 'image/png'];
  
  const validateFile = (file) => {
    if (!file) return null;
    
    // Check file size
    if (file.size > MAX_FILE_SIZE) {
      return `File size exceeds 5 MB limit. Current size: ${(file.size / (1024 * 1024)).toFixed(1)} MB`;
    }
    
    // Check file type
    if (!ALLOWED_TYPES.includes(file.type)) {
      return `File type "${file.type}" is not supported. Please use PDF, JPG, or PNG files.`;
    }
    
    return null;
  };
  
  const handleChange = ({ detail }) => {
    const selectedFile = detail.value;
    const validationError = validateFile(selectedFile);
    
    if (validationError) {
      setError(validationError);
      setFile(null);
    } else {
      setError(null);
      setFile(selectedFile);
    }
  };

  return (
    <Container header={<Header variant="h2">Validated Document Upload</Header>}>
      <SpaceBetween size="m">
        {error && (
          <Alert type="error" dismissible onDismiss={() => setError(null)}>
            {error}
          </Alert>
        )}
        
        <FileInput
          onChange={handleChange}
          value={file}
          ariaLabel="Select document"
          accept=".jpg,.jpeg,.png,.pdf"
          i18nStrings={{
            browseButtonText: 'Choose file',
            removeButtonText: 'Remove',
            dropzoneText: 'Drag and drop a file',
            selectedFileText: data => data.name,
            constraintText: 'Maximum file size: 5 MB. Supported formats: JPG, PNG, PDF.'
          }}
        />
        
        {file && !error && (
          <Alert type="success">
            File "{file.name}" ({(file.size / 1024).toFixed(1)} KB) is valid and ready for upload.
          </Alert>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### File Input with Image Preview

```jsx
import { FileInput, Container, Header, SpaceBetween, Box } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function FileInputWithImagePreview() {
  const [imageFile, setImageFile] = useState(null);
  const [preview, setPreview] = useState(null);
  
  useEffect(() => {
    // Clean up preview URL when component unmounts
    return () => {
      if (preview) {
        URL.revokeObjectURL(preview);
      }
    };
  }, []);
  
  const handleChange = ({ detail }) => {
    const file = detail.value;
    
    // Clean up previous preview
    if (preview) {
      URL.revokeObjectURL(preview);
    }
    
    if (file && file.type.startsWith('image/')) {
      setImageFile(file);
      // Create a preview URL
      setPreview(URL.createObjectURL(file));
    } else {
      setImageFile(file);
      setPreview(null);
    }
  };

  return (
    <Container header={<Header variant="h2">Image Upload with Preview</Header>}>
      <SpaceBetween size="l">
        <FileInput
          onChange={handleChange}
          value={imageFile}
          ariaLabel="Select image"
          accept="image/*"
          i18nStrings={{
            browseButtonText: 'Choose image',
            removeButtonText: 'Remove',
            dropzoneText: 'Drag and drop an image',
            selectedFileText: data => data.name,
            constraintText: 'Only image files are supported (JPG, PNG, GIF, etc.)'
          }}
        />
        
        {preview && (
          <Box padding="m" textAlign="center">
            <h3>Image Preview:</h3>
            <img 
              src={preview} 
              alt="Preview" 
              style={{ 
                maxWidth: '100%', 
                maxHeight: '300px',
                border: '1px solid #eaeded',
                borderRadius: '4px',
                padding: '8px'
              }}
            />
          </Box>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### File Input with Input Mode

```jsx
import { FileInput, Container, Header, SegmentedControl, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function FileInputWithInputMode() {
  const [file, setFile] = useState(null);
  const [inputMode, setInputMode] = useState('input');
  
  const handleChange = ({ detail }) => {
    setFile(detail.value);
  };
  
  const handleInputModeChange = ({ detail }) => {
    setInputMode(detail.selectedId);
  };

  return (
    <Container header={<Header variant="h2">File Input Modes</Header>}>
      <SpaceBetween size="l">
        <SegmentedControl
          selectedId={inputMode}
          onChange={handleInputModeChange}
          label="Input mode"
          options={[
            { id: 'input', text: 'Standard input' },
            { id: 'filedrop', text: 'File drop' }
          ]}
        />
        
        <FileInput
          onChange={handleChange}
          value={file}
          inputMode={inputMode}
          ariaLabel="Select file"
          accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
          i18nStrings={{
            browseButtonText: 'Choose file',
            removeButtonText: 'Remove',
            dropzoneText: 'Drag and drop a file',
            selectedFileText: data => data.name,
            constraintText: 'Supported formats: JPG, PNG, PDF, DOC, DOCX.'
          }}
        />
      </SpaceBetween>
    </Container>
  );
}
```

### File Input with Token Limit

```jsx
import { FileInput, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function FileInputWithTokenLimit() {
  const [files, setFiles] = useState([]);
  
  const handleChange = ({ detail }) => {
    setFiles(detail.value);
  };

  return (
    <Container header={<Header variant="h2">Multiple File Selection</Header>}>
      <FileInput
        onChange={handleChange}
        value={files}
        multiple={true}
        tokenLimit={3}
        showFileSize={true}
        ariaLabel="Select files"
        accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
        i18nStrings={{
          browseButtonText: 'Choose files',
          removeButtonText: 'Remove',
          dropzoneText: 'Drag and drop files',
          limitShowFewer: 'Show fewer files',
          limitShowMore: `Show ${Math.max(0, files.length - 3)} more files`,
          selectedFileText: (data, index) => `${data.name}`,
          constraintText: 'Supported formats: JPG, PNG, PDF, DOC, DOCX.'
        }}
      />
    </Container>
  );
}
```

### Complete Form with File Input

```jsx
import { 
  FileInput, 
  Container, 
  Header, 
  Form, 
  FormField, 
  Input, 
  Button, 
  SpaceBetween,
  Select,
  Alert
} from '@cloudscape-design/components';
import { useState } from 'react';

function CompleteFormWithFileInput() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    documentType: null,
    file: null
  });
  const [error, setError] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  
  const documentTypes = [
    { label: 'ID Card', value: 'id' },
    { label: 'Passport', value: 'passport' },
    { label: 'Driver License', value: 'license' },
    { label: 'Birth Certificate', value: 'birth' },
    { label: 'Other', value: 'other' }
  ];
  
  const handleFileChange = ({ detail }) => {
    setFormData(prev => ({ ...prev, file: detail.value }));
    setError(null);
  };
  
  const handleNameChange = ({ detail }) => {
    setFormData(prev => ({ ...prev, name: detail.value }));
  };
  
  const handleEmailChange = ({ detail }) => {
    setFormData(prev => ({ ...prev, email: detail.value }));
  };
  
  const handleDocumentTypeChange = ({ detail }) => {
    setFormData(prev => ({ ...prev, documentType: detail.selectedOption }));
  };
  
  const validateForm = () => {
    if (!formData.name.trim()) {
      return 'Name is required';
    }
    
    if (!formData.email.trim()) {
      return 'Email is required';
    }
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      return 'Please enter a valid email address';
    }
    
    if (!formData.documentType) {
      return 'Document type selection is required';
    }
    
    if (!formData.file) {
      return 'Document file is required';
    }
    
    // Validate file size (max 10 MB)
    if (formData.file.size > 10 * 1024 * 1024) {
      return 'File size exceeds the maximum limit of 10 MB';
    }
    
    return null;
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    
    const validationError = validateForm();
    if (validationError) {
      setError(validationError);
      setSubmitted(false);
      return;
    }
    
    // In a real application, you would submit the form data to your server here
    console.log('Form submitted:', formData);
    setSubmitted(true);
    setError(null);
  };

  return (
    <Container header={<Header variant="h2">Document Submission Form</Header>}>
      <form onSubmit={handleSubmit}>
        <Form
          actions={
            <SpaceBetween direction="horizontal" size="xs">
              <Button
                variant="link"
                onClick={() => {
                  setFormData({
                    name: '',
                    email: '',
                    documentType: null,
                    file: null
                  });
                  setError(null);
                  setSubmitted(false);
                }}
              >
                Cancel
              </Button>
              <Button variant="primary" formAction="submit">Submit</Button>
            </SpaceBetween>
          }
        >
          <SpaceBetween size="l">
            {error && (
              <Alert type="error" dismissible onDismiss={() => setError(null)}>
                {error}
              </Alert>
            )}
            
            {submitted && (
              <Alert type="success" dismissible onDismiss={() => setSubmitted(false)}>
                Document submitted successfully!
              </Alert>
            )}
            
            <FormField label="Full Name" description="Enter your full legal name">
              <Input
                value={formData.name}
                onChange={handleNameChange}
                placeholder="John Doe"
              />
            </FormField>
            
            <FormField label="Email Address" description="We'll use this to contact you about your submission">
              <Input
                value={formData.email}
                onChange={handleEmailChange}
                placeholder="john.doe@example.com"
                type="email"
              />
            </FormField>
            
            <FormField label="Document Type" description="Select the type of document you're uploading">
              <Select
                selectedOption={formData.documentType}
                onChange={handleDocumentTypeChange}
                options={documentTypes}
                placeholder="Choose a document type"
              />
            </FormField>
            
            <FormField
              label="Document File"
              description="Upload a clear, legible scan or photo of your document"
              constraintText="Maximum file size: 10 MB. Supported formats: JPG, PNG, PDF."
            >
              <FileInput
                onChange={handleFileChange}
                value={formData.file}
                ariaLabel="Select document"
                accept=".jpg,.jpeg,.png,.pdf"
                i18nStrings={{
                  browseButtonText: 'Choose file',
                  removeButtonText: 'Remove',
                  dropzoneText: 'Drag and drop your document',
                  selectedFileText: data => data.name,
                  constraintText: 'Maximum file size: 10 MB. Supported formats: JPG, PNG, PDF.'
                }}
              />
            </FormField>
          </SpaceBetween>
        </Form>
      </form>
    </Container>
  );
}
```

## Integration with Other Components

The FileInput component works well with these related components:

1. **FileUpload** - For a complete file uploading solution that includes FileInput
2. **FileDropzone** - For more customizable drag-and-drop file selection interfaces
3. **FileTokenGroup** - For displaying multiple selected files as tokens
4. **Form** and **FormField** - For integrating file inputs within forms
5. **Alert** - For displaying validation messages related to file selection
6. **Button** - For actions related to file submission
7. **ProgressBar** - For showing upload progress after file selection

## Accessibility

- Uses semantic HTML to ensure proper screen reader interpretation
- Provides keyboard accessible alternatives to drag and drop functionality
- Uses appropriate ARIA attributes for interactive elements
- Maintains focus management for form interactions
- Provides descriptive labels and instructions for assistive technologies
- Supports standard form validation patterns
- Allows customization of accessibility labels through i18nStrings

## Best Practices

1. Always provide clear constraints text to guide users on allowed file types and sizes
2. Use appropriate validation to prevent invalid file uploads
3. Show visual feedback when files are selected or removed
4. Provide meaningful error messages when validation fails
5. Use the multiple attribute when users need to select multiple files
6. Consider file size limits to prevent performance issues
7. Include file type validation for security and usability
8. Use appropriate input mode based on the context
9. Limit the number of visible tokens when displaying many files
10. Consider showing file size and last modified information for user reference
11. Integrate file inputs properly within forms with appropriate labels
12. Provide clear submission feedback after files are uploaded
13. Use consistent styling for all file input components in your application
14. Test with screen readers to ensure accessibility compliance
15. Optimize the component for both desktop and mobile experiences
