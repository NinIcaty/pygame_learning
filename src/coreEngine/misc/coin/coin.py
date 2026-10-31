import random
import pygame as pg

from coreEngine.rigidBody.rigidBody import RigidBody

class Coin(RigidBody):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (255,255,0)
        self.height = 100
        self.width = 100
        #RigidBody init
        super().__init__(x,y,0,0,0,0)
    def coinRuntime(self,gameManager):

        #screen = pg.display.get_surface()
        ##screen_width = screen.get_width()
        #screen_height = screen.get_height()

        self.objectRuntime()
        self.preventLeavingArea(gameManager.map_width, gameManager.map_height,(random.randint(0, gameManager.map_width),random.randint(0, gameManager.map_height)))
        if self.rect.colliderect(gameManager.player.rect):
            gameManager.player.coin_count += 1
            self.x = random.randint(0,gameManager.map_width-1)
            self.y = random.randint(0,gameManager.map_height-1)