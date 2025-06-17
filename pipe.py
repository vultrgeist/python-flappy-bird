import pygame
import random
from constants import PIPE_SPEED, PIPE_GAP

class Pipe:
    def __init__(self, x, image_path, height=None):
        self.pipe_image = pygame.image.load(image_path)
        self.x = x
        if height is None:
            self.height = random.randint(100, 400)
        else:
            self.height = height
        self.top_rect = self.pipe_image.get_rect(midbottom=(self.x, self.height))
        self.bottom_rect = self.pipe_image.get_rect(midtop=(self.x, self.height + PIPE_GAP))

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.pipe_image, self.top_rect)
        screen.blit(pygame.transform.flip(self.pipe_image, False, True), self.bottom_rect)

    def off_screen(self):
        return self.x < -self.pipe_image.get_width()