import json
import re
import traceback
from datetime import datetime
class Utils:

    def __init__(self,schemaFilePath):
            self.schemaMap = {}
            self.timestampField = 0

            try:
                fo = open(schemaFilePath,'rw+')
                column = fo.readline()
                unit = fo.readline()
                type = fo.readline()
                columns = re.split(',',column)
                units = re.split(',',unit)
                types = re.split(',',type)
                fo.close()

                for i in range(len(columns)):
                    if(columns[i] == "timestamp"):
                        self.timestampField = i
                    self.schemaMap[i] = columns[i]+","+units[i]+","+types[i]

                print("In Utils,Size of hash map ", len(self.schemaMap))

            except:
                print(traceback.print_exc())


    def csvToSenML(self,s):
        jsonArr = []
        jsonObj = {}
        try:
            val = re.split(",",s)
            finalSenML = {}
            d = datetime(val[self.timestampField])
            finalSenML['bt'] = d.time()
            for i in range(len(self.schemaMap)):
                sch = re.split(",",self.schemaMap[i])
                if(i != self.timestampField):
                    jsonObj["n"] = sch[0]
                    jsonObj[sch[2]] = val[i]
                    jsonObj["u"] = sch[1]
                    jsonArr.append(jsonObj)

            finalSenML["e"] = jsonArr
            return finalSenML

        except:
            print(traceback.print_exc())


        

if __name__  ==  "__main__":
    util = Utils("pathtofile")
    # read the data file
    try:
        fo = open("pathtofile",'rw+')
        s = fo.readline()
        while s!=None:
            util.csvToSenML(s)
            s = fo.readline()

    except:
        print("error")

