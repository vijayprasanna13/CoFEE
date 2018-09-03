# query local and delta index for all micro-batch points
'''
micro-batch points are of the form (lat, long, time, {key1: value1, key2: value2, key3: value3})
'''

'''
constructs bloom filter from local index in Fog
'''

import sys
from random import shuffle
sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_fog_service/fog_index_manager/GI_periodic_update/')
sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_proto_files/')
sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_fog_service/fog_index_manager/local_index/')
sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_fog_service/')
sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_fog_service/config/')
from bloomfilter import BloomFilter
import math
import fog_service_pb2
import cloud_service_pb2
import index_config
#import local_index
import fog_client
import properties

'''
generic_filter = Filter.Filter()
generic_filter.spatial_coordinates = (index_config.lat_min, index_config.lat_max, index_config.long_min, index_config.long_max)
generic_filter.time = (index_config.t_start, index_config.t_end)
generic_filter.domain = {}

for KVP in index_config.properties:
    generic_filter.domain[KVP] = index_config.properties[KVP]
'''

# temporal bloom filter
n = index_config.no_of_elements      # no. of items to add
p = index_config.false_positive_probability    # false positive probability
temporal_bloomf = BloomFilter(n, p)

'''
for microbatch_metadata in query_index.query_delta_index(generic_filter):
    t = microbatch_metadata[2]/index_config.t_delta
    temporal_bloomf.add(str(t))
'''
'''
for microbatch_id in local_index.query_index(generic_filter):
    temporal_bloomf.add(str(microbatch_id))
'''



# spatial bloom filter
n = index_config.no_of_elements
p = index_config.false_positive_probability
spatial_bloomf = BloomFilter(n, p)

'''
for microbatch_metadata in query_index.query_delta_index(generic_filter):
    lat_ind = math.floor(microbatch_metadata[0]/index_config.lat_delta)
    long_ind = math.floor(microbatch_metadata[1]/index_config.long_delta)

    ind = str(lat_ind)+str(long_ind)
    spatial_bloomf.add(ind)
'''


# domain property bloom filter
n = index_config.no_of_elements
p = index_config.false_positive_probability
domain_property_bloomf = BloomFilter(n, p)

#for microbatch_id in local_index.query_properties():

'''
for microbatch_metadata in query_index.query_delta_index(generic_filter):
    KVP_dict = microbatch_metadata[3]
    for key in KVP_dict:
        ind  = str(key)+str(KVP_dict[key])
        domain_property_bloomf.add(ind)
'''




'''
call client stub with each bloom filter message to send to cloud 
for periodic updation of global index
'''



'''
NEW CODE TO IMPLEMENT ACTUAL FUNCTIONALITY
'''
def add_to_bloom_temporal(time):
    temporal_bloomf.add(str(time/index_config.t_delta))


def add_to_bloom_spatial(spatial_location):
    spatial_bloomf.add(str(spatial_location[0]/index_config.lat_delta) + ":" + str(spatial_location[1]/index_config.long_delta))

def add_to_bloom_property(microbatch_property):
    for KVP in microbatch_property:
        domain_property_bloomf.add(str(KVP)+str(microbatch_property[KVP]))

add_to_bloom_temporal(23344323)
add_to_bloom_spatial((23.4,45.5))
add_to_bloom_property({"Foo1": "Bar1", "Foo2": "Bar2", "Foo3": "Bar3"})


'''
# construct protobuf messages for each bloom filter

temporal_bloom_filter = cloud_service_pb2.bloom_filter(size=temporal_bloomf.size)
#temporal_bloom_filter.size = temporal_bloomf.size

for i in temporal_bloomf.bit_array:
    if(i == False):
        temporal_bloom_filter.bit.append(0)
    else:
        temporal_bloom_filter.bit.append(1)

spatial_bloom_filter = cloud_service_pb2.bloom_filter()
spatial_bloom_filter.size = spatial_bloomf.size

for i in spatial_bloomf.bit_array:
    if(i == False):
        spatial_bloom_filter.bit.append(0)
    else:
        spatial_bloom_filter.bit.append(1)

domain_bloom_filter = cloud_service_pb2.bloom_filter()
domain_bloom_filter.size = domain_property_bloomf.size

for i in domain_property_bloomf.bit_array:
    if(i == False):
        domain_bloom_filter.bit.append(0)
    else:
        domain_bloom_filter.bit.append(1)
'''

fog_client.update_GI(properties.fog_ip, temporal_bloomf, spatial_bloomf, domain_property_bloomf)

