id = 1
no_of_cores = 2
connected_sensor_list = 1
fixed_cost = 10

fog_ip = '10.10.10.10'


'''
LABELS ASSOCIATED WITH THIS PARTICULAR FOG
'''

labels = [1, 2, 3]

bandwidth_edge_edge = 10
bandwidth_edge_fog = 15
latency = 5
Cloud_Timeout = 10


'''
CONNECTED EDGE LATENCY AND BANDWIDTH BETWEEN ALL EDGE AND FOG ENDPOINTS 
TO BE POPULATED INITIALLY BOOTSTRAP
'''

LATENCY_MAP = {}
'''
LATENCY_MAP[endpoint1, endpoint2] = latency_value
'''
BANDWIDTH_MAP = {}
'''
BANDWIDTH_MAP[endpoint1, endpoint2] = bandwidth_value
'''
billing_increment = 10