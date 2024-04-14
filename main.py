import pygame
from logic.Game import Game
from logic.utils import create_terrain,load_music, load_player
from model.Menu.Main_menu import main_menu
from config import WIN_HEIGHT, WIN_WIDTH, tilemap

# Константы
SCREEN_SIZE = (WIN_HEIGHT, WIN_WIDTH)
ASSETS = {
    "player": 'assets/lpc_entry/png/walkcycle/BODY_male.png',
    "music": 'assets/menu.mp3',
    "block": 'assets/Block.png',
    "ground": 'assets/Ground.png'
}

# TODO: Класс для анимаций

# Main
def main():
    pygame.init()
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    pygame.display.set_caption('PRPG Game')
    load_music(ASSETS["music"])

    all_sprites, block_sprites = create_terrain(ASSETS, tilemap)
    player = load_player(ASSETS['player'], 100, 100)
    clock = pygame.time.Clock()

    running = True
    game = Game(screen, running, clock, (all_sprites, block_sprites), player)

    menu = main_menu(screen, game)

    while menu:
        menu = main_menu(screen, game)
    
    game.start()

    pygame.quit()

if __name__ == "__main__":
    main()