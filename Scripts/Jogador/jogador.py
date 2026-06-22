#esse código define todas as configurações
#  relacionadas ao JOGADOR e suas interações

import pygame
from os.path import join
from configs import *
from Scripts.Jogador.tiro import *
from interface import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, groups,tiros_sprites,jogo):
        super().__init__(groups)

        #sprites do jogador
        self.sprites = {
        "right":pygame.image.load(join('Assets','Jogador','player_right.png')).convert_alpha(),
        "left": pygame.image.load(join('Assets','Jogador','player_left.png')).convert_alpha(),
        "up":pygame.image.load(join('Assets','Jogador','player_up.png')).convert_alpha(),
        "down" :pygame.image.load(join('Assets','Jogador','player_down.png')).convert_alpha(),
        }
        
        #vida do jogador
        self.jogo = jogo
        

        #direcao do jogador
        self.direcao = "down"     
        self.image = self.sprites[self.direcao]
        self.rect = self.image.get_frect(center = (largura/2,altura/2))
        self.velocidade = 3

        #tiro setup
        self.pode_atirar = True
        self.tempo_tiro = 0
        self.duracao_cooldown = 200

        #direção do tiro
        self.direcao_tiro = {
        "up": pygame.Vector2(0, -1),
        "down": pygame.Vector2(0, 1),
        "left": pygame.Vector2(-1, 0),
        "right": pygame.Vector2(1, 0),}

        #tiro sprites
        self.todos_sprites = groups
        self.tiros_sprites = tiros_sprites
        
    def temporizador_tiro(self):
        if not self.pode_atirar:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_tiro >= self.duracao_cooldown:
                self.pode_atirar = True

    def update(self):
        """ if self.interface.estado != self.interface.jogando:
            return """
        # movimentação input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.velocidade
            self.direcao = "right"

        elif keys[pygame.K_a]:
            self.rect.x -= self.velocidade
            self.direcao = "left"

        elif keys[pygame.K_w]:
            self.rect.y -= self.velocidade
            self.direcao = "up"

        elif keys[pygame.K_s]:
            self.rect.y += self.velocidade
            self.direcao = "down"

        self.image = self.sprites[self.direcao]

        #input do tiro
        if keys[pygame.K_k] and self.pode_atirar:
            Tiro(self.rect.center,self.direcao_tiro[self.direcao],groups=(self.todos_sprites,self.tiros_sprites))
            self.pode_atirar = False
            self.tempo_tiro = pygame.time.get_ticks() 
        self.temporizador_tiro()