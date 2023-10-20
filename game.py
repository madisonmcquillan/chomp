import pygame
import sys
import random
import fish
from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/disney_fonts.ttf", 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
sand_top.set_colorkey((0, 0, 0))
seagrass.set_colorkey((0, 0, 0))

my_fish = fish.Fish(200, 200)
background = screen.copy()
clock = pygame.time.Clock()


def draw_background():
    # draw water
    background.fill(WATER_COLOR)
    # BLIT SAND TILES ACROSS THE BOTTOM OF THE SCREEN
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
        background.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE))

    # randomly place 4 pieces of seagrass along the bottom of the screen
    for i in range(4):
        x = random.randint(0, SCREEN_WIDTH - TILE_SIZE)
        y = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
        background.blit(seagrass, (x, y))

    # draw the CHOMP! title
    text = game_font.render("Chomp!", True, (100, 150, 75))
    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))


draw_background()


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False

        # update game screen

    screen.blit(background, (0, 0))
    my_fish.update()
    my_fish.draw(screen)
    pygame.display.flip()
    clock.tick(60)


