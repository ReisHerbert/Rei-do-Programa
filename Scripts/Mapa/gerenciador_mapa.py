
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

        return tiles

#MAPAS
F1_MAPA = [
    ["grama", "grama", "grama", "grama"],
    ["grama", "parede", "parede", "grama"],
    ["grama", "tronco",  "tronco",  "grama"],
    ["grama", "grama", "grama", "grama"],
]

#DESENHANDO MAPA E COLISORES
TILE_SIZE = 32
TILES_SOLIDOS = ["tronco", "parede"]

def desenhar_mapa(tela, mapa, tiles):
        for index_linha, linha in enumerate(mapa):
                for index_coluna, nome_tile in enumerate(linha):
                        tile_img = tiles[nome_tile]
                        x = index_coluna * TILE_SIZE
                        y = index_linha * TILE_SIZE

                        tela.blit(tiles, (x, y))

def criar_colisores(mapa):
        paredes = []
        for index_linha, linha in enumerate(mapa):
                for index_coluna, nome_tile in enumerate(linha):
                        if nome_tile in TILES_SOLIDOS:
                                rect = pygame.rect(
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
