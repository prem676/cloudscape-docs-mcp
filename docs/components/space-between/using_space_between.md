# Space between 
A helper component that helps you add consistent spacing between elements on your page.

## space between with buttons

```jsx
import * as React from "react";
import SpaceBetween from "@cloudscape-design/components/space-between";
import Button from "@cloudscape-design/components/button";

export default () => {
  return (
    <SpaceBetween direction="horizontal" size="xs">
      <Button>Edit</Button>
      <Button>Delete</Button>
      <Button variant="primary">
        Create distribution
      </Button>
    </SpaceBetween>
  );
}
```

## space between with containers

```jsx
import * as React from "react";
import SpaceBetween from "@cloudscape-design/components/space-between";
import Container from "@cloudscape-design/components/container";
import Header from "@cloudscape-design/components/header";

export default () => {
  return (
    <SpaceBetween size="l">
      <Container
        header={
          <Header variant="h2">
            Distribution settings
          </Header>
        }
      >
        Container content
      </Container>
      <Container
        header={
          <Header variant="h2">
            Cache behaviour settings
          </Header>
        }
      >
        Container content
      </Container>
      <Container
        header={
          <Header variant="h2">Container title</Header>
        }
      >
        Container content
      </Container>
    </SpaceBetween>
  );
}
```

## space between with form fields

```jsx
import * as React from "react";
import SpaceBetween from "@cloudscape-design/components/space-between";
import FormField from "@cloudscape-design/components/form-field";
import Input from "@cloudscape-design/components/input";

export default () => {
  return (
    <SpaceBetween size="l">
      <FormField
        label="S3 bucket for logs"
        description="The Amazon S3 bucket that you want CloudFront to store your access logs in."
      >
        <Input placeholder="Choose an S3 bucket" />
      </FormField>

      <FormField
        stretch={true}
        label={
          <span id="certificate-expiry-label">
            Certificate expiry
          </span>
        }
        description="Specify the date and time when the certificate should expire."
      >
        <SpaceBetween size="s" direction="horizontal">
          <FormField stretch={true}>
            <Input
              ariaLabelledby="certificate-expiry-label"
              placeholder="YYYY/MM/DD"
            />
          </FormField>
          <FormField
            stretch={true}
            constraintText="Use 24-hour format."
          >
            <Input
              ariaLabelledby="certificate-expiry-label"
              placeholder="hh:mm:ss"
            />
          </FormField>
        </SpaceBetween>
      </FormField>
    </SpaceBetween>
  );
}
```

## space between nested

```jsx
import * as React from "react";
import SpaceBetween from "@cloudscape-design/components/space-between";

export default () => {
  return (
    <SpaceBetween direction="horizontal" size="l">
      <SpaceBetween size="xs">
        <div>Content one</div>
        <div>Content two</div>
        <div>Content three</div>
      </SpaceBetween>

      <SpaceBetween size="s">
        <div>Content four</div>
        <div>Content five</div>
      </SpaceBetween>

      <SpaceBetween size="m">
        <div>Content six</div>
        <div>Content seven</div>
        <div>Content eight</div>
      </SpaceBetween>
    </SpaceBetween>
  );
}
```