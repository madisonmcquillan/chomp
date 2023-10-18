import pygame
import sys

# DIMENSIONS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # TILES ARE SQUARE HEIGHT == WIDTH

# COLORS
WATER_COLOR = (52, 222, 235)
SAND_COLOR = (246, 230, 178)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH/2 - TILE_SIZE/2, SCREEN_HEIGHT/2 - TILE_SIZE/2))

pygame.display.flip()
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
