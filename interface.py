import pygame
from configs import *
from os.path import join

class Interface():
    def __init__(self,jogo):
        #carrega o dado de vidas do jogador
        self.jogo = jogo
        #estados

        self.menu = 0
        self.jogando = 1
        self.game_over = 2
        self.estado = self.menu

        #dados dos pontos da UI
        self.tempo_inicio = 0
        self.tempo_final = 0

        #import fonts
        self.fonte = pygame.font.Font(join("Assets","Pixeboy.ttf"),64)
        self.fonte_p= pygame.font.Font(join("Assets","Pixeboy.ttf"),36)
        self.fonte_pp= pygame.font.Font(join("Assets","Pixeboy.ttf"),28)
        self.background = pygame.image.load(join("Assets","background.png"))
        self.controles = pygame.image.load(join("Assets","controles_t.png")).convert_alpha()
        self.controles_aumentados = pygame.transform.scale(self.controles, (160, 96))

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
                    self.jogo.vidas = 3

    def update(self):
        if self.estado == self.jogando and self.jogo.vidas <= 0:
            self.tempo_final = (pygame.time.get_ticks() - self.tempo_inicio) // 10
            self.estado = self.game_over

    def draw(self,tela):
        # MENU
        if self.estado == self.menu:
            titulo = self.fonte.render('REI DO PROGRAMA', False, Cores["amarelo saturado"])
            subtitulo = self.fonte_p.render('ENTER para jogar', False, Cores["creme"])

            tela.blit(self.background)
            tela.blit(titulo, titulo.get_rect(center=(largura//2, altura//2 - 160)))
            tela.blit(subtitulo, subtitulo.get_rect(center=(largura//2, altura//2 - 120)))
            tela.blit(self.controles_aumentados,self.controles_aumentados.get_rect(topleft=(12,-5)))

        # JOGANDO
        elif self.estado == self.jogando:
            tempo_jogando = (pygame.time.get_ticks() - self.tempo_inicio) // 10

            pontos_text = self.fonte_p.render(
                f'Pontos: {tempo_jogando}',
                False,
                Cores["creme"]
            )

            vida_text = self.fonte_p.render(
                f'Vidas: {self.jogo.vidas}',
                False,
                Cores["creme"]
            )

            tela.blit(pontos_text, (40, 40))
            tela.blit(vida_text, (40, 70))

        # GAME OVER
        elif self.estado == self.game_over:
            self.jogo.tela.fill("black")
            game_over_text = self.fonte.render('GAME OVER', False, Cores["vermelho"])
            sub1 = self.fonte_p.render(f'Pontos: {self.tempo_final}', False, Cores["cinza"])
            sub2 = self.fonte_p.render("PRESS 'R' PARA VOLTAR AO MENU", False, Cores["cinza"])

            tela.blit(game_over_text, game_over_text.get_rect(center=(largura//2, altura//2 - 50)))
            tela.blit(sub1, sub1.get_rect(center=(largura//2, altura//2 + 10)))
            tela.blit(sub2, sub2.get_rect(center=(largura//2, altura//2 + 42)))    