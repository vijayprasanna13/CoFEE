'''
Partition filter
'''

import time
from datetime import datetime, timedelta
'''
def partition_query(t_b,t_e):    # t_b and t_e is in epoch
	last_hour_epoch = datetime.now() - timedelta(hours = 1) # assuming 1 hour updation time in index
	#print last_hour_date_time
	#print time.mktime(last_hour_date_time.timetuple()) + last_hour_date_time.microsecond * 1e-6
	current_epoch = time.time()
	print(current_epoch)
    
	if(t_e < last_hour_epoch):
        pass    # pastQuery
	else:
        pass    # deltaQuery
'''