import pygame
import SplitesSheet
import Character


class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1152, 600))
        self.background = pygame.image.load('assets/Interface/FreePlatformerNA/Mockup.png')
        self.player_splitsheet = SplitesSheet('assets/lpc_entry/png/hurt/BODY_male.png').get_image(0, 0, 64, 64)

        self.player = Character(self.player_splitsheet, 0, 0) 

    def start(self):

        # Основной игровой цикл
        while self.running:
            # Обновление экрана
            self.screen.fill((66, 132, 245))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player_splitsheet, (0,0))

            pygame.display.update()

            # Пауза
            self.clock.tick(24)
            # Проверка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill((66, 132, 245))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player_splitsheet, (0,0))
            pygame.display.update()