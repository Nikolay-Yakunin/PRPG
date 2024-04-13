import pygame
from logic.SplitesSheet import SplitesSheet
from logic.Player import Player
from logic.Terrain import Block, Ground
from logic.Game import Game
from logic.utils import update_screen, create_terrain,load_music, load_player, handle_events
from model.Menu.Main_menu import main_menu
from config import WIN_HEIGHT, WIN_WIDTH, FPS, tilemap


# Константы
SCREEN_SIZE = (WIN_HEIGHT, WIN_WIDTH)
ASSETS = {
    "player": 'assets/lpc_entry/png/walkcycle/BODY_male.png',
    "music": 'assets/menu.mp3',
    "block": 'assets/Block.png',
    "ground": 'assets/Ground.png'
}

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