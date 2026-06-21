#esse código define todas as configurações
#  relacionadas ao jogador e suas interações

import pygame
from os.path import join

largura,altura = 800,600
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

pygame.init()

class Jogador(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        #sprites
        self.sprites = {
        "right":pygame.image.load(join('Assets','Jogador','player_right.png')).convert_alpha(),
        "left": pygame.image.load(join('Assets','Jogador','player_left.png')).convert_alpha(),
        "up":pygame.image.load(join('Assets','Jogador','player_up.png')).convert_alpha(),
        "down" :pygame.image.load(join('Assets','Jogador','player_down.png')).convert_alpha(),
        }
        
        #direcao
        self.direcao = "down"     
        self.image = self.sprites[self.direcao]
        self.rect = self.image.get_frect(center = (largura/2,altura/2))
        self.velocidade = 3

        #tiro
        
        self.pode_atirar = True
        self.tempo_tiro = 0
        self.duracao_cooldown = 200
        self.direcao_tiro = {
        "up": pygame.Vector2(0, -1),
        "down": pygame.Vector2(0, 1),
        "left": pygame.Vector2(-1, 0),
        "right": pygame.Vector2(1, 0),
}
        
    
    def temporizador_tiro(self):
        if not self.pode_atirar:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_tiro >= self.duracao_cooldown:
                self.pode_atirar = True

    def update(self):
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
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_k] and self.pode_atirar:
            Tiro(
            self.rect.center,
            self.direcao_tiro[self.direcao],
            groups=(todos_sprites,tiro_sprites))

            self.pode_atirar = False
            self.tempo_tiro = pygame.time.get_ticks() 
        self.temporizador_tiro()

class Tiro(pygame.sprite.Sprite):
    def __init__(self,pos,direcao,groups):
        super().__init__(groups)

        self.image = pygame.image.load(join('Assets','Jogador','Projetil.png'))
        self.rect = self.image.get_rect(center = pos)
        self.direcao_tiro = direcao
        self.velocidade = 5

    def update(self):
        self.rect.x += self.direcao_tiro.x * self.velocidade
        self.rect.y += self.direcao_tiro.y * self.velocidade
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()

def colisao():
    colisao_jogador = pygame.sprite.spritecollide(jogador, inimigos_sprites, True)
    if colisao_jogador:
        pass
    for tiro in tiro_sprites:
        sprites_colididos = pygame.sprite.spritecollide(tiro,inimigos_sprites,True)
        if sprites_colididos:
            tiro.kill()


#sprites
todos_sprites = pygame.sprite.Group()
jogador = Jogador(todos_sprites)
tiro_sprites = pygame.sprite.Group()
inimigos_sprites = pygame.sprite.Group()


rodando = True
while rodando:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    #draws

    tela.fill('darkgrey')
    todos_sprites.draw(tela)
    colisao()

    #update
    pygame.display.update()
    todos_sprites.update()
pygame.quit()

