import pandas as pd
class ReArranger():
    def __init__(self,reArrangerFile):
        self.reArrangerFile=reArrangerFile
        self.counter =0


    def transform(self,row):

        collectionDict={}
        for collectionKeys,collectionValues in self.reArrangerFile.items():

            reArrangedRow = {}

            for mainKey,mainValue in collectionValues.items():
                if type(mainValue) is not dict and type(mainValue) is not list:
                    reArrangedRow[mainKey]=row[mainKey]
                elif type(mainValue) is dict:
                    reArrangedRow[mainKey]={}
                    for subKey,subValues in mainValue.items():
                        reArrangedRow[mainKey][subKey] = row[subValues]
                elif type(mainValue) is list:
                    reArrangedRow[mainKey] = []
                    for cellValue in row[mainValue]:
                        fundingInfo = {}
                        for subKey, subValue in cellValue.items():
                            fundingInfo[subKey]=row[mainValue][subValue]
                        reArrangedRow[mainKey].append(fundingInfo)

            collectionDict[collectionKeys]=reArrangedRow

        return collectionDict

    def correctFormat(self,row):


        fundingDF = pd.DataFrame({key: row[key] for key in ['roundDate', 'roundInvestmentAmount', 'investorName',
                                                            'startupID']})

        groupedDF = fundingDF.groupby(['roundDate']).agg({
            'investorName': lambda x: list(x),
            'roundInvestmentAmount': 'first',
            'startupID': 'first'
        })

        fundingInfo = []
        for index,rowDF in groupedDF.iterrows():
            self.counter+=1
            rowDF['ID'] = 'round'+str("%04d" % self.counter)
            fundingInfo.append(rowDF.to_dict())

        row['fundingInfo']=fundingInfo
        # groupedDP['ID'] = 'round' + str("%04d" % counter)
        # roundGroupDict = dict([(key, val[0]) for key, val in value.items()])
        # roundGroupedList.append(roundGroupDict)


        return row