#esse código define todas as configurações
#  relacionadas ao TIRO e suas interações
import pygame
from os.path import join

class Tiro(pygame.sprite.Sprite):
    def __init__(self, pos, direcao, groups):
        super().__init__(groups)

        # import imagem da bala
        self.image = pygame.image.load(join('Assets', 'Jogador', 'Projetil.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        #movimento da bala
        self.direcao = pygame.Vector2(direcao)
        self.velocidade = 5

    def update(self):
        #update da direção da bala
        self.rect.x += self.direcao.x * self.velocidade
        self.rect.y += self.direcao.y * self.velocidade

        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()