import pygame
from configs import *
from Scripts.Jogador.jogador import *
from Scripts.Jogador.tiro import *
from interface import Interface
from Scripts.Mapa.gerenciador_mapa import carregar_tiles, desenhar_mapa, criar_colisores, F1_MAPA
from Scripts.Inimigos.instancia_inimigos import instancia_inimigo, InimigoBasico
pygame.mixer.init() #->inicializa o sitema de musica

class Jogo():
    def __init__(self):

        # main sets
        pygame.init()
        self.tela = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption(name_game)
        self.relogio = pygame.time.Clock()
        self.rodando = True

        #SONS
        self.sons = {
            "trilha_sonora": "Assets/Sons/trilha.mp3",
            "game_over": "Assets/Sons/gameover.mp3",
            "hit": "Assets/Sons/hit.wav",
            "passou_nivel":"Assets/Sons/passanivel.wav"
        }
        
        pygame.mixer.music.load(self.sons["trilha_sonora"])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1) #-> -1 para rodar em loop

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
                pygame.mixer.music.pause()
                self.tocarSom(self.sons["game_over"], 1.0)
                self.interface.estado = self.interface.game_over

        self.ultimo_spawn = pygame.time.get_ticks()
        self.tempo_spawn = 1500

        self.fase_atual = 1
        self.fase_maxima = 3
        self.tempo_fase = pygame.time.get_ticks()
        self.duracao_fase = 30000

        self.toquei_morri = True
    
    def tocarSom(self, som: str, volume:float):
        som = pygame.mixer.Sound(som)
        som.set_volume(volume)
        som.play()

    def reset_total(self):
        self.toquei_morri = True

        agora = pygame.time.get_ticks()
        self.ultimo_spawn = agora
        self.tempo_fase = agora
        self.fase_atual = 1

        pygame.mixer.music.unpause()

        self.inimigos_sprites.empty()
        self.tiro_sprites.empty()
        self.jogador.image = self.jogador.sprites["down"]
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
                self.tocarSom(self.sons["passou_nivel"], 0.8)
                self.tempo_fase = agora
                
                if self.fase_atual < self.fase_maxima:  
                    self.fase_atual += 1
                else:
                    self.fase_atual = 1  # volta pra fase 1 ao terminar

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

            if self.vidas <= 0 and self.toquei_morri == True:
                    pygame.mixer.music.pause()
                    self.tocarSom(self.sons["game_over"], 1.0) 
                    self.interface.estado = self.interface.game_over  
                    self.toquei_morri = False    

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
            self.tocarSom(self.sons["hit"], 0.8)
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