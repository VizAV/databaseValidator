import json
from config import path,testSet
def read():

    try:  # Read the input file and the validator file
        reArrangeFile = json.load(open( path+testSet+'/reArrangeFile.json'))
        return reArrangeFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()
