import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica = pygame.mixer.music.load('BoxCat Games - Map Theme.mp3')
pygame.mixer.music.play(-1)

som_moeda = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
x = int(largura/2)
y = int(altura/2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0

fonte = pygame.font.SysFont('arial', 40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Zombie Escape')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
 #       if event.type == KEYDOWN:
  #          if event.key == K_a:
   #             x = x - 20
    #        if event.key == K_d:
     #           x = x + 20
      #      if event.key == K_w:
       #         y = y - 20
        #    if event.key == K_s:
         #       y = y + 20

    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        som_moeda.play()

    tela.blit(texto_formatado, (420,40))




    pygame.display.update()