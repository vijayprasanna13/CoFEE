import grpc
from concurrent import futures
import time
import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/')

import fog_service_pb2
import fog_service_pb2_grpc
import cloud_service_pb2
import cloud_service_pb2_grpc

FOG_ENDPOINT = 'localhost:50052'



def register_openfilter_with_fog_cep():
    channel = grpc.insecure_channel(FOG_ENDPOINT)
    stub = fog_service_pb2_grpc.fogStub(channel)

    print("Cloud trying to contact fog..")
    open_filter = cloud_service_pb2.open_filter()
    open_filter.namevalue_filter["foo5"] = "bar5"
    open_filter.namevalue_filter["foo6"] = "bar6"
    open_filter.nwlat = 2.6
    open_filter.nwlong = 6.9
    open_filter.selat = 60.45
    open_filter.selong = 70.9
    open_filter.startTime = 2
    open_filter.endTime = 5

    for key in open_filter.namevalue_filter:
        print(key)
        print(open_filter.namevalue_filter[key])

    response = stub.register_cep(open_filter)
    print("Response recieved :-")
    print(response.ack)


register_openfilter_with_fog_cep()