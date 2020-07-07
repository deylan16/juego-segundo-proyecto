# ---------------------------
# Importacion de los módulos
# ---------------------------
import pygame
from pygame.locals import *
import sys

pygame.init()
# creamos la ventana y le indicamos un titulo:
ventana = pygame.display.set_mode((300,440))
pygame.display.set_caption("=juego")
#################################################3
#cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def sigue(self):
        self.left,self.top = pygame.mouse.get_pos()
#define el cursor
cursor1 = Cursor()

################################################3
#botones
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = imagen1
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def cambio(self,imagen):
        self.imagen_actual = imagen
        
    def seleccion(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        if  not cursor.colliderect(self.rect) and escogido == base:
            self.imagen_actual = self.imagen_normal
            
        pantalla.blit(self.imagen_actual,self.rect)
#imagenes de los Rocks
torre1 = pygame.image.load("torre1.png")
torre1_2 = pygame.image.load("torre1.2.png")
cancelar1 = pygame.image.load("cancelar1.png")
cancelar1_2 = pygame.image.load("cancelar1.2.png")
base = pygame.image.load("cuadro oscuro.png")
base1 = pygame.image.load("cuadro con torre1.png")
##################################################
#establece si hay algo seleccionado
escogido = base
##########################################3#######
#define el boton de la torre 1
boton1= Boton(torre1,torre1_2,20,20)
#Define el boton cancelar
boton2= Boton(cancelar1,cancelar1_2,20,80)
#cuandro 1
boton3= Boton(base,escogido ,31,101)

###################################################
    
# el bucle principal del juego
while True:
    # Posibles entradas del teclado y mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #evento para seleccionar la torre uno
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton1.rect):
                escogido  = base1
                boton3= Boton(base,escogido ,31,101)
                boton1.cambio(torre1_2)
        #evento para camcelar la selaccion
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton2.rect):
                boton3
                escogido  = base
                
                
                
    #imagende fondo
    fondo = pygame.image.load("mesa.png").convert()
    ventana.blit(fondo, (0, 0))
    #llama al boton de la torre 1
    boton1.seleccion(ventana,cursor1)
    #llama al boton de cancelar
    boton2.seleccion(ventana,cursor1)
    #llama boton cuadro 1
    boton3.seleccion(ventana,cursor1)
    #llama al cursor
    cursor1.sigue()
    #cuadros
    pygame.display.flip()

