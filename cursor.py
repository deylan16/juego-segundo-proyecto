import pygame
from pygame.locals import *
#################################################3
#cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def sigue(self):
        self.left,self.top = pygame.mouse.get_pos()
#define el cursor
cursor1 = Cursor()
