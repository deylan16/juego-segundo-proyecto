import pygame
from pygame.locals import *
import random
from time import *
from threading import Thread
from cuadros import mesa


perdiste= pygame.image.load("perdiste.png")

class avatares(pygame.sprite.Sprite):
    def __init__(self,coords,datos,segundos):
        self.imagen = datos[0]
        self.imagen2 = datos[1]
        self.listaimagenes = [self.imagen,self.imagen2]
        self.posimagen = 0
        self.imagenavatar = self.listaimagenes[self.posimagen]
        self.rect = self.imagenavatar.get_rect()
        self.listadisparo = []
        self.rect.top = coords[1]
        self.rect.left = coords[0]
        self.sigue = True
        self.vida = datos[2]
        self.tiempocambio =1
        self.segundos = segundos
        self.tiempopaso =datos[3]
    def golpe(self,daño):
        self.vida -= daño
        if self.vida <= 0:
            self.rect.top = 550
            self.rect.left = 550
    def coords(self):
        return self.rect.left,self.rect.top
    def cambio_imagen(self,imagen):
        self.imagenavatar = imagen
    def get_tipo(self):
        return self.imagen 
    def aparece(self,ventana):
        self.imagenavatar = self.listaimagenes[self.posimagen]
        ventana.blit(self.imagenavatar,self.rect)
    def comportamiento(self,tiempo):
        if self.tiempocambio == tiempo:
            self.posimagen += 1
            self.tiempocambio += 1
            if self.posimagen > len(self.listaimagenes)-1:
                self.posimagen = 0
    def camina(self,tiempo):
            if self.rect.top > 101:
                if self. segundos == tiempo:            
                    self.segundos += self.tiempopaso
                    self.rect.top -= 35
                if self. segundos == 60:
                    self. segundos -= 60
            
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
#definicion avatares
leñador1= pygame.image.load("leñador1.png")
leñador2= pygame.image.load("leñador2.png")
leñador = [leñador1,leñador2,20,3]
canibal1= pygame.image.load("canibal1.png")
canibal2= pygame.image.load("canibal2.png")
canibal= [canibal1,canibal2,25,4]
escudero1= pygame.image.load("escudero1.png")
escudero2= pygame.image.load("escudero2.png")
escudero= [escudero1,escudero2,10,5]
arquero1= pygame.image.load("arquero1.png")
arquero2= pygame.image.load("arquero2.png")
arquero= [arquero1,arquero2,5,6]

tipo_avatar = [canibal,leñador,arquero,escudero]

def aleatorio_avatar():
    return random.choice(tipo_avatar)
        

lista_avatares =  []
    
poner_avatares = []


def crea_avatar():
    coordenadas = [(31,381),(66,381),(101,381),(138,381),(173,381)]
    for ocupado in lista_avatares:
        if ocupado.coords() == (31,381):
            coordenadas.remove((31,381))
        if ocupado.coords() == (66,381):
            coordenadas.remove((66,381))
        if ocupado.coords() == (101,381):
            coordenadas.remove((101,381))
        if ocupado.coords() == (138,381):
            coordenadas.remove((138,381))
        if ocupado.coords() == (173,381):
            coordenadas.remove((173,381))

    if coordenadas != []:
        avatar_prueba = avatares(random.choice(coordenadas),aleatorio_avatar(),localtime()[5]+2)
        lista_avatares.append(avatar_prueba)
        poner_avatares.append(avatar_prueba)
    sleep(1)
    return crea_avatar()
    
crea = Thread(target=crea_avatar,args=())
crea.start()
    

