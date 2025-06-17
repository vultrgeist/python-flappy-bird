import pygame
import os

# Initialize Pygame
pygame.init()

# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Set up colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create bird image (yellow circle)
bird_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(bird_surface, YELLOW, (20, 20), 20)
pygame.image.save(bird_surface, "assets/bird.png")

# Create pipe image (green rectangle)
pipe_surface = pygame.Surface((80, 320), pygame.SRCALPHA)
pipe_surface.fill(GREEN)
pygame.image.save(pipe_surface, "assets/pipe.png")

# Create background image (blue sky)
background_surface = pygame.Surface((400, 600))
background_surface.fill(BLUE)
pygame.image.save(background_surface, "assets/background.png")

pygame.quit()

print("Assets created successfully!")
