import pygame
from sys import exit
from pygame.math import Vector2
import random
import time

#OBIECTE

class Fruits:
    def __init__(self):

        self.x=random.randint(0,patrate_numar-1)
        self.y=random.randint(0,patrate_numar-1)
        self.pos=Vector2(self.x,self.y)

    def afisare_fruct(self):

        fruit_rect=pygame.Rect((int(self.pos.x*patrate_dimensiune),int(self.pos.y*patrate_dimensiune), patrate_dimensiune, patrate_dimensiune ))
        screen.blit(mar,fruit_rect)
        #pygame.draw.rect(screen, 'red', fruit_rect)

    def fruit_spawn(self):
        self.x = random.randint(0, patrate_numar - 1)
        self.y = random.randint(0, patrate_numar - 1)
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        self.body=[Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1, 0)
        self.grow = False

    def miscare(self):
        nou_cap = self.body[0] + self.direction
        self.body.insert(0, nou_cap)
        #self.body.pop()
        if self.grow:
            self.grow = False
        else:
            self.body.pop()


    def afisare_sarpe(self):
        for block in self.body:
            x_sarpe = int(block.x * patrate_dimensiune)
            y_sarpe = int(block.y * patrate_dimensiune)
            sarpe_rect = pygame.Rect((x_sarpe, y_sarpe, patrate_dimensiune, patrate_dimensiune))
            pygame.draw.rect(screen, 'blue', sarpe_rect)

    def add(self):
        self.grow = True

#MODUL DE FUNTIONARE SI LOGICA JOCULUI

class Game:
    def __init__(self):
        self.fruit = Fruits()
        self.sarpe = Snake()
        self.score = 0
    def update(self):
        self.sarpe.miscare()
        self.collision()
        self.lose()

    def draw_elements(self):
        self.fruit.afisare_fruct()
        self.sarpe.afisare_sarpe()
        self.show_score()
    def collision(self):
        if self.fruit.pos == self.sarpe.body[0]:
            self.fruit.fruit_spawn()
            self.sarpe.add()
            self.score+=10

    def lose(self):
        if not 0 <= self.sarpe.body[0].x < patrate_numar:
            self.game_over()

        if not 0 <= self.sarpe.body[0].y < patrate_numar:
            self.game_over()

        for block in self.sarpe.body[1:]:
            if block == self.sarpe.body[0]:
                self.game_over()



    def game_over(self):
        screen.fill((0,0,0))
        game_over_surface = font.render(f'Game over!Your Score is :  {self.score}' , True, 'red')
        game_over_rect = game_over_surface.get_rect(center=(patrate_dimensiune * patrate_numar // 2, patrate_dimensiune * patrate_numar // 2))
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(4)
        pygame.quit()
        exit()



    def show_score(self):
        score_surface = font.render(f'Score : {self.score}', True, 'white')
        score_rect = score_surface.get_rect(topleft=(10,10))
        screen.blit(score_surface, score_rect)

#Initializari de baza+ chestii grafice si de estetica

pygame.init()
patrate_dimensiune = 40
patrate_numar = 20
screen = pygame.display.set_mode((patrate_dimensiune*patrate_numar, patrate_dimensiune*patrate_numar))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

#background = pygame.image.load('C:/Users/alexc/Desktop/facultate/PROIECTE PERSONALE/Snake/Graphics/iarba.jpg')
mar = pygame.image.load('C:/Users/alexc/Desktop/facultate/PROIECTE PERSONALE/Snake/Graphics/mar.png').convert_alpha()
mar = pygame.transform.scale(mar, (patrate_dimensiune, patrate_dimensiune))
font = pygame.font.SysFont('times new roman', 50)
main_game=Game()

MOVEMENT_EVENT = pygame.USEREVENT
pygame.time.set_timer(MOVEMENT_EVENT, 130)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MOVEMENT_EVENT:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.sarpe.direction != Vector2(0, 1):
                main_game.sarpe.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.sarpe.direction != Vector2(0, -1):
                main_game.sarpe.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.sarpe.direction != Vector2(1, 0):
                main_game.sarpe.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and main_game.sarpe.direction != Vector2(-1, 0):
                main_game.sarpe.direction = Vector2(1, 0)


    screen.fill((155, 235, 52))
    main_game.draw_elements()
    pygame.display.update()
    pygame.display.flip()
    fps.tick(120)



