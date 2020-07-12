import pygame
from pygame.locals import *
from cuadros import *
from cursor import *


################################################3
#botones de los rooks
class Boton_rooks(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = imagen1
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def cambio(self,imagen):
        self.imagen_normal = imagen
    def seleccion(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        if  not cursor.colliderect(self.rect) :
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)
#imagenes de los Rocks
fire_rooks = pygame.image.load("fire rooks.png")
fire_rooks2 = pygame.image.load("fire rooks2.png")
cancelar1 = pygame.image.load("cancelar1.png")
cancelar1_2 = pygame.image.load("cancelar1.2.png")
rock_rooks = pygame.image.load("rock rooks.png")
rock_rooks2 = pygame.image.load("rock rooks2.png")
sand_rooks = pygame.image.load("sand rooks.png")
sand_rooks2 = pygame.image.load("sand rooks2.png")
water_rooks = pygame.image.load("water rooks.png")
water_rooks2 = pygame.image.load("water rooks2.png")


##########################################3#######
#define el boton de la torre de fuego
boton_fire_rooks= Boton_rooks(fire_rooks,fire_rooks2,20,20)
#define el boton de la torre de roca
boton_rock_rooks= Boton_rooks(rock_rooks,rock_rooks2,80,20)
#define el boton de la torre de arena
boton_sand_rooks= Boton_rooks(sand_rooks,sand_rooks2,140,20)
#define el boton de la torre de agua
boton_water_rooks= Boton_rooks(water_rooks,water_rooks2,200,20)
#Define el boton cancelar
cancelar= Boton_rooks(cancelar1,cancelar1_2,20,80)


####################################
#clase para poner rooks de ataque
class rooks(pygame.sprite.Sprite):
    def __init__(self,imagen1,x,y):
        self.imagen_actual = imagen1
        self.rect = self.imagen_actual.get_rect()
        self.x = x
        self.y = y
        self.rect.left,self.rect.top = (x,y)
        self.lista_disparo =[]
    def cambio(self,x_d,y_d, imagen):
        self.x = x_d
        self.y = y_d
        self.imagen_actual = imagen
    def disparos(self):
        if self.imagen_actual  == cuadro_o_con_water_rooks:
                bala = proyectil(self.x,self.y,bola_de_agua)
                self.lista_disparo.append(bala)
        if self.imagen_actual  == cuadro_o_con_fire_rooks:
                bala = proyectil(self.x,self.y,bola_de_fuego)
                self.lista_disparo.append(bala)
        if self.imagen_actual  == cuadro_o_con_rock_rooks:
                bala = proyectil(self.x,self.y,bola_de_roca)
                self.lista_disparo.append(bala)
        if self.imagen_actual  == cuadro_o_con_sand_rooks:
                bala = proyectil(self.x,self.y,bola_de_arena)
                self.lista_disparo.append(bala) 
    def seleccion(self,pantalla,cursor):
        pantalla.blit(self.imagen_actual,(self.x,self.y))

##################################
#funciones y creacion del rook_0_0
rook_0_0= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_0_0():  
    hilo2 = Thread(target=imprimir_0_0, args=())
    hilo2.start()

def imprimir_0_0():
    if mesa[0][0] != cuadro_oscuro:
        rooks_puestos[0].disparos()
        sleep(1)
        imprimir_0_0()
#funciones y creacion del rook_0_1
rook_0_1= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_0_1():  
    hilo2 = Thread(target=imprimir_0_1, args=())
    hilo2.start()

def imprimir_0_1():
    if mesa[0][1] != cuadro_oscuro:
        rooks_puestos[1].disparos()
        sleep(1)
        imprimir_0_1()
#funciones y creacion del rook_0_2
rook_0_2= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_0_2():  
    hilo2 = Thread(target=imprimir_0_2, args=())
    hilo2.start()

def imprimir_0_2():
    if mesa[0][2] != cuadro_oscuro:
        rooks_puestos[2].disparos()
        sleep(1)
        imprimir_0_2()
#funciones y creacion del rook_0_3
rook_0_3= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_0_3():  
    hilo2 = Thread(target=imprimir_0_3, args=())
    hilo2.start()

def imprimir_0_3():
    if mesa[0][3] != cuadro_oscuro:
        rooks_puestos[3].disparos()
        sleep(1)
        imprimir_0_3()
#funciones y creacion del rook_0_4
rook_0_4= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_0_4():  
    hilo2 = Thread(target=imprimir_0_4, args=())
    hilo2.start()

def imprimir_0_4():
    if mesa[0][4] != cuadro_oscuro:
        rooks_puestos[4].disparos()
        sleep(1)
        imprimir_0_4()
################################################
#funciones y creacion del rook_1_0
rook_1_0= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_1_0():  
    hilo2 = Thread(target=imprimir_1_0, args=())
    hilo2.start()

def imprimir_1_0():
    if mesa[1][0] != cuadro_oscuro:
        rooks_puestos[5].disparos()
        sleep(1)
        imprimir_1_0()
#funciones y creacion del rook_1_1
rook_1_1= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_1_1():  
    hilo2 = Thread(target=imprimir_1_1, args=())
    hilo2.start()

def imprimir_1_1():
    if mesa[1][1] != cuadro_oscuro:
        rooks_puestos[6].disparos()
        sleep(1)
        imprimir_1_1()
#funciones y creacion del rook_1_2
rook_1_2= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_1_2():  
    hilo2 = Thread(target=imprimir_1_2, args=())
    hilo2.start()

def imprimir_1_2():
    if mesa[1][2] != cuadro_oscuro:
        rooks_puestos[7].disparos()
        sleep(1)
        imprimir_1_2()
#funciones y creacion del rook_1_3
rook_1_3= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_1_3():  
    hilo2 = Thread(target=imprimir_1_3, args=())
    hilo2.start()

def imprimir_1_3():
    if mesa[1][3] != cuadro_oscuro:
        rooks_puestos[8].disparos()
        sleep(1)
        imprimir_1_3()
#funciones y creacion del rook_1_4
rook_1_4= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_1_4():  
    hilo2 = Thread(target=imprimir_1_4, args=())
    hilo2.start()

def imprimir_1_4():
    if mesa[1][4] != cuadro_oscuro:
        rooks_puestos[9].disparos()
        sleep(1)
        imprimir_1_4()
##################################
#funciones y creacion del rook_2_0
rook_2_0= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_2_0():  
    hilo2 = Thread(target=imprimir_2_0, args=())
    hilo2.start()

def imprimir_2_0():
    if mesa[2][0] != cuadro_oscuro:
        rooks_puestos[10].disparos()
        sleep(1)
        imprimir_2_0()
#funciones y creacion del rook_2_1
rook_2_1= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_2_1():  
    hilo2 = Thread(target=imprimir_2_1, args=())
    hilo2.start()

def imprimir_2_1():
    if mesa[2][1] != cuadro_oscuro:
        rooks_puestos[11].disparos()
        sleep(1)
        imprimir_2_1()
#funciones y creacion del rook_2_2
rook_2_2= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_2_2():  
    hilo2 = Thread(target=imprimir_2_2, args=())
    hilo2.start()

def imprimir_2_2():
    if mesa[2][2] != cuadro_oscuro:
        rooks_puestos[12].disparos()
        sleep(1)
        imprimir_2_2()
#funciones y creacion del rook_2_3
rook_2_3= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_2_3():  
    hilo2 = Thread(target=imprimir_2_3, args=())
    hilo2.start()

def imprimir_2_3():
    if mesa[2][3] != cuadro_oscuro:
        rooks_puestos[13].disparos()
        sleep(1)
        imprimir_2_3()
#funciones y creacion del rook_2_4
rook_2_4= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_2_4():  
    hilo2 = Thread(target=imprimir_2_4, args=())
    hilo2.start()

def imprimir_2_4():
    if mesa[2][4] != cuadro_oscuro:
        rooks_puestos[14].disparos()
        sleep(1)
        imprimir_2_4()
################################################
#funciones y creacion del rook_3_0
rook_3_0= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_3_0():  
    hilo2 = Thread(target=imprimir_3_0, args=())
    hilo2.start()

def imprimir_3_0():
    if mesa[3][0] != cuadro_oscuro:
        rooks_puestos[15].disparos()
        sleep(1)
        imprimir_3_0()
#funciones y creacion del rook_3_1
rook_3_1= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_3_1():  
    hilo2 = Thread(target=imprimir_3_1, args=())
    hilo2.start()

def imprimir_3_1():
    if mesa[3][1] != cuadro_oscuro:
        rooks_puestos[16].disparos()
        sleep(1)
        imprimir_3_1()
#funciones y creacion del rook_3_2
rook_3_2= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_3_2():  
    hilo2 = Thread(target=imprimir_3_2, args=())
    hilo2.start()

def imprimir_3_2():
    if mesa[3][2] != cuadro_oscuro:
        rooks_puestos[17].disparos()
        sleep(1)
        imprimir_3_2()
#funciones y creacion del rook_3_3
rook_3_3= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_3_3():  
    hilo2 = Thread(target=imprimir_3_3, args=())
    hilo2.start()

def imprimir_3_3():
    if mesa[3][3] != cuadro_oscuro:
        rooks_puestos[18].disparos()
        sleep(1)
        imprimir_3_3()
#funciones y creacion del rook_3_4
rook_3_4= rooks(cuadro_oscuro,-200,-200)
def pone_rooks_3_4():  
    hilo2 = Thread(target=imprimir_3_4, args=())
    hilo2.start()

def imprimir_3_4():
    if mesa[3][4] != cuadro_oscuro:
        rooks_puestos[19].disparos()
        sleep(1)
        imprimir_3_4()
        
rooks_puestos = [rook_0_0,rook_0_1,rook_0_2,rook_0_3,rook_0_4,
                 rook_1_0,rook_1_1,rook_1_2,rook_1_3,rook_1_4,
                 rook_2_0,rook_2_1,rook_2_2,rook_2_3,rook_2_4,
                 rook_3_0,rook_3_1,rook_3_2,rook_3_3,rook_3_4]
                 #rook_4_0,rook_4_1,rook_4_2,rook_4_3,rook_4_4,
                 #rook_5_0,rook_5_1,rook_5_2,rook_5_3,rook_5_4,
                 #rook_6_0,rook_6_1,rook_6_2,rook_6_3,rook_6_4,
                 #rook_7_0,rook_7_1,rook_7_2,rook_7_3,rook_7_4,
                 #rook_8_0,rook_8_1,rook_8_2,rook_8_3,rook_8_4]
