from reArrangeFormat.reArrangeProcess import reArrangeData
from validateFormat.validateProcess import validateData
if __name__ =="__main__":
    validatedData = validateData(False)
    print(reArrangeData(validatedData))