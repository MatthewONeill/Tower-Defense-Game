#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

from helper_functions import *
import pygame

#### ====================================================================================================================== ####
#############                                          MAP_CLASS                                                   #############
#### ====================================================================================================================== ####

class Map:
    ''' Map Class - represents a single Map Object. '''
    # Represents common data for all Maps - only loaded once, not per new Map (Class Variable)
    legend_data = {}
    for legend in csv_loader("data/legend.csv"):
        legend_data[legend[0]] = { "type": legend[1], "sprite": legend[2] }
    def __init__(self, settings):
        ''' Initialization for Map.
        Input: Settings Oject
        Output: A Map Object
        '''
        self.map_data = {}
        row = 0; col = 0
        for cell_row in csv_loader("data/map.csv", readall=True):
            for cell_col in cell_row:
                if len(cell_col) > 1:
                    cell_col = cell_col[-1]
                self.map_data[(col, row)] = { "value": cell_col, "sprite": pygame.transform.scale(pygame.image.load(Map.legend_data[cell_col]["sprite"]), settings.tile_size) }
                col += 1
            row += 1; col = 0

#### ====================================================================================================================== ####
#############                                        MAP_FUNCTIONS                                                 #############
#### ====================================================================================================================== ####

def render_map(map, screen, settings):
    ''' Helper function that renders the Map.
    Input: Map Object, screen (pygame display), Settings Object
    Output: None
    '''
    for cell in map.map_data:
        screen.blit(map.map_data[cell]["sprite"], [cell[0] * settings.tile_size[0], cell[1] * settings.tile_size[1]])

def check_location(map, settings, location):
    # Replace this with code for checking a given location for tower placement
    pass # Remove this once you've completed the code