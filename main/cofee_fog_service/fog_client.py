import grpc
from concurrent import futures
import time
import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/cloud/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/config/')
import cloud_service_pb2
import cloud_service_pb2_grpc
import properties


CLOUD_ENDPOINT = 'localhost:50051'

def run():
    channel = grpc.insecure_channel(CLOUD_ENDPOINT)
    stub = cloud_service_pb2_grpc.cloudStub(channel)
    print("fog client started....")
    fog_metadata = cloud_service_pb2.fog_metadata(fog_ip=properties.fog_ip)
    for i in properties.labels:
        fog_label = fog_metadata.labels.add()
        fog_label.label = i

    response = stub.register_fog(fog_metadata)
    print("Fog client process finished: ")

    if(response.ack == 1):
        print("Communication was successful")

def update_GI():
    channel = grpc.insecure_channel(CLOUD_ENDPOINT)
    stub = cloud_service_pb2_grpc.cloudStub(channel)
    print "fog client started..."

    local_index_input = cloud_service_pb2.local_index_input


if __name__ == '__main__':
    #run()
    update_GI()