from file import game
import pygame
from pygame import mixer

pygame.init()
mixer.init()

height = 700
width = 500

background = pygame.image.load("img/background.jpg")
alien = pygame.image.load("img/alien (2).png")
alien2 = pygame.image.load("img/alien (1).png")
alien3 = pygame.image.load("img/alien.png")
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("space invaders")

font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 32)
font2 = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 16)
text = font.render("space invaders", True, (255, 255, 255))
text2 = font2.render("press space to start", True, (255, 255, 255))
textRect = text.get_rect()
textRect2 = text.get_rect()
textRect.center = (350, 200)
textRect2.center = (365, 240)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game()
                run = False
    screen.blit(background, (0, 0))
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(alien, (200, 60))
    screen.blit(alien, (300, 400))
    screen.blit(alien, (60, 300))
    screen.blit(alien2, (500, 100))
    screen.blit(alien2, (440, 250))
    screen.blit(alien2, (30, 150))
    screen.blit(alien3, (300, 270))

    pygame.display.flip()