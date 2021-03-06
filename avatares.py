import shelve
import pygame
from pygame.locals import *
import random
from time import *
from threading import Thread
from cuadros import mesa
from rooks import proyectil

#imagenes para los ataques de lo avatres
flecha= pygame.image.load("flecha.png")
espada= pygame.image.load("espada.png")
hacha= pygame.image.load("hacha.png")
garrote= pygame.image.load("garrote.png")
#iamgenes para mostrar se se gano o perdio
perdiste= pygame.image.load("perdiste.png")
ganaste= pygame.image.load("ganaste.png")
#clase avatares
#artibutos:
#        self.velat: determina cada cuanto ataca el rook
#        self.imagen: imagen del rooks
#        self.imagen2: imagen 2 del rook
#        self.listaimagenes: lista con las dos imagenes del rook
#        self.posimagen: numero para determinar la posicion de listaimagnes
#        self.imagenavatar:imegen que se mostrara
#        self.rect: obtiene el rectangulo del la imagen
#        self.lista_disparo: lista con los disparos para los taques de los avatres
#        self.rect.top: coordenada y
#        self.rect.left: coordenada x
#        self.sigue: boolean si el avatar camina o no
#        self.vida: vida del avatar
#        self.segundos: segundos
#        self.segundosa: segundos
#        self.tiempopaso: determina el tiempo para moverse un fila par arriba
#        self.dañar: determina el golpe a los rooks
#metodos:
#        golpe(daño): le baja la vida al avatar daño
#       coords: retorna las coordenas del avatar
#       cambio_imagen:cambia la imagen que se muestra
#       get_tipo: retorna que tipo es el avatar
#       aparece:muestra el avatar en la pantella
#       comportamiento(tiempo): crea la animacion del avatar y el ataque de los avateres
#       camina(tiempo): hace que el avatar se mueva una fila para arriba
class avatares(pygame.sprite.Sprite):
    def __init__(self,coords,datos,segundos):
        self.velat = datos[5]
        self.imagen = datos[0]
        self.imagen2 = datos[1]
        self.listaimagenes = [self.imagen,self.imagen2]
        self.posimagen = 0
        self.imagenavatar = self.listaimagenes[self.posimagen]
        self.rect = self.imagenavatar.get_rect()
        self.lista_disparo = []
        self.rect.top = coords[1]
        self.rect.left = coords[0]
        self.sigue = True
        self.vida = datos[2]
        self.tiempocambio =1
        self.segundos = segundos
        self.segundosa = segundos
        self.tiempopaso =datos[3]
        self.dañar = datos[4]
    def golpe(self,daño):
        self.vida -= daño
        suma = 0
        if self.vida <= 0:
            self.rect.top = 550
            self.rect.left = 550
            suma+= 100
        return suma
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
        if self.segundosa == tiempo:
            self.posimagen += 1           
            if self.imagen == arquero1  and self.posimagen == 1 :
                bala = proyectil(self.rect.left,self.rect.top,flecha)
                self.lista_disparo.append(bala)
            if self.dañar == True:
                if self.imagen == leñador1:
                    bala = proyectil(self.rect.left,self.rect.top-33,hacha)
                    self.lista_disparo.append(bala)
                if self.imagen == canibal1:
                    bala = proyectil(self.rect.left,self.rect.top-33,garrote)
                    self.lista_disparo.append(bala)
                if self.imagen == escudero1:
                    bala = proyectil(self.rect.left,self.rect.top-33,espada)
                    self.lista_disparo.append(bala)
            self.segundosa += self.velat
            if self.posimagen > len(self.listaimagenes)-1:
                self.posimagen = 0
        if self. segundosa == 60:
                self. segundosa -= 60       
    def camina(self,tiempo):
            if self.rect.top > 101:
                if self. segundos == tiempo:            
                    self.segundos += self.tiempopaso
                    self.rect.top -= 35
                if self. segundos == 60:
                    self. segundos -= 60
            
#################################################################
#definicion avatares
leñador1= pygame.image.load("leñador1.png")
leñador2= pygame.image.load("leñador2.png")
d = shelve.open('configuraciones')
VAC = d['VAC']
VMC = d['VMC']
d.close()
leñador = [leñador1,leñador2,20,VMC,False,VAC]
canibal1= pygame.image.load("canibal1.png")
canibal2= pygame.image.load("canibal2.png")
d = shelve.open('configuraciones')
VAL = d['VAL']
VML = d['VML']
d.close()
canibal= [canibal1,canibal2,25,VML,False,VAL]
escudero1= pygame.image.load("escudero1.png")
escudero2= pygame.image.load("escudero2.png")
d = shelve.open('configuraciones')
VAE = d['VAE']
VME = d['VME']
d.close()
escudero= [escudero1,escudero2,10,VME,False,VAE]
arquero1= pygame.image.load("arquero1.png")
arquero2= pygame.image.load("arquero2.png")
d = shelve.open('configuraciones')
VAF = d['VAF']
VMF = d['VMF']
d.close()
arquero= [arquero1,arquero2,5,VMF,False,VAF]

#lista con los dato de cada avatar
tipo_avatar = [canibal,leñador,arquero,escudero]
#obtine un valor a aleatoreo de la lista tipo_avatar
def aleatorio_avatar():
    return random.choice(tipo_avatar)
        
#listas para poner avatres en la pantalla
lista_avatares =  []   
poner_avatares = []

#variable para determinada cada cuanto aparecen los avatares
segundos_entre_cada_avatar = 7
#E:-
#S:cracion de avatres en la lista_avatares
#R:-
def crea_avatar():
    for numero in range(0,15):
        if numero< 15:
            if numero <= 6:
                sleep(segundos_entre_cada_avatar)
            if numero > 6 and numero<= 11:
                sleep(segundos_entre_cada_avatar*0.7)
            if numero > 11:
                sleep(segundos_entre_cada_avatar*0.4)
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
    
#crea el hilom para que aparescan los avatares  
def aparecen_avatares():
    crea = Thread(target=crea_avatar,args=())
    crea.start()

#obtiene las coordenadas x de los avatres puestos
def coord_x():
    for avatar in lista_avatares:
        return avatar.rect.left
    
