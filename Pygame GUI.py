import pygame
from time import sleep

#globally sets the window and ball size and number of balls
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
BALL_SIZE = 5
NUMBER = 100


#globally sets the colors to be used inside of the pygame window
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 255)
YELLOW = (255, 255, 0)

BUTTON = (165, 234, 45)


#sets starting coords for the lazer pointer
START_X = (SCREEN_WIDTH ) / 2
START_Y = (SCREEN_HEIGHT) / 2



class Pointer(object):

    def __init__(self, x= 0, y= 0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy




    #acessors and mutators
    @property
    def x (self):
        return self._x

    @x.setter
    def x (self, x):
        self._x = x

    @property
    def y (self):
        return self._y

    @y.setter
    def y (self, y):
        self._y = y

    @property
    def dx (self):
        return self._dx

    @dx.setter
    def dx (self, dx):
        self._dx = dx

    @property
    def dy (self):
        return self._dy

    @dy.setter
    def dy (self, dy):
        self._dy = dy


pygame.init()

#sets up screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Aim Trainer")
bg = pygame.image.load("TargetPractice.gif")

#sets the screen refresh rate time
clock = pygame.time.Clock()



pos = Pointer(START_X, START_Y)

i=0

#hard coded positions of the points on the target
point1 = Pointer(150,120)
point2 = Pointer(300,120)
point3 = Pointer(450,120)
point4 = Pointer(150,240)
point5 = Pointer(300,240)
point6 = Pointer(450,240)
point7 = Pointer(150,360)
point8 = Pointer(300,360)
##
points = [point1,point2,point3,point4,point5,point6,point7,point8]
##
##
##pos1 = [0, 0, 0, 50, 70, 0, 0, 0]


def testing(point):

    
    i = 0
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pos.x == point.x and pos.y == point.y:
            done = True

        if pos.x - point.x == 0:
            pos.dx = 0
        
        elif pos.x - point.x > 0:
            pos.dx = -1

            if pos.y - point.y == 0:
                pos.dy = 0
            
            elif pos.y - point.y > 0:
                pos.dy = -1

            elif pos.y - point.y < 0:
                pos.dy = 1
            

        elif pos.x - point.x < 0:
            pos.dx = 1

            if pos.y - point.y == 0:
                pos.dy = 0

            if pos.y - point.y > 0:
                pos.dy = -1

            elif pos.y - point.y < 0:
                pos.dy = 1

        pos.x += pos.dx
        pos.y += pos.dy

        


        screen.fill(WHITE)

        screen.blit(bg, [0,0])


        pygame.draw.circle(screen, RED, [pos.x,pos.y], 20)

        for yes in points:
            pygame.draw.circle(screen, YELLOW, [yes.x,yes.y], 5)

        











        #makes the screen white, and draws the background picture,
        #then the picture of the pointer ontop of the background pic
        

        #adding button?
        pygame.draw.rect(screen, BUTTON, [650,60,100,50])

        #normal stuff
        pygame.draw.circle(screen, RED, [45,203], 1)
        
        clock.tick(60)
        pygame.display.flip()

coords = []
for i in range(10):
    coords.append([i+100, i+250])

    
for x in coords:
    point9 = Pointer(x[0],x[1])
    testing(point9)

testing(point9)

pygame.quit()

    



            
