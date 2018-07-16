# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import edge_service_pb2 as edge__service__pb2


class edgeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.pull_microbatch = channel.unary_unary(
        '/edge/pull_microbatch',
        request_serializer=edge__service__pb2.microbatch_id.SerializeToString,
        response_deserializer=edge__service__pb2.microbatch_payload.FromString,
        )
    self.kill_task = channel.unary_unary(
        '/edge/kill_task',
        request_serializer=edge__service__pb2.task_details.SerializeToString,
        response_deserializer=edge__service__pb2.Empty.FromString,
        )
    self.send_task = channel.unary_unary(
        '/edge/send_task',
        request_serializer=edge__service__pb2.task_info.SerializeToString,
        response_deserializer=edge__service__pb2.result.FromString,
        )


class edgeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def pull_microbatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def kill_task(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def send_task(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_edgeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'pull_microbatch': grpc.unary_unary_rpc_method_handler(
          servicer.pull_microbatch,
          request_deserializer=edge__service__pb2.microbatch_id.FromString,
          response_serializer=edge__service__pb2.microbatch_payload.SerializeToString,
      ),
      'kill_task': grpc.unary_unary_rpc_method_handler(
          servicer.kill_task,
          request_deserializer=edge__service__pb2.task_details.FromString,
          response_serializer=edge__service__pb2.Empty.SerializeToString,
      ),
      'send_task': grpc.unary_unary_rpc_method_handler(
          servicer.send_task,
          request_deserializer=edge__service__pb2.task_info.FromString,
          response_serializer=edge__service__pb2.result.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'edge', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
