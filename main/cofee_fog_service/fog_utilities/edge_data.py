EDGE_LIST = []
OUT_OF_RANGE_EDGE_LIST = []         # same as disconnected edge list


def add_edge(edge_ip, no_of_cores, probability_of_failure, unit_cost_of_execution):
    edge_details = (edge_ip, "free", no_of_cores, probability_of_failure, unit_cost_of_execution)
    EDGE_LIST.append(edge_details)

def add_edge_to_out_of_range(edge_ip):
    OUT_OF_RANGE_EDGE_LIST.append(edge_ip)
    EDGE_LIST.remove(edge_ip)


