'''
Helper class
'''

class TimeStampValue:

    def __init__(self,value,ts):
        self.__value__ =  value
        self.__ts__ =  ts

    def comparable(self,tsv):
        return self.__ts__ - tsv.ts






