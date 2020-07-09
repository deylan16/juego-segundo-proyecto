import pygame
from pygame.locals import *


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
