import pygame

def check_collision_sprite(one, two):
    if pygame.sprite.spritecollideany(one, two):
        return True
    else:
        return False
    
def check_collision_rect(one, two):
    if pygame.rect.Rect.colliderect(one, two):
        return True
    else:
        return False
    
def check_collision_rect_arr(one, two):
    while len(two) > 0:
        if check_collision_rect(one, two[0]):
            return True
        else:
            two.pop(0)
    return False

def push_out(char_hitbox, block_hitbox):
    """
    Выталкивает хитбокс персонажа из блока, если они пересекаются.

    :param char_hitbox: хитбокс персонажа (pygame.Rect)
    :param block_hitbox: хитбокс блока (pygame.Rect)
    """
    # Проверяем коллизию между хитбоксами
    if char_hitbox.colliderect(block_hitbox):
        # Вектор смещения от центра блока до центра персонажа
        dx = char_hitbox.centerx - block_hitbox.centerx
        dy = char_hitbox.centery - block_hitbox.centery

        # Смещаем объект в направлении, противоположном пересечению
        if abs(dx) > abs(dy):  # горизонтальное или вертикальное прижатие
            if dx > 0:  # персонаж слева от центра блока
                char_hitbox.right = block_hitbox.left
            else:  # персонаж справа от центра блока
                char_hitbox.left = block_hitbox.right
        else:
            if dy > 0:  # персонаж выше центра блока
                char_hitbox.bottom = block_hitbox.top
            else:  # персонаж ниже центра блока
                char_hitbox.top = block_hitbox.bottom

    # Возвращаем новые координаты хитбокса персонажа
    return char_hitbox