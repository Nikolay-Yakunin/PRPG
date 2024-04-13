import pygame
from logic.utils import mouse_handler
from config import WHITE, BLACK, BACKGROUND_COLOR

class Button:
    def __init__(self, text, width, height, pos, elevation):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = BLACK

        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = BLACK

        self.text_surf = pygame.font.Font(None, 30).render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen):
        #Elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)

        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = BLACK
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    # Call the function or whatever it is when the button is clicked here
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = BLACK


def main_menu(screen, game):
    background = pygame.Surface(screen.get_size())
    background.fill(BACKGROUND_COLOR)
    
    button_start = Button('Start Game', 200, 40, (100, 150), 5)
    button_settings = Button('Settings', 200, 40, (100, 250), 5)
    button_exit = Button('Exit to OS', 200, 40, (100, 350), 5)

    menu_running = True
    while menu_running:
        screen.blit(background, (0, 0))
        for button in [button_start, button_settings, button_exit]:
            button.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.top_rect.collidepoint(event.pos):
                    print("Start Game button pressed!")
                    game.start()
                elif button_settings.top_rect.collidepoint(event.pos):
                    print("Settings button pressed!")
                    # Here you can call a function to open the settings
                elif button_exit.top_rect.collidepoint(event.pos):
                    print("Exit to OS button pressed!")
                    pygame.quit()

        
        pygame.display.update()

    return False