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
        self.LARGURA = 32
        self.ALTURA = 32

        self.sprites = {
            "right": pygame.transform.scale(pygame.image.load(join('Assets','Jogador','player_right.png')).convert_alpha(), (self.LARGURA, self.ALTURA)),
            "left":  pygame.transform.scale(pygame.image.load(join('Assets','Jogador','player_left.png')).convert_alpha(),  (self.LARGURA, self.ALTURA)),
            "up":    pygame.transform.scale(pygame.image.load(join('Assets','Jogador','player_up.png')).convert_alpha(),    (self.LARGURA, self.ALTURA)),
            "down":  pygame.transform.scale(pygame.image.load(join('Assets','Jogador','player_down.png')).convert_alpha(),  (self.LARGURA, self.ALTURA)),
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
        self.duracao_cooldown = 300

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
    def instanciar_tiro(self,direcao:str):
        som = pygame.mixer.Sound("Assets/Sons/tiro.mp3")
        som.set_volume(0.8)
        som.play()
        Tiro(self.rect.center,self.direcao_tiro[direcao],groups=(self.todos_sprites, self.tiros_sprites))
        self.pode_atirar = False
        self.tempo_tiro = pygame.time.get_ticks()

    def update(self):
        # input movimentação jogador

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

        if self.pode_atirar:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.instanciar_tiro("up")

            elif keys[pygame.K_DOWN]:
                self.instanciar_tiro("down")

            elif keys[pygame.K_LEFT]:
                self.instanciar_tiro("left")

            elif keys[pygame.K_RIGHT]:
                self.instanciar_tiro("right")

        self.temporizador_tiro()