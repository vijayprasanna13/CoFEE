import grpc
from concurrent import futures
import time
import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/edge/')
import edge_service_pb2
import edge_service_pb2_grpc


class edgeServicer(edge_service_pb2_grpc.edgeServicer):
    def pull_microbatch(self, request, context):
        '''
                        PULL MICROBATCH FROM ANOTHER EDGE DEVICE
        :param request:
        :param context:
        :return:
        '''
        pass

    def kill_task(self, request, context):
        '''
                        KILL CURRENLTY EXECUTING TASK
        :param request:
        :param context:
        :return:
        '''

        pass

    def send_task(self, request, context):
        '''
                        EXECUTE TASK GIVEN
        :param request:
        :param context:
        :return:
        '''


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    edge_service_pb2_grpc.add_fogServicer_to_server(edgeServicer(), server)
    print('Started server on Edge Layer. Listening for requests on port 50053.')
    server.add_insecure_port('[::]:50053')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()


