
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rob_width=robot.get_width()
rob_height=robot.get_height()

window.fill((0, 0, 0))

x=0
y=0
vel_x=0
vel_y=1
    

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
            
    window.blit(robot, (random.randint(0, 640), 0))
    pygame.display.flip()
    
    if vel_y>0 and y+rob_height>=480:
        
        if x<=320:
            vel_x=-1
        else:
            vel_x=1
    
    y+=(2*vel_y)
    x+=(2*vel_x)
    