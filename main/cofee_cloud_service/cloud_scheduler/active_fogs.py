'''
Active fog list
contains Fog IP list and their respective labels
'''


active_fogs_map = {}            # dict containing fog:(set of labels) mapping

def add_fog(fog_ip, fog_labels):
    active_fogs_map[fog_ip] = set(fog_labels)
    print("Added fog successfully")
    return

def find_nearest_fog(edge_labels):
    edge_labels = set(edge_labels)

    print("edge labels:- ")
    print(edge_labels)
    print("Active fog map :- ")
    print(active_fogs_map)

    max_intersected_fog_ip = None           # fog ip
    max_intersected_num = 0                 # variable to keep track of maximum intersection overlap number
    max_intersected_fog_labels = None

    for fog in active_fogs_map:
        intersect_num = active_fogs_map.get(fog).intersection(edge_labels)  # finds intersection of each fog_labels
        if(len(intersect_num) > max_intersected_num):                       # with desired edge label
            max_intersected_fog_ip = fog
            max_intersected_fog_labels = active_fogs_map.get(fog)
            max_intersected_num = len(intersect_num)

    return max_intersected_fog_ip, max_intersected_fog_labels           # returning fog with maximum intersected labels