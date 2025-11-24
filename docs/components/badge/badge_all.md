# Badge component

A small, color-coded visual element that contains letters or numbers, that is used to label, categorize, organize, or indicate severity of items.

## Code

### Gray

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge>20</Badge>;
}
```

### Blue


```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge color="blue">52430</Badge>;
}
```

### Red

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge color="red">EC2 key pair</Badge>;
}
```

### Green

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge color="green">Application</Badge>;
}
```

### Critical Severity

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return (
    <Badge color="severity-critical">Critical</Badge>
  );
}
```

### High Severity

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge color="severity-high">High</Badge>;
}
```

### Medium Severity

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge color="severity-medium">Medium</Badge>;
}
```

### Neutral Severity

```jsx
import * as React from "react";
import Badge from "@cloudscape-design/components/badge";

export default () => {
  return <Badge color="severity-neutral">Neutral</Badge>;
}
```

