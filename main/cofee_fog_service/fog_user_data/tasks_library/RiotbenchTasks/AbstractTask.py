from abc import ABC, abstractmethod
import logging, time

class AbstractTask(ABC):
    DEFAULT_KEY = "D"

    def __init__(self):
        self.t = 0
        self.counter = 0
        self.lastResult = None

    @abstractmethod
    def setup(self,p_):
        self.t = 0
        self.counter = 0
        logging.debug("Finished Task Setup")

    def setLastResult(self, r):
        self.lastResult = r
        return self.lastResult


    def doTask(self,map):
        self.t = time.time()
        result = self.doTaskLogic(map)
        assert result>=0
        self.counter += 1
        return result

    def getLastResult(self):
        return self.lastResult


    def tearDown(self):
        self.t = time.time() - self.t
        logging.debug("Finished Task TearDown")
        return (self.t/self.counter)

    @abstractmethod
    def doTaskLogic(self, map):
        return