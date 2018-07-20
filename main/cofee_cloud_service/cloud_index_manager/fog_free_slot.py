# K max heaps
# to store free slots in a heap
import math
from io import StringIO
import heapq
import sys
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_cloud_service/config/')
import properties

# map with fog_ip and heaps
FOGS_AND_FREE_SLOTS_MAP = {}
ALTERNATE_FOGS = []
import time
'''
class FogSlot:
    def __init__(self, slot_length, slot_start, slot_end):
        self.slot_length = slot_length
        self.slot_start = slot_start
        self.slot_end = slot_end

    def __lt__(self, other):
        return self.slot_length < other.slot_length

    def __repr__(self):
        return str(self.slot_length)
    def __str__(self):
        return str(self.slot_length)


def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return




def add_new_fog(fog_ip):
    FOGS_AND_FREE_SLOTS_MAP[fog_ip] = []
    heapq._heapify_max(FOGS_AND_FREE_SLOTS_MAP[fog_ip])


def add_free_slot_to_fog(fog_IP, slot_interval, slot_start, slot_end):
    FOGS_AND_FREE_SLOTS_MAP[fog_IP].append(FogSlot(slot_interval, slot_start, slot_end))
    heapq._heapify_max(FOGS_AND_FREE_SLOTS_MAP[fog_IP])

def find_longest_free_slot(fog_IP):
    print(heapq._heappop_max(FOGS_AND_FREE_SLOTS_MAP[fog_IP]))
'''



'''
# TEST RUN
add_new_fog('12.25.45.27')
add_free_slot_to_fog('12.25.45.27', 5, 23.4, 28.9)
add_free_slot_to_fog('12.25.45.27', 7, 98.5, 65.4)
add_free_slot_to_fog('12.25.45.27', 9, 20.5, 24.6)
add_free_slot_to_fog('12.25.45.27', 1, 11.9, 90.5)
add_free_slot_to_fog('12.25.45.27', 3, 87.4, 80.3)

show_tree(FOGS_AND_FREE_SLOTS_MAP['12.25.45.27'])

find_longest_free_slot('12.25.45.27')
find_longest_free_slot('12.25.45.27')
'''



class SlotNode():
    def __init__(self,fog_ip,  slot_start, slot_end):
        self.fog_ip = fog_ip
        self.start = slot_start
        self.end = slot_end
        self.status = None

def add_new_fog(fog_ip):
    FOGS_AND_FREE_SLOTS_MAP[fog_ip] = []

def update_free_slot_fog(fog_ip, free_slot_list):
    # sort free_slot_list by start time

    for slot in free_slot_list:
        FOGS_AND_FREE_SLOTS_MAP[fog_ip].append(SlotNode(fog_ip, slot[0], slot[1]))


def alternate_fog_slot(task_details, c, size):
    i = 0

    # this is assuming properties.fogs has fog metadata sorted according to ascending cost of execution
    for fog in properties.fogs:      #
        for slot in FOGS_AND_FREE_SLOTS_MAP[fog.fog_ip]:
            if(slot.end <= time.time()):
                FOGS_AND_FREE_SLOTS_MAP[fog.fog_ip].remove(slot)        # delete the slot
            else:
                start = max(time.time() + properties.Cloud_timeout + (c + size/properties.bandwidth_fog_fog + properties.latency), slot.start)
                condition1 = start + task_details.length_wrt_base/properties.FOG_METADATA[fog_ip]["no_of_cores"] <= task_details.sub_deadline
                condition2 = start + task_details.length_wrt_base/properties.FOG_METADATA[fog_ip]["no_of_cores"] <= slot.end

                if(condition2 and condition1):
                    ALTERNATE_FOGS.append(fog.fog_ip)

                if(slot.start < time.time()):
                    slot.start = time.time()

        i += 1
        if(i == properties.m):           #take only properties.m cheapest
            break


    return ALTERNATE_FOGS






















