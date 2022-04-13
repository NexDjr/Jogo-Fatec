import pygame
import constants
import  sprites
import os


class Game:
    def __init__(self):
        #criando a tela do game
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constants.LARGURA , constants.ALTURA))
        pygame.display.set_caption(constants.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.carregar_arquivos()
        self.font = pygame.font.match_font(constants.FONT)

    def novo_jogo(self):
        #instancia as classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constants.FPS)
            self.events()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def events(self):
        #define os eventos do jogando
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        #atualiza as sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        #desenha a ssprites
        self.tela.fill(constants.PRETO)#limpando a tela
        self.todas_as_sprites.draw(self.tela)#desenhando as sprites
        pygame.display.flip()

    def carregar_arquivos(self):
        #vai carregar arquivos de auidio e imagem
        diretorio_imagens = os.path.join(os.getcwd(),'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(),'audios')
        self.spritesheet = os.path.join(diretorio_imagens,constants.SPRITESHEET)
        self.pacman_logo_1 = os.path.join(diretorio_imagens,constants.PACMAN_LOGO_1)
        self.pacman_start_logo = pygame.image.load(self.pacman_logo_1).convert()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        #exibe um texto na tela do jogo
        font = pygame.font.Font(self.font, tamanho)
        texto =  font.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x,y)
        self.tela.blit(texto, texto_rect)

    def mostrar_start_logo(self, x, y):
        start_logo_rect = self.pacman_start_logo.get_rect()
        start_logo_rect.midtop = (x,y)
        self.tela.blit(self.pacman_start_logo, start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constants.MUSICA_START))
        pygame.mixer.music.play()

        self.mostrar_start_logo(constants.LARGURA/2, 20)
        self.mostrar_texto('Aperte uma tecla para jogar',
                           32,
                           constants.AMARELO,
                           constants.LARGURA/2,
                           constants.ALTURA/2
                           )
        self.mostrar_texto('Desenvolvido por:  Alunos Fatec',
                    18,
                    constants.BRANCO,
                    constants.LARGURA/2,
                    constants.ALTURA - 20
                    )
        pygame.display.flip()
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_audios,constants.TECLA_START)).play()

    def mostrar_tela_game_over(self):
        pass

g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()
