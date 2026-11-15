# Basic Guide to coreEngine

## BasicBody
basicBody is the MOST important class in the full thing, most classes will be based of this. basicBody has many functions that are not called but can be called in the object's runtime (generally done in a custom class's runtime).

It has the list of all collision bodies called ``basicBody.CollisionBodies``
### Attributes
All of these are expected when creating an object of the class
- x: float
- y: float
- friction: float
- max_speed
- acceleration: float 
- width: float (Width of the object)
- height: float (Height of the object)
- doBodyUpdates (default is False, dictates if the body should update)
- doesCollision (default is false, dictates if a body should do collision, if it does it is put in the collision body list)
### Functions
- updateBody: Updates the basicBody's rect 
- basicBodyRuntime: Default runtime of a basicBody, only calls ``updateBody`` (if doBodyUpdates is true), calls collision if doesCollision is true and resets ``dir_x`` and ``dir_y``

Optional functions not called in default runtime
- collision: basic collision function just prevents other objects (that are in the ``basicBody.CollisionBodies`` list)
## Entity
Extends bas. It has a list called ``Entity.Entities``.
### Attributes 
All of these are expected attributes when creating an object of the class (In order)
- x: float 
- y: float
- friction: float
- max_speed: float
- acceleration: float
- width: float (Width of rect)
- height: float (Height of rect)
- game_manager (The scene's GameManager)
- doesCollision=False (If the body should do collision)
- isVisible=True (Should the body be drawn)
- Image=None
### Functions
- EntityRuntime: The main Entity runtime
- draw: Draw the Entity
- movement: The basic movement is handled here, only the object's own movement i.e if another body were to run into it, it will not move (Moved to the Entity class in a_0.3 IBT-2)

Optional
- preventLeavingArea: Set the object x and y to a certain thing if it leaves a range of co-ordinates

## ImutBody (MAY BE REMOVED!)
ImutBody is a basicBody that has collision.
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

