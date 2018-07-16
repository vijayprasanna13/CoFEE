'''
FILE TO HANDLE RESERVED SLOTS
AND FREE SLOTS
'''
import sys
sys.path.append('/home/prasanth/Desktop/CoFEE/src/main/cofee_fog_service/config')
import properties
import time
# SLOT RESERVATIONS IN FOG
'''
TO GUARANTEE THAT A TASK RUNNING ON EDGE CAN COMPLETE IN THIS FOG WITHIN IT'S SUB-DEADLINE, EVEN IF EDGE FAILS
'''

'''
MAINTAIN A LINKED LIST FOR SLOTS
'''

HEAD_SLOT = None
END_TIME = time.time()



class ReservedSlotNode:
    def __init__(self, start, end, task_id, microbatch_id):
        self.start = start
        self.end = end
        self.duration = (self.end - self.start)
        self.task_id = task_id
        self.microbatch_id = microbatch_id
        # add more fields over here regarding micro-batch and metadata
        self.next = None        # next points to next node
        self.prev = None        # prev points to previous node
        self.flag = None
        self.right_checked = None
        self.left_checked = None
        self.is_last_reserved = None
        self.is_checked = None
        self.sub_deadline = None
        self.omega = None

    def next_slot_start(self):
        print(self.next.start)

    def prev_slot_end(self):
        print(self.prev.end)



# initialize node
slot = ReservedSlotNode(-1,-1,-1,-1)
HEAD_SLOT = slot
isfound = 0

def init_uncheck():
    current_slot = HEAD_SLOT
    while(current_slot.next != None):
        current_slot.is_checked = 0


def scout_slot(task_details, omega, sub_deadline, microbatch_id):
    if(HEAD_SLOT.start == -1 and HEAD_SLOT.end == -1):
        EPOCH_CHECKPOINT = time.time()
        HEAD_SLOT.start = omega
        HEAD_SLOT.end = task_details.baseline_execution_time/properties.no_of_cores + omega
        HEAD_SLOT.microbatch_id = microbatch_id
        HEAD_SLOT.task_id = task_details.task_id
        return True

    init_uncheck()
    # case 1
    while(1):
        current = HEAD_SLOT
        max = (-sys.maxsize - 1)
        curr_max_index = -1
        start_time = None
        end_time = None
        avail_duration = None
        while(current.next != None):
            avail_duration = current.next.start - current.end
            if(avail_duration >= max and current.is_checked != 1):
                max = avail_duration
                curr_max_index = current
                start_time = current.end
                end_time = current.next.start
                current.is_checked = 1

        maximum_start_possible = max(start_time, omega)
        condition1 = (maximum_start_possible+float(task_details.baseline_execution_time/properties.no_of_cores) <= end_time)
        condition2 = (maximum_start_possible+float(task_details.baseline_execution_time/properties.no_of_cores) <= sub_deadline)
        if(condition1 and condition2):
            isfound = 1
            reserve_slot(current, start_time, end_time, task_details.task_id, microbatch_id, sub_deadline, omega)
            break

    if(isfound == 1):
            return True

    init_uncheck()
    # case 2
    while(1):
        current = HEAD_SLOT
        max = (-sys.maxsize - 1)
        curr_max_index = -1
        start_time = None
        end_time = None
        while (current.next != None):
            avail_duration = current.next.start - current.end
            if (avail_duration >= max and current.is_checked != 1):
                max = avail_duration
                curr_max_index = current
                start_time = current.end
                end_time = current.next.start
                current.is_checked = 1


        avail_start = curr_max_index.end
        r_delta = min(curr_max_index.next.sub_deadline, curr_max_index.next.next.start)-curr_max_index.next.end
        avail_end = curr_max_index.next.start + r_delta
        maximum_start_possible = max(avail_start, omega)
        condition1 = (maximum_start_possible+float(task_details.baseline_execution_time/properties.no_of_cores) <= end_time)
        condition2 = (maximum_start_possible+float(task_details.baseline_execution_time/properties.no_of_cores) <= sub_deadline)

        if(condition1 and condition2):
            isfound = 1
            curr_max_index.next.start = curr_max_index.next.start + r_delta
            curr_max_index.next.end = curr_max_index.next.end + r_delta

            reserve_slot(curr_max_index, avail_start, avail_end, task_details.task_id, microbatch_id, sub_deadline, omega)
            break



        if(isfound == 1):
            return True

        l_delta = max(curr_max_index.omega, curr_max_index.prev.end)
        avail_start = avail_start - l_delta
        maximum_start_possible = max(avail_start, omega)
        condition1 = (maximum_start_possible+float(task_details.baseline_execution_time/properties.no_of_cores) <= end_time)
        condition2 = (maximum_start_possible+float(task_details.baseline_execution_time/properties.no_of_cores) <= sub_deadline)
        if(condition1 and condition2):
            curr_max_index.start = curr_max_index.start - l_delta
            curr_max_index.end = curr_max_index.end - l_delta
            reserve_slot(curr_max_index, start_time, end_time, task_details.task_id, microbatch_id, sub_deadline, omega)
            isfound = 1
            return True

    if(isfound == 0):
        return False





def reserve_slot(current, start, end, task_id, microbatch_id, sub_deadline, omega):
    new_slot = ReservedSlotNode(start, end, task_id, microbatch_id)
    new_slot.sub_deadline = sub_deadline
    new_slot.omega = omega
    new_slot.prev = current
    new_slot.next = current.next
    current.next.prev = new_slot



# TEST
Node1 = ReservedSlotNode(12.5, 16)
Node2 = ReservedSlotNode(17, 20.5)
Node3 = ReservedSlotNode(21, 25)

Node1.next = Node2
Node2.next = Node3

Node1.traverse()

