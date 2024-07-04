import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    # manage assets and behavior

    def __init__(self):
        # initialize game and resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            # simplify run game
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # rodar o jogo
    ai = AlienInvasion()
    ai.run_game()
