import pygame

class Ship:
    
    def __init__(self, ai_game):
        # Inicializa a nave e sua posição inicial

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load(
            "/Users/gabrieldiniz/dev/AlienInvasion/ship.bmp")
        
        # Redimensiona a imagem da nave
        self.image = pygame.transform.scale(self.image, (60, 60))  # Defina o tamanho desejado aqui
        
        self.rect = self.image.get_rect()
        # Coloca a nave na parte inferior central da tela
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Atualiza a posição da nave com base na flag de movimento
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        # Desenha a nave na tela na posição atual
        self.screen.blit(self.image, self.rect)
