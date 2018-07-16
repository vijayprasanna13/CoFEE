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
'''
source_task = data["dag_properties"]["source_task"]
sink_task = data["dag_properties"]["sink_task"]
task_properties = data["task_properties"]
'''
LINEAGE_CHAIN_MAP = {}

'''
map of all source micro-batch ids and list of tasks going through them
'''

source_microbatches = task_properties[source_task]["source_microbatch_id"]
print(source_microbatches)


for microbatch in source_microbatches:
    LINEAGE_CHAIN_MAP[microbatch] = []


print(LINEAGE_CHAIN_MAP)


def start_func():
    print("Came out")
