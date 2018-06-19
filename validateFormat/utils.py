from datetime import datetime

import ast
def assignValues(value):
    value["type"] = eval(value["type"])
    if value["type"] == list:
        value["element"] = assignValues(value["element"])
    if value["type"] == object:
        for subKey, subValue in value['element'].items():
            value["element"][subKey] = assignValues(subValue)
    return value

def convertStringToString(cell):
    return cell,None
def convertStringToFloat(cell):
    return float(cell),None
def convertStringToList(cell):

    try:
        cell = ast.literal_eval(cell)
        return cell,None
    except:
        errorcell = 'Cant convert to List'
        cell = None
        return cell,errorcell

    # for val in range(len(cell)):
    #     for format in ['%d-%m-%Y','%d/%m/%y','%d-%b %y']:
    #         try:
    #             cellValue = datetime.strptime(cell[val],format)
    #             break
    #         except:
    #             cellValue = 'date format not compatible'
    #             continue
    #     cell[val] = cellValue
    # return cell

def convertStringToDatetime(cell):
    for format in ['%d-%m-%Y', '%d/%m/%y', '%d %b %y']:
        try:
            value = datetime.strptime(cell, format)
            errorCell=None
            break
        except:
            value = None
            errorCell = 'Datetime format Not acceptable'
            continue

    cell = value

    return cell,errorCell
def convertStringToObject():
    pass

convertCells = {
    'str':convertStringToString,
    'float':convertStringToFloat,
    'list':convertStringToList,
    'datetime':convertStringToDatetime,
    'object':convertStringToObject
}