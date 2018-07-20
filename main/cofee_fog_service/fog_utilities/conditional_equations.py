import time
import sys
import datetime
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/config')
import properties

now = datetime.datetime.now()


'''
Equation 4.2
'''

def compute_expected_maximum_cost(size, edge, task_details,ip_list):
    '''
    :param edge:
    :param task_details:
    :param billing_increment:
    :return:
    '''
    R = 0           # to be computed by the below pseudo code
    _R = 0          # to be computed by the below pseudo code

    '''
    compute replication cost into the edge R AND fog R'
    '''
    if(edge[0] in ip_list):
        R = 0
    elif(properties.fog_ip not in ip_list):
        R = size*properties.bandwidth_edge_edge
        _R = size*properties.bandwidth_edge_fog
    else:
        R = size*properties.bandwidth_edge_fog
        _R = 0

    billing_increment = properties.billing_increment
    kappa = (R + float(task_details.baseline_execution_time/(edge.no_of_cores*billing_increment))*edge[4]) + (_R + edge[3]*float(task_details.baseline_execution_time/(properties.no_of_cores*billing_increment))*properties.unit_cost_of_execution)

    return kappa



'''
Equation 4.1
'''
def is_executable(size, edge, task_details, endpoint_list):
    T = properties.Cloud_Timeout
    baseline_execution_time = task_details.base_execution_time
    replication_time = get_replication_time(size, edge, endpoint_list)       # TO BE IMPLEMENTED BY CHANGING LOCAL/DELTA INDEX

    total_time = (int(time.time()) + T + replication_time + float(baseline_execution_time/edge.no_of_cores) + float(baseline_execution_time/properties.no_of_cores))
    if(total_time <= task_details.sub_deadline):
        return True
    else:
        return False

def get_replication_time(size, edge, endpoint_list):
    if(edge[0] in endpoint_list):
        return 0
    else:
        min = sys.maxsize
        for ip in endpoint_list:
            cost = properties.LATENCY_MAP[edge[0],ip] + float(size/properties.BANDWIDTH_MAP[edge[0],ip])
            if(cost < min):
                min = cost

        return min

def get_alternate_replication_time(size, edge, ip_list, fog_containing_ip):
    if(edge[0] in ip_list):
        return 0
    else:
        min = sys.maxsize
        for ip in ip_list:
            cost = properties[edge[0]][fog][latency] + float(size/properties[edge[0][ip][bandwidth]]) + c + properties[edge[0]][fog_containing_ip][bandwidth] + properties[edge[0]][fog][latency]
            if(cost < min):
                min = cost

        return min



def omega(size, edge, task_details, device_iplist_containing_microbatch):
    T = properties.Cloud_Timeout
    replication_time = get_replication_time(size, edge, device_iplist_containing_microbatch)
    baseline_execution_time = task_details.base_execution_time
    return (time.time() + T + replication_time + float(baseline_execution_time/edge[2]) + float(baseline_execution_time/properties.no_of_cores))


def alternate_omega(size, tcurr, edge, task_details,c,  device_ip):
    T = properties.Cloud_Timeout
    return tcurr + T + (c + size/properties.bandwidth_edge_fog + properties.latency_edge_fog + size/properties.bandwidth_fog_fog + properties.latency_fog_fog) + task_details.baseline_execution_time/edge.no_of_cores


def is_executable_alternate():
    T = properties.Cloud_Timeout
    baseline_execution_time = task_details.base_execution_time
    replication_time = get_alternate_replication_time(size, edge, ip_list, fog_containing_ip)  # TO BE IMPLEMENTED BY CHANGING LOCAL/DELTA INDEX

    total_time = (int(time.time()) + T + replication_time + float(baseline_execution_time / edge.no_of_cores) +
        baseline_execution_time / properties.no_of_cores)
    if (total_time <= task_details.sub_deadline):
        return True
    else:
        return False



def compute_alternate_expected_maximum_cost(size, edge,c, task_details, billing_increment,ip):
    if(c != 0):
        R = size*(2*properties.bandwidth_edge_fog + properties.bandwidth_edge_fog)
    else:
        R = size*(properties.bandwidth_edge_fog + properties.bandwidth_fog_fog)


    kappa = (R + float(task_details.baseline_execution_time/(edge.no_of_cores*billing_increment))*edge.unit_cost_of_execution) + ( edge.probability_of_failure*float(task_details.baseline_execution_time/(properties.no_of_cores*billing_increment))*properties.unit_cost_of_execution)
    return kappa