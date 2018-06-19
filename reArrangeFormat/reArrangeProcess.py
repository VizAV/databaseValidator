from reArrangeFormat.readWriteOperations import read
from reArrangeFormat.reArranger import ReArranger

def reArrangeData(data):
    reArrangedData=[]
    reArrangeFile = read()

    reArrangeObj = ReArranger(reArrangeFile)


    for row in data:

        # We need to get the tuple thingy here, The transformation along with the ID generation
        #Check sakthivel's json format and get this thing done
        correctedRow = reArrangeObj.correctFormat(row)
        reArrangedData.append(reArrangeObj.transform(correctedRow))

    return reArrangedData

