import pygame
from pygame.locals import *
import sys
from time import *
from threading import Thread
from rooks import *
from cursor import *
from cuadros import *
from proyecto import *


#imagenes de los proyectiles
agua = pygame.image.load("bala.png")
#proyectiles
c = [cuadro_0_0,cuadro_0_1,cuadro_0_2,cuadro_0_3,cuadro_0_4,cuadro_1_0,cuadro_1_1,cuadro_1_2,cuadro_1_3,cuadro_1_4,cuadro_2_0,cuadro_2_1,cuadro_2_2,
                        cuadro_2_3,cuadro_2_4,cuadro_3_0,cuadro_3_1,cuadro_3_2,cuadro_3_3,cuadro_3_4,cuadro_4_0,cuadro_4_1,cuadro_4_2,cuadro_4_3,cuadro_4_4,cuadro_5_0,
                        cuadro_5_1,cuadro_5_2,cuadro_5_3,cuadro_5_4,cuadro_6_0,cuadro_6_1,cuadro_6_2,cuadro_6_3,cuadro_6_4,cuadro_7_0,cuadro_7_1,cuadro_7_2,cuadro_7_3,
                        cuadro_7_4,cuadro_8_0,cuadro_8_1,cuadro_8_2,cuadro_8_3,cuadro_8_4]

y = c[0].coordsy_get()
x = c[0].coordsx_get()

def lanza(estado,x,y):
    if estado.estado_get() == cuadro_o_con_water_rooks:
        ventana.blit(agua,(x,y))
        sleep(1)
        return lanza(estado,x,y)
    else:
        return 0
