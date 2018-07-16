class MicroBatch():
    micro_batch_id = None
    sensor_id = None
    spatial_region = None
    timestamp = None
    microbatch_prop = None
    payload = None
    size = None

    def __init__(self, micro_batch_id, sensor_id):
        self.micro_batch_id = micro_batch_id
        self.sensor_id = sensor_id

    def set_spatial_region(self, spatial_coordinates):
        self.spatial_coordinates = spatial_coordinates

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def set_microbatch_prop(self, micro_batch_prop):
        self.micro_batch_prop = micro_batch_prop

    def set_size(self, size):
        self.size = size

    def set_payload(self, payload):
        self.payload = payload

    def get_spatial_region(self):
        return self.spatial_coordinates

    def get_timestamp(self):
        return self.timestamp

    def get_microbatch_prop(self):
        return self.micro_batch_prop

    def get_micro_batch_id(self):
        return self.micro_batch_id

    def get_sensor_id(self):
        return self.sensor_id



