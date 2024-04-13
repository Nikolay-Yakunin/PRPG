import pygame
import datetime
import json
from config import GROUND_LAYER, BLOCK_LAYER, TILE_SIZE
class Terrain(pygame.sprite.Sprite):
    def __init__(self, image, x, y, walkable=True, layer=GROUND_LAYER):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))
        self.walkable = walkable
        self._layer = layer

class Ground(Terrain):
    def __init__(self, x, y, ground_image):
        super().__init__(ground_image, x, y, walkable=True, layer=GROUND_LAYER)

class Block(Terrain):
    def __init__(self, x, y, block_image):
        super().__init__(block_image, x, y, walkable=False, layer=BLOCK_LAYER)

exampleTiles = {
    'B': Block,
    '.': Ground,
    }

class RenderTerrain:
    def __init__(self, all_sprites, tilemap):
        self.all_sprites = all_sprites
        self.tilemap = tilemap
        self.entities_positions = {}

    def update_entity_position(self, entity_id, position):
        self.entities_positions[entity_id] = position

    def render(self):
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                if tile == 'B':
                    block = Block(x, y, exampleTiles[tile])
                    self.all_sprites.add(block)
                elif tile == '.':
                    ground = Ground(x, y, exampleTiles[tile])
                    self.all_sprites.add(ground)
    def save_tilemap(self):
        filename = f"map_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.json"
        with open(filename, 'w') as file:
            json.dump({
                'tilemap': self.tilemap,
                'entities_positions': self.entities_positions
            }, file, indent=4)
        return filename
        

