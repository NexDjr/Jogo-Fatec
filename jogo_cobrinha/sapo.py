import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura_tela = 640
altura_tela = 480
preto = (0,0,0)
branco = (255,255,255)
azul = (0,0,255)
vermelho = (255,0,0)
verde = (0,255,0)


tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Sprites")

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("sprites/attack_1.png"))
        self.sprites.append(pygame.image.load("sprites/attack_2.png"))
        self.sprites.append(pygame.image.load("sprites/attack_3.png"))
        self.sprites.append(pygame.image.load("sprites/attack_4.png"))
        self.sprites.append(pygame.image.load("sprites/attack_5.png"))
        self.sprites.append(pygame.image.load("sprites/attack_6.png"))
        self.sprites.append(pygame.image.load("sprites/attack_7.png"))
        self.sprites.append(pygame.image.load("sprites/attack_8.png"))
        self.sprites.append(pygame.image.load("sprites/attack_9.png"))
        self.sprites.append(pygame.image.load("sprites/attack_10.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)


while True:
    tela.fill(preto)
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit()
            exit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()