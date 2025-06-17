import pygame
import random
from bird import Bird
from pipe import Pipe
from constants import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load assets
background_image = pygame.image.load("assets/background.png")

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    bird = Bird("assets/bird.png")
    pipes = [Pipe(SCREEN_WIDTH + i * 200, "assets/pipe.png") for i in range(3)]
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()

        # Update game objects
        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                # Get the height of the last pipe
                last_pipe_height = pipes[-1].height
                # Generate a new height within a range of the last pipe's height
                min_height = max(100, last_pipe_height - 100)
                max_height = min(400, last_pipe_height + 100)
                new_height = random.randint(min_height, max_height)
                pipes.append(Pipe(SCREEN_WIDTH, "assets/pipe.png", new_height))
                score += 1

        # Check for collisions
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                running = False
        if bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT:
            running = False

        # Draw everything
        screen.blit(background_image, (0, 0))
        for pipe in pipes:
            pipe.draw(screen)
        bird.draw(screen)

        # Display score
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Wait for key press to exit
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_key = False
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False

    pygame.quit()

if __name__ == "__main__":
    game_loop()
