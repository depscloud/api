# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from depscloud.api.v1beta import rpc_pb2 as depscloud_dot_api_dot_v1beta_dot_rpc__pb2


class SourceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/depscloud.api.v1beta.SourceService/List',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListRequest.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListSourcesResponse.FromString,
                )
        self.ListModules = channel.unary_unary(
                '/depscloud.api.v1beta.SourceService/ListModules',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ManagedSource.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListManagedModulesResponse.FromString,
                )


class SourceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModules(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SourceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListRequest.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListSourcesResponse.SerializeToString,
            ),
            'ListModules': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModules,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ManagedSource.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListManagedModulesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'depscloud.api.v1beta.SourceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SourceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/depscloud.api.v1beta.SourceService/List',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListRequest.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListSourcesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListModules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/depscloud.api.v1beta.SourceService/ListModules',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ManagedSource.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListManagedModulesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class ModuleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/depscloud.api.v1beta.ModuleService/List',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListRequest.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListModulesResponse.FromString,
                )
        self.ListSources = channel.unary_unary(
                '/depscloud.api.v1beta.ModuleService/ListSources',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ManagedModule.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListManagedSourcesResponse.FromString,
                )


class ModuleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSources(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModuleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListRequest.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListModulesResponse.SerializeToString,
            ),
            'ListSources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSources,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ManagedModule.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListManagedSourcesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'depscloud.api.v1beta.ModuleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModuleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/depscloud.api.v1beta.ModuleService/List',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListRequest.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListModulesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/depscloud.api.v1beta.ModuleService/ListSources',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ManagedModule.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.ListManagedSourcesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class TraversalServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDependents = channel.unary_unary(
                '/depscloud.api.v1beta.TraversalService/GetDependents',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.Dependency.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.DependentsResponse.FromString,
                )
        self.GetDependencies = channel.unary_unary(
                '/depscloud.api.v1beta.TraversalService/GetDependencies',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.Dependency.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.DependenciesResponse.FromString,
                )
        self.Search = channel.stream_stream(
                '/depscloud.api.v1beta.TraversalService/Search',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.FromString,
                )
        self.BreadthFirstSearch = channel.stream_stream(
                '/depscloud.api.v1beta.TraversalService/BreadthFirstSearch',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.FromString,
                )
        self.DepthFirstSearch = channel.stream_stream(
                '/depscloud.api.v1beta.TraversalService/DepthFirstSearch',
                request_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.SerializeToString,
                response_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.FromString,
                )


class TraversalServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDependents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDependencies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BreadthFirstSearch(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DepthFirstSearch(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TraversalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDependents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDependents,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.Dependency.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.DependentsResponse.SerializeToString,
            ),
            'GetDependencies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDependencies,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.Dependency.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.DependenciesResponse.SerializeToString,
            ),
            'Search': grpc.stream_stream_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.SerializeToString,
            ),
            'BreadthFirstSearch': grpc.stream_stream_rpc_method_handler(
                    servicer.BreadthFirstSearch,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.SerializeToString,
            ),
            'DepthFirstSearch': grpc.stream_stream_rpc_method_handler(
                    servicer.DepthFirstSearch,
                    request_deserializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.FromString,
                    response_serializer=depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'depscloud.api.v1beta.TraversalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TraversalService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDependents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/depscloud.api.v1beta.TraversalService/GetDependents',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.Dependency.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.DependentsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDependencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/depscloud.api.v1beta.TraversalService/GetDependencies',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.Dependency.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.DependenciesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/depscloud.api.v1beta.TraversalService/Search',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BreadthFirstSearch(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/depscloud.api.v1beta.TraversalService/BreadthFirstSearch',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DepthFirstSearch(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/depscloud.api.v1beta.TraversalService/DepthFirstSearch',
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchRequest.SerializeToString,
            depscloud_dot_api_dot_v1beta_dot_rpc__pb2.SearchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
