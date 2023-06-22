import pygame
import tkinter as tk
from tkinter import simpledialog
from pygame.locals import QUIT
import math


pygame.init()
tamanho = (1000,500)
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Space Marker")
Song = pygame.mixer.Sound("assets/backSoundMusic.wav")
clock = pygame.time.Clock()
Icon = pygame.image.load("assets/space.png")
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("assets/bg.jpg")
saves = "marcacoes.txt"
running  = True

pygame.mixer.music.load("assets/backSoundMusic.wav")
pygame.mixer.music.play(-1)

superficie = pygame.Surface(tamanho)
superficie.blit(fundo, (0, 0))

pontos_estrelas = []

fonte_nome = pygame.font.SysFont(None, 20)

def obter_nome_estrela(posicao):
    root = tk.Tk()
    root.withdraw()
    nome_estrela = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    root.destroy()
    if nome_estrela:
        pontos_estrelas.append((posicao, nome_estrela))
        desenhar_ponto(posicao, nome_estrela)
        desenhar_linhas()


def desenhar_ponto(posicao, nome_estrela):
    ponto_x, ponto_y = posicao
    pygame.draw.circle(superficie, (255, 255, 255), (ponto_x, ponto_y), 5)
    texto_nome = fonte_nome.render(nome_estrela, True, (255, 255, 255))
    texto_rect = texto_nome.get_rect()
    texto_rect.center = (ponto_x, ponto_y + 15)  
    superficie.blit(texto_nome, texto_rect)

def desenhar_linhas():
    for i in range(len(pontos_estrelas) - 1):
        ponto1, _ = pontos_estrelas[i]
        ponto2, _ = pontos_estrelas[i + 1]
        pygame.draw.line(superficie, (255, 255, 255), ponto1, ponto2, 2)
        centro_x = (ponto1[0] + ponto2[0]) // 2
        centro_y = (ponto1[1] + ponto2[1]) // 2
        distancia = math.hypot(ponto2[0] - ponto1[0], ponto2[1] - ponto1[1])
        texto_distancia = fonte_nome.render(f"{distancia:.2f}", True, (255, 255, 255))
        texto_rect = texto_distancia.get_rect()
        texto_rect.center = (centro_x, centro_y - 20)  
        superficie.blit(texto_distancia, texto_rect)

jogo_ativo = True
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == QUIT:
            jogo_ativo = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            obter_nome_estrela(mouse_pos)

    tela.fill((0, 0, 0))
    
    tela.blit(superficie, (0, 0))
    
    pygame.display.flip()

pygame.quit()