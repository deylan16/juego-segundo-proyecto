import pygame
from pygame.locals import *
import random
from time import *
from threading import Thread
avatar1= pygame.image.load("avatar.png")
avatar2= pygame.image.load("avatar2.png")
perdiste= pygame.image.load("perdiste.png")

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
        self.tiempocambio =2
    def golpe(self,daño):
        self.vida -= daño
        if self.vida <= 0:
            self.rect.top = 550
            self.rect.left = 550
    def cambio_imagen(self,imagen):
        self.imagenavatar = imagen
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
######################################33
pasos = [38,35,35,35,35,35,35,35,35]

def mueve():
    global ventana
    i = 0
    while avatar_prueba.rect.left != 550 and avatar_prueba.rect.left != 0:
        i +=1
        
        if i <= len(pasos)-1:
            sleep(2)
            avatar_prueba.rect.top -= pasos[i]
        else:
            break
def movimiento():
    mueve_avatar = Thread(target=mueve, args=())
    mueve_avatar.start()

    

avatares_puestos = [avatar_prueba]
