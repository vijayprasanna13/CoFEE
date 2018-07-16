'''
PERIODIC UPDATE OF LOCAL INDEX FROM DELTA INDEX
'''

import time
import sys
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_index_manager/local_index/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_index_manager/delta_index/')

import delta_index
import local_index

def periodic_update():
    delta_index.update_delta_index()
    print(delta_index.spatial_delta_index)

    microbatch_id_list = []
    for id in delta_index.spatial_delta_index:
        microbatch_id_list.append(id)

    print("LIST OF MICROBATCHES :- ")
    print(microbatch_id_list)

    for id in microbatch_id_list:
        local_index.add_microbatch(id, delta_index.spatial_delta_index[id], delta_index.temporal_delta_index[id],
                                   delta_index.property_delta_index[id])

    print("DONE UPDATING LOCAL INDEX WITH DELTA INDEX!!")


'''
Uncomment to update periodically
while(True):
    periodic_update()
    time.sleep(3)       process sleeps for 3 seconds

'''
periodic_update()