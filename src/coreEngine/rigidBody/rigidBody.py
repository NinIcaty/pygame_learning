import pygame as pg
class RigidBody:

    def __init__(self, x: float, y: float,gravity: float,friction: float,max_speed: float, acceleration: float):
        self.x = x
        self.y = y
        # Movement stuff
        self.velocity = [0, 0]
        self.gravity = gravity
        #self.mass =
        self.friction = friction
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.dir_x = 0
        self.dir_y = 0
        # Dimensions
        self.width = 100
        self.height = 100

    def updateBody(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def applyGravity(self, dt):
        self.velocity[1] += self.gravity * dt



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

    def objectRuntime(self):
        #held_keys = pg.key.get_pressed()

        self.updateBody()
        self.dir_x = 0
        self.dir_y = 0
    #Optional defs to be called in other classes
    def preventLeavingArea(self,area_width,area_height,default_position: tuple):
        if self.x > area_width or self.x < 0 or self.y > area_height or self.y < 0:
            self.x = default_position[0]
            self.y = default_position[1]

    def collision(self, other_bodies: list):
        self.isColliding = False
        self.is_on_floor = False
        self.updateBody()

        for other in other_bodies:
            if other is self:
                continue

            other.updateBody()

            if not self.rect.colliderect(other.rect):
                continue

            overlap_x = min(
                self.rect.right - other.rect.left,
                other.rect.right - self.rect.left
            )
            overlap_y = min(
                self.rect.bottom - other.rect.top,
                other.rect.bottom - self.rect.top
            )

            self.isColliding = True

            if overlap_x < overlap_y:
                # Horizontal collision
                if self.rect.centerx < other.rect.centerx:
                    self.x -= overlap_x
                else:
                    self.x += overlap_x

                self.velocity[0] = 0

            else:
                # Vertical collision
                if self.rect.centery < other.rect.centery:
                    # Player is landing on top
                    self.y -= overlap_y
                    self.is_on_floor = True
                else:
                    # Player hit the underside
                    self.y += overlap_y

                self.velocity[1] = 0

            self.updateBody()




