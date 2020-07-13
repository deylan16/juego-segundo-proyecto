import pygame
from pygame.locals import *
import random
avatar1= pygame.image.load("avatar.png")
avatar2= pygame.image.load("avatar2.png")

class avatares(pygame.sprite.Sprite):
    def __init__(self,coords,vida):
        self.imagen = avatar1
        self.imagen2 = avatar2
        self.listaimagenes = [self.imagen,self.imagen2]
        self.posimagen = 0
        self.imagenavatar = self.listaimagenes[self.posimagen]
        self.rect = self.imagenavatar.get_rect()
        self.listadisparo = []
        self.velocidad = 20
        self.rect.top = coords[1]
        self.rect.left = coords[0]
        self.vida = vida
        self.tiempocambio =1
    def golpe(self,daño):
        self.vida -= daño
        if self.vida <= 0:
            self.rect.top = 550
            self.rect.left = 550
    def direccion(self):
        self.rect.top = self.rect.top - self.velocidad
    def aparece(self,ventana):
        self.imagenavatar = self.listaimagenes[self.posimagen]
        ventana.blit(self.imagenavatar,self.rect)
    def comportamiento(self,tiempo):
        if self.tiempocambio == tiempo:
            self.posimagen += 1
            self.tiempocambio += 1
            if self.posimagen > len(self.listaimagenes)-1:
                self.posimagen = 0
#################################################################
#clase de los proyectiles del los avatares
class proyectil_avatares(pygame.sprite.Sprite):
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

        
coordenadas = [(31,384),(66,384),(101,384),(138,384),(173,384)]
aparece_aleatoreo = random.choice(coordenadas)
avatar_prueba = avatares(aparece_aleatoreo,21)
def pone_avatar_prueba():  
    hilo2 = Thread(target=imprimir_prueba, args=())
    hilo2.start()

def imprimir_prueba():
    if mesa[7][3] == cuadro_oscuro:
        rooks_puestos[38].disparos()
        sleep(1)
        imprimir_7_3()

avatares_puestos = [avatar_prueba]
