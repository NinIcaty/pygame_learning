# Basic Guide to coreEngine

## RigidBody
RigidBody is the MOST important class in the full thing, most classes will be based of this. RigidBody has many functions that are not called but can be called in the object's runtime (generally done in a custom class's runtime).

It has the list of all collision bodies called ``RigidBody.CollisionBodies``
### Attributes
All of these are expected when creating an object of the class
- x: float
- y: float
- friction: float
- max_speed
- acceleration: float 
- width: float (Width of the object)
- height: float (Height of the object)
### Functions
- updateBody: Updates the RigidBody's rect 
- objectRuntime: Default runtime of a RigidBody, only calls ``updateBody`` and resets ``dir_x`` and ``dir_y``

Optional functions not called in default runtime
- applyGravity: For 2D non-top down games, to apply gravity on the body
- movement: The basic movement is handled here, only the object's own movement i.e if another body were to run into it, it will not move
- collision: basic collision function just prevents other objects (that are in the ``RigidBody.CollisionBodies`` list)
- preventLeavingArea: Set the object x and y to a certain thing if it leaves a range of co-ordinates

## ImutBody
ImutBody is a RigidBody that has collision and is automatically put in a list of them.
### Attributes
These are expected when creating an instance of the class
- x: float
- y: float
- friction: float
- max_speed
- acceleration: float 
- width: float (Width of the object)
- height: float (Height of the object)
### Functions
ImutBody only has one special function that is the ImutRuntime
