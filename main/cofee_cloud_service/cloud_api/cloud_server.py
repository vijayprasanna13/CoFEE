import grpc
from concurrent import futures
import time
import sys
from time import sleep
from random import random
from threading import Timer
import math


sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/cloud/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_cloud_service/cloud_scheduler/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_cloud_service/cloud_dag_manager')
import cloud_service_pb2
import cloud_service_pb2_grpc
import active_fogs

import timeit
import lineage_chain

class cloudServicer(cloud_service_pb2_grpc.cloudServicer):

    def register_fog(self, request, context):
        '''
                                        FOG ON-BOARDING
        :param request:
        request object is message fog_metadata which contains following parameters
                1) fog_ip
                2) associated fog_labels

        :param context:
        :return: no return
        '''

        # extract fog_ip and respective labels from request
        fog_ip = request.fog_ip
        print(fog_ip)
        fog_labels = []
        for l in request.labels:
            fog_labels.append(l.label)

        active_fogs.add_fog(fog_ip, fog_labels)         # adds fog to active fog_list
        print(fog_labels)
        return cloud_service_pb2.Empty(ack=1)            # return empty message with acknowledgement


    def request_fog_list(self, request, context):
        '''
                                        EDGE ON BOARDING
        :param request:         request contains the labels of the edge device, which is also the desired
                                labels of the to-be-connected fog device
        :param context:
        :return:
        '''

        print("In request fog list API")
        edge_labels = []
        for l in request.labels:
            edge_labels.append(l.label)

        nearest_fog_ip, nearest_fog_labels = active_fogs.find_nearest_fog(edge_labels)

        fog_metadata = cloud_service_pb2.fog_metadata(fog_ip = nearest_fog_ip)
        for label in nearest_fog_labels:
            l = fog_metadata.labels.add()
            l.label = label

        return fog_metadata


    def dag_input(self, request, context):
        '''
                                        MAIN API FOR USER TO SUBMIT DAG, open Filter and deadline

        :param request:
        :param context:
        :return:
        '''

        # partition open filter logic

        # slack computation logic

        # check Global Index(openFilter) logic

        # call recheck_delta in all matched fogs
        response_list = []
        f = 0

        t = Timer(10.0, lineage_chain.start_func(response_list))
        t.start()



        for fog in matched_fogs:
            response = cloud_client.recheck_delta()
            response_list.append(response)
            if(f == 1):
                break


        # start lineage chain for each triplet (dag_id, task_id, micro-batch_id)


        # compute minimum kappa for all fogs
        BID_DICT = {}

        # initialize
        for response in response_list:
            for rp in response:
                BID_DICT[rp[0], rp[1], rp[2]] = []


        for response in response_list:
            for rp in response:
                BID_DICT[rp[0], rp[1], rp[2]].append(rp[4])

        for key in BID_DICT:
            MIN_KAPPA = sys.maxsize
            for kappa in BID_DICT[key]:
                if(kappa < MIN_KAPPA):
                    MIN_KAPPA = kappa
                    BID_DICT[key] = MIN_KAPPA


        BID_ALT_DICT = {}
        alternate_response_list = []
        for key in BID_DICT:
#            if(BID_DICT[key] != sys.maxsize):
                # scheduling logic
                if(BID_DICT[key] <= (math.floor(length_wrt_base(key[2]))/(properties.fog[properties.m])*properties.billing_increment)*(fog_cost[properties[m]])):
                    cloud_client.acknowledge_task(dag_id, microbatch_id, task_id, OK, next_task_id[], deadlines[])
                else:
                    alternate_fogs = fog_free_slot.alternate_fog_slot()
                    alternate_fog_response_list = []
                    f = 0

                    t = Timer(10.0, lineage_chain.start_func(response_list))
                    t.start()

                    for fog in alternate_fogs:
                        response = cloud_client.alternate_fog_check()
                        alternate_response_list.append(response)
                        if(f == 1):
                            break
                    for alternate_response in alternate_response_list:
                        for rp in alternate_response:
                            BID_ALT_DICT[rp[0]. rp[1], rp[2]] = []

                    for alternate_response in alternate_response_list:
                        for rp in alternate_response:
                            BID_ALT_DICT[rp[0]. rp[1], rp[2]].append(rp[4])


                    for key in BID_ALT_DICT:
                        MIN_ALT_KAPPA = sys.maxsize
                        for kappa in BID_ALT_DICT[key]:
                            if(kappa < MIN_ALT_KAPPA):
                                MIN_ALT_KAPPA = kappa
                                BID_ALT_DICT[key] = MIN_ALT_KAPPA


                    for key in BID_DICT:
                        if(key in BID_ALT_DICT.keys()):
                            min_fog_ip, min_kappa = min(BID_DICT[key], BID_ALT_DICT[key])
                            if(min_kappa != sys.maxsize):
                                cloud_client.acknowledge_task(dag_id, microbatch_id, task_id, OK, next_task_id[], deadlines[])
                            else:
                                # schedule on cloud
                                if(time.time() + (c + size(microbatch)/propertes.bandwidth_fog_edge + properties.latency) + task_details.length_wrt_base/properties.no_of_cores <= task_details.subdeadline):                                                                            # (taken from real fogs which have microbatch
                                    if(c == 0):
                                        B = size*(properties.bandwidth_edge_fog + properties.bandwidth_fog_cloud)
                                    else:
                                        B = size*(properties.bandwidth_fog_cloud)
                                    cost = math.floor(task_details.length_wrt_base/(properties.no_of_cores*billing_increment))* cost_to_execute_on_cloud + B

                                    # pull actual microbatch from fog

                                    # execute task
                                else:
                                    # DAG is marked as failed

















        pass

    def heap_update(self, request, context):
        '''
                                        HEAP UPDATE BY FOG FOR FREE SLOTS

        :param request:
        :param context:
        :return:
        '''
        pass

    def task_done(self, request, context):
        '''
                                        TASK COMPLETION MESSAGE FROM FOG

        :param request:
        :param context:
        :return:
        '''
        # update free slot list
        # schedule derived task
        pass

    def task_undone(self, request, context):
        '''

                                        TASK FAIL MESSAGE FROM FOG
        :param request:
        :param context:
        :return:
        '''

        # called only when fog partition lost the microbatch input , edge disconnects
        # rollback
        # update free slot list
        pass

    def bid_for_task_on_new_microbatch(self, request, context):
        '''
                                        BID FOR TASK EXECUTION BY FOG DEVICE FOR MICRO BATCH
        :param request:
        :param context:
        :return:
        '''








def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cloud_service_pb2_grpc.add_cloudServicer_to_server(cloudServicer(), server)
    print('Started server on Cloud Layer. Listening for requests on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()






