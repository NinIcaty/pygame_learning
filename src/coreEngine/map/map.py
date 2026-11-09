import pygame as pg
import pytmx
from PIL import Image
import sys
import os



class Map:

    def __init__(self, mapFilePath):
        self.mapFilePath = mapFilePath
        self.zoom = 1.5
        tmx_map = pytmx.TiledMap(
            self.mapFilePath,
            image_loader=self.image_loader
        )

        self.map_width = tmx_map.width * tmx_map.tilewidth
        self.map_height = tmx_map.height * tmx_map.tileheight

        # Render the map into one surface
        self.map_surface = pg.Surface((self.map_width,self.map_height), pg.SRCALPHA)

        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image is not None:
                        self.map_surface.blit(
                            image[0] if isinstance(image, tuple) else image,
                            (x * tmx_map.tilewidth, y * tmx_map.tileheight)
                        )
        # Apply zoom
        self.map_surface = pg.transform.scale_by(
            self.map_surface,
            self.zoom
        )

        self.map_width = self.map_surface.get_width()
        self.map_height = self.map_surface.get_height()


    def image_loader(self,filename:str,colorkey=None):

        def load():
            with Image.open(filename) as source:
                pil_image = source.convert("RGBA")

            image = pg.image.fromstring(
                pil_image.tobytes(),
                pil_image.size,
                "RGBA"
            ).convert_alpha()

            if colorkey is not None:
                image.set_colorkey(colorkey)

            return image, image.get_rect()

        return load


