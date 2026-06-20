
import pygame
import random
from inimigo_basico import InimigoBasico
"""
o instancia inimigos deve verificar em qual fase está para  
    pegar as 4 posições em que ele pode instanciar
    escolher uma aleatoriamente
    instanciar um inimigo da lista de tipos de inimigos que a fase tem
"""
TIPOS_INIMIGOS = [
    "terrestre",
    "voador"
]
F1_INIMIGOS_TERRESTRES_PARA_DADOS = [
    "inimigo1_1F"
]
F1_INIMIGOS_VOADORES_PARA_DADOS = [
    "inimigo2_1F"
]

def posicao_aleatoria(largura_tela, altura_tela):
    lado = random.choice(["direita", "esquerda", "baixo", "cima"])

    if lado == "cima":
        return random.randint(0, largura_tela), 0 #-> retorna uma posição aleatoria entre 0 e o tamanho da tela no eixo x e 0 no eixo y
    elif lado == "baixo":
        return random.randint(0, largura_tela), altura_tela #-> retorna uma posição aleatoria entre 0 e o tamanho da tela no eixo x e a altura da tela no eixo y
    elif lado == "direita":
        return largura_tela, random.randint(0, altura_tela) #-> retorna uma posição no tamanho da tela no eixo x e uma posição aleatoria entre 0 e a altura da tela no eixo y
    else:
        return 0, random.randint(0, altura_tela) #-> retorna uma posição em 0 no eixo x e uma posição aleatoria entre 0 e a altura da tela no eixo y
    
def instancia_inimigo(largura_tela, altura_tela, fase_atual, jogador):
    tipo_inimigo = random.choice(TIPOS_INIMIGOS)

    match fase_atual:
        case 1:
            match tipo_inimigo:
                case "terrestre":
                    id_inimigo_atual = random.choice(F1_INIMIGOS_TERRESTRES_PARA_DADOS)
                case "voador":
                    id_inimigo_atual = random.choice(F1_INIMIGOS_VOADORES_PARA_DADOS)
                case _:
                    id_inimigo_atual = random.choice(F1_INIMIGOS_TERRESTRES_PARA_DADOS)
                    
    pos_x, pos_y = posicao_aleatoria(largura_tela, altura_tela)

    return InimigoBasico(id_inimigo_atual, pos_x, pos_y, jogador)

        