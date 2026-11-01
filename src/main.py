import pygame as pg
import random
import pytmx
from PIL import Image
# coreEngine
from coreEngine.rigidBody.rigidBody import RigidBody
from coreEngine.camera.camera import Camera
from coreEngine.player.player import Player
from coreEngine.misc.coin.coin import Coin
from coreEngine.rigidBody.inmutBody.inmutBody import InmutBody
from coreEngine.hud.playerHud.playerHud import PlayerHUD
from coreEngine.map.map import Map
# Initialize Pygame stuff
pg.init()
font = pg.font.Font(None, 36)
screen = pg.display.set_mode((0, 0))
pg.display.set_caption("topDown")
clock = pg.time.Clock()
# Get screen dimensions
screen_width = pg.display.Info().current_w
screen_height = pg.display.Info().current_h

####TEST

map1 = Map("resources/map.tmx")
####END
# Game loop
screen.fill((0, 0, 0))

class GameManager:
    def __init__(self,player,map_width,map_height,dt):
        self.player = player
        #self.imutBodies = InmutBody.InmutBodies
        self.map_height = map_height
        self.map_width = map_width
        self.dt = dt
        self.map_width = map_width
        self.map_height = map_height
dt = clock
# Create objects
coin = Coin(random.randint(0, screen_width - 1),random.randint(0, screen_height - 1))
player = Player(800, 500)
test_body = InmutBody(800, 600,  0, 0, 0, 100 ,100)

player.coin_count = 0
game_manager = GameManager(player,map1.map_width,map1.map_height,dt)
camera = Camera(screen_width, screen_height, game_manager.map_width, game_manager.map_height)
player_HUD = PlayerHUD(game_manager,100,50)

def main():
    running = True

    while running:
        screen.fill((0, 0, 0))
        # Draw map background
        screen.blit(map1.map_surface,(int(camera.offset_x), int(camera.offset_y)))

        # Calculate elapsed time in seconds
        dt = min(clock.tick(60) / 1000.0, 0.05)

        # Game events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if not running:
            break



        # Update physics
        player.playerRuntime( dt)
        coin.coinRuntime(game_manager)
        #CAMERA STUFF
        camera.update(player, dt)
        #Draw stuff
        pg.draw.rect(screen, (35, 33, 73), camera.apply(test_body))
        pg.draw.rect(screen, coin.color, camera.apply(coin))
        pg.draw.rect(screen, player.color, camera.apply(player))
        player.preventLeavingArea(game_manager.map_width,game_manager.map_height,player.spawn)
        player_HUD.draw(screen)
        #Camera dead zone
        #camera.CameraDebugDeadZone()
        pg.display.flip()

main()
pg.quit()