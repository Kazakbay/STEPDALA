import pygame 
from pygame.locals import *
import random



class Cube(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color = (255, 212, 23)
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        self.image = pygame.Surface([20, 20])
        self.image.fill(self.color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = ((self.x_pos, self.y_pos))

sprites = pygame.sprite.Group()


screen = pygame.display.set_mode((1000, 500))
pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            sprites.add(Cube(x, y))
    
    screen.fill((122, 122, 122))
    sprites.draw(screen)
    pygame.display.update()
