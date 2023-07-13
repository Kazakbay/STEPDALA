import pygame 
from pygame.locals import *
import random
screen = pygame.display.set_mode((1000, 500))

pygame.init()
running = True


class Ball():
    def __init__(self):
        super().__init__()
        self.pos = [random.randint(0, 900), random.randint(0, 400)]
        self.color = (random.randint(0, 244), random.randint(0, 244), random.randint(0, 244))
        self.radius = 30
        self.add_x = 3
        self.add_y = 3
    
    def update(self):
        self.pos[0] += self.add_x
        self.pos[1] += self.add_y
        if self.pos[0] > 1000:
            self.add_x = -3
        elif self.pos[0] < 0:
            self.add_x = 3
        if self.pos[1] > 500:
            self.add_y = -3
        elif self.pos[1] < 0:
            self.add_y = 3
        
clock = pygame.time.Clock()

moving_objects = []
for i in range(15):
    i = Ball()
    moving_objects.append(i)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for ball in moving_objects:
        ball.update()
        pygame.draw.circle(screen, ball.color, ball.pos, ball.radius)

    pygame.display.update()
    clock.tick(125)
