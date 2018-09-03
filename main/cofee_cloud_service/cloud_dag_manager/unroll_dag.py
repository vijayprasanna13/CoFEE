# lineage chain of tasks
import sys
import json

# specify absolute path of the DAG in Json format here
DAG_PATH = '/home/prasanth/Desktop/CoFEE/src/input_dags/test_dag.json'

# decode the DAG into a data object
with open(DAG_PATH) as dag:
    data = json.load(dag)


# print the DAG wiring
# print(data["taskwiring"])

# DAG all task properties
# print(data["task_properties"])

source_task = data["dag_properties"]["source_task"]
sink_task = data["dag_properties"]["sink_task"]
task_properties = data["task_properties"]



'''
This function is used to calculate all possible lineage chains from given DAG
DFS to find all possible paths from start to end
'''
def find_all_possible_unrollings(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_possible_unrollings(graph, node, end, path)
            for newpath in newpaths:
                  paths.append(newpath)
    return paths


# compute list of all lineage chains possible
LIST_OF_UNROLLED_DAG = find_all_possible_unrollings(data["taskwiring"], source_task, sink_task)
# print(LIST_OF_LINEAGE_CHAINS)


# print tasks and respective micro batches of all the lineage chains
def print_unrolled_dag():
    count = 0
    for chain in LIST_OF_UNROLLED_DAG:
        for taskName in chain:

            if(len(task_properties[taskName]["source_microbatch_id"]) > 1):
                print(task_properties[taskName]["source_microbatch_id"][count])
            else:
                print(task_properties[taskName]["source_microbatch_id"][0])

            print("---> " + taskName)
        if(len(task_properties[chain[-1]]["sink_microbatch_id"]) > 1):
            print(task_properties[chain[-1]]["sink_microbatch_id"][count])
        else:
            print(task_properties[chain[-1]]["sink_microbatch_id"][0])
        print("end of ONE DAG UNROLL")
        count += 1

#print_unrolled_dag()
