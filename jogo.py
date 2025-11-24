import pygame
import random
import sys          

pygame.init()
LARGURA, ALTURA = 600, 300
TELA = pygame.display.set_mode((LARGURA, ALTURA)) 
pygame.display.set_caption("Astronauta ")
# Cores
BRANCO = (255, 255, 255)

# Carregando imagens
fundo = pygame.image.load("fundo.png")
astronauta_correndo = pygame.image.load("astronauta_correndo.png")
astronauta_correndo = pygame.image.load("astronauta_2correndo.png")    
astronauta_pulando = pygame.image.load("astronauta_pulando.png")
obstaculos_imgs = [
    pygame.image.load("terra_tr.png"),
    pygame.image.load("jupiter_tr.png"),
    pygame.image.load("saturn_tr.png")
] 

# Variáveis do jogo
relogio = pygame.time.Clock()
FPS = 35
astronauta_y = 205
pulo = False
vel_pulo = 0
obstaculos = []
obst_tempo = 0

def desenhar(astronauta_img):
    TELA.blit(fundo, (0, 0))
    TELA.blit(astronauta_img, (50, astronauta_y))
    for obs in obstaculos:
        TELA.blit(obs["img"], (obs["x"], obs["y"]))
    pygame.display.update()

def colisao(astronauta_rect, obstaculos):
    for obs in obstaculos:
        if astronauta_rect.colliderect(pygame.Rect(obs["x"], obs["y"], 35, 35)):
            return True
    return False

rodando = True
while rodando:
    relogio.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not pulo:
            if evento.key == pygame.K_SPACE:
                pulo = True
                vel_pulo = -12

    if pulo:
        astronauta_y += vel_pulo
        vel_pulo += 1
        if astronauta_y >= 205:
            astronauta_y = 205
            pulo = False

    # Obstáculos
    obst_tempo += 1
    if obst_tempo > 60:
        obst_tempo = 0
        obstaculos.append({
            "img": random.choice(obstaculos_imgs),
            "x": LARGURA,
            "y": 220
        })

    for obs in obstaculos:
        obs["x"] -= 6
    obstaculos = [obs for obs in obstaculos if obs["x"] > -40]

    astronauta_img = astronauta_pulando if pulo else astronauta_correndo
    desenhar(astronauta_img)

    if colisao(pygame.Rect(50, astronauta_y, 35, 35), obstaculos):
        print("Game Over")
        pygame.quit() 
        sys.exit()
