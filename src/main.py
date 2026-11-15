import pygame as pg
import random
import argparse
import os

# coreEngine
from coreEngine.body.basicBody import BasicBody
from coreEngine.camera.camera import Camera
from coreEngine.player.player import Player
from coreEngine.misc.coin.coin import Coin
from coreEngine.player.playerHud.playerHud import PlayerHUD
from coreEngine.map.map import Map
from coreEngine.misc.bullet import Bullet
#ARGS
parser = argparse.ArgumentParser(description="A topDown shooter Engine made with pygame")
parser.add_argument("-t", "--testrun", action="store_true", help="Test Run, for non built versions")
parser.add_argument("-d", "--debug", action="store_true", help="For debugging at the moment only turns on the camera overlay") #update msg

args = parser.parse_args()

# Initialize Pygame stuff
pg.init()
font = pg.font.Font(None, 36)
screen = pg.display.set_mode((0, 0))
pg.display.set_caption("topDown")
clock = pg.time.Clock()
# Get screen dimensions
screen_width = pg.display.Info().current_w
screen_height = pg.display.Info().current_h


# Get loadingScreen path relative to this script
base_dir = os.path.dirname(os.path.abspath(__file__))
#Check args and set directory of files
if not args.testrun:
    loading_path = os.path.join(base_dir,"src","resources", "loadingScreen.png")
    map1_path = os.path.join( base_dir,"src","resources", "map.tmx")
else:
    loading_path = os.path.join(base_dir,"resources", "loadingScreen.png")
    map1_path = os.path.join( base_dir,"resources", "map.tmx")
# Load and stretch image to match full monitor dimensions
raw_loading_image = pg.image.load(loading_path).convert()
loading_screen = pg.transform.scale(raw_loading_image, (screen_width, screen_height))


screen.blit(loading_screen, (0, 0))
pg.display.flip()

map1 = Map(map1_path)
class GameManager:
    def __init__(self,screen,map_width,map_height,dt):
        global args
        self.map_height = map_height
        self.map_width = map_width
        self.dt = dt
        self.map_width = map_width
        self.map_height = map_height
        self.screen = screen
        self.launch_args = args
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        if args.debug:
            self.debugMode = True
        ######################
        #SETTING GAME MANAGER#
        ######################
dt = clock
# Create objects

game_manager = GameManager(screen,map1.map_width,map1.map_height,dt)
player = Player(800, 500,game_manager)
camera = Camera(screen_width, screen_height, game_manager)
test_body = BasicBody(800, 600,  0, 0, 0, 100 ,100,doesCollision=True)
player.coin_count = 0
coin = Coin(random.randint(0, screen_width - 1),random.randint(0, screen_height - 1),game_manager)
player_HUD = PlayerHUD(game_manager,100,50)

print(BasicBody.CollisionBodies)
# Game loop
def main():
    running = True

    while running:
        #screen.fill((0, 0, 0))

        # Draw map background

        # Calculate elapsed time in seconds
        dt = min(clock.tick(60) / 1000.0, 0.05)

        # Game events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if not running:
            break



        #print(player.rect)
        #CAMERA STUFF
        camera.update(player, dt)
        screen.blit(map1.map_surface, (int(camera.offset_x), int(camera.offset_y)))  # MAP DRAW

        # Runtimes
        #Bullet logic
        for bullet in Bullet.Bullets:
            bullet.bulletRuntime()
        player.playerRuntime()
        coin.coinRuntime()
        pg.draw.rect(screen, (35, 33, 73), camera.apply(test_body)) #Test body
        #pg.draw.rect(screen, coin.color, camera.apply(coin))
        #pg.draw.rect(screen, player.color, camera.apply(player))
        player.preventLeavingArea(game_manager.map_width,game_manager.map_height,player.spawn)
        player_HUD.draw(screen)
        #Camera dead zone
        if game_manager.debugMode: camera.CameraDebugDeadZone(screen)
        pg.display.flip()

main()
pg.quit()