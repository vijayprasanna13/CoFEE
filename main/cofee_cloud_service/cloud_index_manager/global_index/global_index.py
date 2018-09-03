'''
GLOBAL INDEX FOR CLOUD
USES BLOOM FILTER AND RESPECTIVE OPERATIONS
'''
'''
GLOBAL INDEX IS A LIST OF THE FOLLOWING FORM :- 
GI = [(fog_endpoint, temporal_bloom_filter, spatial_bloom_filter, domain-property_bloom_filter), (fog_endpoint, temporal_bloom_filter, spatial_bloom_filter, domain-property_bloom_filter)
, .....]
'''

import sys
import mmh3
import math
import index_config
import pickle


sys.path.append('/Users/pyadla/Downloads/CoFEE-master/main/cofee_cloud_service/cloud_index_manager/')
from Filter import Filter
file_Name = "globalindexpersistance"
GLOBAL_INDEX = []


def update_global_index(endpoint, temporal_bloom, spatial_bloom, domain_bloom):
    GLOBAL_INDEX.append((endpoint, temporal_bloom, spatial_bloom, domain_bloom))
    # open the file for writing
    fileObject = open(file_Name, 'wb')
    pickle.dump(GLOBAL_INDEX, fileObject)
    fileObject.close()

    fileObject = open(file_Name, 'r')
    b = pickle.load(fileObject)
    print GLOBAL_INDEX == b


def query_global_index(filter):
    temporal_filter = filter.time
    enumerated_temporal_filter = enumerate_temporal(temporal_filter[0], temporal_filter[1])

    spatial_filter = filter.spatial_coordinates
    enumerated_spatial_filter = enumerate_spatial(spatial_filter[0], spatial_filter[1], spatial_filter[2], spatial_filter[3])


    domain_filter = filter.domain

    matched_partitions = []
    for index in GLOBAL_INDEX:
        temporal_flag = 0
        spatial_flag = 0
        domain_flag = 0


        # temporal check
        temporal_bloom_size = len(index[1])
        for unit in enumerated_temporal_filter:
            digests = []
            for i in range(index_config.hash_count):
                digest = int(mmh3.hash((str(unit/index_config.t_delta)), i)) % temporal_bloom_size
                digests.append(digest)

            flag = 1
            for i in digests:
                if(index[1][i] == 0):
                    flag = 0

            if(flag == 1):
                temporal_flag = 1


        # spatial check
        spatial_bloom_size = len(index[2])
        for unit2 in enumerated_spatial_filter:
            digests = []
            for i in range(index_config.hash_count):
                digest = int(mmh3.hash((str(unit2[0]/index_config.lat_delta)+":"+str(unit2[1]/index_config.long_delta)), i)) % spatial_bloom_size
                digests.append(digest)

            flag = 1
            for i in digests:
                if(index[2][i] == 0):
                    flag = 0

            if(flag == 1):
                spatial_flag = 1


        # domain property check
        domain_property_bloom_filter = len(index[3])

        for KVP in domain_filter:
            digests = []
            for i in range(index_config.hash_count):
                digests = []
                digest = int(mmh3.hash((str(KVP)+str(domain_filter[KVP])), i)) % domain_property_bloom_filter
                digests.append(digest)

            flag = 1
            for i in digests:
                if(index[3][i] == 0):
                    flag = 0

            if(flag == 1):
                domain_flag = 1

        if(temporal_flag and spatial_flag and domain_flag):
            matched_partitions.append(index[0])

    return matched_partitions



def enumerate_temporal(t_start, t_end):
    temporal_list = []
    for i in range(t_end):
        if(i> t_start):
            temporal_list.append(i)
    return temporal_list

def enumerate_spatial(lat_start, long_start, lat_end, long_end):
    spatial_list = []
    for i in range(int(math.ceil(lat_end))):
        for j in range(int(math.ceil(long_end))):
            if(i >= int(math.floor(lat_start)) and j >= int(math.floor(long_start))):
                spatial_list.append((i, j))
    return spatial_list





def print_GI():
    print GLOBAL_INDEX

'''
# test filter
test_filter = Filter()
test_filter.spatial_coordinates = (1, 1, 3, 3)
test_filter.time = (2,4)
test_filter.domain = {"Foo1": "Bar1", "Foo2": "Bar2"}






update_global_index('10.34.34.45', [1,2,3,2,2,23,34], [3,5,4,5,4,5,5], [1,2,3,2,1,3,4])
print_GI()
print enumerate_temporal(2, 35)
print enumerate_spatial(2, 2, 6, 6)

print query_global_index(test_filter)
'''