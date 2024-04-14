import pygame
from logic.utils import update_screen, handle_events
from config import FPS


class Game:
    def __init__(self, screen, running, clock, terrain, player):
        self.screen = screen
        self.running = running
        self.clock = clock
        self.terrain = terrain
        self.player = player

    def start(self):

        # Основной игровой цикл
        all_sprites, block_sprites = self.terrain
        player = self.player
        clock = pygame.time.Clock()

        while self.running:
            self.running = handle_events()
            keys = pygame.key.get_pressed()
            directional_mapping = {
                pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
                pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)
            }
            for key, direction in directional_mapping.items():
                if keys[key]:
                    player.move(direction, block_sprites)
            update_screen(self.screen, all_sprites, player) 
            clock.tick(FPS)