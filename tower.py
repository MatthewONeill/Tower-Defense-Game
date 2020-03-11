#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

from helper_functions import *
import pygame
import math

#### ====================================================================================================================== ####
#############                                         TOWER_CLASS                                                  #############
#### ====================================================================================================================== ####

class Tower:
    ''' Tower Class - represents a single Tower Object. '''
    # Represents common data for all towers - only loaded once, not per new Tower (Class Variable)
    tower_data = {}
    for tower in csv_loader("data/towers.csv"):
        tower_data[tower[0]] = { "sprite": tower[1], "damage": int(tower[2]), "rate_of_fire": int(tower[3]), "radius": int(tower[4]) }
    def __init__(self, tower_type, location):
        ''' Initialization for Tower.
        Input: tower_type (string), location (tuple)
        Output: A Tower Object
        '''
        self.name = tower_type
        self.sprite = pygame.image.load(Tower.tower_data[tower_type]["sprite"]).convert_alpha()
        
        self.radius = Tower.tower_data[tower_type]["radius"]
        self.damage = Tower.tower_data[tower_type]["damage"]
        self.rate_of_fire = Tower.tower_data[tower_type]["rate_of_fire"]
        self.location = location
        self.isClicked = False
        self.timer = 0
        self.inRange = False
        self.enemy = None

#### ====================================================================================================================== ####
#############                                       TOWER_FUNCTIONS                                                #############
#### ====================================================================================================================== ####

def update_tower(tower, clicked, game_data):

    check_enemy(tower, game_data)



def check_enemy(tower, game_data):
    for enemy in game_data["enemies"]:
        distance = math.sqrt((enemy.location[0] - tower.location[0])**2 + (enemy.location[1] - tower.location[1])**2) #distance between enemy and tower
        if (distance <= tower.radius): #enemy is in range
            tower.inRange = True
            tower.enemy = enemy
            attack_enemy(tower, enemy, game_data)
        else:
            tower.inRange = False
            #draw a line ->probably call a function
            #call an attack function

def attack_enemy(tower, enemy, game_data):
    if(tower.timer == 10):
        tower.timer = 0
        enemy.health -= tower.damage
        if(enemy.health <= 0):
            game_data["enemies"].remove(enemy)
    else:
        tower.timer += tower.rate_of_fire

def draw_line(tower, enemy, game_data):
    pygame.draw.line(game_data["screen"], (0,0,0), (tower.location[0], tower.location[1]), (enemy.location[0]-20, enemy.location[1]-20), 10)


def render_tower(tower, screen, settings):
    ''' Helper function that renders a single provided Tower.
    Input: Tower Object, screen (pygame display), Settings Object
    Output: None
    '''
    screen.blit(tower.sprite, tower.location)
