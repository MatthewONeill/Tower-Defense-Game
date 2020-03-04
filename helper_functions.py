#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

import csv

#### ====================================================================================================================== ####
#############                                          CSV_LOADER                                                  #############
#### ====================================================================================================================== ####

def csv_loader(filename, readall=False):
    ''' Helper function that reads in a CSV file. Optional flag for including header row.
    Input: filename (string), bool_flag (optional)
    Output: List of Rows (comma separated)
    '''
    returnList = []
    with open(filename) as csvfile:
        for row in csv.reader(csvfile):
            returnList.append(row)
    if readall:
        return returnList
    else:
        return returnList[1:]