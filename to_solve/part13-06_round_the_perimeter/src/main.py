# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity_x = 1
velocity_y = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if velocity_x>0:
        x += velocity_x
    if velocity_y>0:
        y += velocity_y
    
    if x+robot.get_width()>=640 and y+robot.get_height()>=480:
        velocity_x=-velocity_x
    
    if y<=0:
        velocity_y=-velocity_y
    
    if velocity_x > 0 and x+robot.get_width() >= 640:
        velocity_y = -velocity_y
    if velocity < 0 and x <= 0:
        velocity_x = -velocity_x

    clock.tick(60)