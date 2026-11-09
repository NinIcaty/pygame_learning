import pygame as pg
#from coreEngine.camera.camera import Camera
from coreEngine.body.basicBody import BasicBody


class Entity(BasicBody):
    Entities = []
    def __init__(self, x: float, y: float,friction: float,max_speed: float, acceleration: float,width: float,height: float,game_manager,doesCollision=False,isVisible=True,Image=None):
        #Add to entities list
        Entity.Entities.append(self)
        self.x = x
        self.y = y
        #self.game_manager = game_manager
        # Movement stuff
        self.velocity = [0, 0]
        self.friction = friction
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.dir_x = 0
        self.dir_y = 0
        self.game_manager = game_manager
        # Dimensions
        self.width = width
        self.height = height
        #Tags
        self.doesCollision = doesCollision
        self.isVisible = isVisible
        self.Image = Image
        #if self.Image != False:
            #Change later add image support
         #   pass

        super().__init__(x,y,friction,max_speed,acceleration,self.width,self.height,doesCollision=self.doesCollision,doBodyUpdates=True)
    def movement(self):
        # Check if Direction has Changed
        if self.dir_x != 0:
            self.velocity[0] += self.dir_x * self.acceleration
        else:
            self.velocity[0] *= self.friction  # Apply friction/slowdown

        if self.dir_y != 0:
            self.velocity[1] += self.dir_y * self.acceleration
        else:
            self.velocity[1] *= self.friction
        # Setting limits for speed/velocity
        self.velocity[0] = max(-self.max_speed, min(self.velocity[0], self.max_speed))  # x
        self.velocity[1] = max(-self.max_speed, min(self.velocity[1], self.max_speed))  # y

        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.updateBody()
    def draw(self):
        #if self.Image is not None:
            #Change later, make load image
        #    pg.draw.rect(self.game_manager.screen, self.color, self.game_manager.camera.apply(self))
        #else:
        pg.draw.rect(self.game_manager.screen, self.color, self.game_manager.camera.apply(self))
    def EntityRuntime(self,game_manager):
        if self.isVisible == True: self.draw() #DRAW
        self.basicBodyRuntime()
        self.updateBody()
    #Optional defs to be called in other classes
    def preventLeavingArea(self,area_width,area_height,default_position: tuple):
        if self.x > area_width or self.x < 0 or self.y > area_height or self.y < 0:
            self.x = default_position[0]
            self.y = default_position[1]
