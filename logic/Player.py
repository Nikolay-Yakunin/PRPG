import pygame
from logic.Character import Character
from logic.Animation import Animation

class Player(Character):
    def __init__(self, spritesheet, x, y):
        self.animations = {
            'up': Animation(spritesheet, 0, 9),
            'left': Animation(spritesheet, 64, 9),
            'down': Animation(spritesheet, 128, 9),
            'right': Animation(spritesheet, 192, 9)
            }
        initial_image = self.animations['down'].animation[0]
        super().__init__(initial_image, x, y)
        self.current_animation = 'down'
        self.image_index = 0
        self.animation_speed = 0.2 # Скорость анимации, можно регулировать
        self.frame_counter = 0
        self.health = 100
        self.speed = 2

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

        if pygame.sprite.spritecollideany(self, obstacles):
            self.rect.topleft = old_position

        self.image = self.animations[self.current_animation].update()

# TODO: Добавить методы для боя