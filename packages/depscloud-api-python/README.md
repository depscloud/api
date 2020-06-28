# Getting Started with Python

To install:

```txt
grpcio==1.30.0
depscloud_api==0.1.5
```

Usage:

```python
import grpc
from depscloud_api.v1alpha1.tacker import tracker_pb2_grpc

sourceService = tracker_pb2_grpc.SourceServiceStub(grpc.insecure_channel('gateway:80'))
moduleService = tracker_pb2_grpc.ModuleServiceStub(grpc.insecure_channel('gateway:80'))
dependencyService = tracker_pb2_grpc.DependencyServiceStub(grpc.insecure_channel('gateway:80'))
```
