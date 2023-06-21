import pygame

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
running  = True

pygame.mixer.music.load("assets/backSoundMusic.wav")
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    tela.blit(fundo,(0,0))



    pygame.display.update()
    clock.tick(60)

pygame.quit()