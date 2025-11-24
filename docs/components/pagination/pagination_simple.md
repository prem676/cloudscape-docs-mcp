---
title: "Pagination - Cloudscape Design System"
source: "https://cloudscape.design/components/pagination/?tabId=playground"
created: 2025-10-01
description: "Provides horizontal navigation between pages of a collection."
---

## code

```jsx
import * as React from "react";
import Pagination from "@cloudscape-design/components/pagination";

export default () => {
  const [
    currentPageIndex,
    setCurrentPageIndex
  ] = React.useState(1);
  return (
    <Pagination
      currentPageIndex={currentPageIndex}
      onChange={({ detail }) =>
        setCurrentPageIndex(detail.currentPageIndex)
      }
      pagesCount={5}
    />
  );
}
```

### pagination open-end

```jsx
import * as React from "react";
import Pagination from "@cloudscape-design/components/pagination";

export default () => {
  const [
    currentPageIndex,
    setCurrentPageIndex
  ] = React.useState(1);
  return (
    <Pagination
      currentPageIndex={currentPageIndex}
      onChange={({ detail }) =>
        setCurrentPageIndex(detail.currentPageIndex)
      }
      openEnd
      pagesCount={5}
    />
  );
}
```
