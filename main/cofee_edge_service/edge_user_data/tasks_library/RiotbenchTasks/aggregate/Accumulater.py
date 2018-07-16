from AbstractTask import AbstractTask
import configparser
import threading
from collections import deque
from Utils.TimeStampValue import TimeStampValue
import re

class Accumulater(AbstractTask):

    def __init__(self):
        self.valuesMap = {}
        self.tupleWindowsSize = 0
        self.counter = 0
        config = configparser.ConfigParser()

    def setup(self,p_):
        lock = threading.Lock()
        yield from lock
        config = configparser.ConfigParser()
        self.tupleWindowsSize = config.get("VISUALIZE.TUPLE_WINDOW_SIZE")
        lock.release()

    def doTaskLogic(self, map):
        sensorId = map.get("SENSORID")
        meta = map.get("META")
        obsVal = map.get("OBSVALUE")
        obsType = map.get("OBSTYPE")
        ts = map.get("TS")

        innerHashMap = {}
        queue = deque()     # queue of TimeStamp values
        queue = None

        self.counter += 1

        key = ''
        key += sensorId
        key += obsType

        innerHashMap = self.valuesMap.get(key)

        if(innerHashMap == None):
            innerHashMap[meta] = queue
            self.valuesMap[key] = innerHashMap

        queue = innerHashMap[meta]
        if(queue==None):
            queue = deque()
            innerHashMap[meta] = queue

        if(obsType == "SLR"):
            predValues = re.split('#',obsVal)
            for s in predValues:
                tsVal = TimeStampValue(s, ts)
                queue.append(tsVal)
        else:
            tsVal = TimeStampValue(obsVal,ts)
            queue.append(tsVal)

        innerHashMap[meta] = queue
        self.valuesMap[key] = innerHashMap

        if(self.counter == self.tupleWindowsSize):
            self.setLastResult(self.valuesMap)
            self.valuesMap = {}
            self.counter = 0
            return 1.0
        else:
            return 0.0
        














