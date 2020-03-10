from helper_functions import *
from settings import *
from shop import *
from tower import *
from enemy import *
from map import *
import pygame
import sys

class Gui:
    def __init__(self):
        self.holding=None
        self.buttonDown=False
  
        
        
        pass
    def setShop(self,shop):
        self.shop=shop;
    def setData(self,data):
        self.game_data=data
        
    def process(self,events):
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.buttonDown=True
                pass
    
            # Handle Mouse Button Up
            if event.type == pygame.MOUSEBUTTONUP:
                self.buttonDown=False
                pass
        
        pass
    
    def update(self):
        
        selected=self.shop.selected_item
        if selected!=None and self.holding==None :
            
            if self.buttonDown:
                if self.shop.shop_data[selected]["available"] ==True:
                    self.holding=selected;
        if self.holding!=None:
            print(self.holding)
            if not self.buttonDown:
                #handle summoning and stuff
                self.holding=None
        pass
    
    def render(self,game_data):
        (mX, mY) = pygame.mouse.get_pos()
        screen=game_data["screen"]
        if self.holding!=None:
            sprite=self.shop.shop_data[self.holding]["sprite"]
            screen.blit(sprite, (mX-sprite.get_width()/2,mY-sprite.get_height()/2))
        pass
    pass