import pygame
from pygame.locals import *
import sys

pygame.init()
# creamos la ventana y le indicamos un titulo:
ventana = pygame.display.set_mode((267,440))
pygame.display.set_caption("juego")
#################################################3
#cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def sigue(self):
        self.left,self.top = pygame.mouse.get_pos()
#define el cursor
cursor1 = Cursor()
#################################################
#botones de los cuadros
class Boton_cuadros(pygame.sprite.Sprite):
    def __init__(self,imagen1,x,y):
        self.imagen_actual = imagen1
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def cambio(self,imagen):
        self.imagen_actual = imagen
    
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
cuadro_1_0= Boton_cuadros(mesa[0][0] ,31,136)
cuadro_1_1= Boton_cuadros(mesa[0][1] ,66,136)
cuadro_1_2= Boton_cuadros(mesa[0][2] ,101,136)
cuadro_1_3= Boton_cuadros(mesa[0][3] ,138,136)
cuadro_1_4= Boton_cuadros(mesa[0][4] ,173,136)
#fila2
cuadro_2_0= Boton_cuadros(mesa[2][0] ,31,171)
cuadro_2_1= Boton_cuadros(mesa[2][1] ,66,171)
cuadro_2_2= Boton_cuadros(mesa[2][2] ,101,171)
cuadro_2_3= Boton_cuadros(mesa[2][3] ,138,171)
cuadro_2_4= Boton_cuadros(mesa[2][4] ,173,171)

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


###################################################
    
# el bucle principal del juego
while True:
    # Posibles entradas del teclado y mouse
    for event in pygame.event.get():
        #cierra el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ##########################################
        #botones de las torres
        if event.type == pygame.MOUSEBUTTONDOWN:
            #evento para seleccionar la torre de fuego
            if cursor1.colliderect(boton_fire_rooks.rect):
                escogido  = cuadro_o_con_fire_rooks
                boton_fire_rooks.cambio(fire_rooks2)
                boton_water_rooks.cambio(water_rooks)
                boton_sand_rooks.cambio(sand_rooks)
                boton_rock_rooks.cambio(rock_rooks)
            #evento para seleccionar la torre de roca
            if cursor1.colliderect(boton_rock_rooks.rect):
                escogido  = cuadro_o_con_rock_rooks
                boton_rock_rooks.cambio(rock_rooks2)
                boton_water_rooks.cambio(water_rooks)
                boton_sand_rooks.cambio(sand_rooks)
                boton_fire_rooks.cambio(fire_rooks)
            #evento para seleccionar la torre de arena
            if cursor1.colliderect(boton_sand_rooks.rect):
                escogido  = cuadro_o_con_sand_rooks
                boton_sand_rooks.cambio(sand_rooks2)
                boton_water_rooks.cambio(water_rooks)
                boton_rock_rooks.cambio(rock_rooks)
                boton_fire_rooks.cambio(fire_rooks)
            #evento para seleccionar la torre de agua
            if cursor1.colliderect(boton_water_rooks.rect):
                escogido  = cuadro_o_con_water_rooks
                boton_water_rooks.cambio(water_rooks2)
                boton_sand_rooks.cambio(sand_rooks)
                boton_rock_rooks.cambio(rock_rooks)
                boton_fire_rooks.cambio(fire_rooks)
        #########################################      
        #evento para camcelar la selaccion
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(cancelar.rect):
                escogido  = cuadro_oscuro
                boton_sand_rooks.cambio(sand_rooks)
                boton_fire_rooks.cambio(fire_rooks)
                boton_rock_rooks.cambio(rock_rooks)
                boton_water_rooks.cambio(water_rooks)
        #########################################
        #botones de los cuadros
        #pone la escogida en el cuadro
        if event.type == pygame.MOUSEBUTTONDOWN:
            #fila0
            if cursor1.colliderect(cuadro_0_0.rect):
                mesa[0][0]= escogido
                cuadro_0_0.cambio(mesa[0][0])
            if cursor1.colliderect(cuadro_0_1.rect):
                mesa[0][1]= escogido
                cuadro_0_1.cambio(mesa[0][1])
            if cursor1.colliderect(cuadro_0_2.rect):
                mesa[0][2]= escogido
                cuadro_0_2.cambio(mesa[0][2])
            if cursor1.colliderect(cuadro_0_3.rect):
                mesa[0][3]= escogido
                cuadro_0_3.cambio(mesa[0][3])
            if cursor1.colliderect(cuadro_0_4.rect):
                mesa[0][4]= escogido
                cuadro_0_4.cambio(mesa[0][4])
            #fila1
            if cursor1.colliderect(cuadro_1_0.rect):
                mesa[1][0]= escogido
                cuadro_1_0.cambio(mesa[1][0])
            if cursor1.colliderect(cuadro_1_1.rect):
                mesa[1][1]= escogido
                cuadro_1_1.cambio(mesa[1][1])
            if cursor1.colliderect(cuadro_1_2.rect):
                mesa[1][2]= escogido
                cuadro_1_2.cambio(mesa[1][2])
            if cursor1.colliderect(cuadro_1_3.rect):
                mesa[1][3]= escogido
                cuadro_1_3.cambio(mesa[1][3])
            if cursor1.colliderect(cuadro_1_4.rect):
                mesa[1][4]= escogido
                cuadro_1_4.cambio(mesa[1][4])
            #fila2
            if cursor1.colliderect(cuadro_2_0.rect):
                mesa[2][0]= escogido
                cuadro_2_0.cambio(mesa[2][0])
            if cursor1.colliderect(cuadro_2_1.rect):
                mesa[2][1]= escogido
                cuadro_2_1.cambio(mesa[2][1])
            if cursor1.colliderect(cuadro_2_2.rect):
                mesa[2][2]= escogido
                cuadro_2_2.cambio(mesa[2][2])
            if cursor1.colliderect(cuadro_2_3.rect):
                mesa[2][3]= escogido
                cuadro_2_3.cambio(mesa[2][3])
            if cursor1.colliderect(cuadro_2_4.rect):
                mesa[2][4]= escogido
                cuadro_2_4.cambio(mesa[2][4])
                
                
    #imagende fondo
    fondo = pygame.image.load("mesa.png").convert()
    ventana.blit(fondo, (0, 0))
    #############################################33
    #torres
    #llama al boton de la torre de fuego
    boton_rock_rooks.seleccion(ventana,cursor1)
    #llama al boton de la torre de roca
    boton_fire_rooks.seleccion(ventana,cursor1)
    #llama al boton de la torre de arena
    boton_sand_rooks.seleccion(ventana,cursor1)
    #llama al boton de la torre de agua
    boton_water_rooks.seleccion(ventana,cursor1)
    #############################################
    #cancelar
    #llama al boton de cancelar
    cancelar.seleccion(ventana,cursor1)
    #############################################
    #cuadros
    #fila1
    cuadro_0_0.seleccion(ventana,cursor1)
    cuadro_0_1.seleccion(ventana,cursor1)
    cuadro_0_2.seleccion(ventana,cursor1)
    cuadro_0_3.seleccion(ventana,cursor1)
    cuadro_0_4.seleccion(ventana,cursor1)
    #fila1
    cuadro_1_0.seleccion(ventana,cursor1)
    cuadro_1_1.seleccion(ventana,cursor1)
    cuadro_1_2.seleccion(ventana,cursor1)
    cuadro_1_3.seleccion(ventana,cursor1)
    cuadro_1_4.seleccion(ventana,cursor1)
    #fila2
    cuadro_2_0.seleccion(ventana,cursor1)
    cuadro_2_1.seleccion(ventana,cursor1)
    cuadro_2_2.seleccion(ventana,cursor1)
    cuadro_2_3.seleccion(ventana,cursor1)
    cuadro_2_4.seleccion(ventana,cursor1)
    #llama al cursor
    cursor1.sigue()
    #actualiza la pantalla
    pygame.display.flip()

