# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

rock=pygame.image.load("rock.png")
r_x=0
r_y=0

to_right = False
to_left = False


game_points=0
game_font = pygame.font.SysFont("Arial", 24)


while True:
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
        
        if event.type == pygame.QUIT:
            exit()
            
    if to_right and x+robot.get_width()<640:
        x += 2
    if to_left and x>0:
        x -= 2
        
    r_x=randint(0, 640-rock.get_width())
    r_y+=1
        
    display.fill((0, 0, 0))
    display.blit(robot, (x, y))
    text = game_font.render("Points: %s" % game_points, True, (255, 0, 0))
    display.blit(text, (500, 10))
    pygame.display.flip()