from hexadecimalToBinary import hexadecimalToBinary
import pandas as pd
import re
import mysql.connector
from dbConfig import dbConfig

# this function receives a bitmap, and return all the present fields
# either hexadecimal or binary inputs are accepted
def bitMapper(isoString):

    # # code to run in case an xls file is necessary to be used
    # sheetName = "ISO - todos"
    # fileLocation = "files\infotable.xls"
    #
    # # array to access info from fields's data elements
    # de = pd.read_excel(fileLocation, index_col=0, sheet_name=sheetName)
    # dataElements = []
    # for i in de.index:
    #     dataElements.append(i)
    #
    # # array to access info from fields's length
    # legt = pd.read_excel(fileLocation, index_col=1, sheet_name=sheetName)
    # length = []
    # for i in legt.index:
    #     length.append(i)
    #
    # # array to access info from fields's description
    # desc = pd.read_excel(fileLocation, index_col=2, sheet_name=sheetName)
    # description = []
    # for i in desc.index:
    #     description.append(i)
    #
    # # getting binary code by calling hexadecimalToBinary external function
    # binaryString = HexadecimalToBinary(ISOString)
    #
    # # array to be filled and returned when calling BitMapper function
    # bitMapInfo = []
    #
    # for index, i in enumerate(binaryString):
    #
    #     # statement to save field if present
    #     if int(i) == 1:
    #         item = []
    #         item.append(dataElements[int(index)])
    #         item.append(length[int(index)])
    #         item.append(description[int(index)])
    #         bitMapInfo.append(item)
    #
    # return bitMapInfo

    # function to get database data from config file
    dbdata = dbConfig('./files/config.ini')

    connection = mysql.connector.connect(
        host=dbdata['host'],
        user=dbdata['user'],
        password=dbdata['password'],
        database=dbdata['database']
    )

    cursor = connection.cursor()
    query = f'SELECT element_log_iso, length_log_iso, description_log_iso FROM log_iso'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    # getting binary code by calling hexadecimalToBinary external function if string parameter isn't binary already
    try:
        binaryString = isoString
    except:
        binaryString = HexadecimalToBinary(isoString)


    # array to return information
    bitMapInfo = []

    for index, i in enumerate(binaryString):

        # statement to save field if present
        if int(i) == 1 and result[index][0] != 1:
            bitMapInfo.append(result[index])

    return bitMapInfo