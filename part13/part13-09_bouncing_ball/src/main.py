# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x=0
y=0
vel_x=1
vel_y=1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    
    if (vel_x>0 and x+ball.get_width()>=640) or (vel_x<0 and x<=0):
        vel_x=-vel_x
    if (vel_y>0 and y+ball.get_height()>=480) or (vel_y<0 and y<=0):
        vel_y=-vel_y
    
    x+=(3*vel_x)
    y+=(3*vel_y)
    
    pygame.display.flip()
    
    
    clock.tick(60)