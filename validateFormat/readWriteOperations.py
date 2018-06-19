from config import path,testSet
import pandas as pd
import json

def read():
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path

    try:  # Read the input file and the validator file

        dataFile = pd.read_csv(testSet+'/data.csv', encoding='ISO-8859-1')
        dataFile = dataFile.to_dict(orient='records')
        validatorFile = json.load(open(path+'/dataTypeValidator.json'))

        return dataFile, validatorFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()

def write(file):
    outPutFile = pd.DataFrame(file)
    outPutFile.to_csv(path+'/errorFile.csv')
