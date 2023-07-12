import pygame
from pygame.locals import *
import random
screen = pygame.display.set_mode((1000, 500))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (122, 122, 122)

running = True 
snake_body = [[500, 200, 20, 20], [480, 200, 20, 20], [460, 200, 20, 20]]

food_pos = [0, 0, 20, 20]
pygame.display.set_mode((1000, 500))

dir = None 

#moves the head of the snake
def move_body(dir):
    x, y = snake_body[len(snake_body)-1][0], snake_body[len(snake_body)-1][1]
    #set the position of the snake's head
    if dir == 'left':
        snake_body[0][0] -= 20
    elif dir == 'right':
        snake_body[0][0] += 20
    elif dir == 'up':
        snake_body[0][1] -= 20
    elif dir == 'down':
        snake_body[0][1] += 20


    #if the snake's head crosses the borders it makes cordinates change to the opposite side
    # x position
    if snake_body[0][0] >= 1000:
        snake_body[0][0] = 0
    elif snake_body[0][0] < 0:
        snake_body[0][0] = 980

    # y position
    if snake_body[0][1] >= 500:
        snake_body[0][1] = 0
    elif snake_body[0][1] < 0:
        snake_body[0][1] = 480
   
    #moves whole snake body by changing positions of all body parts by previous body parts positions
    for i, item in enumerate(snake_body):
        index_for = len(snake_body) - i - 1
        if index_for >= 1:
            snake_body[index_for][0] = snake_body[index_for - 1][0]
            snake_body[index_for][1] = snake_body[index_for - 1][1]
    return snake_body ,x, y

def food(snake_body):
    food_pos[0] = random.randrange(0, 980, 20)
    food_pos[1] = random.randrange(0, 480, 20)
    for part in snake_body:
        if food_pos[0] != part[0] and food_pos[1] != part[1]:
            continue
        else:
            food_pos[0] = random.randrange(0, 980, 20)
            food_pos[1] = random.randrange(0, 480, 20)
    return food_pos

def is_eat(snake_body, food_pos):
    if snake_body[0][0] == food_pos[0] and snake_body[0][1] == food_pos[1]:
        return True

def add_part(snake_body):
    snake_body.append(x, y, 20, 20)

food(snake_body=snake_body)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                dir = 'up'
            elif event.key == K_s:
                dir = 'down'
            elif event.key == K_a:
                dir = 'left'
            elif event.key == K_d:
                dir = 'right'
    snake_body, x, y = move_body(dir=dir)
    if is_eat(snake_body=snake_body, food_pos=food_pos):
        snake_body.append([x, y, 20, 20])
        food(snake_body=snake_body)
    for item in snake_body:
        pygame.draw.rect(screen, RED, item) 
    pygame.draw.rect(screen, GREEN, food_pos)
    pygame.time.wait(80)    
    pygame.display.update()
    screen.fill(GRAY)
    
