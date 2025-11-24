# File Dropzone

The FileDropzone component provides a dedicated area for users to drag and drop files for upload. It offers a visually intuitive way to upload files, complementing the standard file selection dialog.

## Import

```jsx
import { FileDropzone } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { FileDropzone } from '@cloudscape-design/components';

function BasicFileDropzone() {
  const handleDropzoneChange = ({ detail }) => {
    console.log('Files added:', detail.files);
  };

  return (
    <FileDropzone
      onChange={handleDropzoneChange}
      accept=".jpg,.jpeg,.png,.pdf"
      i18nStrings={{
        dropzoneHeader: 'Drag and drop files',
        dropzoneHeaderDragging: 'Drop files to upload',
        uploadButtonText: 'Upload files'
      }}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `onChange` | (event: { detail: { files: File[] } }) => void | Event handler called when files are added |
| `accept` | string | File types that the dropzone accepts (comma-separated MIME types or extensions) |
| `multiple` | boolean | Whether multiple files can be selected |
| `disabled` | boolean | Whether the dropzone is disabled |
| `constraints` | ReactNode | Text that describes file constraints |
| `header` | ReactNode | Custom header text for the dropzone |
| `i18nStrings` | object | Internationalization strings |
| `hideUploadButton` | boolean | Whether to hide the upload button |
| `showFileSize` | boolean | Whether to show file size information |
| `maxFileSize` | number | Maximum allowed file size in bytes |
| `maxFilesCount` | number | Maximum number of files that can be uploaded |

## Examples

### File Dropzone with Constraints

```jsx
import { FileDropzone, Container, Header } from '@cloudscape-design/components';

function FileDropzoneWithConstraints() {
  const handleDropzoneChange = ({ detail }) => {
    console.log('Files added:', detail.files);
  };

  return (
    <Container header={<Header variant="h2">Upload Documents</Header>}>
      <FileDropzone
        onChange={handleDropzoneChange}
        accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
        multiple={true}
        constraints="Maximum file size: 10 MB. Supported formats: JPG, PNG, PDF, DOC, DOCX."
        i18nStrings={{
          dropzoneHeader: 'Drag and drop files',
          dropzoneHeaderDragging: 'Drop files to upload',
          dropzoneHeaderMultiple: 'Drag and drop files',
          dropzoneHeaderMultipleDragging: 'Drop files to upload',
          uploadButtonText: 'Choose files',
          removeFileAriaLabel: file => `Remove ${file.name}`
        }}
      />
    </Container>
  );
}
```

### File Dropzone with Size Limits

```jsx
import { FileDropzone, Container, Header, Alert, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function FileDropzoneWithSizeLimits() {
  const [files, setFiles] = useState([]);
  const [error, setError] = useState(null);
  
  // 10 MB size limit
  const MAX_FILE_SIZE = 10 * 1024 * 1024;
  
  const handleDropzoneChange = ({ detail }) => {
    const oversizedFiles = detail.files.filter(file => file.size > MAX_FILE_SIZE);
    
    if (oversizedFiles.length > 0) {
      setError(`The following files exceed the 10 MB size limit: ${oversizedFiles.map(f => f.name).join(', ')}`);
      
      // Filter out oversized files
      const validFiles = detail.files.filter(file => file.size <= MAX_FILE_SIZE);
      setFiles(prevFiles => [...prevFiles, ...validFiles]);
    } else {
      setError(null);
      setFiles(prevFiles => [...prevFiles, ...detail.files]);
    }
  };

  return (
    <Container header={<Header variant="h2">Upload with Size Limits</Header>}>
      <SpaceBetween size="m">
        {error && (
          <Alert type="error" dismissible onDismiss={() => setError(null)}>
            {error}
          </Alert>
        )}
        
        <FileDropzone
          onChange={handleDropzoneChange}
          accept=".jpg,.jpeg,.png,.pdf"
          multiple={true}
          constraints="Maximum file size: 10 MB. Supported formats: JPG, PNG, PDF."
          maxFileSize={MAX_FILE_SIZE}
          showFileSize={true}
          i18nStrings={{
            dropzoneHeader: 'Drag and drop files',
            dropzoneHeaderDragging: 'Drop files to upload',
            uploadButtonText: 'Choose files'
          }}
        />
        
        {files.length > 0 && (
          <div>
            <h3>Selected files:</h3>
            <ul>
              {files.map((file, index) => (
                <li key={index}>
                  {file.name} - {(file.size / 1024 / 1024).toFixed(2)} MB
                </li>
              ))}
            </ul>
          </div>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### File Dropzone with File Type Validation

```jsx
import { FileDropzone, Container, Header, Alert, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function FileDropzoneWithTypeValidation() {
  const [files, setFiles] = useState([]);
  const [error, setError] = useState(null);
  
  const ACCEPTED_TYPES = ['.jpg', '.jpeg', '.png', '.pdf'];
  
  const handleDropzoneChange = ({ detail }) => {
    const invalidFiles = detail.files.filter(file => {
      const extension = '.' + file.name.split('.').pop().toLowerCase();
      return !ACCEPTED_TYPES.includes(extension);
    });
    
    if (invalidFiles.length > 0) {
      setError(`The following files have unsupported formats: ${invalidFiles.map(f => f.name).join(', ')}`);
      
      // Filter out invalid files
      const validFiles = detail.files.filter(file => {
        const extension = '.' + file.name.split('.').pop().toLowerCase();
        return ACCEPTED_TYPES.includes(extension);
      });
      
      setFiles(prevFiles => [...prevFiles, ...validFiles]);
    } else {
      setError(null);
      setFiles(prevFiles => [...prevFiles, ...detail.files]);
    }
  };

  return (
    <Container header={<Header variant="h2">Upload with Type Validation</Header>}>
      <SpaceBetween size="m">
        {error && (
          <Alert type="error" dismissible onDismiss={() => setError(null)}>
            {error}
          </Alert>
        )}
        
        <FileDropzone
          onChange={handleDropzoneChange}
          accept=".jpg,.jpeg,.png,.pdf"
          multiple={true}
          constraints="Supported formats: JPG, PNG, PDF."
          i18nStrings={{
            dropzoneHeader: 'Drag and drop files',
            dropzoneHeaderDragging: 'Drop files to upload',
            uploadButtonText: 'Choose files'
          }}
        />
        
        {files.length > 0 && (
          <div>
            <h3>Selected files:</h3>
            <ul>
              {files.map((file, index) => (
                <li key={index}>{file.name}</li>
              ))}
            </ul>
          </div>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

### File Dropzone with Custom Header

```jsx
import { FileDropzone, Container, Header, Box, Icon } from '@cloudscape-design/components';

function FileDropzoneWithCustomHeader() {
  const handleDropzoneChange = ({ detail }) => {
    console.log('Files added:', detail.files);
  };

  const CustomHeader = () => (
    <Box textAlign="center">
      <Box fontSize="heading-m" fontWeight="bold" padding={{ bottom: 's' }}>
        <Icon name="upload" size="medium" /> Upload Your Data Files
      </Box>
      <Box fontSize="body-m" color="text-body-secondary">
        Drag and drop CSV, Excel, or JSON files to begin analysis
      </Box>
    </Box>
  );

  return (
    <Container header={<Header variant="h2">Data Import</Header>}>
      <FileDropzone
        onChange={handleDropzoneChange}
        accept=".csv,.xlsx,.json"
        multiple={true}
        header={<CustomHeader />}
        constraints="Maximum file size: 50 MB. Supported formats: CSV, Excel, JSON."
        i18nStrings={{
          dropzoneHeaderDragging: 'Drop files to begin analysis',
          uploadButtonText: 'Select data files'
        }}
      />
    </Container>
  );
}
```

### File Dropzone with Progress Tracking

```jsx
import { FileDropzone, Container, Header, ProgressBar, SpaceBetween, Button } from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function FileDropzoneWithProgressTracking() {
  const [files, setFiles] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  
  useEffect(() => {
    let timer;
    if (uploading && uploadProgress < 100) {
      timer = setTimeout(() => {
        setUploadProgress(prev => Math.min(prev + 10, 100));
      }, 500);
    } else if (uploadProgress >= 100) {
      setUploading(false);
    }
    
    return () => clearTimeout(timer);
  }, [uploading, uploadProgress]);
  
  const handleDropzoneChange = ({ detail }) => {
    setFiles(prevFiles => [...prevFiles, ...detail.files]);
  };
  
  const handleUpload = () => {
    if (files.length > 0) {
      setUploading(true);
      setUploadProgress(0);
      // In a real application, you would upload the files to your server here
    }
  };
  
  const handleReset = () => {
    setFiles([]);
    setUploading(false);
    setUploadProgress(0);
  };

  return (
    <Container header={<Header variant="h2">File Upload with Progress</Header>}>
      <SpaceBetween size="m">
        <FileDropzone
          onChange={handleDropzoneChange}
          accept=".jpg,.jpeg,.png,.pdf"
          multiple={true}
          constraints="Supported formats: JPG, PNG, PDF."
          hideUploadButton={true}
          disabled={uploading}
          i18nStrings={{
            dropzoneHeader: uploading ? 'Upload in progress...' : 'Drag and drop files',
            dropzoneHeaderDragging: 'Drop files to upload'
          }}
        />
        
        {files.length > 0 && !uploading && (
          <div>
            <h3>Selected files ({files.length}):</h3>
            <ul>
              {files.map((file, index) => (
                <li key={index}>{file.name}</li>
              ))}
            </ul>
          </div>
        )}
        
        {uploading && (
          <ProgressBar
            value={uploadProgress}
            label="Uploading files"
            description={`Uploading ${files.length} file${files.length !== 1 ? 's' : ''}`}
            additionalInfo={`${uploadProgress}%`}
          />
        )}
        
        <SpaceBetween direction="horizontal" size="xs">
          <Button onClick={handleUpload} disabled={files.length === 0 || uploading}>
            Upload
          </Button>
          <Button onClick={handleReset} disabled={files.length === 0 && !uploading}>
            Reset
          </Button>
        </SpaceBetween>
      </SpaceBetween>
    </Container>
  );
}
```

### File Dropzone with Drag State Styling

```jsx
import { FileDropzone, Container, Header, Box } from '@cloudscape-design/components';
import { useState } from 'react';

function FileDropzoneWithDragStateStyling() {
  const [isDragging, setIsDragging] = useState(false);
  
  const handleDropzoneChange = ({ detail }) => {
    console.log('Files added:', detail.files);
    setIsDragging(false);
  };
  
  // Custom styling wrapper for drag state
  const DropzoneWrapper = ({ children }) => (
    <Box
      padding="m"
      borderRadius="default"
      border={isDragging ? "active" : "divider-standard"}
      bgcolor={isDragging ? "background.notification.info" : "background.container"}
      color={isDragging ? "text.interactive.default" : "text.body-default"}
      onDragEnter={() => setIsDragging(true)}
      onDragLeave={() => setIsDragging(false)}
      onDrop={() => setIsDragging(false)}
    >
      {children}
    </Box>
  );

  return (
    <Container header={<Header variant="h2">Interactive File Dropzone</Header>}>
      <DropzoneWrapper>
        <FileDropzone
          onChange={handleDropzoneChange}
          accept=".jpg,.jpeg,.png,.pdf"
          multiple={true}
          i18nStrings={{
            dropzoneHeader: 'Drag and drop files',
            dropzoneHeaderDragging: 'Release to upload files',
            uploadButtonText: 'Choose files'
          }}
        />
      </DropzoneWrapper>
    </Container>
  );
}
```

### File Dropzone with Image Preview

```jsx
import { FileDropzone, Container, Header, SpaceBetween, Box, Button, Grid } from '@cloudscape-design/components';
import { useState } from 'react';

function FileDropzoneWithImagePreview() {
  const [files, setFiles] = useState([]);
  const [previews, setPreviews] = useState([]);
  
  const handleDropzoneChange = ({ detail }) => {
    // Filter only image files
    const imageFiles = detail.files.filter(file => file.type.startsWith('image/'));
    setFiles(prevFiles => [...prevFiles, ...imageFiles]);
    
    // Generate previews for each image
    imageFiles.forEach(file => {
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviews(prevPreviews => [
          ...prevPreviews,
          { file: file, url: reader.result }
        ]);
      };
      reader.readAsDataURL(file);
    });
  };
  
  const handleRemovePreview = (fileToRemove) => {
    setPreviews(prevPreviews => prevPreviews.filter(preview => preview.file !== fileToRemove));
    setFiles(prevFiles => prevFiles.filter(file => file !== fileToRemove));
  };

  return (
    <Container header={<Header variant="h2">Image Upload with Previews</Header>}>
      <SpaceBetween size="l">
        <FileDropzone
          onChange={handleDropzoneChange}
          accept="image/*"
          multiple={true}
          constraints="Only image files are supported (JPG, PNG, GIF, etc.)"
          i18nStrings={{
            dropzoneHeader: 'Drag and drop images',
            dropzoneHeaderDragging: 'Drop images to upload',
            uploadButtonText: 'Choose images'
          }}
        />
        
        {previews.length > 0 && (
          <div>
            <h3>Image Previews:</h3>
            <Grid
              gridDefinition={[
                { colspan: { default: 12, xxs: 6, xs: 4, s: 3, m: 3, l: 2, xl: 2 } }
              ]}
            >
              {previews.map((preview, index) => (
                <Box
                  key={index}
                  padding="s"
                  textAlign="center"
                >
                  <Box
                    padding="s"
                    border="divider-standard"
                    borderRadius="default"
                    marginBottom="s"
                  >
                    <img
                      src={preview.url}
                      alt={`Preview of ${preview.file.name}`}
                      style={{
                        maxWidth: '100%',
                        maxHeight: '150px',
                        objectFit: 'contain'
                      }}
                    />
                  </Box>
                  <Box fontSize="body-s" textAlign="center" marginBottom="s">
                    {preview.file.name.length > 20
                      ? preview.file.name.substring(0, 17) + '...'
                      : preview.file.name}
                  </Box>
                  <Button
                    variant="link"
                    onClick={() => handleRemovePreview(preview.file)}
                  >
                    Remove
                  </Button>
                </Box>
              ))}
            </Grid>
          </div>
        )}
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Other Components

The FileDropzone component works well with these related components:

1. **FileUpload** - For a complete file uploading solution
2. **FileInput** - For simple file input functionality
3. **FileTokenGroup** - For displaying selected files as tokens
4. **ProgressBar** - For showing upload progress
5. **Alert** - For displaying validation errors
6. **Button** - For action controls related to uploading
7. **Container** - For properly framing the upload area

## Accessibility

- Uses ARIA attributes to ensure proper screen reader interpretation
- Provides keyboard accessible alternatives to drag and drop functionality
- Announces status changes to screen readers
- Ensures proper focus management for interactive elements
- Uses appropriate color contrast for visibility
- Provides text alternatives for icons and visual elements

## Best Practices

1. Always provide clear constraints text to guide users on allowed file types and sizes
2. Use appropriate validation to prevent invalid file uploads
3. Show progress indicators for long-running uploads
4. Provide meaningful error messages when validation fails
5. Use visual cues to indicate when files are being dragged over the dropzone
6. Consider providing previews for uploaded images when appropriate
7. Include a button alternative for users who cannot use drag and drop
8. Limit the maximum file size to prevent performance issues
9. Consider using file type validation for security and usability
10. Provide feedback when files are successfully uploaded
11. Use consistent styling for all file upload components in your application
12. Consider the appropriate size of the dropzone based on its importance
13. Test with screen readers to ensure accessibility compliance
14. Use appropriate internationalization strings for global users
15. Optimize the dropzone for both desktop and mobile experiences
