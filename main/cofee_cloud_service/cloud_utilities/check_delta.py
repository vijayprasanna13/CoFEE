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



def check_delta():
    channel = grpc.insecure_channel(FOG_ENDPOINT)
    stub = fog_service_pb2_grpc.fogStub(channel)

    print("Cloud trying to contact fog for rechecking delta index..")
    open_filter = cloud_service_pb2.open_filter()
    task_details = cloud_service_pb2_grpc.task_details()
    task_details.task_name = "B"
    task_details.task_id = 2
    task_details.slack_time = 23
    open_filter.namevalue_filter["foo10"] = "bar10"
    open_filter.namevalue_filter["foo11"] = "bar11"
    open_filter.nwlat = 1.6
    open_filter.nwlong = 5.9
    open_filter.selat = 10.45
    open_filter.selong = 20.9
    open_filter.startTime = 20
    open_filter.endTime = 50

    for key in open_filter.namevalue_filter:
        print(key)
        print(open_filter.namevalue_filter[key])

    task_and_open_filter_details = cloud_service_pb2.task_and_open_filter_details(open_filter= open_filter, task_details= task_details)


    response = stub.recheck_delta(task_and_open_filter_details)

    print("Response recieved :-")
    print(response.ack)


check_delta()