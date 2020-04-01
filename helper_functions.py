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

def checkBoss(enemies):
    for enemy in enemies:
        if enemy.name=="Blue Flame":
            print("enemy here")
            print(enemy.location)
            return True
    return False

def buy_item(game_data, tower):
    '''removes price of tower from total currency
    Input: game_data, tower (name of tower as a string)
    Output: nothing'''
    game_data["current_currency"] -= game_data["shop"].shop_data[tower]["cost"]

def receive_currency(game_data):
    '''adds given amount to total currency
    Input: game_data, amount
    Output: nothing'''
    game_data["current_currency"] += 10