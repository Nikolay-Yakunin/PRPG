import pygame
from logic.Character import Character

class Player(Character):
    def __init__(self, spritesheet, x, y):
        self.animations = {
            'up': [spritesheet.get_image(frame * 64, 0, 64, 64) for frame in range(9)],
            'left': [spritesheet.get_image(frame * 64, 64, 64, 64) for frame in range(9)],
            'down': [spritesheet.get_image(frame * 64, 128, 64, 64) for frame in range(9)],
            'right': [spritesheet.get_image(frame * 64, 192, 64, 64) for frame in range(9)]
        }
        initial_image = self.animations['down'][0]
        super().__init__(initial_image, x, y)
        self.current_animation = 'down'
        self.image_index = 0
        self.animation_speed = 0.2 # Скорость анимации, можно регулировать
        self.frame_counter = 0
        self.health = 100
        self.speed = 2

    def update(self):
        self.frame_counter += self.animation_speed
        if self.frame_counter >= len(self.animations[self.current_animation]):
            self.frame_counter = 0

        self.image_index = int(self.frame_counter)
        self.image = self.animations[self.current_animation][self.image_index]

    def move(self, direction, obstacles):
        dx, dy = direction
        old_position = self.rect.topleft
        self.rect.move_ip(dx * self.speed, dy * self.speed)
        
        if dx < 0:
            self.current_animation = 'left'
        elif dx > 0:
            self.current_animation = 'right'
        elif dy < 0:
            self.current_animation = 'up'
        elif dy > 0:
            self.current_animation = 'down'
        else:
            self.current_animation = 'down'
            self.frame_counter = 0
            self.image_index = 0

        if pygame.sprite.spritecollideany(self, obstacles):
            self.rect.topleft = old_position

        self.update()