import grpc
from concurrent import futures
import time
import sys

sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_proto_files')
sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_fog_service/config/')
import cloud_service_pb2
import cloud_service_pb2_grpc
import properties


CLOUD_ENDPOINT = 'localhost:50051'

def run():
    channel = grpc.insecure_channel(CLOUD_ENDPOINT)
    stub = cloud_service_pb2_grpc.cloudStub(channel)
    print("fog client started....")
    fog_metadata = cloud_service_pb2.fog_metadata(fog_ip=properties.fog_ip)
    for i in properties.labels:
        fog_label = fog_metadata.labels.add()
        fog_label.label = i

    response = stub.register_fog(fog_metadata)
    print("Fog client process finished: ")

    if(response.ack == 1):
        print("Communication was successful")

def update_GI(fog_endpoint, temporal_bloomf, spatial_bloomf, domain_property_bloomf):
    channel = grpc.insecure_channel(CLOUD_ENDPOINT)
    stub = cloud_service_pb2_grpc.cloudStub(channel)
    print "fog client started..."

    # construct protobuf messages for each bloom filter

    temporal_bloom_filter = cloud_service_pb2.bloom_filter(size=temporal_bloomf.size)
    # temporal_bloom_filter.size = temporal_bloomf.size

    for i in temporal_bloomf.bit_array:
        if (i == False):
            temporal_bloom_filter.bit.append(0)
        else:
            temporal_bloom_filter.bit.append(1)

    spatial_bloom_filter = cloud_service_pb2.bloom_filter()
    spatial_bloom_filter.size = spatial_bloomf.size

    for i in spatial_bloomf.bit_array:
        if (i == False):
            spatial_bloom_filter.bit.append(0)
        else:
            spatial_bloom_filter.bit.append(1)

    domain_bloom_filter = cloud_service_pb2.bloom_filter()
    domain_bloom_filter.size = domain_property_bloomf.size

    for i in domain_property_bloomf.bit_array:
        if (i == False):
            domain_bloom_filter.bit.append(0)
        else:
            domain_bloom_filter.bit.append(1)




    local_index_input = cloud_service_pb2.local_index_input(fog_endpoint=fog_endpoint,temporal_bloom= temporal_bloom_filter,
                                                            spatial_bloom= spatial_bloom_filter,  domain_bloom=domain_bloom_filter)

    response = stub.update_global_index(local_index_input)
    print("Fog finished passing it's bloom filter to Cloud....!")


#if __name__ == '__main__':
    #run()
    #update_GI()