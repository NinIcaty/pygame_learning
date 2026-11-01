# Top Down Game Framework (TDGF)
version: a_0.2
## About

Top Down  game Framework is a random game based of my "coreEngine" I'm tryna make for my personal pygame projects, for how to use got to [Basic Guide](docs/basic.md)

## Changelog

### Added
- Added the ability to load a tmx map
- Added a basic map 
- Made a new class ``Map`` that has the attribute ``mapFilePath`` that needs the location of the tmx file for the map
- Made a list in RigidBody called ``CollisionBodies`` that contains all the bodies running the collision function 
### Changes
- Changed the player size to 32 * 32
- Changed the coin size to 24 * 24
- Removed the RigidBody's automatic setting of size to 100 * 100
- Made ``ImutBody``s require a width and height
- Made ``RigidBody`` Require width and height 
### Problems
- Tiles do not appear rotated 
## Plans
- Improve maps, add layer / collision support, death zones and object spawn areas 