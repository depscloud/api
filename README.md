# deps.cloud API and SDK definitions

![license](https://img.shields.io/github/license/depscloud/api.svg)
[![license check](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fdepscloud%2Fapi.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fdepscloud%2Fapi?ref=badge_shield)

* API - application programming interface
* SDK - software development kit

This repository contains all API definitions and associated language SDKs available for the [deps.cloud] ecosystem.
APIs are defined using Google's [Protocol Buffers].
Using [gRPC], we're able to code generate client libraries.
This repository currently produces 3 libraries:

| Tech   | Source          | Package                          |
|:-------|:----------------|:---------------------------------|
| npm    | [nodejs source] | [`@depscloud/api`]               |
| pip    | [python source] | [`depscloud_api`] (coming soon!) |
| go mod |                 | [`github.com/depscloud/api`]     |

[deps.cloud]: https://deps.cloud
[Protocol Buffers]: https://developers.google.com/protocol-buffers
[gRPC]: https://grpc.io
[nodejs source]: packages/depscloud-api-nodejs
[python source]: packages/depscloud-api-python
[`@depscloud/api`]: https://www.npmjs.com/package/@depscloud/api
[`depscloud_api`]: https://pypi.org/project/depscloud_api/
[`github.com/depscloud/api`]: https://github.com/depscloud/api

## Getting Started with Go

To install:

```bash
go get -u github.com/depscloud/api
```

Usage:

```go
package main

import (
    "crypto/tls"

    "github.com/depscloud/api/v1alpha/extractor"
    "github.com/depscloud/api/v1alpha/tracker"

    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials"
)

func main() {
    target := "api.deps.cloud:443"
    creds := credentials.NewTLS(&tls.Config{})

    conn, _ := grpc.Dial(target, grpc.WithTransportCredentials(creds))
    defer conn.Close()

    sourceService := tracker.NewSourceServiceClient(conn)
    moduleService := tracker.NewModuleServiceClient(conn)
    dependencyService := tracker.NewDependencyServiceClient(conn)
}
```

# Support

Join our [mailing list] and ask any questions there.

We also have a [Slack] channel.

[mailing list]: https://groups.google.com/a/deps.cloud/forum/#!forum/community/join
[Slack]: https://depscloud.slack.com/join/shared_invite/zt-fd03dm8x-L5Vxh07smWr_vlK9Qg9q5A

## Release Checks

![tag](https://github.com/depscloud/api/workflows/tag/badge.svg)
![npm](https://img.shields.io/npm/v/@depscloud/api?color=green&label=%40depscloud%2Fapi)
![go.mod](https://img.shields.io/github/go-mod/go-version/depscloud/api?color=green&label=go%20mod)
![pypi](https://img.shields.io/pypi/v/depscloud_api)

## License Checks

[![fossa](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fdepscloud%2Fapi.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fdepscloud%2Fapi?ref=badge_large)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=api&dt=api&tid=UA-143087272-2)
