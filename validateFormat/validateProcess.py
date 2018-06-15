from validateFormat.readWriteOperations import read
from validateFormat.validator import Validator

def validateData(path):

    dataFile,validatorFile = read(path)

    #initialize the validator
    validatorObj = Validator(validatorFile)

    #Get the data types from the input file
    # validatorObj.convertStringToDataTypes()

    for row in dataFile:
        print(validatorObj.transform(row))

    return

