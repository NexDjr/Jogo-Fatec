import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

altura = 650
largura = 950

#para a posição inicial ser o meio da tela
poicao_em_x_do_circulo = largura/2
poicao_em_y_do_circulo = altura/2

x_1 = 0
y_1 = 0
r = 250
g = 0
b = 0

d = 15
cm = 15

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Nex-Game")
clock = pygame.time.Clock()

while True:
    tela.fill((0,0,0))
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                x_1 -= 20
                d += 20
            if event.key == K_d or event.key == K_RIGHT:
                x += 20
            if event.key == K_w or event.key == K_UP:
                y -= 20
            if event.key == K_s or event.key == K_DOWN:
                y += 20'''
    if pygame.key.get_pressed()[K_a]:
         x -= 10
    if pygame.key.get_pressed()[K_d]:
         x += 10
    if pygame.key.get_pressed()[K_w]:
         y -= 10
    if pygame.key.get_pressed()[K_s]:
         y += 10
    if pygame.key.get_pressed()[K_LEFT]:
         x_1 -= 10
    if pygame.key.get_pressed()[K_RIGHT]:
         x_1 += 10
    if pygame.key.get_pressed()[K_UP]:
         y_1 -= 10
    if pygame.key.get_pressed()[K_DOWN]:
         y_1 += 10
    circulo = pygame.draw.circle(tela, (r,g,b), (x,y),(7))
    retangulo = pygame.draw.rect(tela, (0,255,0), (x_1,y_1,15,15))
    if x >= largura:
        x = 0
    if x < 0:
        x = largura
    if y < 0:
        y = altura
    if y > altura:
        y = 0
    if x_1 >= largura:
            x = 0
    if x_1 < 0:
        x_1 = largura
    if y_1 < 0:
        y_1 = altura
    if y_1 > altura:
        y_1 = 0
    if pygame.key.get_pressed()[K_SPACE]:
        d = x_1 + 2
        x_1 -= d
        retangulo = pygame.draw.rect(tela, (0,0,255), (x_1,y_1,d,cm))
    pygame.display.update()

