import pygame
from configs import *

class Jogo():
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption(name_game)
        self.relogio = pygame.time.Clock()
        self.rodando = True
    def run(self):
        while self.rodando:
            #relogio
            relogio = self.relogio.tick(60)
            #eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
            #update

            #draw
            pygame.display.update()
        
        pygame.quit()

jogo = Jogo()
jogo.run()