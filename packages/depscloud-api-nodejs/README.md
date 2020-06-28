# Getting Started with NodeJS

To install:

``` bash
npm install --save @depscloud/api
```

Usage:

```javascript
const grpc = require('grpc');

const { DependencyExtractor } = require('@depscloud/api/v1alpha/extractor');
const {
    SourceService,
    ModuleService,
    DependencyService,
} = require('@depscloud/api/v1alpha/tracker');

const credentials = grpc.credentials.createInsecure();

const dependencyExtractor = new DependencyExtractor('gateway:80', credentials);
const sourceService = new SourceService('gateway:80', credentials);
const moduleService = new ModuleService('gateway:80', credentials);
const dependencyService = new DependencyService('gateway:80', credentials);
```
