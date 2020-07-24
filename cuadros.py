import pygame
from pygame.locals import *
from time import *
from threading import Thread


#botones de los cuadros
class Boton_cuadros(pygame.sprite.Sprite):
    def __init__(self,imagen1,x,y):
        self.imagen_actual = imagen1
        self.x = x
        self.y = y
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
        
    def estado_get(self):
        return self.imagen_actual
    def coordsx_get(self):
        return self.x
    def coordsy_get(self):
        return self.y
  
    def seleccion(self,pantalla,cursor):
        pantalla.blit(self.imagen_actual,self.rect)
        
        
#imagenes de los cuadros
cuadro_oscuro = pygame.image.load("cuadro oscuro.png")
cuadro_o_con_fire_rooks = pygame.image.load("cuadro o con fire rooks.png")
cuadro_o_con_rock_rooks = pygame.image.load("cuadro o con rock rooks.png")
cuadro_o_con_sand_rooks = pygame.image.load("cuadro o con sand rooks.png")
cuadro_o_con_water_rooks = pygame.image.load("cuadro o con water rooks.png")

def establece(guardado):
    if guardado == 'ninguno':
        return [[cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]]
    else:
        return  [[cuadro_oscuro,cuadro_o_con_fire_rooks,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]]

#matriz madre
mesa = establece('ninguno')


#botones de los cuadro
#fila0
cuadro_0_0= Boton_cuadros(cuadro_oscuro ,31,101)
cuadro_0_1= Boton_cuadros(cuadro_oscuro ,66,101)
cuadro_0_2= Boton_cuadros(cuadro_oscuro ,101,101)
cuadro_0_3= Boton_cuadros(cuadro_oscuro ,138,101)
cuadro_0_4= Boton_cuadros(cuadro_oscuro ,173,101)
#fila1
cuadro_1_0= Boton_cuadros(cuadro_oscuro ,31,136)
cuadro_1_1= Boton_cuadros(cuadro_oscuro ,66,136)
cuadro_1_2= Boton_cuadros(cuadro_oscuro ,101,136)
cuadro_1_3= Boton_cuadros(cuadro_oscuro ,138,136)
cuadro_1_4= Boton_cuadros(cuadro_oscuro ,173,136)
#fila2
cuadro_2_0= Boton_cuadros(cuadro_oscuro ,31,171)
cuadro_2_1= Boton_cuadros(cuadro_oscuro ,66,171)
cuadro_2_2= Boton_cuadros(cuadro_oscuro ,101,171)
cuadro_2_3= Boton_cuadros(cuadro_oscuro ,138,171)
cuadro_2_4= Boton_cuadros(cuadro_oscuro ,173,171)
#fila3
cuadro_3_0= Boton_cuadros(cuadro_oscuro ,31,206)
cuadro_3_1= Boton_cuadros(cuadro_oscuro ,66,206)
cuadro_3_2= Boton_cuadros(cuadro_oscuro ,101,206)
cuadro_3_3= Boton_cuadros(cuadro_oscuro ,138,206)
cuadro_3_4= Boton_cuadros(cuadro_oscuro ,173,206)
#fila4
cuadro_4_0= Boton_cuadros(cuadro_oscuro ,31,241)
cuadro_4_1= Boton_cuadros(cuadro_oscuro ,66,241)
cuadro_4_2= Boton_cuadros(cuadro_oscuro ,101,241)
cuadro_4_3= Boton_cuadros(cuadro_oscuro ,138,241)
cuadro_4_4= Boton_cuadros(cuadro_oscuro ,173,241)
#fila5
cuadro_5_0= Boton_cuadros(cuadro_oscuro ,31,276)
cuadro_5_1= Boton_cuadros(cuadro_oscuro ,66,276)
cuadro_5_2= Boton_cuadros(cuadro_oscuro ,101,276)
cuadro_5_3= Boton_cuadros(cuadro_oscuro ,138,276)
cuadro_5_4= Boton_cuadros(cuadro_oscuro ,173,276)
#fila6
cuadro_6_0= Boton_cuadros(cuadro_oscuro ,31,311)
cuadro_6_1= Boton_cuadros(cuadro_oscuro ,66,311)
cuadro_6_2= Boton_cuadros(cuadro_oscuro ,101,311)
cuadro_6_3= Boton_cuadros(cuadro_oscuro ,138,311)
cuadro_6_4= Boton_cuadros(cuadro_oscuro ,173,311)
#fila7
cuadro_7_0= Boton_cuadros(cuadro_oscuro ,31,346)
cuadro_7_1= Boton_cuadros(cuadro_oscuro ,66,346)
cuadro_7_2= Boton_cuadros(cuadro_oscuro ,101,346)
cuadro_7_3= Boton_cuadros(cuadro_oscuro ,138,346)
cuadro_7_4= Boton_cuadros(cuadro_oscuro ,173,346)
#fila8
cuadro_8_0= Boton_cuadros(cuadro_oscuro ,31,381)
cuadro_8_1= Boton_cuadros(cuadro_oscuro ,66,381)
cuadro_8_2= Boton_cuadros(cuadro_oscuro ,101,381)
cuadro_8_3= Boton_cuadros(cuadro_oscuro ,138,381)
cuadro_8_4= Boton_cuadros(cuadro_oscuro ,173,381)



################################################3

def cambio_mesa(i,j,estado):
            mesa[i][j] = estado

volumenS = pygame.image.load('volumenS.png')
volumenN = pygame.image.load('volumenN.png')
volumen= Boton_cuadros(volumenS ,0,0)





