import sys
import json
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_cloud_service/cloud_dag_manager/')
import unroll_dag


# specify absolute path of the DAG in Json format here
DAG_PATH = '/home/prasanth/Desktop/CoFEE/src/input_dags/test_dag.json'

# decode the DAG into a data object
with open(DAG_PATH) as dag:
    data = json.load(dag)

# unrolled dag path list
UNROLLED_DAG_PATH_LIST = unroll_dag.LIST_OF_UNROLLED_DAG

TASK_PROPERTIES = data["task_properties"]

# baseline resource execution cost of all unrolled dag paths
UNROLLED_DAG_PATH_LENGTH = []

# maintains a hashmap of all tasks and their slack time
GLOBAL_TASKS_SLACK_MAP = {}

# computing slacks
#print(lineage_chain.LIST_OF_LINEAGE_CHAINS)



# initialize hashmap of slacks
'''
TASKNAME -> (lineageChain1, lineageChain2, finalValueifshared)
'''
def populate_inital_slackmap():
    for taskName in TASK_PROPERTIES:
        GLOBAL_TASKS_SLACK_MAP[taskName] = [None]*(len(LINEAGE_CHAINS)+1)


# use formula to calculate induvidual lineage chain lengths
def calculate_lineage_chain_lengths():
    for lineage_chain in LINEAGE_CHAINS:
        length_of_lineage_chain = 0
        for taskName in lineage_chain:
            length_of_lineage_chain += TASK_PROPERTIES[taskName]["length_wrt_base"]
        LINEAGE_CHAIN_LENGTH.append(length_of_lineage_chain)

    #print(LINEAGE_CHAIN_LENGTH)



# main driver function
def main():
    populate_inital_slackmap()
    calculate_lineage_chain_lengths()
    deadline = data["deadline"]

    # loop to index out maximum lineage chains
    while(len(LINEAGE_CHAIN_LENGTH) > 0):
        max_length = max(LINEAGE_CHAIN_LENGTH)
        index = LINEAGE_CHAIN_LENGTH.index(max_length)
        recompute_length(index)
        compute_slacks(LINEAGE_CHAINS[index], index, deadline)

        deadline = refresh_deadline(LINEAGE_CHAINS[index], index)
        del LINEAGE_CHAIN_LENGTH[index]
        print(GLOBAL_TASKS_SLACK_MAP)

    #print(GLOBAL_TASKS_SLACK_MAP)



# refresh deadline for shared tasks
def refresh_deadline(lineage_chain, index):
    newdeadline = data["deadline"]
    for taskName in lineage_chain:
        if((len(TASK_PROPERTIES[taskName]["sink_microbatch_id"]) > 1) and (len(TASK_PROPERTIES[taskName]["source_microbatch_id"])==1)):
            if GLOBAL_TASKS_SLACK_MAP[taskName][-1] == None:
                GLOBAL_TASKS_SLACK_MAP[taskName][-1] = GLOBAL_TASKS_SLACK_MAP[taskName][index]
                newdeadline -= GLOBAL_TASKS_SLACK_MAP[taskName][-1]
    print("New Deadline")
    print(newdeadline)
    return newdeadline


# recompute length for shared tasks
def recompute_length(index):
    lineage_chain = LINEAGE_CHAINS[index]
    for taskName in lineage_chain:
        if(GLOBAL_TASKS_SLACK_MAP[taskName][-1]):
            LINEAGE_CHAIN_LENGTH[index] = LINEAGE_CHAIN_LENGTH[index] - (GLOBAL_TASKS_SLACK_MAP[taskName][-1]/len(TASK_PROPERTIES[taskName]["sink_microbatch_id"]))
            print("LINEAGE CHAIN LENGTH")
            print(LINEAGE_CHAIN_LENGTH[index])

# compute slack for each lineage
def compute_slacks(lineage_chain, chain_index, deadline):
    for taskName in lineage_chain:
        task_slack = float((TASK_PROPERTIES[taskName]["length_wrt_base"]*deadline)/(LINEAGE_CHAIN_LENGTH[chain_index]))
        GLOBAL_TASKS_SLACK_MAP[taskName][chain_index] = task_slack


main()


'''
def unroll_dag(param):
    pass

def compute_quana(param):
    pass

def compute_deadlines(param):
    pass

def rollback_lineage(param):
    pass
'''