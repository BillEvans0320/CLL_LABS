# Snake Game

import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)

screen_width = 600
screen_height = 600

pygame.init()
pygame.display.set_caption("Snake Game")

screen = pygame.display.set_mode((screen_width,screen_height))


pos_x = screen_width//2
pos_y = screen_height//2

start = False

while not start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = True

    # Keep moving

    key_event = pygame.key.get_pressed()
    print(type(key_event))
    if key_event[pygame.K_LEFT]:
        pos_x -= 1
    if key_event[pygame.K_RIGHT]:
        pos_x += 1
    if key_event[pygame.K_UP]:
        pos_y -= 1
    if key_event[pygame.K_DOWN]:
        pos_y += 1

    screen.fill(black)
    pygame.draw.rect(screen, white, (pos_x, pos_y, 20, 20))  #(x, y, weight, height)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()