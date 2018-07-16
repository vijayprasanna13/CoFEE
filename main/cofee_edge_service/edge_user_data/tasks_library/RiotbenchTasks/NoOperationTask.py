import AbstractTask
import threading


class NoOperationTask(AbstractTask):
    def setup(self):
        lock = threading.Lock()


        lock.release()

    def doTaskLogic(self,map):
        return 0.0
