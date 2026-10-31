import pygame as pg
import random
from coreEngine.camera.camera import Camera
from coreEngine.player.player import Player
from coreEngine.misc.coin.coin import Coin
from coreEngine.rigidBody.inmutBody.inmutBody import InmutBody
from coreEngine.hud.playerHud.playerHud import PlayerHUD
# Initialize Pygame stuff
pg.init()
font = pg.font.Font(None, 36)
screen = pg.display.set_mode((0, 0))
pg.display.set_caption("test_window")
clock = pg.time.Clock()

# Get screen dimensions
screen_width = pg.display.Info().current_w
screen_height = pg.display.Info().current_h


# Game loop
screen.fill((0, 0, 0))

class GameManager:
    def __init__(self,player,map_width,map_height,dt):
        self.player = player
        self.imutBodies = InmutBody.InmutBodies
        self.map_height = screen_height * 2
        self.map_width = screen_width * 2
        self.dt = dt
        self.map_width = map_width
        self.map_height = map_height
dt = clock
# Create objects
coin = Coin(random.randint(0, screen_width - 1),random.randint(0, screen_height - 1))
player = Player(800, 500)
test_body = InmutBody(800, 600, 0, 0, 0, 0)

player.coin_count = 0
game_manager = GameManager(player,screen_width*2,screen_height*2,dt)
camera = Camera(screen_width, screen_height, game_manager.map_width, game_manager.map_height)
player_HUD = PlayerHUD(game_manager,10,10)
def main():
    running = True

    while running:
        screen.fill((0, 0, 0))
        # Calculate elapsed time in seconds
        dt = min(clock.tick(60) / 1000.0, 0.05)

        # Game events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if not running:
            break

        #Score

        #screen.blit(text_surface, (0,2))

        # Update physics
        player.playerRuntime(game_manager.imutBodies, dt)
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
