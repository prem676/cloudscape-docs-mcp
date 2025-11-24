## Alert Info

```jsx
import * as React from "react";
import Alert from "@cloudscape-design/components/alert";

export default () => {
  return (
    <Alert
      statusIconAriaLabel="Info"
      header="Known issues/limitations"
    >
      Review the documentation to learn about potential
      compatibility issues with specific database
      versions.
    </Alert>
  );
}
```

## Alert Success

```jsx
import * as React from "react";
import Alert from "@cloudscape-design/components/alert";

export default () => {
  return (
    <Alert
      dismissible
      statusIconAriaLabel="Success"
      type="success"
    >
      Your instance has been created successfully.
    </Alert>
  );
}
```

## Alert Error

```jsx
import * as React from "react";
import Alert from "@cloudscape-design/components/alert";

export default () => {
  return (
    <Alert
      statusIconAriaLabel="Error"
      type="error"
      header="Your instances could not be stopped"
    >
      Remove the instance from the load balancer before
      stopping it.
    </Alert>
  );
}
```

## Alert Warning

```jsx
import * as React from "react";
import Alert from "@cloudscape-design/components/alert";

export default () => {
  return (
    <Alert statusIconAriaLabel="Warning" type="warning">
      Changing the configuration might require stopping
      the instance.
    </Alert>
  );
}
```

## Alert with button

```jsx
import * as React from "react";
import Alert from "@cloudscape-design/components/alert";
import Button from "@cloudscape-design/components/button";

export default () => {
  return (
    <Alert
      statusIconAriaLabel="Info"
      action={<Button>Enable versioning</Button>}
      header="Versioning is not enabled"
    >
      Versioning is not enabled for objects in bucket
      [IAM-user].
    </Alert>
  );
}
```
