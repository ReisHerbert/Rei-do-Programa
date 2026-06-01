
import pygame
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
from database_inimigo import INIMIGO_DB # importa o database para ser usado

class InimigoBasico(pygame.sprite.Sprite): #importa funções necessarias
    def __init__(self, tipo, x, y):#inicializa o objeto
        super().__init__()#chama a função para iniciar um novo objeto

        dados = INIMIGO_DB[tipo]

        self.velocidade = dados["velocidade"]
        self.sprite = dados["sprite"]

        def update(self):
            self.movimento()
            self.morri()

        def movimento(self):
            pass

        def morri(self):
            self.kill()
            pass

        def receber_dano(self):
            #verificar se colidiu com o jogador
            self.morri()
            pass
    