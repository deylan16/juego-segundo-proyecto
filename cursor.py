import pygame
from pygame.locals import *
#################################################3
#cursor
#clase boton_rooks
#artibutos:
#         pygame.Rect.__init__:crea un pequeño cuadro
#metodos:
#        sigue: hace que el cuadro siga el mouseo
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def sigue(self):
        self.left,self.top = pygame.mouse.get_pos()
#define el cursor
cursor1 = Cursor()
