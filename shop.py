#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

from helper_functions import *
import pygame

#### ====================================================================================================================== ####
#############                                          SHOP_CLASS                                                  #############
#### ====================================================================================================================== ####

class Shop:
    ''' Settings Class - represents a single Setting Object. '''
    def __init__(self, theme, settings):
        ''' Initialization for Shop.
        Input: theme (string), Settings Oject
        Output: A Shop Object
        '''
        
        self.location = [800, 0]
        self.size = [200, settings.window_size[1]]
        self.shop_data = {}
        for shop in csv_loader("data/shop.csv"):
            self.shop_data[shop[0]] = { "sprite": pygame.transform.scale(pygame.image.load(shop[1]).convert_alpha(), (80, 80)), "sprite_disabled": pygame.transform.scale(pygame.image.load(shop[2]).convert_alpha(), (80, 80)), "available": bool(shop[3]), "cost": int(shop[4]), "radius": int(shop[5]) }
        self.ui_data = {}
        for ui in csv_loader("data/ui.csv"):
            if ui[0] == theme:
                self.ui_data["shop_background"] = pygame.transform.scale(pygame.image.load("assets\\ui\\shop_background.png").convert_alpha(), (200,1000))
                self.ui_data["currency"] = pygame.transform.scale(pygame.image.load(ui[4]).convert_alpha(), (24, 24))
                self.ui_data["item_size"] = int(ui[5])
                self.ui_data["item_background"] = pygame.transform.scale(pygame.image.load(ui[1]).convert_alpha(), (self.ui_data["item_size"], self.ui_data["item_size"]))
                self.ui_data["item_background_disabled"] = pygame.transform.scale(pygame.image.load(ui[2]).convert_alpha(), (self.ui_data["item_size"], self.ui_data["item_size"]))
                self.ui_data["radius_sprite"] = pygame.image.load(ui[6]).convert_alpha()
                self.infobox=pygame.transform.scale(pygame.image.load(ui[1]).convert_alpha(), (200,300))
        self.selected_item = None
        self.clicked_item = None
        item_location = [self.location[0] + (self.size[0] - 2 * self.ui_data["item_size"]) / 3, self.location[1] + (self.size[0] - 2 * self.ui_data["item_size"]) / 3 + 150]
        for item in self.shop_data:
            self.shop_data[item]["location"] = item_location
            if item_location[0] + self.ui_data["item_size"] * 2 > settings.window_size[0]:
                item_location = [self.location[0] + (self.size[0] - 2 * self.ui_data["item_size"]) / 3, item_location[1] + (self.size[0] - 2 * self.ui_data["item_size"]) / 3 + self.ui_data["item_size"] + 25]
            else:
                item_location = [item_location[0] + (self.size[0] - 2 * self.ui_data["item_size"]) / 3 + self.ui_data["item_size"], item_location[1]]

#### ====================================================================================================================== ####
#############                                         SHOP_FUNCTIONS                                               #############
#### ====================================================================================================================== ####

def update_shop(shop, current_currency, settings):
    ''' Helper function that updates the Shop.
    Input: Shop Object, current currency (int), Settings Object
    Output: None
    '''
    # Handle Mouse-Over tower in shop, sets it as 'selected_item' for rendering purposes
    # Also handles unaffordable towers in shop (switched to available to False)
    shop.selected_item = None
    (mX, mY) = pygame.mouse.get_pos()
    for item in shop.shop_data:
        if current_currency < shop.shop_data[item]["cost"]:
            shop.shop_data[item]["available"] = False
        else:
            shop.shop_data[item]["available"] = True
        if (mX > shop.shop_data[item]["location"][0] and mX < shop.shop_data[item]["location"][0] + shop.ui_data["item_size"]) and (mY > shop.shop_data[item]["location"][1] and mY < shop.shop_data[item]["location"][1] + shop.ui_data["item_size"]):
                shop.selected_item = item
    # Replace with code to update the Shop
    pass # Remove this once you've completed the code

def render_shop(shop, screen, settings, current_currency):
    ''' Helper function that renders the Shop.
    Input: Shop Object, screen (pygame display), Settings Object, current currency (int)
    Output: None
    '''
    # Rendering Shop Background

    screen.blit(shop.ui_data["shop_background"], (800,0))
    screen.blit(shop.infobox, (800,500))

    # Rendering Top Section
    towers_text = settings.title_font.render("Towers", True, (254, 207, 0))
    screen.blit(towers_text, (shop.location[0] + towers_text.get_width() // 3, 15))

    # Rendering Towers
    for item in shop.shop_data:
        # -- Optional Split for Unavailable Icons --
        if shop.shop_data[item]["available"]:
            screen.blit(shop.ui_data["item_background"], shop.shop_data[item]["location"])
            screen.blit(shop.shop_data[item]["sprite"], shop.shop_data[item]["location"])
        else:
            screen.blit(shop.ui_data["item_background_disabled"], shop.shop_data[item]["location"])
            screen.blit(shop.shop_data[item]["sprite_disabled"], shop.shop_data[item]["location"])
            
        # Rendering Item Information (Text)
        item_cost_text = settings.font.render("{}".format(shop.shop_data[item]["cost"]), True, (254, 207, 0))
        screen.blit(item_cost_text, (shop.shop_data[item]["location"][0] + 30, shop.shop_data[item]["location"][1] + shop.ui_data["item_size"] - 2))
        screen.blit(shop.ui_data["currency"], (shop.shop_data[item]["location"][0], shop.shop_data[item]["location"][1] + shop.ui_data["item_size"] + 3))
    
    # Handle Player Currency
    current_currency_text = settings.font.render("{}".format(current_currency), True, (254, 207, 0))
    screen.blit(current_currency_text, (shop.location[0] + current_currency_text.get_width() // 3 + 50, 645))
    screen.blit(shop.ui_data["currency"], (shop.location[0] + 25, 650))

    # Handle Mouse Over Tower
    if shop.selected_item is not None:
        selected_tower_text = settings.font.render(shop.selected_item, True, (254, 207, 0))
        screen.blit(selected_tower_text, (shop.location[0] + selected_tower_text.get_width() // 8, 100))

    # Handle Selected Tower
    if shop.clicked_item is not None:
        screen.blit(pygame.transform.scale(shop.ui_data["radius_sprite"], (shop.shop_data[shop.clicked_item]["radius"] * 2, shop.shop_data[shop.clicked_item]["radius"] * 2)), (pygame.mouse.get_pos()[0] - shop.shop_data[shop.clicked_item]["radius"], pygame.mouse.get_pos()[1] - shop.shop_data[shop.clicked_item]["radius"]))
        screen.blit(shop.shop_data[shop.clicked_item]["sprite"], (pygame.mouse.get_pos()[0] - shop.ui_data["item_size"] // 2, pygame.mouse.get_pos()[1] - shop.ui_data["item_size"] // 2))
