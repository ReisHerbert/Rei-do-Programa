import pygame
from configs import *
from Scripts.Jogador.jogador import *
from Scripts.Jogador.tiro import *

class Jogo():
    def __init__(self):
        # main sets
        pygame.init()
        self.tela = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption(name_game)
        self.relogio = pygame.time.Clock()
        self.rodando = True

        #grupos
        self.todos_sprites = pygame.sprite.Group()
        self.tiro_sprites = pygame.sprite.Group()
        self.inimigos_sprites = pygame.sprite.Group()

        #jogador
        self.jogador = Jogador(self.todos_sprites, self.tiro_sprites)

    def run(self):
        while self.rodando:
            #relogio
            self.relogio.tick(60)

            #eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            #draw
            self.tela.fill("black")
            self.todos_sprites.draw(self.tela)
            self.colisao()

            #update
            self.todos_sprites.update()
            pygame.display.update()
        pygame.quit()

    def colisao(self):
        # jogador vs inimigos
        if pygame.sprite.spritecollide(self.jogador, self.inimigos_sprites, True):
            pass  # dano aqui depois

        # tiros vs inimigos
        pygame.sprite.groupcollide(
            self.tiro_sprites,
            self.inimigos_sprites,
            True,
            True
        )

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()