
import pygame
import os

#CARREGANDO IMAGENS 
def carregar_tiles(pasta):
        tiles = {}

        for arquivo in os.listdir(pasta):#retorna uma lista com os nomes de arquivos e subdiretórios em um caminho fornecido
                if arquivo.endswith(".png"):
                        nome = arquivo.replace(".png", "") #retira '.png' do nome do arquivo 
                        caminho = os.path.join(pasta, arquivo)
                        tiles[nome] = pygame.image.load(caminho).convert_alpha()
                        img = pygame.image.load(caminho).convert_alpha()
                        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                        tiles[nome] = img

        return tiles

#MAPAS
#DESENHANDO MAPA E COLISORES
TILE_SIZE = 32
TILES_SOLIDOS = ["tronco", "parede"]

COLUNAS = 896  // TILE_SIZE  #->28
LINHAS  = 512 // TILE_SIZE  #-> 16 

F1_MAPA = []
for i in range(LINHAS):
        if i == 0 or i == LINHAS - 1:       # primeira (0) ou última (16)
                linha = ["parede"] * COLUNAS    # linha inteira de parede
        elif i == 4 or i == 8 or i == 12 : 
                linha = (
                        ["parede"] +
                        ["grama"] * 6 +
                        ["tronco"] * 2 +
                        ["grama"] * 9 +
                        ["tronco"] * 2 +
                        ["grama"] * 7 +
                        ["parede"]
                )          
        else:
                linha = ["parede"] + ["grama"] * (COLUNAS  - 2) + ["parede"]   # linha normal de grama com paredes nas laterais
        F1_MAPA.append(linha)




def desenhar_mapa(tela, mapa, tiles):
        for index_linha, linha in enumerate(mapa):
                for index_coluna, nome_tile in enumerate(linha):
                        tile_img = tiles[nome_tile]
                        x = index_coluna * TILE_SIZE
                        y = index_linha * TILE_SIZE
                        tela.blit(tile_img, (x, y))

def criar_colisores(mapa):
        paredes = []
        for index_linha, linha in enumerate(mapa):
                for index_coluna, nome_tile in enumerate(linha):
                        if nome_tile in TILES_SOLIDOS:
                                rect = pygame.Rect(
                                        index_coluna * TILE_SIZE, 
                                        index_linha * TILE_SIZE, 
                                        TILE_SIZE, 
                                        TILE_SIZE
                                        )
                                paredes.append(rect)
        return paredes

#metodos a serem chamados
#tiles = carregar_tiles("Assets/Tiles")
#paredes = criar_colisores(F1_MAPA)
#desenhar_mapa(tela, F1_MAPA, tiles)
