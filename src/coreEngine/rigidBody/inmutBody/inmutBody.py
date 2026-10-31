from coreEngine.rigidBody.rigidBody import RigidBody


class InmutBody(RigidBody):
    InmutBodies = []
    def __init__(self,x: float, y: float,gravity: float,friction: float,max_speed: float, acceleration: float):
        InmutBody.InmutBodies.append(self)#add to list
        self.x = x
        self.y = y
        self.gravity = gravity
        self.friction = friction
        self.max_speed = max_speed
        self.acceleration = acceleration
        super().__init__(x,y,gravity,friction,max_speed,acceleration)

    def InmutRuntime(self,player):
        self.collision(InmutBody.InmutBodies+player)
