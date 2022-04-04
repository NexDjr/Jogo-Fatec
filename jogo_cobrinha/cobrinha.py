import pygame 
import pygame.freetype
from pygame.locals import *
from sys import exit
import time
from random import randint

pygame.init()
#Pedro é besta
altura = 500
largura = 550
fonte = pygame.font.Font('PKMN RBYGSC.ttf', 20)
fonte2 = pygame.font.Font('PKMN RBYGSC.ttf', 40)
pontos = 0
tamanho_cobra = 2
lista_corpo_cobra = []
morreu = False


pygame.mixer.music.set_volume(0.22)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Passing Time.mp3')
pygame.mixer.music.play(-1)

som_de_colisao = pygame.mixer.Sound('smw_1-up.wav')

#para a posição inicial do circulo ser o meio da tela
posicao_em_x_do_circulo =  randint(20,altura - 20)
posicao_em_y_do_circulo = randint(20,largura - 20)

#para a posição inicial do quadrado 100/100
posicao_em_x_do_retangulo = 100
posicao_em_y_do_retangulo = 100

# variaveis para alterar as cores
r = 250
g = 0
b = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Cobrinha")
clock = pygame.time.Clock()

velocidade = 10
x_controle = velocidade
y_controle = 0



def aumenta_cobra(lista_corpo_cobra):
    for XeY in lista_corpo_cobra:
        pygame.draw.rect(tela, (255,0,255),(XeY[0],XeY[1],15,15))

def reiniciar_jogo():
    global pontos, tamanho_cobra, posicao_em_y_do_retangulo, posicao_em_y_do_retangulo,lista_corpo_cobra, lista_cobra, posicao_em_y_do_circulo, posicao_em_x_do_circulo, morreu
    pontos = 0
    tamanho_cobra = 2
    posicao_em_x_do_retangulo = 100
    posicao_em_y_do_retangulo = 100
    lista_corpo_cobra =[]
    lista_cobra = []
    posicao_em_y_do_circulo = int(randint(20,480))
    posicao_em_x_do_circulo = (20,500)
    morreu = False

while True:
    tela.fill((0,0,0))
    clock.tick(25)
    mensagem = f'Pontos => {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    #Trecho de código que faz o programa parar quando a janela é fechada
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    posicao_em_x_do_retangulo += x_controle
    posicao_em_y_do_retangulo += y_controle

    #Criação dos objetos
    circulo = pygame.draw.circle(tela, (0,0,255), (posicao_em_x_do_circulo,posicao_em_y_do_circulo),(7))
    retangulo = pygame.draw.rect(tela, (0,255,0), (posicao_em_x_do_retangulo,posicao_em_y_do_retangulo,15,15))

    if retangulo.colliderect(circulo):
        posicao_em_x_do_circulo = int(randint(20,500))
        posicao_em_y_do_circulo = int(randint(20,480))
        pontos += 1
        som_de_colisao.play()
        tamanho_cobra +=1

    lista_cobra = []
    lista_cobra.append(posicao_em_x_do_retangulo)
    lista_cobra.append(posicao_em_y_do_retangulo)

    lista_corpo_cobra.append(lista_cobra)
    if lista_corpo_cobra.count(lista_cobra) > 1:
        morreu = True
        while morreu:
            mensagem_fim = "Game Over"
            mensagem_morte = fonte2.render(mensagem_fim, True, (0,0,0))
            tela.fill((255,0,0))
            tela.blit(mensagem_morte, (largura/2,altura/2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            pygame.display.update()
    if len(lista_corpo_cobra) > tamanho_cobra:
        del lista_corpo_cobra[0]

    aumenta_cobra(lista_corpo_cobra)


    # Condicionais para criar a impressão de fluxo continuo no movimento dos objetos
    if posicao_em_x_do_circulo >= largura:
        posicao_em_x_do_circulo = 0
    if posicao_em_x_do_circulo < 0:
        posicao_em_x_do_circulo = largura
    if posicao_em_y_do_circulo < 0:
        posicao_em_y_do_circulo = altura
    if posicao_em_y_do_circulo > altura:
        posicao_em_y_do_circulo = 0
    if posicao_em_x_do_retangulo >= largura:
        posicao_em_x_do_retangulo = 0
    if posicao_em_x_do_retangulo < 0:
        posicao_em_x_do_retangulo = largura
    if posicao_em_y_do_retangulo < 0:
        posicao_em_y_do_retangulo = altura
    if  posicao_em_y_do_retangulo > altura:
        posicao_em_y_do_retangulo = 0

    tela.blit(texto_formatado, (0,0))
    pygame.display.update()

