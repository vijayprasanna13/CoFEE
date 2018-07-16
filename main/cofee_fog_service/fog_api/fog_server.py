import grpc
from concurrent import futures
import time
import sys
import datetime


sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_index_manager/cep_engine/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_scheduler/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_utilities/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_index_manager')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/config/')

import fog_service_pb2
import fog_service_pb2_grpc
import cloud_service_pb2_grpc
import cloud_service_pb2
import Filter
import query_index
import edge_data
import conditional_equations
import slots
import properties



class fogServicer(fog_service_pb2_grpc.fogServicer):
    def register_edge(self, request, context):
        '''
                                EDGE ONBOARDING
        :param request: contains edge_ip and no_of_cores
        :param context:
        :return:
        '''
        edge_data.add_edge(request.ip, request.number_of_cores)
        return cloud_service_pb2.Empty(ack=1)

    def new_microbatch(self, request, context):
        '''

                                NEW MICROBATCH GENERATED @EDGE OR @FOG
        :param request:
        :param context:
        :return:
        '''
        pass

    def register_cep(self, request, context):
        '''

                                REGISTER OPEN FILTER WITH CEP MODULE
        :param request:
            request contains open filter, CEP end-time, (Task Metadata and Task Slack time)
        :param context:
        :return:
        '''
        open_filter = Filter.Filter()
        open_filter.spatial_coordinates = (
        request.open_filter.nwlat, request.open_filter.nwlong, request.open_filter.selat,
        request.open_filter.selong)

        open_filter.time = (request.open_filter.startTime, request.open_filter.endTime)
        open_filter.domain = {}
        for key in request.open_filter.namevalue_filter:
            open_filter.domain[key] = request.open_filter.namevalue_filter[key]

        # send this open filter to CEP engine


    def recheck_delta(self, request, context):
        '''
                                RECHECK OPEN FILTER WITH DELTA and LOCAL INDEX FOR SAKE OF FALSE POSITIVES
        :param request:
            OPEN FILTER,
        :param context:
        :return:
        '''
        request_time = datetime.datetime.now()

        # check for matched micro batches from open filter
        # for the micro-batches present in this fog partition


        # open filter logic
        open_filter = Filter.Filter()
        open_filter.spatial_coordinates = (request.open_filter.nwlat, request.open_filter.nwlong, request.open_filter.selat,
                                           request.open_filter.selong)

        open_filter.time = (request.open_filter.startTime, request.open_filter.endTime)
        open_filter.domain = {}
        for key in request.open_filter.namevalue_filter:
            open_filter.domain[key] = request.open_filter.namevalue_filter[key]

        # contains microbatches matched by given open filter in fog partition
        matched_microbatch_device_list = []

        # check output from local index
        local_index_matches = query_index.query_local_index(open_filter)
        if not local_index_matches:
            print("no matches in local index for open filter")
        else:
            for microbatch_data, ip in local_index_matches:
                matched_microbatch_device_list.append((microbatch_data,ip))

        # check output from delta index
        delta_index_matches = query_index.query_delta_index(open_filter)
        if not delta_index_matches:
            print("no matches in delta index for open filter")
        else:
            for microbatch_data, ip in query_index.query_delta_index(open_filter):
                matched_microbatch_device_list.append((microbatch_data, ip))


        # queried data in matched_micro-batch_device_list[]


        kappa_values = {}
        # for each micro-batch, fog to check whether it can execute
        # the source task on the micro-batch before the sub-deadline for the task
        for microbatch_data, ip_list in matched_microbatch_device_list:      # iterate over all matched micro-batches
            for edge in edge_data.EDGE_LIST:                      # iterate over all edges in self partition
                if((edge[1] == "free") and (conditional_equations.is_executable(microbatch_data.size, edge, request.task_details, ip_list))):      # edge is free if it is not executing a task or replicating a micro-batch or executing a task    # equation 4.1
                        kappa_values[edge, microbatch_data] = conditional_equations.compute_expected_maximum_cost(microbatch_data.size, edge, request.task_details, 10, ip_list)     # equation 4.2


        refactored_kappa_values = {}
        for microbatch_data in matched_microbatch_device_list:
            li = []
            for key in kappa_values:
                if(key[1] == microbatch_data):
                    li.append((key[0], kappa_values[key[0], microbatch_data]))
            refactored_kappa_values[microbatch_data] = li

        for mubatch in refactored_kappa_values:
            sorted(refactored_kappa_values[mubatch], key=lambda x: x[1])



        # Reserve slot in fog device.

        for mubatch in refactored_kappa_values:
            flag = 0
            for edge in refactored_kappa_values[mubatch]:
                if(slots.scout_slot(request.task_details, conditional_equations.omega(),request.task_details.sub_deadline, mubatch)):
                    flag = 1

                    # persist edge device in GLOBAL MAP for dag_id, mubatch_id, task_id
                    # call cloud server with necessary parameters and edge kappa
                    break


            if(flag == 0):
                c = conditional_equations.get_replication_time(size(mubatch), fog ,ip_list)
                if(slots.scout_slot(request.task_details, time.time()+ properties.Cloud_Timeout+c, request.deadline, mubatch)):
                  flag = 1
                  # call cloud server with Fog Kappa, task and microbatch


            if(flag == 0):
                # return kappa = infinity with other parameters(task and microbATCH ID)










        '''
        CORE SLOT SCHEDULING ALGORITHM
        please use the library fog_scheduling
        '''
        '''
        while(not_done_scheduling):
            # sort the edges based on their increasing order of kappa
            cheapest_edge = sort(kappa_values)
            CHECK_FOR_FREE_SLOT(edge, task)     # access slots.py

            # slot reservation on self fog
            
            GIVEN (OMEGA,SUB-DEADLINE FOR TASK)
        '''

    def acknowledge_task(self, request, context):
        '''
                                CONFIRM TASK TO EXECUTE FROM CLOUD
        :param request:
        :param context:
        :return:
        '''
        edge/fog = tasks.TASK_MAPPING[request.dag, request.task, request.mubatch]
        # take care of replications
        tasks.NEXT_TASK_REGISTRY[request.dag_id, request.task_id, request.mubatch_id] = []
        for task_id, sub_deadline in request.next_tasks:
            tasks.NEXT_TASK_REGISTRY[request.dag_id, request.task_id, request.mubatch_id].append((task_id, sub_deadline))



        # make temporary slot permanant
        # send permanant slots update to cloud (send updated top k available slots) in periodic_slot_update

        pass

    def reject_task(self, request, context):
        '''
                                CONFIRM TASK TO REJECT FROM CLOUD
        :param request:
        :param context:
        :return:
        '''

        # free reserved edges in TASK_MAPPING (unmap)
        # remove task slot from reserved slot list (need to be figured out)


        pass

    def request_bid_for_task(self, request, context):           # RENAMED to alternate_fog_check DOWN BELOW
        '''
                                BID FOR TASK BY FOG
        :param request:
        :param context:
        :return:
        '''
        pass

    def task_completed(self, request, context):
        '''

        :param request:   <DAGID, TASKID, I/P MICROBATCHID>
        :param context:
        :return:
        '''

        # STEP 1 :- current task completes, send new microbatch metadata to CEP.
                    # TO BE CONTINUED

        # NEXT TASK REGISTRY

        next_tasks = tasks.NEXT_TASK_REGISTRY[request.dag_id, request.task_details.task_id, request.microbatch_id]
        for task in next_tasks:
            kappa_values = {}

            for edge in edge_data.EDGE_LIST:
                if ((edge[1] == "free") and (
                        conditional_equations.is_executable(microbatch_data.size, edge, request.task_details,
                                                            edge_ip))):  # edge is free if it is not executing a task or replicating a micro-batch or executing a task    # equation 4.1
                    kappa_values[edge, microbatch_data] = conditional_equations.compute_expected_maximum_cost(
                        microbatch_data.size, edge, request.task_details, 10, ip_list)  # equation 4.2

            '''
            
            # the source task on the micro-batch before the sub-deadline for the task
            for microbatch_data, ip_list in matched_microbatch_device_list:  # iterate over all matched micro-batches
                for edge in edge_data.EDGE_LIST:  # iterate over all edges in self partition
                    if ((edge[1] == "free") and (
                            conditional_equations.is_executable(microbatch_data.size, edge, request.task_details,
                                                                ip_list))):  # edge is free if it is not executing a task or replicating a micro-batch or executing a task    # equation 4.1
                        kappa_values[edge, microbatch_data] = conditional_equations.compute_expected_maximum_cost(
                            microbatch_data.size, edge, request.task_details, 10, ip_list)  # equation 4.2

            refactored_kappa_values = {}
            for microbatch_data in matched_microbatch_device_list:
                li = []
                for key in kappa_values:
                    if (key[1] == microbatch_data):
                        li.append((key[0], kappa_values[key[0], microbatch_data]))
                refactored_kappa_values[microbatch_data] = li

            for mubatch in refactored_kappa_values:
                sorted(refactored_kappa_values[mubatch], key=lambda x: x[1])

            # Reserve slot in fog device.

            for mubatch in refactored_kappa_values:
                flag = 0
                for edge in refactored_kappa_values[mubatch]:
                    if (slots.scout_slot(request.task_details, conditional_equations.omega(),
                                         request.task_details.sub_deadline, mubatch)):
                        flag = 1
                        # call cloud server with necessary parameters and edge kappa
                        break

                if (flag == 0):
                    c = conditional_equations.get_replication_time(size(mubatch), fog, ip_list)
                    if (
                            slots.scout_slot(request.task_details, time.time() + properties.Cloud_Timeout + c,
                                             request.deadline,
                                             mubatch)):
                        flag = 1
                        # call cloud server with Fog Kappa, task and microbatch

                if (flag == 0):
            # return kappa = infinity with other parameters(task and microbATCH ID)
            '''
        pass

    def termination_notice(self, request, context):
        '''
                                TERMINATION NOTICE BY EDGE
        :param request: gamma, edge details
        :param context:
        :return:
        '''

        edge_data.add_edge_to_out_of_range(request.edge_ip)

        '''
        IS MICROBATCH FROM EDGE AVAILABLE IN THIS FOG
            1) yes, then do nothing
            2) if no, is pull possible(mu, gamma) ?  # compute within
        '''

        # case 1 :- if fog can pull microbatch from edge
        # call edge to pull microbatch
        #fog_client.pull_microbatch(microbatch_id)

        # update mu1's metadata in LI/DELTA index to append this Fog

        # case 2 :- if fog can't pull microbatch from edge

        # fog_client.task_undone(task)

        pass

    def alternate_fog_check(self, request, context):
        '''


        :param request: task, sub_deadline, microbatch, fog_ip_containing_microatch, c, size(microbatch))
        :param context:
        :return:
        '''

        found = 0
        # create open filter out of microbatch metadata

        open_filter = open_filter(microabatch_time, space, KVP)

        # query local index
        # query delta index

        local_index_matches = query_index.query_local_index(openfilter)

        for muid in local_index_matches:
            if(muid == request.microbatch_data.id):
                found = 1

        delta_index_matches = query_index.query_delta_index(open_filter)

        for muid in delta_index_matches:
            if(muid == request.microbatch_data.id):
                found = 1


        if(found == 1):
            kappa_values = {}
            # for each micro-batch, fog to check whether it can execute
            # the source task on the micro-batch before the sub-deadline for the task
            for microbatch_data, ip_list in matched_microbatch_device_list:  # iterate over all matched micro-batches
                for edge in edge_data.EDGE_LIST:  # iterate over all edges in self partition
                    if ((edge[1] == "free") and (
                    conditional_equations.is_executable(microbatch_data.size, edge, request.task_details,
                                                        ip_list))):  # edge is free if it is not executing a task or replicating a micro-batch or executing a task    # equation 4.1
                        kappa_values[edge, microbatch_data] = conditional_equations.compute_expected_maximum_cost(
                            microbatch_data.size, edge, request.task_details, 10, ip_list)  # equation 4.2

            refactored_kappa_values = {}
            for microbatch_data in matched_microbatch_device_list:
                li = []
                for key in kappa_values:
                    if (key[1] == microbatch_data):
                        li.append((key[0], kappa_values[key[0], microbatch_data]))
                refactored_kappa_values[microbatch_data] = li

            for mubatch in refactored_kappa_values:
                sorted(refactored_kappa_values[mubatch], key=lambda x: x[1])

            # Reserve slot in fog device.

            for mubatch in refactored_kappa_values:
                flag = 0
                for edge in refactored_kappa_values[mubatch]:
                    if (slots.scout_slot(request.task_details, conditional_equations.omega(),
                                         request.task_details.sub_deadline, mubatch)):
                        flag = 1
                        # call cloud server with necessary parameters and edge kappa
                        break

                if (flag == 0):
                    c = conditional_equations.get_replication_time(size(mubatch), fog, ip_list)
                    if (
                    slots.scout_slot(request.task_details, time.time() + properties.Cloud_Timeout + c, request.deadline,
                                     mubatch)):
                        flag = 1
                        # call cloud server with Fog Kappa, task and microbatch

                if (flag == 0):
            # return kappa = infinity with other parameters(task and microbATCH ID)
        else:
            kappa_values = {}
            # for each micro-batch, fog to check whether it can execute
            # the source task on the micro-batch before the sub-deadline for the task
            for microbatch_data, ip_list in matched_microbatch_device_list:  # iterate over all matched micro-batches
                for edge in edge_data.EDGE_LIST:  # iterate over all edges in self partition
                    if ((edge[1] == "free") and (
                    conditional_equations.is_executable_alternate(microbatch_data.size, edge, request.task_details,
                                                        ip_list))):  # edge is free if it is not executing a task or replicating a micro-batch or executing a task    # equation 4.1
                        kappa_values[edge, microbatch_data] = conditional_equations.compute_alternate_expected_maximum_cost(
                            microbatch_data.size, edge, request.task_details, 10, ip_list)  # equation 4.2

            refactored_kappa_values = {}
            for microbatch_data in matched_microbatch_device_list:
                li = []
                for key in kappa_values:
                    if (key[1] == microbatch_data):
                        li.append((key[0], kappa_values[key[0], microbatch_data]))
                refactored_kappa_values[microbatch_data] = li

            for mubatch in refactored_kappa_values:
                sorted(refactored_kappa_values[mubatch], key=lambda x: x[1])

            for mubatch in refactored_kappa_values:
                flag = 0
                for edge in refactored_kappa_values[mubatch]:
                    if (slots.scout_slot(request.task_details, conditional_equations.omega(),
                                         request.task_details.sub_deadline, mubatch)):
                        flag = 1
                        # call cloud server with necessary parameters and edge kappa
                        break

                if (flag == 0):
                    c = conditional_equations.get_replication_time(size(mubatch), fog, ip_list)
                    if (
                    slots.scout_slot(request.task_details, time.time() + properties.Cloud_Timeout + c + size(microbatch)/properties.bandwidth_fog_fog + properties.latency, request.deadline,
                                     mubatch)):
                        flag = 1
                        # call cloud server with Fog Kappa, task and microbatch

                if (flag == 0):
                    # return kappa = infinity with other parameters(task and microbATCH ID)
                    pass

            response = ()
            return response
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fog_service_pb2_grpc.add_fogServicer_to_server(fogServicer(), server)
    print('Started server on Fog Layer. Listening for requests on port 50052.')
    server.add_insecure_port('[::]:50052')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()





