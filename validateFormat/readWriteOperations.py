from config import path,testSet,filename
import pandas as pd
import json

def read():
    import os


    try:  # Read the input file and the validator file

        dataFile = pd.read_csv(path+testSet+filename, encoding='ISO-8859-1')
        dataFile = dataFile.to_dict(orient='records')
        validatorFile = json.load(open(path+testSet+'/dataTypeValidator.json'))

        return dataFile, validatorFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()

def write(file,filename):
    outPutFile = pd.DataFrame(file)
    outPutFile.to_csv(path+testSet+'/'+filename)
