# query local and delta index for all micro-batch points
'''
micro-batch points are of the form (lat, long, time, {key1: value1, key2: value2, key3: value3})

'''
import sys
from random import shuffle
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/fog_index_manager/GI_periodic_update/')
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_proto_files/')
from bloomfilter import BloomFilter
import math
import fog_service_pb2

generic_filter = Filter.Filter()
generic_filter.spatial_coordinates = (index_config.nwlat, index_config.nwlong, index_config.selat, index_config.selong)
generic_filter.time = (index_config.t_start, index_config.t_end)
generic_filter.domain = {}

for KVP in index_config.properties:
    generic_filter.domain[KVP] = index_config.properties[KVP]


# temporal bloom filter
n = 20      # no. of items to add
p = 0.05    # false positive probability
temporal_bloomf = BloomFilter(n, p)

for microbatch_metadata in query_index.query_delta_index(generic_filter):
    t = microbatch_metadata[2]/index_config.t_delta
    temporal_bloomf.add(str(t))



# spatial bloom filter
n = 20
p = 0.05
spatial_bloomf = BloomFilter(n, p)

for microbatch_metadata in query_index.query_delta_index(generic_filter):
    lat_ind = math.floor(microbatch_metadata[0]/index_config.lat_delta)
    long_ind = math.floor(microbatch_metadata[1]/index_config.long_delta)

    ind = str(lat_ind)+str(long_ind)
    spatial_bloomf.add(ind)


# domain property bloom filter
n = 20
p = 0.05
domain_property_bloomf = BloomFilter(n,p)

for microbatch_metadata in query_index.query_delta_index(generic_filter):
    KVP_dict = microbatch_metadata[3]
    for key in KVP_dict:
        ind  = str(key)+str(KVP_dict[key])
        domain_property_bloomf.add(ind)




# construct protobuf messages for each bloom filter

temporal_bloom_filter = fog_service_pb2.bloom_filter()
temporal_bloom_filter.size = temporal_bloomf.size

for i in temporal_bloomf.bit_array:
    if(i == False):
        temporal_bloom_filter.bit.append(0)
    else:
        temporal_bloom_filter.bit.append(1)

spatial_bloom_filter = fog_service_pb2.bloom_filter()
spatial_bloom_filter.size = spatial_bloomf.size

for i in spatial_bloomf.bit_array:
    if(i == False):
        spatial_bloom_filter.bit.append(0)
    else:
        spatial_bloom_filter.bit.append(1)

domain_bloom_filter = fog_service_pb2.bloom_filter()
domain_bloom_filter.size = domain_property_bloomf.size

for i in domain_bloom_filter:
    if(i == False):
        domain_bloom_filter.bit.append(0)
    else:
        domain_bloom_filter.bit.append(1)


'''
call client stub with each bloom filter message to send to cloud 
for periodic updation of global index
'''
