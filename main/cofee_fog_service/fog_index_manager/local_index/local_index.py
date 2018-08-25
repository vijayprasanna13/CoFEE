import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from rtree import index


# USING 3-D INDEXING for RTree
# perform required initialization here


'''
You have to delete 3d_RTree_index.data and 3d_RTree_index.index
to run tests
as previous results are also stored
'''
p = index.Property()
p.dimension = 3
p.dat_extension = 'data'
p.idx_extension = 'index'
idx3d = index.Index('3d_RTree_index', properties=p)


'''
2 Dimensional R Tree
'''
idx = index.Index()


# name-value properties is indexed at whoosh
# perform initializations for whoosh
#schema = Schema(key=TEXT(stored=True), microbatch_id=ID, endpoint=TEXT, value=TEXT(stored=True))
schema = Schema(key=TEXT(stored=True), endpoint=TEXT, value=TEXT(stored=True))

os.mkdir("indexdir")


ix = create_in("indexdir", schema)

#writer = ix.writer()


def add_microbatch(microbatch_id, microbatch_spatial_location, microbatch_temporal_location, microbatch_property, device_endpoint):

    # add to rtree index
    print ("MICROBATCH SPATIAL LOCATION IN LOCAL INDEX .....")
    print microbatch_spatial_location
    left = microbatch_spatial_location[0]
    bottom = microbatch_spatial_location[1]
    right = left
    top = bottom


    print("MICROBATCH TEMPORAL LOCATION IN LOCAL INDEX .....")
    print(microbatch_temporal_location)

    '''
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

    '''
    #zmin = float(device_endpoint[:5])
    print "zmin :- "
    #print type(zmin)

    #zmax = float(device_endpoint[6:])
    print "zmax :- "
    #print device_endpoint[6:]
    '''

    '''
    xmin, xmax :- minimum and maximum spatial locality
    '''

    '''
    ymin, ymax :- minimum and maximum temporal region
    '''
    '''
    print(microbatch_id)
    idx3d.insert(microbatch_id, (xmin, ymin, 0,
                                 xmax, ymax, 0), None)
    '''

    #idx.insert(microbatch_id, (left, bottom, right, top))

    #idx.insert(microbatch_id, xmin, ymin)
    '''   
    idx3d.insert(microbatch_id, (microbatch_spatial_location[0], microbatch_spatial_location[1], microbatch_temporal_location[0],
                                 microbatch_temporal_location[1], float(device_endpoint[6:]), float(device_endpoint[:5])))
    '''
    idx3d.insert(microbatch_id, (left, bottom, microbatch_temporal_location[0], right, top, microbatch_temporal_location[1]))
    # add name-value properties to whoosh index
    for KVP in microbatch_property:
        try:
            writer = ix.writer()
            #writer.add_document(key=KVP[0], microbatch_id=unicode(str(microbatch_id), "utf-8"), endpoint=device_endpoint, value=KVP[1])
            writer.add_document(key=KVP[0], endpoint=device_endpoint, value=unicode(str(microbatch_id), "utf-8"))

            writer.commit()
        finally:
            pass

def query_properties():
    match_list = []
    with ix.searcher() as searcher:
        query = QueryParser("key", ix.schema).parse("foo1")
        results = searcher.search(query)
        print results[0:]
        for match in results[0:]:
            match_list.append(int(match["value"]))

    print "matched microbatch list from KVP...."
    print match_list




def query_index():

    print("Intersection results : -")
    #lst = list(idx.intersection((1, 1, 4, 4)))

    lst3D = list(idx3d.intersection((1, 1, 7, 4, 4, 50)))
    #print lst


    print lst3D

    # print(idx3d.intersection((1, 10, 0, 4, 100, 0)))



#query_index()
#add_microbatch()