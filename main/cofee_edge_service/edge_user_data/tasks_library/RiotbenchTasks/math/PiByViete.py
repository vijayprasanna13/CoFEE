from AbstractTask import AbstractTask
import configparser
import threading
import traceback
import math

class PiByViete(AbstractTask):
    iteration = 0

    def setup(self,p_):
        config = configparser.ConfigParser({'nothingThere': '1600'})
        try:
            lock = threading.Lock()
            yield from lock

            self.iteration = (int)(config["MATH.PI_VIETE.ITERS"],'nothingThere')
            assert self.iteration>=0
            lock.release()

        except(IOError):
            print(traceback.print_exc())


    def doTaskLogic(self,map):
        m= str(map[AbstractTask.DEFAULT_KEY])
        result = self.getPiByViete(self.iteration)
        return result


    def getPiByViete(self,n):
        pi = 1

        for i in range(2,n,-1):
            f = 2
            for j in range(1,i,1):
                f = 2 + math.sqrt(f)

            f = math.sqrt(f)
            pi = pi * f/2

        pi *= math.sqrt(2)/2
        pi = 2.0/pi
        return pi



