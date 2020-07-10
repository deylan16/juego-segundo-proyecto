import pygame
from pygame.locals import *
from time import *


#botones de los cuadros
class Boton_cuadros(pygame.sprite.Sprite):
    def __init__(self,imagen1,x,y):
        self.imagen_actual = imagen1
        self.x = x
        self.y = y
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
        self.lista_disparo =[]
    def cambio(self,imagen):
        self.imagen_actual = imagen
    def estado_get(self):
        return self.imagen_actual
    def coordsx_get(self):
        return self.x
    def coordsy_get(self):
        return self.y
    def disparos(self,x,y,img):
        if self.imagen_actual  == cuadro_o_con_water_rooks:
                bala = proyectil(x,y,img)
                self.lista_disparo.append(bala)
        
    def seleccion(self,pantalla,cursor):
        pantalla.blit(self.imagen_actual,self.rect)
        
        
#imagenes de los cuadros
cuadro_oscuro = pygame.image.load("cuadro oscuro.png")
cuadro_o_con_fire_rooks = pygame.image.load("cuadro o con fire rooks.png")
cuadro_o_con_rock_rooks = pygame.image.load("cuadro o con rock rooks.png")
cuadro_o_con_sand_rooks = pygame.image.load("cuadro o con sand rooks.png")
cuadro_o_con_water_rooks = pygame.image.load("cuadro o con water rooks.png")
#establece si hay algo seleccionado
escogido = cuadro_oscuro
#matriz madre
mesa = [[cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro],
        [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]]
#botones de los cuadro
#fila0
cuadro_0_0= Boton_cuadros(mesa[0][0] ,31,101)
cuadro_0_1= Boton_cuadros(mesa[0][1] ,66,101)
cuadro_0_2= Boton_cuadros(mesa[0][2] ,101,101)
cuadro_0_3= Boton_cuadros(mesa[0][3] ,138,101)
cuadro_0_4= Boton_cuadros(mesa[0][4] ,173,101)
#fila1
cuadro_1_0= Boton_cuadros(mesa[1][0] ,31,136)
cuadro_1_1= Boton_cuadros(mesa[1][1] ,66,136)
cuadro_1_2= Boton_cuadros(mesa[1][2] ,101,136)
cuadro_1_3= Boton_cuadros(mesa[1][3] ,138,136)
cuadro_1_4= Boton_cuadros(mesa[1][4] ,173,136)
#fila2
cuadro_2_0= Boton_cuadros(mesa[2][0] ,31,171)
cuadro_2_1= Boton_cuadros(mesa[2][1] ,66,171)
cuadro_2_2= Boton_cuadros(mesa[2][2] ,101,171)
cuadro_2_3= Boton_cuadros(mesa[2][3] ,138,171)
cuadro_2_4= Boton_cuadros(mesa[2][4] ,173,171)
#fila3
cuadro_3_0= Boton_cuadros(mesa[3][0] ,31,206)
cuadro_3_1= Boton_cuadros(mesa[3][1] ,66,206)
cuadro_3_2= Boton_cuadros(mesa[3][2] ,101,206)
cuadro_3_3= Boton_cuadros(mesa[3][3] ,138,206)
cuadro_3_4= Boton_cuadros(mesa[3][4] ,173,206)
#fila4
cuadro_4_0= Boton_cuadros(mesa[4][0] ,31,241)
cuadro_4_1= Boton_cuadros(mesa[4][1] ,66,241)
cuadro_4_2= Boton_cuadros(mesa[4][2] ,101,241)
cuadro_4_3= Boton_cuadros(mesa[4][3] ,138,241)
cuadro_4_4= Boton_cuadros(mesa[4][4] ,173,241)
#fila5
cuadro_5_0= Boton_cuadros(mesa[5][0] ,31,276)
cuadro_5_1= Boton_cuadros(mesa[5][1] ,66,276)
cuadro_5_2= Boton_cuadros(mesa[5][2] ,101,276)
cuadro_5_3= Boton_cuadros(mesa[5][3] ,138,276)
cuadro_5_4= Boton_cuadros(mesa[5][4] ,173,276)
#fila6
cuadro_6_0= Boton_cuadros(mesa[6][0] ,31,311)
cuadro_6_1= Boton_cuadros(mesa[6][1] ,66,311)
cuadro_6_2= Boton_cuadros(mesa[6][2] ,101,311)
cuadro_6_3= Boton_cuadros(mesa[6][3] ,138,311)
cuadro_6_4= Boton_cuadros(mesa[6][4] ,173,311)
#fila7
cuadro_7_0= Boton_cuadros(mesa[7][0] ,31,346)
cuadro_7_1= Boton_cuadros(mesa[7][1] ,66,346)
cuadro_7_2= Boton_cuadros(mesa[7][2] ,101,346)
cuadro_7_3= Boton_cuadros(mesa[7][3] ,138,346)
cuadro_7_4= Boton_cuadros(mesa[7][4] ,173,346)
#fila8
cuadro_8_0= Boton_cuadros(mesa[2][0] ,31,384)
cuadro_8_1= Boton_cuadros(mesa[8][1] ,66,384)
cuadro_8_2= Boton_cuadros(mesa[8][2] ,101,384)
cuadro_8_3= Boton_cuadros(mesa[8][3] ,138,384)
cuadro_8_4= Boton_cuadros(mesa[8][4] ,173,384)



################################################3
c = [cuadro_0_0,cuadro_0_1,cuadro_0_2,cuadro_0_3,cuadro_0_4,cuadro_1_0,cuadro_1_1,cuadro_1_2,cuadro_1_3,cuadro_1_4,cuadro_2_0,cuadro_2_1,cuadro_2_2,
    cuadro_2_3,cuadro_2_4,cuadro_3_0,cuadro_3_1,cuadro_3_2,cuadro_3_3,cuadro_3_4,cuadro_4_0,cuadro_4_1,cuadro_4_2,cuadro_4_3,cuadro_4_4,cuadro_5_0,
    cuadro_5_1,cuadro_5_2,cuadro_5_3,cuadro_5_4,cuadro_6_0,cuadro_6_1,cuadro_6_2,cuadro_6_3,cuadro_6_4,cuadro_7_0,cuadro_7_1,cuadro_7_2,cuadro_7_3,
    cuadro_7_4,cuadro_8_0,cuadro_8_1,cuadro_8_2,cuadro_8_3,cuadro_8_4]


#imagenes de los proyectiles
bola_de_agua = pygame.image.load("bala.png")








class proyectil(pygame.sprite.Sprite):
    def __init__(self,x,y,imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.velocidad = -1
        self.rect.top = y
        self.rect.left = x

    def direccion(self):
        self.rect.top = self.rect.top - self.velocidad
    def disparo(self,ventana):
        ventana.blit(self.imagen,self.rect)
         
