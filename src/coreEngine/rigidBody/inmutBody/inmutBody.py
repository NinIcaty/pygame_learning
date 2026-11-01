from coreEngine.rigidBody.rigidBody import RigidBody


class InmutBody(RigidBody):
    InmutBodies = []
    def __init__(self,x: float, y: float,friction: float,max_speed: float, acceleration: float,width: float,height: float):
        #InmutBody.InmutBodies.append(self)#add to list
        self.x = x
        self.y = y
        self.friction = friction
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.width = width
        self.height = height
        self.updateBody()
        super().__init__(x,y,friction,max_speed,acceleration,self.width,self.height,doesCollision=True)

    def InmutRuntime(self):
        self.objectRuntime()
        self.collision()
