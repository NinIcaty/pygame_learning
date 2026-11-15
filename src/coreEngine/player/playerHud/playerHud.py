import pygame as pg

class PlayerHUD:

    def __init__(self, gameManager, width, height):

        self.player = gameManager.player
        self.gameManager = gameManager
        self.width = width
        self.height = height

        # HUD panel position and size
        self.rect = pg.Rect(
            20, 20,
            width, height
        )

        # Styling
        self.background_color = (35, 33, 73)
        self.border_color = (100, 100, 180)

        self.font = pg.font.SysFont("Arial", 20)
        self.coinCounter = self.font.render(
            f"Coins: {self.gameManager.player.coin_count}",
            True,
            (255, 230, 240)
        )
    def draw(self, screen):
        self.coinCounter = self.font.render(
            f"Coins: {self.gameManager.player.coin_count}",
            True,
            (255, 230, 240)
        )

        # Draw background
        pg.draw.rect(screen,self.background_color,self.rect,border_radius=10)

        # Draw border
        pg.draw.rect(screen,self.border_color,self.rect,width=2,border_radius=10)

        # Coin counter

        #print(self.coinCounter(self))
        screen.blit(self.coinCounter,(self.rect.x + 15, self.rect.y + 15))