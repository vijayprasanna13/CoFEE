import uuid
import json
from pprint import pprint
import random
import datetime
import numpy as np
import sys
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_edge_service/')
from MicroBatch import MicroBatch
import pickle


'''
random microbatch generating function can be invoked with configurations specified in sensor_config.json
'''
def microbatch_gen(sensor_prop):
    u = uuid.uuid1()

    # microbatch id
    microbatch_id = u.int

    # microbatch spatial region
    microbatch_lat = random.uniform(sensor_prop["microbatch_spatial_northwest_latitude"] ,sensor_prop["microbatch_spatial_southeast_latitude"])
    microbatch_long = random.uniform(sensor_prop["microbatch_spatial_northwest_longitude"] , sensor_prop["microbatch_spatial_southeast_longitude"])
    microbatch_spatial_locality = (microbatch_lat, microbatch_long)

    # microbatch temporal range
    temporal_range_size = random.uniform(sensor_prop["minimum_temporal_range"], sensor_prop["maximum_temporal_range"])
    microbatch_temporal_range = (datetime.datetime.now().minute-temporal_range_size, datetime.datetime.now().minute)

    # microbatch properties
    no_of_prop = random.uniform(sensor_prop["min_number_properties"], sensor_prop["max_number_properties"])
    microbatch_properties = []          # contains dicts of microbatch properties
    count = 0
    for prop in sensor_prop["properties"]:
        microbatch_properties.append((prop, sensor_prop["properties"].get(prop)))
        #microbatch_properties.append(prop)
        if(count == (no_of_prop-1)):
            break

    print("MICROBATCH METADATA GENERATED :- ")
    print(microbatch_spatial_locality)
    print(microbatch_temporal_range)
    print(microbatch_properties)

    # generate microbatch data payload
    batch_size = int(random.uniform(sensor_prop["min_size_of_batch_payload"], sensor_prop["max_size_of_batch_payload"]))
    microbatch_payload = np.random.bytes(batch_size)

    print("microbatch_payload and size :- ")
    print(microbatch_payload)
    print(batch_size)
    return microbatch_id, microbatch_spatial_locality, microbatch_temporal_range, microbatch_properties, batch_size, microbatch_payload

'''
converts the generated microbatch data into standard predefined Microbatch class 
'''
def convert_to_class(microbatch_id,microbatch_spatial_locality,microbatch_temporal_range,microbatch_properties,batch_size, microbatch_payload,sensor_prop):
    microbatch_object = MicroBatch(microbatch_id, sensor_prop["sensorid"])
    microbatch_object.set_spatial_region(microbatch_spatial_locality)
    microbatch_object.set_timestamp(microbatch_temporal_range)
    microbatch_object.set_microbatch_prop(microbatch_properties)
    microbatch_object.set_payload(microbatch_payload)
    microbatch_object.set_size(batch_size)

    return microbatch_object


'''
persists the Microbatch object into disk location (specified in config file) using pickle
'''
def persist_object(object, location):
    d = "MICROBATCH"
    print(object)
    with open(location, 'wb') as f:
        pickle.dump(object, f)

'''
generate_and_store() is the function called when a new process is forked
'''
def generate_and_store():

    # open config file tailored to particular sensor
    with open('sensor_config.json') as f:
        data = json.load(f)
    sensor_prop = data["sensor_generated_microbatch_properties"]

    # get all fields of the microbatch from the data generating function
    microbatch_id,microbatch_spatial_locality,microbatch_temporal_range,microbatch_properties,batch_size, microbatch_payload = microbatch_gen(sensor_prop)

    # convert all the fields into a MicroBatch object
    microbatch_object = convert_to_class(microbatch_id,microbatch_spatial_locality,microbatch_temporal_range,microbatch_properties,batch_size, microbatch_payload,sensor_prop)

    # get shared location to persist microbatch
    SHARED_MICROBATCH_RESOURCE_LOCATION_FILE = sensor_prop["MICROBATCH_SHARED_FILE_PATH"] + str(microbatch_object.get_micro_batch_id())+'.pkl'

    # persist microbatch
    persist_object(microbatch_object, SHARED_MICROBATCH_RESOURCE_LOCATION_FILE)

generate_and_store()