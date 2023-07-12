import pygame
from pygame.locals import *
import os




class Sonic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('tile000.png'))
        self.sprites.append(pygame.image.load('tile001.png'))
        self.sprites.append(pygame.image.load('tile002.png'))
        self.sprites.append(pygame.image.load('tile003.png'))
        self.sprites.append(pygame.image.load('tile004.png'))
        self.sprites.append(pygame.image.load('tile005.png'))

        for image in self.sprites:
            self.sprites[self.sprites.index(image)] = pygame.transform.scale(image, (200, 200))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 100]
    
    def update(self, speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.walk_left = False
        self.image = self.sprites[int(self.current_sprite)]

# General setup 
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Sonic()
moving_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Drawing
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(10)