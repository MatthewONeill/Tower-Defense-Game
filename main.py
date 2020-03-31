
#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

from helper_functions import *
from settings import *
from shop import *
from tower import *
from gui import *
from enemy import *
from map import *
import pygame
import sys

#### ====================================================================================================================== ####
#############                                         INITIALIZE                                                   #############
#### ====================================================================================================================== ####

def initialize():
    ''' Initialization function - initializes various aspects of the game including settings, shop, and more.
    Input: None
    Output: game_data dictionary
    '''
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("COMP 1501 - Tutorial 7: Tower Defense (TD) Base Code")

    # Initialize the Settings Object
    settings = Settings()

    # Initialize game_data and return it
    game_data = { "screen": pygame.display.set_mode(settings.window_size),
                  "current_currency": settings.starting_currency,
                  "current_wave": 0,
                  "stay_open": True,
                  "selected_tower": None,
                  "clicked": False,
                  "settings": settings,
                  "towers": [],
                  "enemies": [],
                  "shop": Shop("Space", settings),
                  "gui": Gui(),
                  "map": Map(settings),
                  "frame_rate": 40,
                  "time_counter": 0,
                  "enemy_list": ["Lesser Alien", "Lesser Alien", "Lesser Alien", "Alien", "Alien", "Alien",
                                              "Greater Alien", "Greater Alien", "Elder Alien", "Elder Alien", "Larry"],
                  "enemy_index": 0,
                  "spawn_interval": 0,
                  "endGame": 100}

    game_data["gui"].setShop(game_data["shop"]);
    game_data["gui"].setData(game_data);

    return game_data

#### ====================================================================================================================== ####
#############                                           PROCESS                                                    #############
#### ====================================================================================================================== ####

def process(game_data):
    ''' Processing function - handles all form of user input. Raises flags to trigger certain actions in Update().
    Input: game_data dictionary
    Output: None
    '''
    events=pygame.event.get()
    for event in events:

        # Handle [X] press
        if event.type == pygame.QUIT:
            game_data["stay_open"] = False

        # Handle Mouse Button Down
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_data["clicked"] = True
            game_data["selected_tower"] = False

        # Handle Mouse Button Up
        if event.type == pygame.MOUSEBUTTONUP:
            game_data["clicked"] = False
            
    game_data["gui"].process(events)

#### ====================================================================================================================== ####
#############                                            UPDATE                                                    #############
#### ====================================================================================================================== ####

def update(game_data):
    ''' Updating function - handles all the modifications to the game_data objects (other than boolean flags).
    Input: game_data
    Output: None
    '''
    update_shop(game_data["shop"], game_data["current_currency"], game_data["settings"])
    game_data["gui"].update()

    for towers in game_data["towers"]:
        update_tower(towers, game_data)

    ## Replace this with code to update the Enemies ##
    if game_data["spawn_interval"] == 0 and game_data["enemy_index"] != 11:
        #spawn enemy
        game_data["enemies"].append(Enemy(game_data["enemy_list"][game_data["enemy_index"]], (1, 0)))
        game_data["spawn_interval"] = 6 #reset spawn_interval
        if game_data["enemy_index"] < 11:
            game_data["enemy_index"] += 1

    for enemy in game_data["enemies"]:
        if enemy.health <= 0:
            receive_currency(game_data)
            downgrade_enemy(enemy, game_data)
            game_data["enemies"].remove(enemy)
        else:
            update_enemy(enemy, game_data)
           

    if game_data["time_counter"] == game_data["frame_rate"]:
        # 1 second
        game_data["spawn_interval"] -= 1
        game_data["time_counter"] = 0 # reset time_counter
    else:
        game_data["time_counter"] += 1

    if(game_data["endGame"] <= 0):
        print("You Lost")
        exit()

    ## Replace this with code to update the Towers ##
    print(game_data["endGame"])
    # Remove this once you've implemented 'update()'

#### ====================================================================================================================== ####
#############                                            RENDER                                                    #############
#### ====================================================================================================================== ####

def render(game_data):
    ''' Rendering function - displays all objects to screen.
    Input: game_data
    Output: None
    '''
    render_map(game_data["map"], game_data["screen"], game_data["settings"])
   
    for enemy in game_data["enemies"]:
        render_enemy(enemy, game_data["screen"], game_data["settings"])
    for tower in game_data["towers"]:
        render_tower(tower, game_data["screen"], game_data["settings"])
        if(tower.inRange == True):
            draw_line(tower, tower.enemy, game_data)
            
    render_shop(game_data["shop"], game_data["screen"], game_data["settings"], game_data["current_currency"])
    game_data["gui"].render(game_data);
    pygame.display.update()

#### ====================================================================================================================== ####
#############                                             MAIN                                                     #############
#### ====================================================================================================================== ####

def main():
    ''' Main function - initializes everything and then enters the primary game loop.
    Input: None
    Output: None
    '''
    # Initialize all required variables and objects
    game_data = initialize()
    clock = pygame.time.Clock()

    # Begin Central Game Loop
    while game_data["stay_open"]:
        process(game_data)
        update(game_data)
        render(game_data)
        
        clock.tick(game_data["frame_rate"])

    # Exit pygame and Python
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
