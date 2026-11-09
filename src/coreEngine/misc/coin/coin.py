import random
import pygame as pg
from coreEngine.entity.entity import Entity
class Coin(Entity):
    def __init__(self,x,y,game_manager):
        self.game_manager = game_manager
        self.x = x
        self.y = y
        self.color = (255,255,0)
        self.height = 24
        self.width = 24
        #basicBody init
        self.isVisible = True
        super().__init__(x,y,0,0,0,self.width,self.height,self.game_manager,isVisible=self.isVisible)
        self.updateBody()

    def coinRuntime(self):

        #screen = pg.display.get_surface()
        ##screen_width = screen.get_width()
        #screen_height = screen.get_height()

        self.EntityRuntime(self.game_manager)
        self.preventLeavingArea(self.game_manager.map_width, self.game_manager.map_height,(random.randint(0, self.game_manager.map_width),random.randint(0, self.game_manager.map_height)))
        if self.rect.colliderect(self.game_manager.player.rect):
            self.game_manager.player.coin_count += 1
            self.x = random.randint(0,self.game_manager.map_width-1)
            self.y = random.randint(0,self.game_manager.map_height-1)