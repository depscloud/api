# api

All deps.cloud API definitions consolidated into a single repository.
This repository currently produces 3 libraries:

* npm: [@depscloud/api](https://www.npmjs.com/package/@depscloud/api)
* pip: [depscloud_api](https://pypi.org/project/depscloud_api/)
* vgo: [github.com/depscloud/api](https://github.com/depscloud/api)

## Getting Started with Go

To install:

```bash
go get -u github.com/depscloud/api
```

Usage:

```go
package main

import (
    "github.com/depscloud/api/v1alpha/extractor"
    "github.com/depscloud/api/v1alpha/tracker"

    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials"
)

func dial(target string) *grpc.ClientConn {
    cc, _ := grpc.Dial(target, grpc.WithBlock(), grpc.WithInsecure())
    return cc
}

func main() {
    dependencyExtractor := extractor.NewDependencyExtractorClient(dial("gateway:80"))
    sourceService := tracker.NewSourceServiceClient(dial("gateway:80"))
    moduleService := tracker.NewModuleServiceClient(dial("gateway:80"))
    dependencyService := tracker.NewDependencyServiceClient(dial("gateway:80"))
}
```
