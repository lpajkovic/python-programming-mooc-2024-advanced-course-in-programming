# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_1 = pygame.image.load("robot.png")


x_1 = 0
y_1 = 480-robot_1.get_height()

to_right_1 = False
to_left_1 = False
to_up_1 = False
to_down_1 = False

robot_2 = pygame.image.load("robot.png")

x_2=150
y_2=200

to_right_2 = False
to_left_2 = False
to_up_2 = False
to_down_2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left_1 = True
            if event.key == pygame.K_RIGHT:
                to_right_1 = True
            if event.key == pygame.K_UP:
                to_up_1 = True
            if event.key == pygame.K_DOWN:
                to_down_1 = True
            
            if event.key == pygame.K_a:
                to_left_2 = True
            if event.key == pygame.K_d:
                to_right_2 = True
            if event.key == pygame.K_w:
                to_up_2 = True
            if event.key == pygame.K_s:
                to_down_2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left_1 = False
            if event.key == pygame.K_RIGHT:
                to_right_1 = False
            if event.key == pygame.K_UP:
                to_up_1 = False
            if event.key == pygame.K_DOWN:
                to_down_1 = False
                
            if event.key == pygame.K_a:
                to_left_2 = False
            if event.key == pygame.K_d:
                to_right_2 = False
            if event.key == pygame.K_w:
                to_up_2 = False
            if event.key == pygame.K_s:
                to_down_2 = False

        if event.type == pygame.QUIT:
            exit()

    if to_right_1 and x_1+robot_1.get_width()<640:
        x_1 += 2
    if to_left_1 and x_1>0:
        x_1 -= 2
    if to_up_1 and y_1>0:
        y_1-=2
    if to_down_1 and y_1+robot_1.get_height()<480:
        y_1+=2
        
    if to_right_2 and x_2+robot_2.get_width()<640:
        x_2 += 2
    if to_left_2 and x_2>0:
        x_2 -= 2
    if to_up_2 and y_2>0:
        y_2-=2
    if to_down_2 and y_2+robot_1.get_height()<480:
        y_2+=2

    window.fill((0, 0, 0))
    window.blit(robot_1, (x_1, y_1))
    window.blit(robot_1, (x_2, y_2))
    pygame.display.flip()

    clock.tick(60)