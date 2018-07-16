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
schema = Schema(key=TEXT(stored=True), microbatch_id=ID, value=TEXT(stored=True))
os.mkdir("indexdir")
ix = create_in("indexdir", schema)
#writer = ix.writer()


def add_microbatch(microbatch_id, microbatch_spatial_location, microbatch_temporal_location, microbatch_property):

    # add to rtree index
    idx3d.insert(microbatch_id, (microbatch_spatial_location[0], microbatch_spatial_location[1], microbatch_temporal_location[0],
                                 microbatch_spatial_location[0], microbatch_spatial_location[1], microbatch_temporal_location[1]))

    # add name-value properties to whoosh index
    for KVP in microbatch_property:
        try:
            writer = ix.writer()
            writer.add_document(key=KVP[0], microbatch_id=str(microbatch_id), value=KVP[1])
            writer.commit()
        finally:
            pass


#add_microbatch()
