import sys
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_index_manager/cep_engine/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_edge_service/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/')


import MicroBatch
import fog_service_pb2



test_microbatch_metadata = fog_service_pb2.microbatch_metadata(id = 100, sensorid = 2, lat = 23.4, long = 26.7,
                                                               startTime=10, endTime=21)
test_microbatch_metadata.prop["Foo1"] = "Bar1"
test_microbatch_metadata.prop["Foo2"] = "Bar2"
print(test_microbatch_metadata)



'''
microbatch_event = MicroBatch(test_microbatch_metadata.id, test_microbatch_metadata.sensorid)
microbatch_event.spatial_region = (test_microbatch_metadata.lat, test_microbatch_metadata.long)
microbatch_event.timestamp = (test_microbatch_metadata.startTime, test_microbatch_metadata.endTime)

microbatch_event.size = 100
'''
