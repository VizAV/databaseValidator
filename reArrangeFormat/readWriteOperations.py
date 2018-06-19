import json
import os
def read():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path

    try:  # Read the input file and the validator file
        reArrangeFile = json.load(open( path+'/reArrangeFile.json'))
        return reArrangeFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()
