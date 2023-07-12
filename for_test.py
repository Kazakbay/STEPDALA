import pygame 
from pygame.locals import *
import random

screen = pygame.display.set_mode((1000, 500))

COLORS = [(244, 133, 234), (234, 234, 234), (112, 122, 122), (120, 12 ,12)]

class Cube(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.color = COLORS[random.randint(0, 3)]

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([20, 20])
        self.image.fill(self.color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = random.randrange(0, 980, 20), random.randrange(0, 480, 20)
        self.collide_rect = pygame.Rect(self.rect, (20, 20))

    def update(self):
        self.rect = random.randrange(0, 980, 20), random.randrange(0, 480, 20)
        self.collide_rect = pygame.Rect(self.rect, (20, 20))

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.color = (45, 45, 45)
        self.rect = [0, 0]
        self.image = pygame.Surface([20, 20])
        self.image.fill(self.color)
        self.dir = 'right'
        self.collide_rect = pygame.Rect(0, 0, 20, 20)


    #creating method for moving the Player
    def update(self):
        if self.dir == 'right':
            self.rect[0] += 20
        elif self.dir == 'left':
            self.rect[0] -= 20
        elif self.dir == 'up':
            self.rect[1] -= 20
        elif self.dir == 'down':
            self.rect[1] += 20

        if self.rect[0] < 0:
            self.rect[0] = 980
        elif self.rect[0] > 980:
            self.rect[0] = 0
        elif self.rect[1] < 0:
            self.rect[1] = 480
        elif self.rect[1] > 480:
            self.rect[1] = 0

        self.collide_rect = pygame.Rect(self.rect, (20, 20))

#creating the sprites and groups
container = pygame.sprite.Group()
characters = pygame.sprite.Group()
player = Player()
characters.add(player)

for item in range(10):
    item = Cube()
    container.add(item)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                dir = 'left'
            elif event.key == K_d:
                dir = 'right'
            elif event.key == K_w:
                dir = 'up'
            elif event.key == K_s:
                dir = 'down'
    player.dir = dir
    player.update()
    for sprite in container:
        if pygame.Rect.colliderect(sprite.collide_rect, player.collide_rect):
            sprite.update()
    screen.fill((0, 0, 0))
    characters.draw(screen)
    container.draw(screen)
    pygame.display.update()
    pygame.time.wait(60)



    