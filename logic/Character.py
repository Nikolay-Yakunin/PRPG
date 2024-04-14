import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = pygame.Rect(self.rect.x + 16, self.rect.y, 32, self.rect.height)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)
        self.hitbox = pygame.Rect(self.rect.x + 16, self.rect.y, 32, self.rect.height)
        self.hitbox = pygame.draw.rect(surface, (255,0,0), self.hitbox,2)
        
    def move(self, x: int, y: int) -> None:
        self.hitbox.x += x
        self.hitbox.y += y
        self.rect.x += x
        self.rect.y += y
