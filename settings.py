#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

from helper_functions import *
from ast import literal_eval
import pygame

#### ====================================================================================================================== ####
#############                                        SETTINGS_CLASS                                                #############
#### ====================================================================================================================== ####

class Settings:
    ''' Settings Class - represents a single Setting Object. '''
    # Represents common data for all settings - only loaded once, not per new Setting (Class Variable)
    setting_data = {}
    for setting in csv_loader("data/settings.csv"):
        setting_data[setting[0]] = { "starting_currency": setting[1], 
                                     "waves": setting[2], 
                                     "enemy_modifier": setting[3], 
                                     "framerate": setting[4], 
                                     "font": setting[5], 
                                     "window_size": setting[6], 
                                     "tile_size": setting[7] }
    def __init__(self, difficulty="Default"):
        ''' Initialization for Setting.
        Input: difficulty level (string, default="Default")
        Output: A Settings Object
        '''
        self.starting_currency = int(Settings.setting_data[difficulty]["starting_currency"])
        self.num_waves = int(Settings.setting_data[difficulty]["waves"])
        self.enemy_modifier = float(Settings.setting_data[difficulty]["enemy_modifier"])
        self.framerate = int(Settings.setting_data[difficulty]["framerate"])
        self.font = pygame.font.Font(Settings.setting_data[difficulty]["font"], 25)
        self.title_font = pygame.font.Font(Settings.setting_data[difficulty]["font"], 45)
        self.window_size = literal_eval(Settings.setting_data[difficulty]["window_size"])
        self.tile_size = literal_eval(Settings.setting_data[difficulty]["tile_size"])

#### ====================================================================================================================== ####
#############                                       SETTINGS_FUNCTIONS                                             #############
#### ====================================================================================================================== ####