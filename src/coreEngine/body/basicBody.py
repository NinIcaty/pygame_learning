import pygame as pg
class BasicBody:
    #all = []
    CollisionBodies = []

    def __init__(self, x: float, y: float,friction: float,max_speed: float, acceleration: float,width: float,height: float,doesCollision=False,doBodyUpdates = False):
        #BasicBody.all.append(self)
        if doesCollision == True:
            BasicBody.CollisionBodies.append(self)
        self.doesCollision = doesCollision
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
        self.doBodyUpdates = doBodyUpdates
        self.isColliding = False
    def updateBody(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def basicBodyRuntime(self):
        #temp removed
        if self.doBodyUpdates: self.updateBody()
        if self.doesCollision: self.collision()
        self.dir_x = 0
        self.dir_y = 0


    #Optional defs to be called in other classes


    def collision(self):
        self.isColliding = False
        self.updateBody()

        for other in BasicBody.CollisionBodies:
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




