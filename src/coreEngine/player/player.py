import pygame as pg
from coreEngine.rigidBody.rigidBody import RigidBody
#Keybinds
class Keybinds:
    def __init__(self):
        self.move_up = pg.K_UP
        self.move_down = pg.K_DOWN
        self.move_left = pg.K_LEFT
        self.move_right = pg.K_RIGHT

class Player(RigidBody):
    def __init__(self,x,y):
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
        self.is_on_floor = False
        self.jump_was_pressed = False

        self.keybinds = Keybinds()

        self.spawn = (x,y)
        #rigidBody init
        super().__init__(x,y,self.friction,self.max_speed,self.acceleration,self.width,self.height,doesCollision=True)


    def playerRuntime(self, dt):
        screen = pg.display.get_surface()

        held_keys = pg.key.get_pressed()

        self.dir_x = 0
        self.dir_y = 0

        # Horizontal movement
        if held_keys[self.keybinds.move_left]: self.dir_x -= .25
        if held_keys[self.keybinds.move_right]: self.dir_x += .25
        if held_keys[self.keybinds.move_up]: self.dir_y -= .25
        if held_keys[self.keybinds.move_down]: self.dir_y += .25
        # Jump only on a fresh key press



        # Update physics
        self.movement()
        self.collision()

        #self.preventLeavingScreen(screen.get_width(),screen.get_height(),(self.spawn[0],self.spawn[1]))

        self.objectRuntime()