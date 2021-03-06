#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

from helper_functions import *
import pygame

#### ====================================================================================================================== ####
#############                                         ENEMY_CLASS                                                  #############
#### ====================================================================================================================== ####

class Enemy:
    ''' Enemy Class - represents a single Enemy Object. '''
    # Represents common data for all enemies - only loaded once, not per new Enemy (Class Variable)
    enemy_data = {}
    for enemy in csv_loader("data/enemies.csv"):
        enemy_data[enemy[0]] = { "sprite": enemy[1], "health": int(enemy[2]), "speed": int(enemy[3]), "tier": int(enemy[4]), "damage": int(enemy[5]) }
    def __init__(self, enemy_type, location):
        ''' Initialization for Enemy.
        Input: enemy type (string), location (tuple of ints)
        Output: An Enemy Object
        '''
        self.realLocation=(0,0)
        self.distance = 0
        self.name = enemy_type
        self.sprite = pygame.image.load(Enemy.enemy_data[enemy_type]["sprite"]).convert_alpha()
        self.health = Enemy.enemy_data[enemy_type]["health"]
        self.speed = Enemy.enemy_data[enemy_type]["speed"]
        self.location = location
        self.direction = None
        self.previous_direction = "down"
        self.wait_to_move = 12/self.speed
        self.counter = 0
        self.distance_per_frame = 40/(12/self.speed * 40)
        self.reach_the_end = False
        self.tier = Enemy.enemy_data[enemy_type]["tier"]
        self.damage = Enemy.enemy_data[enemy_type]["damage"]

#### ====================================================================================================================== ####
#############                                       ENEMY_FUNCTIONS                                                #############
#### ====================================================================================================================== ####

def update_enemy(enemy, game_data,direction=None, damage=0):
    enemy.counter += enemy.distance_per_frame
    
    enemy.distance+=enemy.distance_per_frame
    if enemy.wait_to_move == 12/enemy.speed:
        # check right
        if (game_data["map"].map_data[(enemy.location[0] + 1, enemy.location[1])][
            "value"] == "R" or game_data["map"].map_data[(enemy.location[0] + 1, enemy.location[1])][
            "value"] == "E") and enemy.previous_direction != "left":
            enemy.direction = "right"
            if game_data["map"].map_data[(enemy.location[0] + 1, enemy.location[1])][
            "value"] == "E":
                enemy.reach_the_end = True
        # check down
        elif (game_data["map"].map_data[(enemy.location[0], enemy.location[1] + 1)][
            "value"] == "R" or game_data["map"].map_data[(enemy.location[0], enemy.location[1] + 1)][
            "value"] == "E") and enemy.previous_direction != "up":
            enemy.direction = "down"
            if game_data["map"].map_data[(enemy.location[0], enemy.location[1] + 1)][
            "value"] == "E":
                enemy.reach_the_end = True
                
        # check left
        elif (game_data["map"].map_data[(enemy.location[0] - 1, enemy.location[1])][
            "value"] == "R" or game_data["map"].map_data[(enemy.location[0] - 1, enemy.location[1])][
            "value"] == "E") and enemy.previous_direction != "right":
            enemy.direction = "left"
            if game_data["map"].map_data[(enemy.location[0] - 1, enemy.location[1])][
            "value"] == "E":
                enemy.reach_the_end = True
                
        # check up
        elif (game_data["map"].map_data[(enemy.location[0], enemy.location[1] - 1)][
            "value"] == "R" or game_data["map"].map_data[(enemy.location[0], enemy.location[1] - 1)][
            "value"] == "E") and enemy.previous_direction != "down":
            enemy.direction = "up"
            if game_data["map"].map_data[(enemy.location[0], enemy.location[1] - 1)][
            "value"] == "E":
                enemy.reach_the_end = True
                

    if enemy.counter>=40.9:
        enemy.counter = 0
        #check right
        
        if enemy.direction == "right":
            if enemy.reach_the_end:
                game_data["endGame"] -= enemy.damage
                game_data["enemies"].remove(enemy)
            enemy.location = (enemy.location[0]+1, enemy.location[1])
            enemy.previous_direction = "right"
        # check down
        elif enemy.direction == "down":
            if enemy.reach_the_end:
                game_data["endGame"] -= enemy.damage
                game_data["enemies"].remove(enemy)
            enemy.location = (enemy.location[0], enemy.location[1]+1)
            enemy.previous_direction = "down"
        # check left
        elif enemy.direction == "left":
            if enemy.reach_the_end:
                game_data["endGame"] -= enemy.damage
                game_data["enemies"].remove(enemy)
            enemy.location = (enemy.location[0]-1, enemy.location[1])
            enemy.previous_direction = "left"
        #check up
        elif enemy.direction == "up":
            if enemy.reach_the_end:
                game_data["endGame"] -= enemy.damage
                game_data["enemies"].remove(enemy)
            enemy.location = (enemy.location[0], enemy.location[1]-1)
            enemy.previous_direction = "up"

        enemy.wait_to_move = 12/enemy.speed
        

    elif game_data["time_counter"] == game_data["frame_rate"]:
        # 1 second
        enemy.wait_to_move -= 1

        


def render_enemy(enemy, screen, settings):
    ''' Helper function that renders a single provided Enemy.
    Input: Enemy Object, screen (pygame display), Settings Object
    Output: None
    '''
    if enemy.counter>40.9:
        enemy.counter=40.9    
    if enemy.direction == "right":
        screen.blit(pygame.transform.smoothscale(enemy.sprite, (40, 40)),
                    (enemy.location[0] * settings.tile_size[0] + enemy.counter, enemy.location[1] * settings.tile_size[1]))
        enemy.realLocation= (enemy.location[0] * settings.tile_size[0] + enemy.counter, enemy.location[1] * settings.tile_size[1])
    elif enemy.direction == "down":
        screen.blit(pygame.transform.smoothscale(enemy.sprite, (40, 40)),
                    (enemy.location[0] * settings.tile_size[0], enemy.location[1] * settings.tile_size[1] + enemy.counter))
        
        enemy.realLocation=  (enemy.location[0] * settings.tile_size[0], enemy.location[1] * settings.tile_size[1] + enemy.counter)
    elif enemy.direction == "left":
        screen.blit(pygame.transform.smoothscale(enemy.sprite, (40, 40)),
                    (enemy.location[0] * settings.tile_size[0] - enemy.counter, enemy.location[1] * settings.tile_size[1]))
        enemy.realLocation = (enemy.location[0] * settings.tile_size[0] - enemy.counter, enemy.location[1] * settings.tile_size[1])
    elif enemy.direction == "up":
        screen.blit(pygame.transform.smoothscale(enemy.sprite, (40, 40)),
                    (enemy.location[0] * settings.tile_size[0], enemy.location[1] * settings.tile_size[1] - enemy.counter))
        enemy.realLocation = (enemy.location[0] * settings.tile_size[0], enemy.location[1] * settings.tile_size[1] - enemy.counter)
    

def downgrade_enemy(enemy, game_data):
    if(enemy.tier > 1):
        enemy.tier = enemy.tier - 1
    
        if(enemy.tier == 1):
            newflame=Enemy("Red Flame", enemy.location)
            newflame.counter = enemy.counter
            newflame.direction=enemy.direction
            newflame.previous_direction=enemy.previous_direction
            update_enemy(newflame,game_data)
            game_data["enemies"].append(newflame)
            
            
        elif(enemy.tier == 2):
            newflame=Enemy("Orange Flame", enemy.location)
            newflame.counter = enemy.counter
  
            newflame.direction=enemy.direction
            newflame.previous_direction=enemy.previous_direction   
            update_enemy(newflame,game_data)
            game_data["enemies"].append(newflame)
            
        elif(enemy.tier == 3):
            newflame=Enemy("Yellow Flame", enemy.location)
            newflame.counter = enemy.counter
  
            newflame.direction=enemy.direction
            newflame.previous_direction=enemy.previous_direction       
            update_enemy(newflame,game_data)
            
            game_data["enemies"].append(newflame)
            
        elif(enemy.tier == 4):
            newflame=Enemy("White Flame", enemy.location)
            newflame.counter = enemy.counter

            newflame.direction=enemy.direction
            newflame.previous_direction=enemy.previous_direction            
            update_enemy(newflame,game_data)
            game_data["enemies"].append(newflame)
            
        elif(enemy.tier == 5):
            
            newflame=Enemy("Blue Flame", enemy.location)
            newflame.counter = enemy.counter
       
            newflame.direction=enemy.direction
            newflame.previous_direction=enemy.previous_direction 
            update_enemy(newflame,game_data)
            game_data["enemies"].append(newflame)
        enemy.counter += enemy.distance_per_frame
            

