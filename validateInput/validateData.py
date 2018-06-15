import pandas as pd
from datetime import datetime
import json
# Args: The path of the input File and template file

class Validator():
    def __init__(self,validatorFile):
        self.validatorFile=validatorFile

    def convertStringToDataTypes(self):
        for key, value in self.validatorFile.items():
            try:
                self.validatorFile[key] = assignValues(value)
            except NameError as e:
                print(e.__str__(), ' in key: ', key, '. Proceeding with other keys')
                self.validatorFile.pop(key, None)
        return

    def filterDataFile(self,row):
        for key in list(row.keys()):
            if key not in list(self.validatorFile.keys()):
                del row[key]
        return row

    def convertFormat(self,row):

        #remove columns not in our validator
        row = self.filterDataFile(row)

        return row

def readData(path):
    try:  # Read the input file and the validator file

        dataFile = pd.read_csv(path+'/data.csv', encoding='ISO-8859-1')
        dataFile = dataFile.to_dict(orient='records')
        validatorFile = json.load(open( path+'/dataTypeValidator.json'))

        return dataFile, validatorFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()




def assignValues(value):
        value["type"] = eval(value["type"])
        if value["type"] == list:
            value["element"]= assignValues(value["element"])
        if value["type"] == object:
            for subKey,subValue in value['element'].items():
                value["element"][subKey]=assignValues(subValue)
        return value

def validateData(path):

    dataFile,validatorFile = readData(path)

    #initialize the validator
    validatorObj = Validator(validatorFile)

    #Get the data types from the input file
    validatorObj.convertStringToDataTypes()

    for row in dataFile:
       print( validatorObj.convertFormat(row))



    return


if __name__ =="__main__":
    from config import path

    validateData(path)
