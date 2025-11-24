# File Token Group

The FileTokenGroup component displays files as interactive tokens, allowing users to view and manage selected files before or after upload. It provides a compact representation of file selections with options for removal and status indication.

## Import

```jsx
import { FileTokenGroup } from '@cloudscape-design/components';
```

## Basic Usage

```jsx
import { FileTokenGroup } from '@cloudscape-design/components';
import { useState } from 'react';

function BasicFileTokenGroup() {
  const [files, setFiles] = useState([
    { name: 'document.pdf', size: 2500000, type: 'application/pdf' }
  ]);
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    setFiles(prevFiles => {
      const newFiles = [...prevFiles];
      newFiles.splice(itemIndex, 1);
      return newFiles;
    });
  };

  return (
    <FileTokenGroup
      items={files.map(file => ({ label: file.name, iconName: 'file' }))}
      onDismiss={handleDismiss}
      i18nStrings={{
        limitShowFewer: 'Show fewer files',
        limitShowMore: 'Show more files'
      }}
    />
  );
}
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `items` | Array<{ label: string, description?: string, iconName?: string, iconUrl?: string, iconAlt?: string, tags?: Array<{ label: string, color?: string }>, disabled?: boolean, status?: 'loading' \| 'finished' \| 'error', errorText?: string }> | Array of file tokens to display |
| `onDismiss` | (event: { detail: { itemIndex: number } }) => void | Event handler called when a file token is dismissed |
| `i18nStrings` | object | Internationalization strings |
| `alignment` | 'horizontal' \| 'vertical' | Alignment of the file tokens |
| `limit` | number | Maximum number of file tokens to display before showing a "Show more" button |
| `showFileSize` | boolean | Whether to show file size as a tag on each token |
| `fileGroupId` | string | Unique identifier for the file group for ARIA attributes |
| `dismissLabel` | string | Accessible label for dismiss buttons |

## Examples

### File Token Group with File Types and Sizes

```jsx
import { FileTokenGroup, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function FileTokenGroupWithTypeAndSize() {
  const [files, setFiles] = useState([
    { name: 'document.pdf', size: 1500000, type: 'application/pdf' },
    { name: 'image.jpg', size: 3200000, type: 'image/jpeg' },
    { name: 'spreadsheet.xlsx', size: 950000, type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }
  ]);
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    setFiles(prevFiles => {
      const newFiles = [...prevFiles];
      newFiles.splice(itemIndex, 1);
      return newFiles;
    });
  };
  
  const getIconNameForFile = (file) => {
    if (file.type.includes('pdf')) return 'file-pdf';
    if (file.type.includes('image')) return 'file-image';
    if (file.type.includes('spreadsheet') || file.type.includes('excel')) return 'file-excel';
    if (file.type.includes('word')) return 'file-word';
    return 'file';
  };
  
  const formatFileSize = (bytes) => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">Selected Files</Header>}>
      <FileTokenGroup
        items={files.map(file => ({
          label: file.name,
          iconName: getIconNameForFile(file),
          tags: [{ label: formatFileSize(file.size) }]
        }))}
        onDismiss={handleDismiss}
        i18nStrings={{
          limitShowFewer: 'Show fewer files',
          limitShowMore: 'Show more files'
        }}
      />
    </Container>
  );
}
```

### File Token Group with Upload Status

```jsx
import { FileTokenGroup, Container, Header, Button, SpaceBetween } from '@cloudscape-design/components';
import { useState } from 'react';

function FileTokenGroupWithUploadStatus() {
  const initialFiles = [
    { name: 'document1.pdf', size: 1500000, type: 'application/pdf', status: 'pending' },
    { name: 'document2.pdf', size: 2500000, type: 'application/pdf', status: 'pending' },
    { name: 'image.jpg', size: 3200000, type: 'image/jpeg', status: 'pending' }
  ];
  
  const [files, setFiles] = useState(initialFiles);
  const [uploading, setUploading] = useState(false);
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    if (!uploading) {
      setFiles(prevFiles => {
        const newFiles = [...prevFiles];
        newFiles.splice(itemIndex, 1);
        return newFiles;
      });
    }
  };
  
  const simulateUpload = () => {
    setUploading(true);
    
    // Update each file status sequentially
    let currentIndex = 0;
    
    const updateNextFile = () => {
      if (currentIndex < files.length) {
        setFiles(prevFiles => {
          const newFiles = [...prevFiles];
          newFiles[currentIndex] = { ...newFiles[currentIndex], status: 'loading' };
          return newFiles;
        });
        
        // Simulate upload time
        setTimeout(() => {
          // Randomly succeed or fail for demonstration
          const success = Math.random() > 0.3;
          
          setFiles(prevFiles => {
            const newFiles = [...prevFiles];
            newFiles[currentIndex] = { 
              ...newFiles[currentIndex], 
              status: success ? 'finished' : 'error',
              errorText: success ? undefined : 'Upload failed. Try again.'
            };
            return newFiles;
          });
          
          currentIndex++;
          updateNextFile();
        }, 1500);
      } else {
        setUploading(false);
      }
    };
    
    updateNextFile();
  };
  
  const resetFiles = () => {
    setFiles(initialFiles);
    setUploading(false);
  };
  
  return (
    <Container header={<Header variant="h2">File Upload Status</Header>}>
      <SpaceBetween size="m">
        <FileTokenGroup
          items={files.map(file => ({
            label: file.name,
            iconName: 'file',
            tags: [{ label: (file.size / (1024 * 1024)).toFixed(1) + ' MB' }],
            status: file.status === 'loading' ? 'loading' : 
                   file.status === 'finished' ? 'finished' : 
                   file.status === 'error' ? 'error' : undefined,
            errorText: file.errorText
          }))}
          onDismiss={handleDismiss}
          i18nStrings={{
            limitShowFewer: 'Show fewer files',
            limitShowMore: 'Show more files'
          }}
        />
        
        <SpaceBetween direction="horizontal" size="xs">
          <Button onClick={simulateUpload} disabled={uploading || files.length === 0}>
            Upload Files
          </Button>
          <Button onClick={resetFiles} disabled={uploading}>
            Reset
          </Button>
        </SpaceBetween>
      </SpaceBetween>
    </Container>
  );
}
```

### Vertical File Token Group

```jsx
import { FileTokenGroup, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function VerticalFileTokenGroup() {
  const [files, setFiles] = useState([
    { name: 'annual-report-2023.pdf', size: 5500000, type: 'application/pdf' },
    { name: 'financial-summary.xlsx', size: 2800000, type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' },
    { name: 'presentation.pptx', size: 6200000, type: 'application/vnd.openxmlformats-officedocument.presentationml.presentation' },
    { name: 'contract.docx', size: 1800000, type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' }
  ]);
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    setFiles(prevFiles => {
      const newFiles = [...prevFiles];
      newFiles.splice(itemIndex, 1);
      return newFiles;
    });
  };
  
  const getIconNameForFile = (file) => {
    if (file.type.includes('pdf')) return 'file-pdf';
    if (file.type.includes('spreadsheet') || file.type.includes('excel')) return 'file-excel';
    if (file.type.includes('presentation') || file.type.includes('powerpoint')) return 'file-powerpoint';
    if (file.type.includes('word') || file.type.includes('document')) return 'file-word';
    return 'file';
  };
  
  const formatFileSize = (bytes) => {
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">Document Repository</Header>}>
      <FileTokenGroup
        alignment="vertical"
        items={files.map(file => ({
          label: file.name,
          description: `Last modified: ${new Date().toLocaleDateString()}`,
          iconName: getIconNameForFile(file),
          tags: [{ label: formatFileSize(file.size) }]
        }))}
        onDismiss={handleDismiss}
        i18nStrings={{
          limitShowFewer: 'Show fewer documents',
          limitShowMore: 'Show more documents'
        }}
      />
    </Container>
  );
}
```

### File Token Group with Limited Display

```jsx
import { FileTokenGroup, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function LimitedFileTokenGroup() {
  const [files, setFiles] = useState([
    { name: 'image1.jpg', size: 1500000, type: 'image/jpeg' },
    { name: 'image2.jpg', size: 2200000, type: 'image/jpeg' },
    { name: 'image3.jpg', size: 1800000, type: 'image/jpeg' },
    { name: 'image4.jpg', size: 2500000, type: 'image/jpeg' },
    { name: 'image5.jpg', size: 3200000, type: 'image/jpeg' },
    { name: 'image6.jpg', size: 2800000, type: 'image/jpeg' },
    { name: 'image7.jpg', size: 1900000, type: 'image/jpeg' },
    { name: 'image8.jpg', size: 2700000, type: 'image/jpeg' }
  ]);
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    setFiles(prevFiles => {
      const newFiles = [...prevFiles];
      newFiles.splice(itemIndex, 1);
      return newFiles;
    });
  };
  
  const formatFileSize = (bytes) => {
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">Image Gallery</Header>}>
      <FileTokenGroup
        items={files.map(file => ({
          label: file.name,
          iconName: 'file-image',
          tags: [{ label: formatFileSize(file.size) }]
        }))}
        onDismiss={handleDismiss}
        limit={4}
        i18nStrings={{
          limitShowFewer: 'Show fewer images',
          limitShowMore: `Show ${files.length - 4} more images`
        }}
      />
    </Container>
  );
}
```

### File Token Group with Custom Tags

```jsx
import { FileTokenGroup, Container, Header } from '@cloudscape-design/components';
import { useState } from 'react';

function FileTokenGroupWithCustomTags() {
  const [files, setFiles] = useState([
    { 
      name: 'report.pdf', 
      size: 2500000, 
      type: 'application/pdf',
      status: 'approved',
      department: 'finance'
    },
    { 
      name: 'contract.docx', 
      size: 1800000, 
      type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      status: 'pending',
      department: 'legal'
    },
    { 
      name: 'presentation.pptx', 
      size: 6200000, 
      type: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
      status: 'approved',
      department: 'marketing'
    }
  ]);
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    setFiles(prevFiles => {
      const newFiles = [...prevFiles];
      newFiles.splice(itemIndex, 1);
      return newFiles;
    });
  };
  
  const getIconNameForFile = (file) => {
    if (file.type.includes('pdf')) return 'file-pdf';
    if (file.type.includes('spreadsheet') || file.type.includes('excel')) return 'file-excel';
    if (file.type.includes('presentation') || file.type.includes('powerpoint')) return 'file-powerpoint';
    if (file.type.includes('word') || file.type.includes('document')) return 'file-word';
    return 'file';
  };
  
  const getStatusColor = (status) => {
    if (status === 'approved') return 'green';
    if (status === 'pending') return 'blue';
    if (status === 'rejected') return 'red';
    return 'grey';
  };
  
  const getDepartmentColor = (department) => {
    if (department === 'finance') return 'blue';
    if (department === 'legal') return 'purple';
    if (department === 'marketing') return 'orange';
    if (department === 'hr') return 'green';
    return 'grey';
  };
  
  const formatFileSize = (bytes) => {
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">Document Management</Header>}>
      <FileTokenGroup
        items={files.map(file => ({
          label: file.name,
          iconName: getIconNameForFile(file),
          tags: [
            { label: formatFileSize(file.size) },
            { label: file.status, color: getStatusColor(file.status) },
            { label: file.department, color: getDepartmentColor(file.department) }
          ]
        }))}
        onDismiss={handleDismiss}
        i18nStrings={{
          limitShowFewer: 'Show fewer documents',
          limitShowMore: 'Show more documents'
        }}
      />
    </Container>
  );
}
```

### Complete File Upload with FileTokenGroup

```jsx
import { 
  FileTokenGroup, 
  FileUpload, 
  Container, 
  Header, 
  SpaceBetween, 
  Button, 
  ProgressBar 
} from '@cloudscape-design/components';
import { useState, useEffect } from 'react';

function CompleteFileUploadWithTokens() {
  const [files, setFiles] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  
  useEffect(() => {
    let timer;
    if (uploading && uploadProgress < 100) {
      timer = setTimeout(() => {
        setUploadProgress(prev => {
          const newProgress = prev + 5;
          
          // When reaching 100%, update file statuses to finished
          if (newProgress >= 100) {
            setFiles(prevFiles => 
              prevFiles.map(file => ({
                ...file,
                status: 'uploaded'
              }))
            );
            setUploading(false);
          }
          
          return Math.min(newProgress, 100);
        });
      }, 300);
    }
    
    return () => clearTimeout(timer);
  }, [uploading, uploadProgress]);
  
  const handleFileChange = ({ detail }) => {
    const newFiles = detail.value.map(file => ({
      name: file.name,
      size: file.size,
      type: file.type,
      status: 'ready',
      file: file // Store the actual file object
    }));
    
    setFiles(newFiles);
    setUploadProgress(0);
  };
  
  const handleDismiss = ({ detail: { itemIndex } }) => {
    if (!uploading) {
      setFiles(prevFiles => {
        const newFiles = [...prevFiles];
        newFiles.splice(itemIndex, 1);
        return newFiles;
      });
    }
  };
  
  const handleUpload = () => {
    if (files.length > 0 && !uploading) {
      setUploading(true);
      setUploadProgress(0);
      // In a real application, you would upload the files to your server here
    }
  };
  
  const handleReset = () => {
    if (!uploading) {
      setFiles([]);
      setUploadProgress(0);
    }
  };
  
  const getIconNameForFile = (file) => {
    if (file.type.includes('pdf')) return 'file-pdf';
    if (file.type.includes('image')) return 'file-image';
    if (file.type.includes('spreadsheet') || file.type.includes('excel')) return 'file-excel';
    if (file.type.includes('presentation') || file.type.includes('powerpoint')) return 'file-powerpoint';
    if (file.type.includes('word') || file.type.includes('document')) return 'file-word';
    if (file.type.includes('text') || file.type.includes('txt')) return 'file-text';
    return 'file';
  };
  
  const formatFileSize = (bytes) => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <Container header={<Header variant="h2">File Upload Manager</Header>}>
      <SpaceBetween size="l">
        <FileUpload
          onChange={handleFileChange}
          value={files.map(file => file.file)}
          multiple={true}
          accept=".jpg,.jpeg,.png,.pdf,.doc,.docx,.xlsx,.pptx"
          constraintText="Maximum file size: 10 MB. Supported formats: JPG, PNG, PDF, DOC, DOCX, XLSX, PPTX."
          i18nStrings={{
            uploadButtonText: 'Choose files',
            dropzoneText: 'Drag and drop files',
            removeFileAriaLabel: file => `Remove ${file.name}`
          }}
        />
        
        {files.length > 0 && (
          <div>
            <Header variant="h3">Selected Files</Header>
            <FileTokenGroup
              items={files.map(file => ({
                label: file.name,
                iconName: getIconNameForFile(file),
                tags: [
                  { label: formatFileSize(file.size) },
                  { 
                    label: file.status === 'uploaded' ? 'Uploaded' : 
                           file.status === 'ready' ? 'Ready' : 'Processing',
                    color: file.status === 'uploaded' ? 'green' : 
                           file.status === 'ready' ? 'blue' : 'grey'
                  }
                ],
                status: uploading ? 'loading' : undefined
              }))}
              onDismiss={handleDismiss}
              i18nStrings={{
                limitShowFewer: 'Show fewer files',
                limitShowMore: 'Show more files'
              }}
            />
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
          <Button onClick={handleReset} disabled={files.length === 0 || uploading}>
            Reset
          </Button>
        </SpaceBetween>
      </SpaceBetween>
    </Container>
  );
}
```

## Integration with Other Components

The FileTokenGroup component works well with these related components:

1. **FileUpload** - For selecting files and displaying them as tokens
2. **FileDropzone** - For drag-and-drop file selection before displaying as tokens
3. **FileInput** - For simple file input that can feed into tokens
4. **ProgressBar** - For showing upload progress of files in tokens
5. **Button** - For actions related to file management
6. **Container** - For properly framing the file token display
7. **Alert** - For displaying messages related to file operations

## Accessibility

- Uses appropriate ARIA attributes for interactive elements
- Provides keyboard navigation for token interactions
- Ensures focus management for dismissible tokens
- Uses proper color contrast for visibility of tags and status indicators
- Supports screen reader announcements for token changes
- Allows customization of accessibility labels through i18nStrings

## Best Practices

1. Provide clear visual indication of file types through appropriate icons
2. Include file size information as tags for user reference
3. Use status indicators to show upload progress and completion
4. Group related files together with consistent styling
5. Limit the number of visible tokens when displaying many files
6. Consider using vertical alignment for detailed file information
7. Include error states and messages for failed uploads
8. Allow users to dismiss tokens for files they no longer need
9. Use custom tags to provide additional context about files
10. Maintain consistent styling across all file management components
11. Consider mobile responsiveness when designing token layouts
12. Provide clear feedback when files are successfully uploaded
13. Use appropriate tag colors to indicate file status or categorization
14. Test with screen readers to ensure accessibility compliance
15. Consider internationalization requirements for different languages
