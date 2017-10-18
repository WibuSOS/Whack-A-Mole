import pygame,sys
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import *
from pygame.font import *


class Mole(Sprite):
    def __init__(self,imagefile = "mole.gif"):
        Sprite.__init__(self)
        self.image = image.load(imagefile)
        x,y = self.image.get_size()
        self.image = transform.scale(self.image,(int(x/3),int(y/3)))
        self.rect = self.image.get_rect()
        self.rect.center = [440,358]

    def flee(self):
        poslist = {"pos1": [196,358],"pos2": [316,358],"pos3": [440,358],"pos4": [196,426],"pos5": [316,426],"pos6": [440,426]}
        namelist = ["pos1","pos2","pos3","pos4","pos5","pos6"]
        self.rect.center = poslist[namelist[randint(0,5)]]


class Hole(Sprite):
    def __init__(self,*position):
        Sprite.__init__(self)
        self.image = image.load("hole.png")
        self.image = transform.scale(self.image,(160,170))
        self.rect = self.image.get_rect()
        self.rect.center = position

class Background(Sprite):
    def __init__(self,imagefile):
        Sprite.__init__(self)
        self.image = image.load(imagefile)
        self.image = transform.scale(self.image,(640,480))
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = [0,0]

class Score(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = SysFont(None,26)
        self.score = 0
        self.image = self.font.render("Score: %s" % self.score,True,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [320,40]

    def renew(self):
        self.image = self.font.render("Score: %s" % self.score,True,(0,0,0))

    def reset(self):
        self.score = 0
        self.image = self.font.render("Score: %s" % self.score,True,(0,0,0))

class Start(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("start.gif")
        self.image = transform.scale(self.image,(300,128))
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = [320,140]

class Out(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("exit.gif")
        self.image = transform.scale(self.image,(300,128))
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = [320,340]

#loop for whack mole
def game():
    running = True
    while running:
        screen.blit(background.image,background.rect)
        all_sprites.draw(screen)
        name = event.wait()
        if name.type == QUIT:
            running = False
            pygame.quit()
        elif name.type == KEYDOWN:
            if name.key == K_ESCAPE:
                score_mole.reset()
                running = False
        elif name.type == MOUSEBUTTONDOWN:
            if name.button == 1:
                if my_mole.rect.collidepoint(mouse.get_pos()):
                    score_mole.score += 1
                    score_mole.renew()
                    my_mole.flee()
        display.update()

#main
pygame.init()
display.set_caption("Whack-A-Mole")
screen = display.set_mode((640,480))
    #mole
my_mole = Mole()
score_mole = Score()
hole1 = Hole([196,358])
hole2 = Hole([316,358])
hole3 = Hole([440,358])
hole4 = Hole([196,426])
hole5 = Hole([316,426])
hole6 = Hole([440,426])
    #menu
start = Start()
out = Out()
    #game background and grouping
background = Background("farm.jpg")
menu_sprites = Group(start,out)
all_sprites = Group(hole1,hole2,hole3,hole4,hole5,hole6,my_mole,score_mole)

#loop for main menu
running = True
while running:
    screen.fill((255,255,255))
    menu_sprites.draw(screen)
    command = event.wait()
    if command.type == QUIT:
        running = False
    elif command.type == MOUSEBUTTONDOWN:
        if start.rect.collidepoint(mouse.get_pos()):
            game()
        elif out.rect.collidepoint(mouse.get_pos()):
            running = False
    elif command.type == KEYDOWN:
        if command.key == K_ESCAPE:
            running = False
    display.update()
