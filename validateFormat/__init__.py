from validateFormat.validateProcess import validateData
import pandas as pd
if __name__ =="__main__":

    pd.DataFrame(validateData(True)).to_csv('successFile.csv')