from AbstractTask import AbstractTask
import configparser
import threading
from collections import deque
from Utils.TimeStampValue import TimeStampValue
import re

class Annotate(AbstractTask):
    annotationMap = {}
    filePath = ''
    useMsgField = None

    def setup(self,p_):
        config = configparser.ConfigParser({'nothingThere': '0'})
        self.annotationMap = {}
        try:
            lock = threading.Lock()
            yield from lock

            self.useMsgField = (int)(config['ANNOTATE.ANNOTATE_MSG_USE_FIELD'], 'nothingThere')
            self.filePath += config['ANNOTATE.ANNOTATE_FILE_PATH']

            fo = open(self.filePath,'rw+')

            for line in fo:
                annotation = re.split(':',line)
                assert len(annotation) == 2
                self.annotationMap[annotation[0]] = annotation[1]

            lock.release()

        except(IOError):
            print("Error")

    def doTaskLogic(self,map):
        ini = (map[AbstractTask.DEFAULT_KEY])
        annotateKey = re.split(",",ini)[self.useMsgField]

        annotation = self.annotationMap.get(annotateKey)

        if(annotation != None):
            annotatedValue = (ini + ',' + annotation)
            self.setLastResult(annotatedValue)

        return 0.0








