import pygame
import tkinter as tk
from tkinter import simpledialog
from pygame.locals import QUIT

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


def desenhar_ponto(posicao, nome_estrela):
    ponto_x, ponto_y = posicao
    pygame.draw.circle(superficie, (255, 255, 255), (ponto_x, ponto_y), 5)
    texto_nome = fonte_nome.render(nome_estrela, True, (255, 255, 255))
    texto_rect = texto_nome.get_rect()
    texto_rect.center = (ponto_x, ponto_y + 15)
    superficie.blit(texto_nome, texto_rect)


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