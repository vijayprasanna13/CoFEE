from AbstractTask import AbstractTask
import configparser
import threading
import re
import json

class CsvToSenMLParse(AbstractTask):
    timestampField = 0
    sampledata = ""
    useMsgField = 0
    schemaMap = {}

    def setup(self):
        lock = threading.Lock()
        yield from lock
        config = configparser.ConfigParser()
        schemaFilePath = config.get("PARSE.CSV_SCHEMA_WITH_ANNOTATEDFIELDS_FILEPATH")
        self.useMsgField = config.get("PARSE.CSV_SENML_USE_MSG_FIELD")

        try:
            fo = open(schemaFilePath,"rw+")

            column = fo.readline()
            unit = fo.readline()
            type = fo.readline()

            columns = re.split(",",column)
            units = re.split(",",unit)
            types = re.split(",",type)

            for i in range(0,len(columns)):
                if(columns[i] == "timestamp"):
                    self.timestampField = i

                self.schemaMap[i] = columns[i]+','+units[i]+','+types[i]
        except(IOError):
            print("Error")

        sampledata = "024BE2DFD1B98AF1EA941DEDA63A15CB,9F5FE566E3EE57B85B723B71E370154C,2013-01-14 03:57:00,2013-01-14 04:23:00,200,10,-73.953178,40.776016,-73.779190,40.645145,CRD,52.00,0.00,0.50,13.00,4.80,70.30,uber,sam,Houston";

        lock.release()


    def doTaskLogic(self):
        obj = {}
        jsonArray = []

        try:
            if(self.useMsgField == -1):
                m = self.sampledata
            else:
                m = str(map[AbstractTask.DEFAULT_KEY])

            val = re.split(',',m)
            finalSenML = {}
            finalSenML["bt"] = val[self.timestampField]

            for i in range(len(self.schemaMap)):
                sch = re.split(',',self.schemaMap.get(i))
                if(i != self.timestampField):
                    obj["n"] = sch[0]
                    obj[sch[2]] = val[i]
                    obj["u"] = sch[1]
                    jsonArray += obj


            finalSenML["e"] = jsonArray
            self.setLastResult(str(finalSenML))
            return None

        except():
            print("Error")







