import pygame
   

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()   