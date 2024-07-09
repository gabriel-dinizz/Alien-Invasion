import pygame

class Ship:
    
    def __init__(self, ai_game):
        # Inicializa a nave e sua posição inicial

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load(
            "/Users/gabrieldiniz/dev/AlienInvasion/ship.bmp")
        
        # Redimensiona a imagem da nave
        self.image = pygame.transform.scale(self.image, (60, 60))  # Defina o tamanho desejado aqui
        
        self.rect = self.image.get_rect()
        # Coloca a nave na parte inferior central da tela
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Atualiza a posição da nave com base na flag de movimento
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        # Desenha a nave na tela na posição atual
        self.screen.blit(self.image, self.rect)

