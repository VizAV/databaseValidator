from validateFormat.utils import assignValues,convertCells

class Validator():
    def __init__(self,validatorFile):
        self.validator=validatorFile
        self.errorFile = []

    def convertStringToDataTypes(self):
        for key in list(self.validator.keys()):
            try:
                self.validator[key] = assignValues(self.validator[key])
            except NameError as e:
                print(e.__str__(), ' in key: ', key, '. Proceeding with other keys')
                del self.validator[key]
        return

    def filterDataFile(self,row):
        for key in list(row.keys()):
            if key not in list(self.validator.keys()):
                del row[key]

        return row

    def convertData(self,row):
        errorRow={}
        for key,value in self.validator.items():
            if key in list(row.keys()):
                row[key],errorRow[key] = convertCells[value['type']](row[key])

                if value['type']=='list':
                    errorRow[key]=[]
                    try:
                        for cellElem in range(len(row[key])):
                            row[key][cellElem],error=convertCells[value['element']['type']](row[key][cellElem])
                            errorRow[key].append(error)
                    except Exception as e:
                        row[key] = None
                        errorRow[key]='List Length Zero'
            else:
                errorRow[key] = 'Not present in inputFile'

        self.errorFile.append(errorRow)
        return row

    def transform(self,row):

        row = self.filterDataFile(row)

        row = self.convertData(row)

        return row

