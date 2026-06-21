import pygame
from configs import *
from os.path import join

pygame.init()

#set configs
largura,altura = 800,600
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
menu,jogando,game_over = 0,1,2
estado = menu
vidas = 3

#import fonts
fonte = pygame.font.Font(join("Assets","Pixeboy.ttf"),64)
fonte_p= pygame.font.Font(join("Assets","Pixeboy.ttf"),36)

#loop main
rodando = True
while rodando:
    relogio.tick(60)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        # MENU
        if estado == menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                estado = jogando
                tempo_inicio = pygame.time.get_ticks()

        # GAME OVER 
        elif estado == game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                estado = menu
                vidas = 3

    #draw
    tela.fill("black")

    if estado == jogando and vidas <= 0:
        tempo_final = (pygame.time.get_ticks() - tempo_inicio) // 10
        estado = game_over

    if estado == menu:
        # criando texto
        titulo = fonte.render('REI DO PROGRAMA', False, Cores["azul"])
        subtitulo = fonte_p.render('ENTER para jogar', False, Cores["branco"])
        controles_mov = fonte_p.render('MOVIMENTAR: W,A,S,D', False, Cores["branco"])
        controles_tiro = fonte_p.render('ATIRAR: K', False, Cores["branco"])

        # drawing text
        tela.blit(titulo, titulo.get_rect(center=(largura//2, altura//2 - 50)))
        tela.blit(subtitulo, subtitulo.get_rect(center=(largura//2, altura//2 + 50)))
        tela.blit(controles_mov, controles_mov.get_rect(bottomleft=(20,altura -50)))
        tela.blit(controles_tiro, controles_tiro.get_rect(bottomleft=(20,altura -20)))


    elif estado == jogando:
        
        tempo_jogando = (pygame.time.get_ticks() - tempo_inicio) //10

        pontos_text = fonte_p.render(f'Pontos:{tempo_jogando}', False, Cores["branco"])
        vida_text = fonte_p.render(f"Vidas: {vidas}",False, Cores["branco"])

        tela.blit(pontos_text, (20, 20))
        tela.blit(vida_text,(20,50))
     
    elif estado == game_over:
        game_over_text = fonte.render('GAME OVER', False, Cores["vermelho"])
        subtitulo1 = fonte_p.render(f'Pontos: {tempo_final}',False,Cores["branco"])
        subtitulo2 = fonte_p.render("PRESS 'R' PARA VOLTAR AO MENU", False,Cores["branco"] )

        tela.blit(game_over_text, game_over_text.get_rect(center=(largura//2,altura//2 - 50)))
        tela.blit(subtitulo1, subtitulo1.get_rect(center=(largura//2, altura//2 + 10)))
        tela.blit(subtitulo2, subtitulo2.get_rect(center=(largura//2, altura//2 + 42)))
    
    #updates
    pygame.display.update()


pygame.quit()


        
