import pygame
from constants import GRAVITY, BIRD_FLAP_STRENGTH, SCREEN_HEIGHT

class Bird:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(50, SCREEN_HEIGHT // 2))
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = BIRD_FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)