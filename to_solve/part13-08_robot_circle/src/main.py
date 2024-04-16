# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    

    window.fill((0, 0, 0))
    #window.blit(robot, (x, y))
    pygame.display.flip()
    
    for i in range(10):
        x = 50+math.cos(angle)*100-robot.get_width()/2
        y = 100+math.sin(angle)*100-robot.get_height()/2
        window.blit(robot, (x,y))

    angle += 0.01
    clock.tick(60)