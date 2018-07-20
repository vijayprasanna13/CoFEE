'''
GLOBAL INDEX FOR CLOUD
USES BLOOM FILTER AND RESPECTIVE OPERATIONS
'''
'''
GLOBAL INDEX IS A LIST OF THE FOLLOWING FORM :- 
GI = [(fog_endpoint, temporal_bloom_filter, spatial_bloom_filter, domain-property_bloom_filter), (fog_endpoint, temporal_bloom_filter, spatial_bloom_filter, domain-property_bloom_filter)
, .....]
'''
import mmh3
import math

GLOBAL_INDEX = []


def update_global_index(endpoint, temporal_bloom, spatial_bloom, domain_bloom):
    GLOBAL_INDEX.append((endpoint, temporal_bloom, spatial_bloom, domain_bloom))


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
        for unit in enumerated_temporal_filter:
            for i in range(index_config.hash_count):
                digests = []
                digest = mmh3.hash(math.floor(unit/index_config.t_delta), i)
                digests.append(digest)

            flag = 1
            for i in digests:
                if(index[1][i] == 0):
                    flag = 0

            if(flag == 1):
                temporal_flag = 1




        # spatial check
        for unit in enumerated_spatial_filter:
            for i in range(index_config.hash_count):
                digests = []
                digest = mmh3.hash(math.floor(str(unit[0]/index_config.lat_delta+":"unit[1]/index_config.long_delta)), i)
                digests.append(digest)

            flag = 1
            for i in digests:
                if(index[2][i] == 0):
                    flag = 0

            if(flag == 1):
                spatial_flag = 1


        # domain property check
        for KVP in domain_filter:
            for i in range(index_config.hash_count):
                digests = []
                digest = mmh3.hash(math.floor(str(KVP)+str(domain_filter[KVP])), i)
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
    l = []
    for i in t_start:
        for j in t_end:
            if(i>t_start):
                l.append(j)
    return l

def enumerate_spatial(lat_start, lat_end, long_start, long_end):
    l = []
    for i in math.ceil(lat_end):
        for j in math.ceil(long_end):
            if(i>lat_start and j>long_start):
                l.append((i,j))

    return l



def check_global_index(openFilter):
    pass