import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_edge_service/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/cloud/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/fog')

import MicroBatch
import fog_service_pb2


def convert_event_to_metadata(Microbatch):

    spatial_location = MicroBatch.get_spatial_region()
    temporal_range = MicroBatch.get_timestamp()

    output_meta_data = fog_service_pb2.microbatch_metadata(microbatch_id=Microbatch.micro_batch_id, sensorid = Microbatch.sensorid
                                           ,lat=spatial_location[0], long = spatial_location[1], startTime = temporal_range[0],
                                           endTime = temporal_range[1])

    for KVP in Microbatch.microbatch_prop:
        output_meta_data.prop[KVP[0]] = KVP[1]


    print(output_meta_data)
    return output_meta_data