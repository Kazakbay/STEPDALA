import pygame 
from pygame.locals import *
import os 

class Sonic(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, speed):
        super().__init__()
        self.sprites = []
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.is_pressed = False
        self.sprites.append(pygame.image.load('tile000.png'))
        self.sprites.append(pygame.image.load('tile001.png'))
        self.sprites.append(pygame.image.load('tile002.png'))
        self.sprites.append(pygame.image.load('tile003.png'))
        self.sprites.append(pygame.image.load('tile004.png'))
        self.sprites.append(pygame.image.load('tile005.png'))

        for image in self.sprites:
            self.sprites[self.sprites.index(image)] = pygame.transform.scale(image, (100, 100))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x_pos, self.y_pos]

    def update(self, coordinates):
        if self.is_pressed:
            self.current_sprite += self.speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.walk_left = False
            self.image = self.sprites[int(self.current_sprite)]

            
            if self.rect.left > coordinates[0]:
                self.rect.left -= 5
            elif self.rect.left < coordinates[0]:
                self.rect.left += 5
            
            if self.rect.top > coordinates[1]:
                self.rect.top -= 5
            elif self.rect.top < coordinates[1]:
                self.rect.top += 5

# General setup 
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Sonic(0, 0, 1)
moving_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            player.is_pressed = True
        
    
    coordinates = pygame.mouse.get_pos()
    # Drawing
    screen.fill((122, 122, 122))
    moving_sprites.draw(screen)
    moving_sprites.update(coordinates)
    pygame.display.flip()
    clock.tick(10)
