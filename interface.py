import pygame
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

        # JOGANDO
        elif estado == jogando:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                vidas -= 1

        # GAME OVER (só reset)
        elif estado == game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                estado = menu
                vidas = 3


    tela.fill("black")

    if estado == jogando and vidas <= 0:
        tempo_final = (pygame.time.get_ticks() - tempo_inicio) // 10
        estado = game_over

    if estado == menu:
        texto = fonte.render('REI DO PROGRAMA', False, (37, 99, 235))
        tela.blit(texto, texto.get_rect(center=(400, 220)))
        t2 = fonte_p.render('ENTER para jogar', False, (203, 213, 225))
        tela.blit(t2, t2.get_rect(center=(400, 320)))

    elif estado == jogando:
        
        tempo_jogando = (pygame.time.get_ticks() - tempo_inicio) //10
        texto = fonte_p.render(f'Pontos:{tempo_jogando}', False, (255, 255, 255))
        vida_text = fonte_p.render(f"Vidas: {vidas}",False,(255, 255, 255))
        tela.blit(texto, (20, 20))
        tela.blit(vida_text,(20,50))
     
    elif estado == game_over:
        t = fonte.render('GAME OVER', False, (220, 38, 38))
        t2 = fonte_p.render(f'Pontos: {tempo_final} | PRESS "R" PARA VOLTAR AO MENU',False,(203, 213, 225))

        tela.blit(t, t.get_rect(center=(400, 230)))
        tela.blit(t2, t2.get_rect(center=(400, 320)))
    
    pygame.display.update()


pygame.quit()


        
