'''
FILE TO HANDLE REGISTRY OF ACTIVE AND NEXT_TASKS
'''
import sys
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_utilities/')
import edge_data

TASK_MAPPING = {}
NEXT_TASK_REGISTRY = {}


def add_mapping(task_id, device_ip, microbatch_id):
    TASK_MAPPING[task_id, microbatch_id] = device_ip
    # update repsective edge in EDGE_LIST

def remove_mapping(task_id, device_ip):
    # remove task mapping in TASK_MAPPING
    # update corresponding edge in edge_data