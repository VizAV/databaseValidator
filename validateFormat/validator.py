
from validateFormat.utils import assignValues,convertCells



class Validator():
    def __init__(self,validatorFile):
        self.validator=validatorFile

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
        for key,value in self.validator.items():
            row[key] = convertCells[value['type']](row[key],value)
        return row
    def transform(self,row):

        row = self.filterDataFile(row)

        row = self.convertData(row)


        return row







