import pygame as pg
class RigidBody:
    CollisionBodies = []
    def __init__(self, x: float, y: float,friction: float,max_speed: float, acceleration: float,width: float,height: float,doesCollision=False):
        if doesCollision == True:
            RigidBody.CollisionBodies.append(self)
        self.x = x
        self.y = y
        # Movement stuff
        self.velocity = [0, 0]
        self.friction = friction
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.dir_x = 0
        self.dir_y = 0
        # Dimensions
        self.width = width
        self.height = height
    def updateBody(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def objectRuntime(self):

        self.updateBody()
        self.dir_x = 0
        self.dir_y = 0


    #Optional defs to be called in other classes
    def preventLeavingArea(self,area_width,area_height,default_position: tuple):
        if self.x > area_width or self.x < 0 or self.y > area_height or self.y < 0:
            self.x = default_position[0]
            self.y = default_position[1]

    def collision(self):
        self.isColliding = False
        self.updateBody()

        for other in RigidBody.CollisionBodies:
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
                    self.y -= overlap_y
                else:
                    self.y += overlap_y

                self.velocity[1] = 0

            self.updateBody()

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



