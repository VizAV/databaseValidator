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

def convertStringToString(cell,value):
    return cell
def convertStringToFloat(cell,value):
    return float(cell)
def convertStringToList(cell,value):
    if value["element"]['type'] != 'datetime':
        cell = ast.literal_eval(cell)
    else:
        cell = ast.literal_eval(cell)
        for val in range(len(cell)):
            cell[val] = datetime.strptime(cell[val], '%d-%m-%y')
    return cell
def convertStringToDatetime(cell,value):

    cell = datetime.strptime(cell, '%d/%m/%y')
    return cell
def convertStringToObject():
    pass

convertCells = {
    'str':convertStringToString,
    'float':convertStringToFloat,
    'list':convertStringToList,
    'datetime':convertStringToDatetime,
    'object':convertStringToObject
}