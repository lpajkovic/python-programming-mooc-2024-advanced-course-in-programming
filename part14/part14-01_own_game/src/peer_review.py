# Complete your game here
import pygame
import random
 
 
class Bullet:
    def __init__(self) -> None:
        # of course, the sizes of bullet should be smaller
        # but, unfortunately, i can't change this
        self.bullet = pygame.image.load('coin.png')
        self.x = 0
        self.y = 0
        self.velocity = 5
 
    def move(self) -> None:
        self.y -= self.velocity
 
 
class Player:
    def __init__(self) -> None:
        self.player = pygame.image.load('robot.png')
        self.x = 0
        self.y = 400 - self.player.get_height()
        self.velocity = 5
        self.bullets = list()
        self.counts_of_bullets = 5
        self.to_right = False
        self.to_left = False
 
    def move(self) -> None:
        if self.to_right:
            self.x += self.velocity
 
        if self.to_left:
            self.x -= self.velocity
 
    def init_bullets(self) -> None:
        for i in range(self.counts_of_bullets):
            self.bullets.append(Bullet())
 
    def fire(self) -> pygame.Surface:
        bullet = self.bullets.pop()
        bullet.x = self.x + 5
        bullet.y = self.y - self.player.get_height() / 2
        self.counts_of_bullets -= 1
 
        return bullet
 
    def is_out_of_bounce(self) -> None:
        if self.x <= 0:
            self.to_left = False
        if self.x + self.player.get_width() >= 640:
            self.to_right = False
 
    def reset(self) -> None:
        self.x = 0
        self.y = 400 - self.player.get_height()
        self.counts_of_bullets = 5
        self.init_bullets()
        self.to_right = False
        self.to_left = False
 
 
class Monster:
    def __init__(self) -> None:
        self.monster = pygame.image.load('monster.png')
        self.x = random.randint(0, 640 - self.monster.get_width())
        self.y = random.randint(-700, -100)
        self.velocity = 2
 
    def move(self) -> None:
        self.y += self.velocity
 
    def reset(self) -> None:
        self.x = random.randint(0, 640 - self.monster.get_width())
        self.y = random.randint(-1000, -300)
 
    def is_out_of_bounce(self) -> bool:
        return True if self.y + self.monster.get_height() / 2 >= 480 else False
 
 
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.bullet = None
        self.monsters = list()
        self.kills = 0
        self.font = pygame.font.SysFont('Arial', 24)
        self.need_help = False
 
    def play(self) -> None:
        self.player.init_bullets()
        self.init_monsters()
        while True:
            for event in pygame.event.get():
                self.event_handler(event)
 
            while self.need_help:
                self.drawing_help()
                for event in pygame.event.get():
                    self.event_handler(event)
 
            self.drawing()
            self.calculating()
 
            self.clock.tick(60)
 
    def init_monsters(self) -> None:
        for i in range(5):
            self.monsters.append(Monster())
 
    def is_hitting_monster(self) -> None:
        for monster in self.monsters:
            condition1 = round(self.bullet.x + self.bullet.bullet.get_width() / 2) in range(round(monster.x), round(monster.x + monster.monster.get_width()))
            condition2 = round(self.bullet.x - self.bullet.bullet.get_width() / 2) in range(round(monster.x), round(monster.x + monster.monster.get_width()))
            if condition1 or condition2:
                if round(self.bullet.y) in range(round(monster.y), round(monster.y + monster.monster.get_height())):
                    self.bullet = None
                    monster.reset()
                    self.player.bullets.append(Bullet())
                    self.player.counts_of_bullets += 1
                    self.kills += 1
                    return
 
    def is_losing(self) -> bool:
        return True if self.player.counts_of_bullets <= 0 else False
 
    def calculating(self) -> None:
        losing = False
 
        self.player.is_out_of_bounce()
        self.player.move()
 
        if self.bullet is not None:
            self.bullet.move()
            self.is_hitting_monster()
 
        for monster in self.monsters:
            losing = monster.is_out_of_bounce()
            monster.move()
            if losing:
                break
 
        if losing or self.is_losing():
            self.drawing_lose_screen()
            self.reset()
 
        if self.kills > 10:
            self.drawing_win_screen()
            self.reset()
 
    def reset(self) -> None:
        self.player.reset()
        for monster in self.monsters:
            monster.reset()
        self.kills = 0
 
    def event_handler(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            exit()
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_RIGHT:
                self.player.to_right = True
            if event.key == pygame.K_LEFT:
                self.player.to_left = True
            if event.key == pygame.K_LCTRL:
                self.bullet = self.player.fire()
            if event.key == pygame.K_F1:
                self.need_help = not self.need_help
                self.reset()
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.player.to_right = False
            if event.key == pygame.K_LEFT:
                self.player.to_left = False
 
    def drawing(self) -> None:
        self.display.fill((13, 13, 13))
 
        self.drawing_text()
 
        self.display.blit(self.player.player, (self.player.x, self.player.y))
 
        if self.bullet is not None:
            self.display.blit(self.bullet.bullet, (self.bullet.x, self.bullet.y))
 
        for monster in self.monsters:
            self.display.blit(monster.monster, (monster.x, monster.y))
 
        pygame.display.flip()
 
    def drawing_help(self) -> None:
        self.display.fill((13, 13, 13))
        helper1 = self.font.render('Press F1 to start game', True, (255, 0, 0))
        helper2 = self.font.render('Use arrows to move to left or to right', True, (255, 0, 0))
        helper3 = self.font.render('Use left CTRL to fire', True, (255, 0, 0))
        helper4 = self.font.render('You need to get at least 11 kills to win', True, (255, 0, 0))
 
        self.display.blit(helper1, (100, 100))
        self.display.blit(helper2, (100, 200))
        self.display.blit(helper3, (100, 300))
        self.display.blit(helper4, (100, 400))
 
        pygame.display.flip()
 
    def drawing_text(self) -> None:
        kills = self.font.render(f'Kills: {self.kills}', True, (255, 0, 0))
        bullets = self.font.render(f'Bullets: {self.player.counts_of_bullets}', True, (255, 0, 0))
        helper = self.font.render('F1 to help', True, (255, 0, 0))
 
        self.display.blit(kills, (100, 420))
        self.display.blit(bullets, (300, 420))
        self.display.blit(helper, (500, 420))
 
    def drawing_win_screen(self) -> None:
        text = self.font.render('You WIN!!! Congratulations!', True, (0, 255, 0))
        self.display.fill((0, 0, 0))
        self.display.blit(text, (320 - text.get_width() / 2, 240 - text.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(1500)
 
    def drawing_lose_screen(self) -> None:
        text = self.font.render('You LOSE!!! Try again!', True, (255, 0, 0))
        self.display.fill((0, 0, 0))
        self.display.blit(text, (320 - text.get_width() / 2, 240 - text.get_height() / 2))
        pygame.display.flip()
        pygame.time.delay(1500)
 
 
def main():
    my_game = Game()
    my_game.play()
 
 
main()