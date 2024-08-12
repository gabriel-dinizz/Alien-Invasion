import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # class to represent a single alien

    def __init__(self, ai_game):
        # initialize the alien and its starting position

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #load the alien image and set its rect attribute
        self.image = pygame.image.load( "/Users/gabrieldiniz/dev/AlienInvasion/images/alien.bmp")
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #sguarda [psociao] horizontal do alien
        self.x = float(self.rect.x)
    def updat(self):
        #move the alien to the right
        self.x += self.settings.alien_speed
        self.rect.x = self.x

