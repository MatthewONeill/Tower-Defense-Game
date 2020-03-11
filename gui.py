from helper_functions import *
from settings import *
from shop import *
from tower import *
from enemy import *
from map import *
import pygame
import sys
import math

class Gui:
    #Initialize the GUI
    def __init__(self):
        self.holding=None
        self.buttonDown=False
  
        
        
        pass
    def setShop(self,shop): #Initialize some values
        self.shop=shop;
    def setData(self,data): #Initialize some values
        self.game_data=data 
        
    def process(self,events):
        #dedicated input processing for Gui
        for event in events:
             # Handle Mouse Button Down
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.buttonDown=True
                pass
    
            # Handle Mouse Button Up
            if event.type == pygame.MOUSEBUTTONUP:
                self.buttonDown=False
                pass
        
        pass
    
    def checkPath(self,xy):
        #Find if given x or y lands on path or not.
        x=xy[0]
        y=xy[1]
        settings=self.game_data["settings"]
        tileX=settings.tile_size[0]
        tileY=settings.tile_size[1]
 
        try:
            if self.game_data["map"].map_data[(math.floor(x/tileX),math.floor(y/tileY))]["value"]=="R":
                return True
            else:
                if self.game_data["map"].map_data[(math.floor(x/tileX)+1,math.floor(y/tileY))]["value"]=="R":
                    return True
                else:
                    if self.game_data["map"].map_data[(math.floor(x/tileX)-1,math.floor(y/tileY))]["value"]=="R":
                        return True  
                    else:
                        if self.game_data["map"].map_data[(math.floor(x/tileX),math.floor(y/tileY)+1)]["value"]=="R":
                            return True 
                        else:
                            if self.game_data["map"].map_data[(math.floor(x/tileX),math.floor(y/tileY)-1)]["value"]=="R":
                                return True        
                            else:
                                if self.game_data["map"].map_data[(math.floor(x/tileX)+1,math.floor(y/tileY)+1)]["value"]=="R":
                                    return True
                                else:
                                    if self.game_data["map"].map_data[(math.floor(x/tileX)-1,math.floor(y/tileY)-1)]["value"]=="R":
                                        return True
                                    else:
                                        if self.game_data["map"].map_data[(math.floor(x/tileX)-1,math.floor(y/tileY)+1)]["value"]=="R":
                                            return True                                  
                                        else:
                                            if self.game_data["map"].map_data[(math.floor(x/tileX)+1,math.floor(y/tileY)-1)]["value"]=="R":
                                                return True       
                                            else:
                                                return False
        except:
            return True
    def checkObstruct(self,xy):
        mX=xy[0]
        mY=xy[1]
        #check if tower unit is too close to another.
        for tower in self.game_data["towers"]:
            x=tower.location[0]
            y=tower.location[1]
            if mX>x and mX<x+100 and mY>y and mY<y+100:
                return False
        return True
 
    def update(self):
        print(self.game_data["towers"])
        #Main update loop for gui
        selected=self.shop.selected_item #Hook into the shop to determine which item the mouse is over
        
        if selected!=None and self.holding==None :
            
            if self.buttonDown:
                if self.shop.shop_data[selected]["available"] ==True: #Check if has enough moneys
                    self.holding=selected; #Tell game the user is holding a tower and which tower.
        if self.holding!=None:
            print(self.holding)
            if not self.buttonDown:
                #handle summoning and stuff here
                (mX, mY) = pygame.mouse.get_pos() #Get mouse position
                if not self.checkPath((mX,mY)) and self.checkObstruct((mX,mY)): # check if attempting to place on path or another unit
                    #center tower on tile
                    settings=self.game_data["settings"]
                    tileX=settings.tile_size[0]
                    tileY=settings.tile_size[1]
                    x=math.floor(mX/tileX)
                    y=math.floor(mY/tileY)
                    xy=(x*tileX-20,y*tileY-20)
                    self.game_data["towers"].append(Tower(self.holding,xy))
                    self.game_data["current_currency"]-=self.shop.shop_data[self.holding]["cost"];
                    self.holding=None #Release
                else:
                    self.holding=None #Release
   
    
    def render(self,game_data):
        (mX, mY) = pygame.mouse.get_pos() #Get mouse position
        screen=game_data["screen"]
        if self.holding!=None: #If user is holding unit, render it
            pygame.draw.circle(screen, (255, 255, 255,120), (mX, mY),int(self.shop.shop_data[self.holding]["radius"]), 3)
            sprite=self.shop.shop_data[self.holding]["sprite"]
            screen.blit(sprite, (mX-sprite.get_width()/2,mY-sprite.get_height()/2))
        pass
    pass