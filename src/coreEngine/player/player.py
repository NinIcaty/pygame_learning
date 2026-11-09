import os

import pygame as pg
from coreEngine.entity.entity import Entity
#Keybinds
class Keybinds:
    def __init__(self):
        self.move_up = pg.K_w
        self.move_down = pg.K_s
        self.move_left = pg.K_a
        self.move_right = pg.K_d

class Player(Entity):
    def __init__(self,x,y,game_manager):
        self.game_manager = game_manager
        self.height = 32
        self.width = 32
        #Movement
        self.friction = 0.80
        self.max_speed = 7.5
        self.acceleration = 1.5
        self.dir_x = 0
        self.dir_y = 0
        self.color = (255,255,255)
        #Collision
        self.isColliding = False

        self.x = x
        self.y = y


        self.keybinds = Keybinds()
        self.game_manager.player = self
        self.spawn = [x,y]
        #body init
        self.updateBody()
        super().__init__(x,y,self.friction,self.max_speed,self.acceleration,self.width,self.height,self.game_manager, doesCollision=True)
        ##TESTING

        #self.player_image = pg.image.load("src/resources/player.png").convert_alpha()
    def playerRuntime(self):
        #gm.screen.blit(self.player_image,self.player_rect)

        held_keys = pg.key.get_pressed()

        self.dir_x = 0
        self.dir_y = 0

        # Horizontal movement
        if held_keys[self.keybinds.move_left]: self.dir_x -= .25
        if held_keys[self.keybinds.move_right]: self.dir_x += .25
        if held_keys[self.keybinds.move_up]: self.dir_y -= .25
        if held_keys[self.keybinds.move_down]: self.dir_y += .25


        # Update physics
        self.movement()
        self.EntityRuntime(self.game_manager)
        #self.preventLeavingScreen(screen.get_width(),screen.get_height(),(self.spawn[0],self.spawn[1]))
        #self.updateBody()

