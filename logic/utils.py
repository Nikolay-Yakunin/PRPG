import pygame
from logic.Player import Player
from logic.SplitesSheet import SplitesSheet
from logic.Terrain import Block, Ground
from config import BACKGROUND_COLOR

def mouse_handler():
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    if mouse_pressed[0]:
        click_action = 'left_click'

    elif mouse_pressed[2]:
        click_action = 'right_click'

    elif mouse_pressed[1]:
        click_action = 'middle_click'
    else:
        click_action = None
    
    return mouse_pos, click_action

def update_screen(screen, all_sprites, player):
    # Отрисовка бэкграунда и игрока
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    player.draw(screen)
    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def load_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1, 0.0)

def load_player(assets, x, y):
    player = Player(assets, x, y)

    return player

def create_terrain(assets, tilemap):
    all_sprites = pygame.sprite.LayeredUpdates()
    block_sprites = pygame.sprite.Group()  # Group for non-walkable sprites
    block_image = SplitesSheet(assets['block']).get_image(0, 0, 64, 64)
    ground_image = SplitesSheet(assets['ground']).get_image(0, 0, 64, 64)


    for y, row in enumerate(tilemap):
        for x, tile in enumerate(row):
            if tile == 'B':
                block = Block(x, y, block_image)
                all_sprites.add(block)
                block_sprites.add(block)
            elif tile == '.':
                ground = Ground(x, y, ground_image)
                all_sprites.add(ground)
    return all_sprites, block_sprites
