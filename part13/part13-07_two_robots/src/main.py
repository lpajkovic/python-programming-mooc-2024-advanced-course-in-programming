# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_1 = pygame.image.load("robot.png")
robot_2 = pygame.image.load("robot.png")

x_1 = 0
y_1 = 0
x_2=0
y_2=150
velocity_1 = 1
velocity_2= 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot_1, (x_1, y_1))
    window.blit(robot_2, (x_2,y_2))
    pygame.display.flip()
    
    x_1 += velocity_1
    x_2 += (2*velocity_2)
    
    if velocity_1 > 0 and x_1+robot_1.get_width() >= 640:
        velocity_1 = -velocity_1
    if velocity_1 < 0 and x_1 <= 0:
        velocity_1 = -velocity_1
        
    if velocity_2 > 0 and x_2+robot_2.get_width() >= 640:
        velocity_2 = -velocity_2
    if velocity_2 < 0 and x_2 <= 0:
        velocity_2 = -velocity_2

    clock.tick(60)