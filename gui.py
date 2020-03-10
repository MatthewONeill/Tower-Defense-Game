from helper_functions import *
from settings import *
from shop import *
from tower import *
from enemy import *
from map import *
import pygame
import sys

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
    
    def update(self):
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
                self.holding=None #Release
        pass
    
    def render(self,game_data):
        (mX, mY) = pygame.mouse.get_pos() #Get mouse position
        screen=game_data["screen"]
        if self.holding!=None: #If user is holding unit, render it
            sprite=self.shop.shop_data[self.holding]["sprite"]
            screen.blit(sprite, (mX-sprite.get_width()/2,mY-sprite.get_height()/2))
        pass
    pass