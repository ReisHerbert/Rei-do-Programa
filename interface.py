import pygame
from os.path import join

pygame.init()

#setup display temporario
largura,altura = 800,600
tela = pygame.display.set_mode((largura,altura))
game_name = pygame.display.set_caption('Rei do Programa')

class Interface():
    def __init__(self):
        pass

    def score_tela():
        tempo_atual = pygame.time.get_ticks()//100
        fonte = pygame.font.Font(join('Assets', 'Pixeboy.ttf'),50)
        text_surf = fonte.render(str(tempo_atual), False,(240,240,240))
        text_rect = text_surf.get_frect(midbottom = (largura/2,altura-50))
        tela.blit(text_surf,text_rect)
        pygame.draw.rect(tela, 'white',text_rect.inflate(20,15).move(0,-12),5,10)




#loop main
rodando=True
while rodando:
    #eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
    #update
    

    #draw
    tela.fill('black')

    pygame.display.update()

pygame.quit()    

