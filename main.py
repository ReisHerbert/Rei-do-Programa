import pygame
from configs import *
from Scripts.Jogador.jogador import *
from Scripts.Jogador.tiro import *
from interface import Interface
from Scripts.Mapa.gerenciador_mapa import carregar_tiles, desenhar_mapa, criar_colisores, F1_MAPA
from Scripts.Inimigos.instancia_inimigos import instancia_inimigo, InimigoBasico

class Jogo():
    def __init__(self):

        # main sets
        pygame.init()
        self.tela = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption(name_game)
        self.relogio = pygame.time.Clock()
        self.rodando = True

        #MAPA
        self.tiles = carregar_tiles("Assets/Mapa")
        self.paredes = criar_colisores(F1_MAPA)

        #grupos
        self.todos_sprites = pygame.sprite.Group()
        self.tiro_sprites = pygame.sprite.Group()
        self.inimigos_sprites = pygame.sprite.Group()

        #jogador
        self.vidas = 3
        self.jogador = Jogador(self.todos_sprites, self.tiro_sprites, self)

        # estados do jogo
        self.interface = Interface(self)

        # verifica morte
        if self.interface.estado == self.interface.jogando:
            if self.vidas <= 0:
                self.interface.estado = self.interface.game_over

        self.ultimo_spawn = pygame.time.get_ticks()
        self.tempo_spawn = 2000

        self.fase_atual = 1
        self.fase_maxima = 3
        self.tempo_fase = pygame.time.get_ticks()
        self.duracao_fase = 30000
    
    def reset_total(self):
        self.inimigos_sprites.empty()
        self.tiro_sprites.empty()
        self.jogador.rect = self.jogador.image.get_frect(center = (largura/2,altura/2))

    def run(self):
        while self.rodando:
            #relogio
            self.relogio.tick(60)

            #eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False  
                if self.interface.estado == self.interface.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.reset_total()
                self.interface.handle_event(event)

            agora = pygame.time.get_ticks()
            if agora - self.tempo_fase > self.duracao_fase:
                if self.fase_atual <= self.fase_maxima:
                    self.fase_atual += 1
                    self.tempo_fase = agora

            # spawn automático ↓
            if self.interface.estado == self.interface.jogando:
                agora = pygame.time.get_ticks()
                if agora - self.ultimo_spawn > self.tempo_spawn:
                    novo = instancia_inimigo(largura, altura, self.fase_atual, self.jogador)
                    self.inimigos_sprites.add(novo)
                    self.ultimo_spawn = agora

            # UPDATE
            if self.interface.estado == self.interface.jogando:
                self.todos_sprites.update()
                for inimigo in self.inimigos_sprites:  # ← update separado com paredes
                    inimigo.update(self.paredes)
                self.colisao()
            self.interface.update()         

            # DRAW
        
            self.tela.fill("black")
            desenhar_mapa(self.tela, F1_MAPA, self.tiles)
            self.todos_sprites.draw(self.tela)
            self.inimigos_sprites.draw(self.tela)
            self.interface.draw(self.tela)

            pygame.display.update()
        pygame.quit()

    def colisao(self):
        # jogador vs inimigos
        if pygame.sprite.spritecollide(self.jogador, self.inimigos_sprites, True):
            self.vidas -= 1
            pass 

        # tiros vs inimigos
        for tiro in self.tiro_sprites:
            inimigos_acertados = pygame.sprite.spritecollide(tiro, self.inimigos_sprites, False)
            for inimigo in inimigos_acertados:
                inimigo.morri()  # elimina só esse inimigo
                tiro.kill()    

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()