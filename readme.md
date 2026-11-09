# Top Down Game Framework (TDGF)
version: a_0.3
## About

Top Down  game Framework is a random game based of my "coreEngine" I'm tryna make for my personal pygame projects, for how to use got to [Basic Guide](docs/basic.md). Run the game from the parent folder of src if you are not using the pyz.
## Changelog

### Added
- Added new Zoom to map, default is 1.5
- Added new function ``draw()`` to map that requires the parameter screen and camera
- Added new doBodyUpdates tag to ``basicBody``, if true it will update the body in the runtime 
- Made new class ```Entity```, shifted player to it (MORE TO BE ADDED)
- Made basicBody's runtime call the ``collision`` function if the tag ``doesCollision`` is true
- Now coins and players need a game manager in the new attribute game_manager
- Added a new tile called "border.py" id:9
- Added a new launcher tag that is --testrun (-t) that is meant for when you haven't converted it to a pyinstaller file
### Changes
- Changed Grass texture
- Changed Dirt texture
- Renamed the class ```RigidBody``` to ```basicBody```
- Refactored the module ```RigidBody``` to ```Body```
- Refactored the file ```rigidBody.py``` to ``basicBody.py``
- Moved the ``movement`` function to the new ``Entity`` class from the ``basicBody`` class
- Renamed the function ``objectRuntime`` to ``basicBodyRuntime`` (BasicBody)
- Renamed the parameter for the game manager from the coin's runtime from "gameManager" to ``game_manager``
- Removed the player parameter from GameManager, now the player class sets itself as the player in the game_manager
- Revamped camera, player and coin to also have a game_manager parameter and use it in place of extra parameters 
- Made the camera set itself as it's GameManager's camera
- Changed keybinds to WSAD
- Made the EntityRuntime dray the objects like player and coin instead of bliting them seperately
- Made The map get loaded using the OS module
- Updated the map
- Added a loading screen
- Switched to using pyinstaller instead of pyz
#### Removed
- Removed old tags ```is_on_floor``` and ``jump_was_pressed from`` player (They were used in the platformer that I had made earlier from which I took the Engine for)
- Removed ``applyGravity`` function from the ``basicBody`` class (Same reason as previous)
## Plans
- Improve maps, add layer / collision support, death zones and object spawn areas 
- Make Entity more defined 
- MAY REMOVE ImutBody SO DO NOT USE THEM 