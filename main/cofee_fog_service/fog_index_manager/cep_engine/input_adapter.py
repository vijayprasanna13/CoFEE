import sys

sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_edge_service/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/cloud/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/fog')

import MicroBatch
import fog_service_pb2


def convert_metadata_to_event(microbatch_metadata):
    MuBatch = MicroBatch(microbatch_metadata.id, microbatch_metadata.sensorid)
    MuBatch.spatial_region = (microbatch_metadata.lat, microbatch_metadata.long)
    MuBatch.timestamp = (microbatch_metadata.startTime, microbatch_metadata.endTime)

    for KVP in microbatch_metadata.prop:
        MuBatch.microbatch_prop[KVP.key] = KVP.value

    return MuBatch




