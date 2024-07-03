import sys

import pygame

from settings import Settings

class AlienInvasion:
    #classe para gerenciar assets e comportamento

    def __init__(self):
        #inicia jogo e recursos
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            self.settings.screen.widht, self.settings.screen.height
        )
        pygame.display.set_caption("Alien Invasion")
        #cor do background
        self.bg_color = (230, 230, 230)

    def run_game(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg.color)
            pygame.display.flip()
if __name__ == '__main__':
    #rodar o jogo
    ai = AlienInvasion()
    ai.run_game
