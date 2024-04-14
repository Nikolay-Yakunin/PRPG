import pygame
from logic.Character import Character
from logic.Animation import Animation
from logic.check_collision import check_collision_sprite, push_out

class Player(Character):
    def __init__(self, spritesheet: str, x: int, y: int):
        self.animations = {
            'up': Animation(spritesheet, 0, 9),
            'left': Animation(spritesheet, 64, 9),
            'down': Animation(spritesheet, 128, 9),
            'right': Animation(spritesheet, 192, 9)
            }
        initial_image = self.animations['down'].animation[0]
        super().__init__(initial_image, x, y)
        self.current_animation = 'down'
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

        if check_collision_sprite(self, obstacles):
            self.rect.topleft = old_position

        self.image = self.animations[self.current_animation].update()

    def hit(self):
        pass
    
# TODO: Добавить методы для боя

class Weapon:
    def __init__(self, name, image, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.range = (0, 0)
    
    def update(self):
        pass