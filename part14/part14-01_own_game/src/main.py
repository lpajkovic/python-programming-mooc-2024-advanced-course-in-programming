# My goal was to make a pong-like game using the .png assets provided by TMC
# Since there's no ball.png which was used in an exercise in part 13, i decided to use monster.png as ball,
# so it looks like robots are playing with a monster, I guess
#
# Instructions:
#   - left player moves up and down with W and S keys, right player moves with Up and Down arrow
#   - when monster passes over the coin, the value of points awarded for scoring increases by 1
# 
# Bugs:
#   - collision between robots and monster tends to get glitchy when monster is behind robots
#   - there's lag while changing direction of robot's movement (for example if both W and S keys are pressed at the same time)
#
# Things I'd like to add:
#   - time under score
#   - introduction screen
#   - two doors (using door.png) to serve as teleportation for monster
#   - monster bounce relative to part of robot's body which it hit
#   - clean up code a little bit





import pygame
from random import randint #used for randomly generating each coin's coordinates

class RobotPlayer:
    
    def __init__(self, x_pos:int, y_pos:int):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.move_speed=3
        self.points=0

        
        self.robot=pygame.image.load("robot.png")

        self.width=self.robot.get_width()
        self.height=self.robot.get_height()
        
        #collision box uses pygame.Rect.colliderect function
        self.robot_collision_box=self.robot.get_rect(topleft=(self.x_pos,self.y_pos))        
        
    def ret_collision_box(self):
        return self.robot_collision_box
        
    def display(self, main_window):
        main_window.blit(self.robot, (self.x_pos,self.y_pos))
        
    def move(self, y_mov:int):
        
        new_y=self.y_pos+(y_mov*self.move_speed)
        
        if new_y<=0:
            return
        elif new_y + self.height>600:
            return
        else:
            self.y_pos=new_y
            
            #updating the collision box
            self.robot_collision_box=self.robot.get_rect(topleft=(self.x_pos, self.y_pos))
        

class Monster:
    
    #I'm using the monster.png image as a ball    
    def __init__(self, x_pos:int, y_pos:int):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.x_move_speed=5
        self.y_move_speed=5
        
        self.monster=pygame.image.load("monster.png")
        
        self.width=self.monster.get_width()
        self.height=self.monster.get_height() 
        
        #collision box for pygame.Rect.colliderect function    
        self.monster_collision_box=self.monster.get_rect(topleft=(self.x_pos, self.y_pos))   
     
    def ret_collision_box(self):
        return self.monster_collision_box 
        
    def display(self, main_window):
        main_window.blit(self.monster, (self.x_pos, self.y_pos))
        
    def reset(self):
        
        #I've used fixed coordinates for resetting so that game could be harder to play
        self.x_pos=360
        self.y_pos=260
        self.x_move_speed*=-1
        self.monster_collision_box=self.monster.get_rect(topleft=(self.x_pos, self.y_pos))
        
    def bounce(self):
        self.x_move_speed*=-1
            
    def move(self):
        new_x=self.x_pos+(1*self.x_move_speed)
        new_y=self.y_pos+(1*self.y_move_speed)
            
            
        #if the monster is out of the screen, points are awarded
        #1 - point for player 2 (right-side player)
        #-1 - point for player 1 (left-side player)
        #0 - round is still active
        if new_x<=-60:
            self.reset()
            return 1
        elif new_x+self.width>860:
            self.reset()
            return -1
        elif new_y<=0 or new_y+self.height>600:
            self.y_move_speed*=-1
        else:
            self.x_pos=new_x
            self.y_pos=new_y
            self.monster_collision_box=self.monster.get_rect(topleft=(self.x_pos, self.y_pos))
            
        return 0


class Coin:
    
    def __init__(self):
        self.x_pos=randint(100, 700)
        self.y_pos=randint(50, 550)
        
        self.coin=pygame.image.load("coin.png")
        
        self.coin_collision_box=self.coin.get_rect(topleft=(self.x_pos, self.y_pos))


    def display(self, main_window):
        main_window.blit(self.coin, (self.x_pos, self.y_pos))
    
    #helper method to remove coin from screen for when monster ("ball" so to speak) passes over the coin
    def remove(self, main_window):
        main_window.blit(self.coin, (-999, -999))
        
    def new_pos(self, x_pos:int, y_pos:int):
        self.x_pos=x_pos
        self.y_pos=y_pos
        
    def ret_collision_box(self):
        return self.coin_collision_box
                
class Scoreboard:
    
    def __init__(self):
        self.x_pos=370
        self.y_pos=20
        self.p1_pts=0
        self.p2_pts=0
        
    def score(self, main_window):
        game_font=pygame.font.SysFont("Arial", 32)
        text=game_font.render(f"{self.p1_pts} : {self.p2_pts}", True, (0,0,0))
        main_window.blit(text, (self.x_pos, self.y_pos))
        
        
    def score_update(self, p1_pts:int, p2_pts:int):
        self.p1_pts=p1_pts
        self.p2_pts=p2_pts
            

class MonsterPong:
    
    def __init__(self):
        pygame.init()
        
        
        self.height=600
        self.width=800

        self.window=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Monster Pong")
        
        self.robot1=RobotPlayer(40, 300)
        self.robot2=RobotPlayer(710, 300)
        self.monster=Monster(360, 260)
        self.coin=Coin()
        self.scoreboard=Scoreboard()
        
        #helper variables for player movement input
        self.p1_move=0
        self.p2_move=0
        
        #for some reason I couldn't log the first goal scored
        #so I made this little bool variable to keep track of the first goal so that Scoreboard object
        #can properly increment the score
        self.first_goal=True
        self.points_to_add=1
        
        self.clock=pygame.time.Clock()
        
        self.main_loop()
        
    #This was supposed to be introduction screen, but for some reason I couldn't get it to sync properly with the rest of the game
    
    #def intro_screen(self, main_window):
    #    title_font=pygame.font.SysFont("Arial", 50)
    #    text=title_font.render(f"Monster Pong", True, (0,0,0))
    #    main_window.blit(text, (300, 250))
    #    
    #    description_font=pygame.font.SysFont("Arial", 12)
    #    text=description_font.render(
    #        "Player 1 (left): W - up, S - down\n"
    #        "Player 2 (right): Up arrow - up, Down arrow - down\n"
    #        "Monster passing over the coin increments the value of points awarded for scoring\n"
    #        "Press P to play", True, (0,0,0), 540)
    #    main_window.blit(text, (360, 250))
    #    
    #    while True:
    #        for event in pygame.event.get():
    #            if event.type==pygame.KEYDOWN:
    #                if event.key==pygame.K_p:
    #                    return
    #                if event.key==pygame.QUIT:
    #                    quit()
        
        
    def main_loop(self):
        
        while True:
            self.window.fill((139, 238, 226))
            self.scoreboard.score(self.window)
            #self.intro_screen(self.window)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                 
                if event.type==pygame.KEYDOWN:   
                    if event.key==pygame.K_UP:
                        self.p2_move=-1
                    if event.key==pygame.K_DOWN:
                        self.p2_move=1
                    if event.key==pygame.K_w:
                        self.p1_move=-1
                    if event.key==pygame.K_s:
                        self.p1_move=1
                
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                        self.p2_move=0
                    if event.key==pygame.K_w or event.key==pygame.K_s:
                        self.p1_move=0
            
            #collision detection for robots and monster 
            if pygame.Rect.colliderect(self.monster.ret_collision_box(), self.robot1.ret_collision_box()):
                self.monster.bounce()
            elif pygame.Rect.colliderect(self.monster.ret_collision_box(), self.robot2.ret_collision_box()):
                self.monster.bounce()
            
            #collision detection for monster and coins
            #upon collision, coin is removed from screen, points available to score increment by 1 and a new Coin object is created   
            if pygame.Rect.colliderect(self.monster.ret_collision_box(), self.coin.ret_collision_box()):
                self.coin.remove(self.window)
                self.points_to_add+=1
                self.coin=Coin()
            
            self.robot1.move(self.p1_move)
            self.robot2.move(self.p2_move)
            
            point=self.monster.move()
            
            
            if point==-1:
                #hack to deal with the first goal not being tracked
                if self.first_goal is True:
                    self.robot1.points+=self.points_to_add
                    self.first_goal=False
                    self.robot1.points-=self.points_to_add
                    
                self.robot1.points+=self.points_to_add
                self.points_to_add=1 #when a player concedes a goal, for next iteration of play starting value of points to get is 1
                self.monster.reset()
                self.scoreboard.score_update(self.robot1.points, self.robot2.points)
            elif point==1:
                #hack to deal with the first goal not being tracked
                if self.first_goal is True:
                    self.robot2.points+=self.points_to_add
                    self.first_goal=False
                    self.robot2.points-=self.points_to_add
                    
                self.robot2.points+=self.points_to_add
                self.points_to_add=1
                self.monster.reset()
                self.scoreboard.score_update(self.robot1.points, self.robot2.points)
               
                    
            self.robot1.display(self.window)
            self.robot2.display(self.window)
            self.monster.display(self.window)
            self.coin.display(self.window)
            
                    
            pygame.display.flip()
            self.clock.tick(60)

 
if __name__=="__main__":
    MonsterPong()