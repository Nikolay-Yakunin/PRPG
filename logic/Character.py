import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        """
        Constructor for the Character class.

        :param image: The image surface associated with the character.
        :param x: The horizontal position of the character.
        :param y: The vertical position of the character.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the image of the character onto the given surface at the character's current position.
        
        :param surface: The surface onto which the image will be drawn.
        """
        surface.blit(self.image, self.rect)

    def move(self, x: int, y: int) -> None:
        """
        Moves the character by the specified x and y offsets.
        
        :param x: The amount to move the character horizontally.
        :param y: The amount to move the character vertically.
        """
        self.rect.x += x
        self.rect.y += y