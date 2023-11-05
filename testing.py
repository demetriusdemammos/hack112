import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Draw Rectangle in Pygame")

# Define rectangle parameters
rectangle_color = (255, 0, 0)  # Red color in RGB
rectangle_x = 100
rectangle_y = 100
rectangle_width = 200
rectangle_height = 100

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Draw the rectangle on the screen
    pygame.draw.rect(screen, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()