import pygame as pg
class Camera:
    def __init__(self, width, height, map_width, map_height):
        self.camera = pg.Rect(0, 0, width, height)

        self.width = width
        self.height = height

        self.map_width = map_width
        self.map_height = map_height

        # Dead zone (area where camera doesn't move)
        self.dead_zone = pg.Rect(
            width // 3,
            height // 3,
            width // 3,
            height // 3
        )

        # Camera movement
        self.offset_x = 0.0
        self.offset_y = 0.0

        self.speed_multiplier = 5.0

    def apply(self, entity):
        return entity.rect.move(
            int(self.offset_x),
            int(self.offset_y)
        )

    def update(self, target, dt):

        # Player position on screen
        player_x = target.rect.centerx + self.offset_x
        player_y = target.rect.centery + self.offset_y

        # How far outside the dead zone the player is
        dx = 0
        dy = 0

        if player_x < self.dead_zone.left:
            dx = self.dead_zone.left - player_x

        elif player_x > self.dead_zone.right:
            dx = self.dead_zone.right - player_x

        if player_y < self.dead_zone.top:
            dy = self.dead_zone.top - player_y

        elif player_y > self.dead_zone.bottom:
            dy = self.dead_zone.bottom - player_y

        # Calculate camera movement based on distance
        self.offset_x += dx * self.speed_multiplier * dt
        self.offset_y += dy * self.speed_multiplier * dt

        # Clamp camera to map boundaries
        self.offset_x = min(0, self.offset_x)
        self.offset_y = min(0, self.offset_y)

        self.offset_x = max(
            -(self.map_width - self.width),
            self.offset_x
        )

        self.offset_y = max(
            -(self.map_height - self.height),
            self.offset_y
        )

        self.camera.topleft = (
            int(self.offset_x),
            int(self.offset_y)
        )
    def CameraDebugDeadZone(self):
        pg.draw.rect(
            screen,
            (255, 0, 0),
            camera.dead_zone,
            2
        )