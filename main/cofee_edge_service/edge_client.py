import grpc
from concurrent import futures
import time
import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/cloud/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_edge_service/config/')

import cloud_service_pb2
import cloud_service_pb2_grpc
import properties


CLOUD_ENDPOINT = 'localhost:50051'


def run():
    channel = grpc.insecure_channel(CLOUD_ENDPOINT)
    stub = cloud_service_pb2_grpc.cloudStub(channel)

    print("edge client started....")
    edge_labels = cloud_service_pb2.fog_labels()

    # desired fog properties (indirectly current edge properties)
    for i in properties.labels:
        edge_label = edge_labels.labels.add()
        edge_label.label = i


    response = stub.request_fog_list(edge_labels)
    print("response :- " + response.fog_ip)
    for l in response.labels:
        print(l.label)

if __name__ == '__main__':
    run()