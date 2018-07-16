from AbstractTask import AbstractTask
import traceback


class Join(AbstractTask):
    timestampField = 0
    doneSetup = False

    schemaMap = {}

    def setup(self,p_):
        return

    def doTaskLogic(self,map):
        m = map[AbstractTask.DEFAULT_KEY]
        try:
            print("")
        except:
            print(traceback.print_exc())



