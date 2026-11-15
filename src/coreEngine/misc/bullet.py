import pygame as pg
from coreEngine.entity.entity import Entity
class Bullet(Entity):
    Bullets = []
    def __init__(self, owner):
        Bullet.Bullets.append(self)
        self.owner = owner
        self.x = self.owner.x
        self.y = self.owner.y
        self.game_manager = self.owner.game_manager
        self.friction = 0.80
        self.max_speed = 10
        self.acceleration = 1
        self.width = 5
        self.height = 20
        super().__init__(self.x,self.y,self.friction,self.max_speed,self.acceleration,self.width,self.height,self.game_manager, doesCollision=False)

        self.color = (0,0,0)



        self.facing_angle = self.owner.facing_angle
        self.updateBody()
        self.dir_x = self.owner.dir_x
        self.dir_y = self.owner.dir_y
        print(self.dir_x,self.dir_y)
        self.draw()
    def bulletRuntime(self):
        self.draw()
        self.movement()
        self.updateBody()
        #self.basicBodyRuntime()
       #print(self.dir_x,self.dir_y)
        if self.x > self.game_manager.map_width or self.x < 0 or self.y > self.game_manager.map_height or self.y < 0:
            print("Killing bullet")
            del self
