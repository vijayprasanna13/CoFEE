import os
from whoosh.index import create_in
from whoosh.fields import *
from rtree import index


# USING 3-D INDEXING for RTree
# perform required initialization here

p = index.Property()
p.dimension = 3
p.dat_extension = 'data'
p.idx_extension = 'index'
idx3d = index.Index('3d_RTree_index', properties=p)


# name-value properties is indexed at whoosh
# perform initializations for whoosh
schema = Schema(key=TEXT(stored=True), microbatch_id=ID, endpoint=TEXT, value=TEXT(stored=True))
#os.mkdir("indexdir")
ix = create_in("indexdir", schema)
#writer = ix.writer()


def add_microbatch(microbatch_id, microbatch_spatial_location, microbatch_temporal_location, microbatch_property, device_endpoint):

    # add to rtree index
    if(microbatch_spatial_location[0] > microbatch_spatial_location[1]):
        xmin = microbatch_spatial_location[1]
        xmax = microbatch_spatial_location[0]
    else:
        xmin = microbatch_spatial_location[0]
        xmax = microbatch_spatial_location[1]

    if(microbatch_temporal_location[0] > microbatch_temporal_location[1]):
        ymin = microbatch_temporal_location[1]
        ymax = microbatch_temporal_location[0]
    else:
        ymin = microbatch_temporal_location[0]
        ymax = microbatch_temporal_location[1]

    print("xmin :- ")
    print(xmin)

    print("xmax :- ")
    print(xmax)

    print "ymin :- "
    print ymin

    print "ymax :- "
    print ymax

    '''
    #zmin = float(device_endpoint[:5])
    print "zmin :- "
    #print type(zmin)

    #zmax = float(device_endpoint[6:])
    print "zmax :- "
    #print device_endpoint[6:]
    '''
    idx3d.insert(microbatch_id, (xmin, ymin, 0,
                                 xmax, ymax, 0), None)
    '''   
    idx3d.insert(microbatch_id, (microbatch_spatial_location[0], microbatch_spatial_location[1], microbatch_temporal_location[0],
                                 microbatch_temporal_location[1], float(device_endpoint[6:]), float(device_endpoint[:5])))
    '''

    # add name-value properties to whoosh index
    for KVP in microbatch_property:
        try:
            writer = ix.writer()
            writer.add_document(key=KVP[0], microbatch_id=unicode(str(microbatch_id), "utf-8"), endpoint=device_endpoint, value=KVP[1])
            writer.commit()
        finally:
            pass


#add_microbatch()
