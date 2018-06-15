import pandas as pd
import json
def read(path):
    try:  # Read the input file and the validator file

        dataFile = pd.read_csv(path+'/data.csv', encoding='ISO-8859-1')
        dataFile = dataFile.to_dict(orient='records')
        validatorFile = json.load(open( path+'/dataTypeValidator.json'))

        return dataFile, validatorFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()
