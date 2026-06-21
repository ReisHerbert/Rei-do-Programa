import pygame
from configs import *
from os.path import join

class Interface():
    def __init__(self):
        #estados

        self.menu = 0
        self.jogando = 1
        self.game_over = 2
        self.estado = self.menu

        #dados do jogo
        self.vidas = 3
        self.tempo_inicio = 0
        self.tempo_final = 0

        #import fonts
        self.fonte = pygame.font.Font(join("Assets","Pixeboy.ttf"),64)
        self.fonte_p= pygame.font.Font(join("Assets","Pixeboy.ttf"),36)

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN:
            # MENU
            if self.estado == self.menu:
                if event.key == pygame.K_RETURN:
                    self.estado = self.jogando
                    self.tempo_inicio = pygame.time.get_ticks()

            # GAME OVER 
            elif self.estado == self.game_over:
                if event.key == pygame.K_r:
                    self.estado = self.menu

    def update(self):
        if self.estado == self.jogando and self.vidas <= 0:
            self.tempo_final = (pygame.time.get_ticks() - self.tempo_inicio) // 10
            self.estado = self.game_over

    def draw(self,tela):
        # MENU
        if self.estado == self.menu:
            titulo = self.fonte.render('REI DO PROGRAMA', False, Cores["azul"])
            subtitulo = self.fonte_p.render('ENTER para jogar', False, Cores["branco"])
            mov = self.fonte_p.render('MOVIMENTAR: W,A,S,D', False, Cores["branco"])
            tiro = self.fonte_p.render('ATIRAR: K', False, Cores["branco"])

            tela.blit(titulo, titulo.get_rect(center=(largura//2, altura//2 - 50)))
            tela.blit(subtitulo, subtitulo.get_rect(center=(largura//2, altura//2 + 50)))
            tela.blit(mov, mov.get_rect(bottomleft=(20, altura - 50)))
            tela.blit(tiro, tiro.get_rect(bottomleft=(20, altura - 20)))

        # JOGANDO
        elif self.estado == self.jogando:
            tempo_jogando = (pygame.time.get_ticks() - self.tempo_inicio) // 10

            pontos_text = self.fonte_p.render(
                f'Pontos: {tempo_jogando}',
                False,
                Cores["branco"]
            )

            vida_text = self.fonte_p.render(
                f'Vidas: {self.vidas}',
                False,
                Cores["branco"]
            )

            tela.blit(pontos_text, (20, 20))
            tela.blit(vida_text, (20, 50))

        # GAME OVER
        elif self.estado == self.game_over:
            game_over_text = self.fonte.render('GAME OVER', False, Cores["vermelho"])
            sub1 = self.fonte_p.render(f'Pontos: {self.tempo_final}', False, Cores["branco"])
            sub2 = self.fonte_p.render("PRESS 'R' PARA VOLTAR AO MENU", False, Cores["branco"])

            tela.blit(game_over_text, game_over_text.get_rect(center=(largura//2, altura//2 - 50)))
            tela.blit(sub1, sub1.get_rect(center=(largura//2, altura//2 + 10)))
            tela.blit(sub2, sub2.get_rect(center=(largura//2, altura//2 + 42)))