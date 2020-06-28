# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc_gateway.examples.internal.proto.examplepb import flow_combination_pb2 as grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2


class FlowCombinationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RpcEmptyRpc = channel.unary_unary(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcEmptyRpc',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcEmptyStream = channel.unary_stream(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcEmptyStream',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.StreamEmptyRpc = channel.stream_unary(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/StreamEmptyRpc',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.StreamEmptyStream = channel.stream_stream(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/StreamEmptyStream',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcBodyRpc = channel.unary_unary(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcBodyRpc',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NonEmptyProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcPathSingleNestedRpc = channel.unary_unary(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathSingleNestedRpc',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.SingleNestedProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcPathNestedRpc = channel.unary_unary(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathNestedRpc',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NestedProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcBodyStream = channel.unary_stream(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcBodyStream',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NonEmptyProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcPathSingleNestedStream = channel.unary_stream(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathSingleNestedStream',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.SingleNestedProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )
        self.RpcPathNestedStream = channel.unary_stream(
                '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathNestedStream',
                request_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NestedProto.SerializeToString,
                response_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                )


class FlowCombinationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RpcEmptyRpc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcEmptyStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamEmptyRpc(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamEmptyStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcBodyRpc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcPathSingleNestedRpc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcPathNestedRpc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcBodyStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcPathSingleNestedStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RpcPathNestedStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlowCombinationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RpcEmptyRpc': grpc.unary_unary_rpc_method_handler(
                    servicer.RpcEmptyRpc,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcEmptyStream': grpc.unary_stream_rpc_method_handler(
                    servicer.RpcEmptyStream,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'StreamEmptyRpc': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamEmptyRpc,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'StreamEmptyStream': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamEmptyStream,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcBodyRpc': grpc.unary_unary_rpc_method_handler(
                    servicer.RpcBodyRpc,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NonEmptyProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcPathSingleNestedRpc': grpc.unary_unary_rpc_method_handler(
                    servicer.RpcPathSingleNestedRpc,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.SingleNestedProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcPathNestedRpc': grpc.unary_unary_rpc_method_handler(
                    servicer.RpcPathNestedRpc,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NestedProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcBodyStream': grpc.unary_stream_rpc_method_handler(
                    servicer.RpcBodyStream,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NonEmptyProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcPathSingleNestedStream': grpc.unary_stream_rpc_method_handler(
                    servicer.RpcPathSingleNestedStream,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.SingleNestedProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
            'RpcPathNestedStream': grpc.unary_stream_rpc_method_handler(
                    servicer.RpcPathNestedStream,
                    request_deserializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NestedProto.FromString,
                    response_serializer=grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.gateway.examples.internal.examplepb.FlowCombination', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlowCombination(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RpcEmptyRpc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcEmptyRpc',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcEmptyStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcEmptyStream',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamEmptyRpc(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/StreamEmptyRpc',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamEmptyStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/StreamEmptyStream',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcBodyRpc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcBodyRpc',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NonEmptyProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcPathSingleNestedRpc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathSingleNestedRpc',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.SingleNestedProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcPathNestedRpc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathNestedRpc',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NestedProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcBodyStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcBodyStream',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NonEmptyProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcPathSingleNestedStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathSingleNestedStream',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.SingleNestedProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RpcPathNestedStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.gateway.examples.internal.examplepb.FlowCombination/RpcPathNestedStream',
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.NestedProto.SerializeToString,
            grpc__gateway_dot_examples_dot_internal_dot_proto_dot_examplepb_dot_flow__combination__pb2.EmptyProto.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)