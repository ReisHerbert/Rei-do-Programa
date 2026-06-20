#esse código define todas as configurações
#  relacionadas ao jogador e suas interações

import pygame
from os.path import join

largura,altura = 800,600
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load (join('player.png'))
        self.rect = self.image.get_frect(center = (largura/2,altura/2))

        #cooldown

        self.pode_atirar = True
        self.tempo_tiro = 0
        self.duracao_cooldown = 400
    
    def temporizador_tiro(self):
        if not self.pode_atirar:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_tiro >= self.duracao_cooldown:
                self.pode_atirar = True

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]: 
            self.rect.x += 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_RIGHT] and self.can_shoot:
            print("fire shoot")
            Tiro(self.rect.midtop,groups=(todos_sprites,tiro_sprites))
            self.pode_atirar = False
            self.tempo_tiro = pygame.time.get_ticks() 
        self.temporizador_tiro()


class Tiro(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("player.png"))
        self.rect = self.image.get_rect(midbottom = pos)
    def update(self):
        self.rect.centery-=400


#sprites
todos_sprites = pygame.sprite.Group()
tiro_sprites = pygame.sprite.Group()
inimigos_sprites = pygame.sprite.Group()


rodando = True
while rodando:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    for tiro in tiro_sprites:
        pygame.sprite.spritecollide(tiro,inimigos_sprites, True)

    tela.fill('darkgrey')
    todos_sprites.draw(tela)
    tiro_sprites.draw(tela)

    pygame.display.update()

pygame.quit()

