import pygame


#setting different array's with values to test the GUI
pos1 = [x*2 for x in range(10)]
pos2 = [x*3 for x in range(10)]
pos3 = [x*4 for x in range(10)]
pos4 = [x*5 for x in range(10)]

print pos1
print pos2
print pos3
print pos4

#globally sets the window and ball size and number of balls
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 5
NUMBER = 100


#globally sets the colors to be used inside of the pygame window
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)



class Pointer(object):

    def __init__(self, x=0, y=0, dx=0, dy=0):
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

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True











    #makes the screen white, and draws the background picture,
    #then the picture of the pointer ontop of the background pic
    screen.fill(WHITE)

    screen.blit(bg, [0,0])

    clock.tick(60)
    pygame.display.flip()   

pygame.quit()

    



            
