from Filter import Filter
import output_adapter
import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_edge_service/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/cloud/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/fog')
import MicroBatch


'''
### example filter ####
f1 = Filter()
f1.spatial_coordinates = (24.2028,24.2028, 76.56, 76.56)
f1.time = (1, 4)
f1.domain = {"degree": "celsius", "fOO2": BAAR2}
#### #####
'''


GLOBAL_FILTER_LIST = []             # MAINTAINS ALL FILTERS


def register_filter(filter):            # API TO REGISTER A FILTER
    GLOBAL_FILTER_LIST.append(filter)


def process_event(microbatch_event):                # PROCESS EVENT API
    if compute_matching_event(microbatch_event) == (True, True, True):
        output_adapter.convert_event_to_metadata(microbatch_event)


def compute_matching_event(microbatch_event):       # MATCHING LOGIC FOR EVENT
    temp_flag = False
    spatial_flag = False
    domain_flag = False

    for filter in GLOBAL_FILTER_LIST:
        if(microbatch_event.timestamp[0] >= filter.time[0] and microbatch_event.timestamp[1] <= filter.time[1]):
            temp_flag = True

        if(microbatch_event.spatial_region[0] > filter.spatial_coordinates[0]
            and microbatch_event.spatial_region[1] > filter.spatial_coordinates[1]
            and microbatch_event.spatial_region[0] < filter.spatial_coordinates[2]
            and microbatch_event.spatial_region[1] < filter.spatial_coordinates[3]):
            spatial_flag = True

        loopflag = True
        for kvp in microbatch_event.microbatch_prop:
            if(kvp[0] in filter.domain and kvp[1]==filter.domain[kvp[0]]):
                pass
            else:
                loopflag = False

        domain_flag = loopflag

    return (temp_flag,spatial_flag,domain_flag)



#### DATABASE CONNECTION CODE TO PERSIST IF NEEDED #####

### DATABASE CHOSEN :- POSTGRES ###