import pygame
from random import randint
from os.path import join

pygame.init()

# configurações base
largura,altura = 800,600
display_surface = pygame.display.set_mode((largura,altura))
name_game = pygame.display.set_caption(('Rei do Programa'))
clock = pygame.time.Clock()

#script do 

rodando = True
while rodando:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    display_surface.fill ('darkgray')
   
    pygame.display.update()
    

pygame.quit()