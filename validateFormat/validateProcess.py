from validateFormat.readWriteOperations import read,write
from validateFormat.validator import Validator


def validateData(isWriteErrorFile=True,isWriteSuccessFile=True):

    validatedData=[]
    errorData=[]
    dataFile,validatorFile = read()

    #initialize the validator
    validatorObj = Validator(validatorFile)

    #Get the data types from the input file
    # validatorObj.convertStringToDataTypes()

    for row in dataFile:
        validatedRow,errorRow = validatorObj.transform(row)
        validatedData.append(validatedRow)
        errorData.append(errorRow)

    if isWriteErrorFile: write(errorData,'errorData.csv')
    if isWriteSuccessFile: write(validatedData,'successData.csv')

    return validatedData

