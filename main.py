import pygame
from logic.SplitesSheet import SplitesSheet
from logic.Player import Player
from logic.Terrain import Block, Ground
from config import WIN_HEIGHT, WIN_WIDTH, FPS, tilemap


# Константы
SCREEN_SIZE = (WIN_HEIGHT, WIN_WIDTH)
BACKGROUND_COLOR = (66, 132, 245)
ASSETS = {
    "player": 'assets/lpc_entry/png/walkcycle/BODY_male.png',
    "music": 'assets/menu.mp3',
    "block": 'assets/Block.png',
    "ground": 'assets/Ground.png'
}

def load_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1, 0.0)

def load_player():
    player = Player(SplitesSheet(ASSETS['player']), 100, 100)

    return player

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

# Add camera
def update_screen(screen, all_sprites, player):
    # Отрисовка бэкграунда и игрока
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    player.draw(screen)
    pygame.display.update()

# Terrain
def create_terrain():
    all_sprites = pygame.sprite.LayeredUpdates()
    block_sprites = pygame.sprite.Group()  # Group for non-walkable sprites
    block_image = SplitesSheet(ASSETS['block']).get_image(0, 0, 64, 64)
    ground_image = SplitesSheet(ASSETS['ground']).get_image(0, 0, 64, 64)


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

# Main
def main():
    pygame.init()
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    pygame.display.set_caption('PRPG Game')
    load_music(ASSETS["music"])
    all_sprites, block_sprites = create_terrain()
    player = load_player()
    clock = pygame.time.Clock()

    # TODO: Камера должна двигаться за персонажем

    running = True
    while running:
        running = handle_events()
        keys = pygame.key.get_pressed()
        directional_mapping = {
            pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
            pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)
        }
        for key, direction in directional_mapping.items():
            if keys[key]:
                player.move(direction, block_sprites)
        update_screen(screen, all_sprites, player) #camera
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()