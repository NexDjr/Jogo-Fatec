import pygame
from pygame.locals import *
from sys import exit

pygame.init()



largura = 500
altura = 420

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()


fonte = pygame.font.Font('PKMN RBYGSC.ttf', 18)

click = False
def menu():
    while True:
        tela.fill((0, 0, 0))
        clock.tick(25)
        # Trecho de código que faz o programa parar quando a janela é fechada
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        mx,my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint(mx, my):
            if click:
                jogo()
        if button_2.collidepoint(mx, my):
            pass
        pygame.draw.rect(tela, (255,0,0), button_1)
        pygame.draw.rect(tela, (255,0,0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()



def jogo():
    while True:
        tela.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()


menu()