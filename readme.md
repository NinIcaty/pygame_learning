# Top Down Game Framework (TDGF)
version: a_0.3.1
## About

Top Down  game Framework is a random game based of my "coreEngine" I'm tryna make for my personal pygame projects, for how to use got to [Basic Guide](docs/basic.md). Run the game from the parent folder of src if you are not using the pyz.
## Changelog

### Added
- Added new launch argument --debug, for debugging, turns on stuff like the camera overlay (short -d)
- Added Image support for Entity default the Image is none and it just draws a rect but if it has an image it draws self.Image
- Made the Player render the player.png added in the previous version
- Added the ability for Entity.draw() to have rotate the image and increase it's size`
- Added new __main__.py as the main file
### Changes
- Made test_body an instance of `BasicBody` not ``ImutBody``
#### Removed
- Removed ImutBody
## Plans
- Improve maps, add layer / collision support, death zones and object spawn areas 

