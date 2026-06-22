
import pygame
import math
"""
O inimigo básico deve servir como pai de todos os inimigos
ele deve resceber os dados de um tipo de inimigo e atribuir nas variaveis que irão ser utilizadas para:
    mover o inimigo na direção do player 
    morrer caso ele seja atingido
    evitar colisões (caso tipo: voador)
    ter colisões (caso tipo: terrestre)
variaveis:
    velocidade
    sprite
"""
from Scripts.Inimigos.database_inimigo import INIMIGO_DB # importa o database para ser usado

class InimigoBasico(pygame.sprite.Sprite): #importa funções necessarias
    def __init__(self, id, x, y, jogador):#inicializa o objeto
        super().__init__()#chama a função para iniciar um novo objeto

        dados = INIMIGO_DB[id]

        self.tipo = dados["tipo"]
        self.velocidade = dados["velocidade"]
        self.animacao_dados = dados["animacao_frames"]
        self.animacao_frames = []
        for frame in self.animacao_dados:
            sprite_atual = pygame.image.load(frame).convert_alpha()
            self.animacao_frames.append(sprite_atual)
        self.frame_index = 0
        self.animacao_velocidade = 0.1
        self.jogador = jogador
        self.lado = "left"
        self.ALTURA = 32
        self.LARGURA = 32
        self.tempo = 0

        self.tempo_spawn = pygame.time.get_ticks()  # momento que nasceu
        self.delay_colisao = 2000

        self.pos_x = float(x) 
        self.pos_y = float(y) 

        self.image = self.animacao_frames[0]

        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, paredes):
        self.movimento( paredes)

    def movimento(self, paredes):
        posicao_jogador = pygame.math.Vector2(self.jogador.rect.center)
        posicao_self = pygame.math.Vector2(self.rect.center)
        direcao = posicao_jogador - posicao_self
        print(f"jogador: {posicao_jogador} | inimigo: {posicao_self} | direcao: {direcao}")  # ← add

        if direcao.length() > 0:
            direcao  = direcao.normalize()
        
        if direcao.x > 0:
            self.lado = "right"
        else:
            self.lado = "left"

        if self.tipo != "voador":
            self.pos_x += direcao.x * self.velocidade * (1/60)
            self.pos_y += direcao.y * self.velocidade * (1/60)
            self.rect.x = int(self.pos_x)  # ← converte só aqui
            self.rect.y = int(self.pos_y)
        else:
            self.tempo += 1
            self.pos_x += direcao.x * self.velocidade * (1/60)
            self.pos_y += direcao.y * self.velocidade * (1/60) + math.sin(self.tempo * 0.05) * 1.5
            self.rect.x = int(self.pos_x)
            self.rect.y = int(self.pos_y)

        self.colisao(paredes, direcao)
        self.animacao()

    def animacao(self):
        self.frame_index += self.animacao_velocidade * (1/120)

        if self.frame_index > len(self.animacao_frames) - 1:
            self.frame_index = 0

        frame_atual = self.animacao_frames[int(self.frame_index)]
        
        if self.lado == "right":
            self.image = pygame.transform.flip(frame_atual, True, False)
        else:
            self.image = frame_atual
        pass

    def morri(self):
        self.kill()
        pass

    def colisao(self, paredes, direcao):
        if self.tipo == "voador":
            return

        agora = pygame.time.get_ticks()
        if agora - self.tempo_spawn < self.delay_colisao:
            # ainda no delay — só move, sem testar colisão
            self.pos_x += direcao.x * self.velocidade * (1/60)
            self.pos_y += direcao.y * self.velocidade * (1/60)
            self.rect.x = int(self.pos_x)
            self.rect.y = int(self.pos_y)
            return

        self.pos_x += direcao.x * self.velocidade * (1/60)
        self.rect.x = int(self.pos_x)
        for parede in paredes:
            if self.rect.colliderect(parede):
                if direcao.x > 0:
                    self.rect.right = parede.left
                else:
                    self.rect.left = parede.right
                self.pos_x = float(self.rect.x)  # ← sincroniza o float com a correção

    # move Y → testa → corrige
        self.pos_y += direcao.y * self.velocidade * (1/60)
        self.rect.y = int(self.pos_y)
        for parede in paredes:
            if self.rect.colliderect(parede):
                if direcao.y > 0:
                    self.rect.bottom = parede.top
                else:
                    self.rect.top = parede.bottom
                self.pos_y = float(self.rect.y)

        
    #verificar se colidiu com o jogador
    #colidiu com o jogador ou com projetil
    #colidiu com a parede
