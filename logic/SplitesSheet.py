import pygame

class SplitesSheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image
