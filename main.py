import pygame
from configs import *
from Scripts.Jogador.jogador import *
from Scripts.Jogador.tiro import *
from interface import Interface

class Jogo():
    def __init__(self):

        # main sets
        pygame.init()
        self.tela = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption(name_game)
        self.relogio = pygame.time.Clock()
        self.rodando = True

        # estados do jogo
        self.interface = Interface()

        #grupos
        self.todos_sprites = pygame.sprite.Group()
        self.tiro_sprites = pygame.sprite.Group()
        self.inimigos_sprites = pygame.sprite.Group()

        #jogador
        self.jogador = Jogador(self.todos_sprites, self.tiro_sprites, self.interface)

    def run(self):
        while self.rodando:
            #relogio
            self.relogio.tick(60)

            #eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False  
                self.interface.handle_event(event)

            # UPDATE 
            self.todos_sprites.update()
            self.colisao()

            # sincroniza dados do jogador → interface
            self.interface.vidas = self.jogador.vidas
            self.interface.update()

            # verifica morte
            if self.interface.estado == self.interface.jogando:
                if self.jogador.vidas <= 0:
                    self.interface.estado = self.interface.game_over

            # DRAW
        
            self.tela.fill("black")
            self.todos_sprites.draw(self.tela)
            self.interface.draw(self.tela)

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