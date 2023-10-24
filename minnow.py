import pygame
from settings import *


class Minnow:
    def __init__(self,x,y):
        self.right_image = pygame.image.load("assets/images/purplefish.png")
        self.right_image.set_colorkey((0,0,0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = True

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.rect.bottom = SCREEN_HEIGHT - 2 * TILE_SIZE
            self.moving_up = True
            self.moving_down = False
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.moving_left = True
            self.moving_right = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

