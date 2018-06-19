from validateFormat.readWriteOperations import read,write
from validateFormat.validator import Validator


def validateData(isWriteErrorFile=True):

    validatatedData = []
    dataFile,validatorFile = read()

    #initialize the validator
    validatorObj = Validator(validatorFile)

    #Get the data types from the input file
    # validatorObj.convertStringToDataTypes()

    for row in dataFile:
        validatatedData.append(validatorObj.transform(row))

    if isWriteErrorFile: write(validatorObj.errorFile)

    return validatatedData

