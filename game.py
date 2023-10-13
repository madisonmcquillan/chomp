import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")
screen.fill((52, 222, 235))

pygame.draw.rect(screen, (246, 230, 178), (0, 300, 400, 400))
pygame.draw.rect(screen, (0, 200, 0), (200, 150, 75, 25))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200, 200, 64, 64))
pygame.display.flip()
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
