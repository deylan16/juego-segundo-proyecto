import pygame
from pygame.locals import *
import sys
from time import *
from threading import Thread
from rooks import *
from cursor import *
from cuadros import *
from cuadros import mesa
from avatares import *

monedas_para_comprar = 100
monedas = 0
muertos = 0
activo = True

def monedas_aleatorias():
    global monedas
    tipos = [25,50,100]
    sleep(6)
    monedas += random.choice(tipos)
    return monedas_aleatorias()

genera = Thread(target= monedas_aleatorias,args = ())
genera.start()


#establece si hay algo seleccionado
escogido = 'no hace nada'

    
def empieza(guardado):
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    ventana = pygame.display.set_mode((267,480))
    pygame.display.set_caption("Battle: Avatars vs Rooks")

    #Fuente
    Fuenteti = pygame.font.SysFont("Arial",24)

    #bandera para restablecer niveles
    restablece = 0

    
    #reloj
    reloj = pygame.time.Clock()
    #########################################################################################################################################################################
    banderas =[[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]

    #musica
    pygame.mixer.music.load('musica.mp3')

    
    
    ##########################################################################################################################################################################   
    
    # el bucle principal del juego
    hola = True
    empieza_0 = pygame.time.get_ticks()
    contadorI = True
    aux=1
    pygame.mixer.music.play(4)
    while hola:
        
        reloj.tick(60)
        global escogido
        #obtiene el tiepo
        tiempo = abs((empieza_0 -pygame.time.get_ticks()))//1000
        #contador
        if aux==tiempo and contadorI:
            aux+=1
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            #cierra el programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
            ##########################################
            #botones de las torres
            if event.type == pygame.MOUSEBUTTONDOWN:
                #bon para recoger las monedas
                if cursor1.colliderect(boton_recoger_monedas):
                    global monedas
                    global monedas_para_comprar
                    monedas_para_comprar += monedas
                    monedas = 0
                #evento para seleccionar la torre de fuego
                if cursor1.colliderect(boton_fire_rooks.rect):
                    if monedas_para_comprar >= 150 and escogido == 'no hace nada':
                        monedas_para_comprar -= 150
                        escogido  = cuadro_o_con_fire_rooks
                        boton_fire_rooks.cambio(fire_rooks2)
                        boton_water_rooks.cambio(water_rooks)
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                #evento para seleccionar la torre de roca
                if cursor1.colliderect(boton_rock_rooks.rect):
                    if monedas_para_comprar >= 100 and escogido == 'no hace nada':
                        monedas_para_comprar -= 100
                        escogido  = cuadro_o_con_rock_rooks
                        boton_rock_rooks.cambio(rock_rooks2)
                        boton_water_rooks.cambio(water_rooks)
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                #evento para seleccionar la torre de arena
                if cursor1.colliderect(boton_sand_rooks.rect):
                    if monedas_para_comprar >= 50 and escogido == 'no hace nada':
                        monedas_para_comprar -= 50
                        escogido  = cuadro_o_con_sand_rooks
                        boton_sand_rooks.cambio(sand_rooks2)
                        boton_water_rooks.cambio(water_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                #evento para seleccionar la torre de agua
                if cursor1.colliderect(boton_water_rooks.rect):
                    if monedas_para_comprar >= 150 and escogido == 'no hace nada':
                        monedas_para_comprar -= 150
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
                if cursor1.colliderect(volumen.rect):
                    if volumen.imagen_actual == volumenS:
                        volumen.imagen_actual = volumenN
                        pygame.mixer.music.stop()
                        
                    elif volumen.imagen_actual == volumenN:
                        volumen.imagen_actual = volumenS
                        pygame.mixer.music.play(4)
            
           
                    
        #imagende fondo
        global muertos
        fondo = pygame.image.load("mesa.png")
        fondo2 = pygame.image.load("mesa2.png")
        fondo3 = pygame.image.load("mesa3.png")
        if muertos >= 0:
            ventana.blit(fondo, (0, 0))
        if muertos >= 5:
            ventana.blit(fondo2, (0, 0))
        if muertos >= 10:
            ventana.blit(fondo3, (0, 0))

        if muertos == 5 and restablece == 0:
            mesa[0] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[1] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[2] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[3] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[4] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[5] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[6] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[7] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[8] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            restablece += 1
        if muertos == 10 and restablece == 1:
            mesa[0] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[1] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[2] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[3] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[4] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[5] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[6] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[7] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            mesa[8] = [cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro,cuadro_oscuro]
            restablece += 1
            
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
        
        #############################################
        #cuadros
        #fila0
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
        #fila3
        cuadro_3_0.seleccion(ventana,cursor1)
        cuadro_3_1.seleccion(ventana,cursor1)
        cuadro_3_2.seleccion(ventana,cursor1)
        cuadro_3_3.seleccion(ventana,cursor1)
        cuadro_3_4.seleccion(ventana,cursor1)
        #fila4
        cuadro_4_0.seleccion(ventana,cursor1)
        cuadro_4_1.seleccion(ventana,cursor1)
        cuadro_4_2.seleccion(ventana,cursor1)
        cuadro_4_3.seleccion(ventana,cursor1)
        cuadro_4_4.seleccion(ventana,cursor1)
        #fila5
        cuadro_5_0.seleccion(ventana,cursor1)
        cuadro_5_1.seleccion(ventana,cursor1)
        cuadro_5_2.seleccion(ventana,cursor1)
        cuadro_5_3.seleccion(ventana,cursor1)
        cuadro_5_4.seleccion(ventana,cursor1)
        #fila6
        cuadro_6_0.seleccion(ventana,cursor1)
        cuadro_6_1.seleccion(ventana,cursor1)
        cuadro_6_2.seleccion(ventana,cursor1)
        cuadro_6_3.seleccion(ventana,cursor1)
        cuadro_6_4.seleccion(ventana,cursor1)
        #fila7
        cuadro_7_0.seleccion(ventana,cursor1)
        cuadro_7_1.seleccion(ventana,cursor1)
        cuadro_7_2.seleccion(ventana,cursor1)
        cuadro_7_3.seleccion(ventana,cursor1)
        cuadro_7_4.seleccion(ventana,cursor1)
         #fila8
        cuadro_8_0.seleccion(ventana,cursor1)
        cuadro_8_1.seleccion(ventana,cursor1)
        cuadro_8_2.seleccion(ventana,cursor1)
        
        cuadro_8_3.seleccion(ventana,cursor1)
        cuadro_8_4.seleccion(ventana,cursor1)

    
         #########################################
        #cambia el estado de la matriz principal
        if escogido != 'no hace nada':
            if event.type == pygame.MOUSEBUTTONDOWN:
                #fila0
                if cursor1.colliderect(cuadro_0_0.rect):
                        cambio_mesa(0,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_0_1.rect):
                        cambio_mesa(0,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_0_2.rect):
                        cambio_mesa(0,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_0_3.rect):
                        cambio_mesa(0,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_0_4.rect):
                        cambio_mesa(0,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila1
                if cursor1.colliderect(cuadro_1_0.rect):
                        cambio_mesa(1,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_1_1.rect):
                        cambio_mesa(1,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_1_2.rect):
                        cambio_mesa(1,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_1_3.rect):
                        cambio_mesa(1,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_1_4.rect):
                        cambio_mesa(1,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila2
                if cursor1.colliderect(cuadro_2_0.rect):
                        cambio_mesa(2,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_2_1.rect):
                        cambio_mesa(2,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_2_2.rect):
                        cambio_mesa(2,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_2_3.rect):
                        cambio_mesa(2,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_2_4.rect):
                        cambio_mesa(2,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila3
                if cursor1.colliderect(cuadro_3_0.rect):
                        cambio_mesa(3,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_3_1.rect):
                        cambio_mesa(3,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_3_2.rect):
                        cambio_mesa(3,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_3_3.rect):
                        cambio_mesa(3,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_3_4.rect):
                        cambio_mesa(3,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila4
                if cursor1.colliderect(cuadro_4_0.rect):
                        cambio_mesa(4,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_4_1.rect):
                        cambio_mesa(4,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_4_2.rect):
                        cambio_mesa(4,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_4_3.rect):
                        cambio_mesa(4,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_4_4.rect):
                        cambio_mesa(4,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila5
                if cursor1.colliderect(cuadro_5_0.rect):
                        cambio_mesa(5,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_5_1.rect):
                        cambio_mesa(5,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_5_2.rect):
                        cambio_mesa(5,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_5_3.rect):
                        cambio_mesa(5,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_5_4.rect):
                        cambio_mesa(5,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila6
                if cursor1.colliderect(cuadro_6_0.rect):
                        cambio_mesa(6,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_6_1.rect):
                        cambio_mesa(6,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_6_2.rect):
                        cambio_mesa(6,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_6_3.rect):
                        cambio_mesa(6,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_6_4.rect):
                        cambio_mesa(6,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                #fila7
                if cursor1.colliderect(cuadro_7_0.rect):
                        cambio_mesa(7,0,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_7_1.rect):
                        cambio_mesa(7,1,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_7_2.rect):
                        cambio_mesa(7,2,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_7_3.rect):
                        cambio_mesa(7,3,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)
                if cursor1.colliderect(cuadro_7_4.rect):
                        cambio_mesa(7,4,escogido)
                        escogido = 'no hace nada'
                        boton_sand_rooks.cambio(sand_rooks)
                        boton_fire_rooks.cambio(fire_rooks)
                        boton_rock_rooks.cambio(rock_rooks)
                        boton_water_rooks.cambio(water_rooks)


        #fila2
        rook_0_0.seleccion(ventana,cursor1)
        rook_0_1.seleccion(ventana,cursor1)
        rook_0_2.seleccion(ventana,cursor1)
        rook_0_3.seleccion(ventana,cursor1)
        rook_0_4.seleccion(ventana,cursor1)
        #fila1
        rook_1_0.seleccion(ventana,cursor1)
        rook_1_1.seleccion(ventana,cursor1)
        rook_1_2.seleccion(ventana,cursor1)
        rook_1_3.seleccion(ventana,cursor1)
        rook_1_4.seleccion(ventana,cursor1)
        #fila2
        rook_2_0.seleccion(ventana,cursor1)
        rook_2_1.seleccion(ventana,cursor1)
        rook_2_2.seleccion(ventana,cursor1)
        rook_2_3.seleccion(ventana,cursor1)
        rook_2_4.seleccion(ventana,cursor1)
        #fila3
        rook_3_0.seleccion(ventana,cursor1)
        rook_3_1.seleccion(ventana,cursor1)
        rook_3_2.seleccion(ventana,cursor1)
        rook_3_3.seleccion(ventana,cursor1)
        rook_3_4.seleccion(ventana,cursor1)
        #fila4
        rook_4_0.seleccion(ventana,cursor1)
        rook_4_1.seleccion(ventana,cursor1)
        rook_4_2.seleccion(ventana,cursor1)
        rook_4_3.seleccion(ventana,cursor1)
        rook_4_4.seleccion(ventana,cursor1)
        #fila5
        rook_5_0.seleccion(ventana,cursor1)
        rook_5_1.seleccion(ventana,cursor1)
        rook_5_2.seleccion(ventana,cursor1)
        rook_5_3.seleccion(ventana,cursor1)
        rook_5_4.seleccion(ventana,cursor1)
        #fila6
        rook_6_0.seleccion(ventana,cursor1)
        rook_6_1.seleccion(ventana,cursor1)
        rook_6_2.seleccion(ventana,cursor1)
        rook_6_3.seleccion(ventana,cursor1)
        rook_6_4.seleccion(ventana,cursor1)
        #fila7
        rook_7_0.seleccion(ventana,cursor1)
        rook_7_1.seleccion(ventana,cursor1)
        rook_7_2.seleccion(ventana,cursor1)
        rook_7_3.seleccion(ventana,cursor1)
        rook_7_4.seleccion(ventana,cursor1)
       
        #verifica la matriz principal y pone los roocks
        ########################################
        #fila0
        #rook_0_0    
        if mesa[0][0] != cuadro_oscuro and banderas[0][0] == 0:            
            pone_rooks_0_0()
            banderas[0][0] = 1
            if mesa[0][0] == cuadro_o_con_sand_rooks:
                rook_0_0.cambio(cuadro_0_0.coordsx_get(),cuadro_0_0.coordsy_get(),mesa[0][0],7)
            if mesa[0][0] == cuadro_o_con_water_rooks:
                rook_0_0.cambio(cuadro_0_0.coordsx_get(),cuadro_0_0.coordsy_get(),mesa[0][0],16)
            if mesa[0][0] == cuadro_o_con_fire_rooks:
                rook_0_0.cambio(cuadro_0_0.coordsx_get(),cuadro_0_0.coordsy_get(),mesa[0][0],16)
            if mesa[0][0] == cuadro_o_con_rock_rooks:
                rook_0_0.cambio(cuadro_0_0.coordsx_get(),cuadro_0_0.coordsy_get(),mesa[0][0],14)
        if mesa[0][0] == cuadro_oscuro:
            banderas[0][0] = 0
            rook_0_0.cambio(-200,-200,mesa[0][0],0)
        #rook_0_1
        if mesa[0][1] != cuadro_oscuro and banderas[0][1] == 0:
            pone_rooks_0_1()
            banderas[0][1] = 1
            if mesa[0][1] == cuadro_o_con_sand_rooks:
                rook_0_1.cambio(cuadro_0_1.coordsx_get(),cuadro_0_1.coordsy_get(),mesa[0][1],7)
            if mesa[0][1] == cuadro_o_con_water_rooks:
                rook_0_1.cambio(cuadro_0_1.coordsx_get(),cuadro_0_1.coordsy_get(),mesa[0][1],16)
            if mesa[0][1] == cuadro_o_con_fire_rooks:
                rook_0_1.cambio(cuadro_0_1.coordsx_get(),cuadro_0_1.coordsy_get(),mesa[0][1],16)
            if mesa[0][1] == cuadro_o_con_rock_rooks:
                rook_0_1.cambio(cuadro_0_1.coordsx_get(),cuadro_0_1.coordsy_get(),mesa[0][1],14)
        if mesa[0][1] == cuadro_oscuro:
            banderas[0][1] = 0
            rook_0_1.cambio(-200,-200,mesa[0][1],0)
        #rook_0_2    
        if mesa[0][2] != cuadro_oscuro and banderas[0][2] == 0:
            pone_rooks_0_2()
            banderas[0][2] = 1
            if mesa[0][2] == cuadro_o_con_sand_rooks:
                rook_0_2.cambio(cuadro_0_2.coordsx_get(),cuadro_0_2.coordsy_get(),mesa[0][2],7)
            if mesa[0][2] == cuadro_o_con_water_rooks:
                rook_0_2.cambio(cuadro_0_2.coordsx_get(),cuadro_0_2.coordsy_get(),mesa[0][2],16)
            if mesa[0][2] == cuadro_o_con_fire_rooks:
                rook_0_2.cambio(cuadro_0_2.coordsx_get(),cuadro_0_2.coordsy_get(),mesa[0][2],16)
            if mesa[0][2] == cuadro_o_con_rock_rooks:
                rook_0_2.cambio(cuadro_0_2.coordsx_get(),cuadro_0_2.coordsy_get(),mesa[0][2],14)
        if mesa[0][2] == cuadro_oscuro:
            banderas[0][2] = 0
            rook_0_2.cambio(-200,-200,mesa[0][2],0)
        #rook_0_3
        if mesa[0][3] != cuadro_oscuro and banderas[0][3] == 0:
            pone_rooks_0_3()
            banderas[0][3] = 1
            if mesa[0][3] == cuadro_o_con_sand_rooks:
                rook_0_3.cambio(cuadro_0_3.coordsx_get(),cuadro_0_3.coordsy_get(),mesa[0][3],7)
            if mesa[0][3] == cuadro_o_con_water_rooks:
                rook_0_3.cambio(cuadro_0_3.coordsx_get(),cuadro_0_3.coordsy_get(),mesa[0][3],16)
            if mesa[0][3] == cuadro_o_con_fire_rooks:
                rook_0_3.cambio(cuadro_0_3.coordsx_get(),cuadro_0_3.coordsy_get(),mesa[0][3],16)
            if mesa[0][3] == cuadro_o_con_rock_rooks:
                rook_0_3.cambio(cuadro_0_3.coordsx_get(),cuadro_0_3.coordsy_get(),mesa[0][3],14)
        if mesa[0][3] == cuadro_oscuro:
            banderas[0][3] = 0
            rook_0_3.cambio(-200,-200,mesa[0][3],0)
        #rook_0_4
        if mesa[0][4] != cuadro_oscuro and banderas[0][4] == 0:
            pone_rooks_0_4()
            banderas[0][4] = 1
            if mesa[0][4] == cuadro_o_con_sand_rooks:
                rook_0_4.cambio(cuadro_0_4.coordsx_get(),cuadro_0_4.coordsy_get(),mesa[0][4],7)
            if mesa[0][4] == cuadro_o_con_water_rooks:
                rook_0_4.cambio(cuadro_0_4.coordsx_get(),cuadro_0_4.coordsy_get(),mesa[0][4],16)
            if mesa[0][4] == cuadro_o_con_fire_rooks:
                rook_0_4.cambio(cuadro_0_4.coordsx_get(),cuadro_0_4.coordsy_get(),mesa[0][4],16)
            if mesa[0][4] == cuadro_o_con_rock_rooks:
                rook_0_4.cambio(cuadro_0_4.coordsx_get(),cuadro_0_4.coordsy_get(),mesa[0][4],14)
        if mesa[0][4] == cuadro_oscuro:
            banderas[0][4] = 0
            rook_0_4.cambio(-200,-200,mesa[0][4],0)
        ########################################
        #fila1
        #rook_1_0    
        if mesa[1][0] != cuadro_oscuro and banderas[1][0] == 0:
            pone_rooks_1_0()
            banderas[1][0] = 1
            if mesa[1][0] == cuadro_o_con_sand_rooks:
                rook_1_0.cambio(cuadro_1_0.coordsx_get(),cuadro_1_0.coordsy_get(),mesa[1][0],7)
            if mesa[1][0] == cuadro_o_con_water_rooks:
                rook_1_0.cambio(cuadro_1_0.coordsx_get(),cuadro_1_0.coordsy_get(),mesa[1][0],16)
            if mesa[1][0] == cuadro_o_con_fire_rooks:
                rook_1_0.cambio(cuadro_1_0.coordsx_get(),cuadro_1_0.coordsy_get(),mesa[1][0],16)
            if mesa[1][0] == cuadro_o_con_rock_rooks:
                rook_1_0.cambio(cuadro_1_0.coordsx_get(),cuadro_1_0.coordsy_get(),mesa[1][0],14)
        if mesa[1][0] == cuadro_oscuro:
            banderas[1][0] = 0
            rook_1_0.cambio(-200,-200,mesa[1][0],0)
        #rook_1_1
        if mesa[1][1] != cuadro_oscuro and banderas[1][1] == 0:
            pone_rooks_1_1()
            banderas[1][1] = 1
            if mesa[1][1] == cuadro_o_con_sand_rooks:
                rook_1_1.cambio(cuadro_1_1.coordsx_get(),cuadro_1_1.coordsy_get(),mesa[1][1],7)
            if mesa[1][1] == cuadro_o_con_water_rooks:
                rook_1_1.cambio(cuadro_1_1.coordsx_get(),cuadro_1_1.coordsy_get(),mesa[1][1],16)
            if mesa[1][1] == cuadro_o_con_fire_rooks:
                rook_1_1.cambio(cuadro_1_1.coordsx_get(),cuadro_1_1.coordsy_get(),mesa[1][1],16)
            if mesa[1][1] == cuadro_o_con_rock_rooks:
                rook_1_1.cambio(cuadro_1_1.coordsx_get(),cuadro_1_1.coordsy_get(),mesa[1][1],14)
        if mesa[1][1] == cuadro_oscuro:
            banderas[1][1] = 0
            rook_1_1.cambio(-200,-200,mesa[1][1],0)
        #rook_1_2    
        if mesa[1][2] != cuadro_oscuro and banderas[1][2] == 0:
            pone_rooks_1_2()
            banderas[1][2] = 1
            if mesa[1][2] == cuadro_o_con_sand_rooks:
                rook_1_2.cambio(cuadro_1_2.coordsx_get(),cuadro_1_2.coordsy_get(),mesa[1][2],7)
            if mesa[1][2] == cuadro_o_con_water_rooks:
                rook_1_2.cambio(cuadro_1_2.coordsx_get(),cuadro_1_2.coordsy_get(),mesa[1][2],16)
            if mesa[1][2] == cuadro_o_con_fire_rooks:
                rook_1_2.cambio(cuadro_1_2.coordsx_get(),cuadro_1_2.coordsy_get(),mesa[1][2],16)
            if mesa[1][2] == cuadro_o_con_rock_rooks:
                rook_1_2.cambio(cuadro_1_2.coordsx_get(),cuadro_1_2.coordsy_get(),mesa[1][2],14)
        if mesa[1][2] == cuadro_oscuro:
            banderas[1][2] = 0
            rook_1_2.cambio(-200,-200,mesa[1][2],0)
        #rook_1_3    
        if mesa[1][3] != cuadro_oscuro and banderas[1][3] == 0:
            pone_rooks_1_3()
            banderas[1][3] = 1
            if mesa[1][3] == cuadro_o_con_sand_rooks:
                rook_1_3.cambio(cuadro_1_3.coordsx_get(),cuadro_1_3.coordsy_get(),mesa[1][3],7)
            if mesa[1][3] == cuadro_o_con_water_rooks:
                rook_1_3.cambio(cuadro_1_3.coordsx_get(),cuadro_1_3.coordsy_get(),mesa[1][3],16)
            if mesa[1][3] == cuadro_o_con_fire_rooks:
                rook_1_3.cambio(cuadro_1_3.coordsx_get(),cuadro_1_3.coordsy_get(),mesa[1][3],16)
            if mesa[1][3] == cuadro_o_con_rock_rooks:
                rook_1_3.cambio(cuadro_1_3.coordsx_get(),cuadro_1_3.coordsy_get(),mesa[1][3],14)
        if mesa[1][3] == cuadro_oscuro:
            banderas[1][3] = 0
            rook_1_3.cambio(-200,-200,mesa[1][3],0)

        #rook_1_4
        if mesa[1][4] != cuadro_oscuro and banderas[1][4] == 0:
            pone_rooks_1_4()
            banderas[1][4] = 1
            if mesa[1][4] == cuadro_o_con_sand_rooks:
                rook_1_4.cambio(cuadro_1_4.coordsx_get(),cuadro_1_4.coordsy_get(),mesa[1][4],7)
            if mesa[1][4] == cuadro_o_con_water_rooks:
                rook_1_4.cambio(cuadro_1_4.coordsx_get(),cuadro_1_4.coordsy_get(),mesa[1][4],16)
            if mesa[1][4] == cuadro_o_con_fire_rooks:
                rook_1_4.cambio(cuadro_1_4.coordsx_get(),cuadro_1_4.coordsy_get(),mesa[1][4],16)
            if mesa[1][4] == cuadro_o_con_rock_rooks:
                rook_1_4.cambio(cuadro_1_4.coordsx_get(),cuadro_1_4.coordsy_get(),mesa[1][4],14)
        if mesa[1][4] == cuadro_oscuro:
            banderas[1][4] = 0
            rook_1_4.cambio(-200,-200,mesa[1][4],0)
        ########################################    
        #fila2
        #rook_2_0    
        if mesa[2][0] != cuadro_oscuro and banderas[2][0] == 0:
            pone_rooks_2_0()
            banderas[2][0] = 1
            if mesa[2][0] == cuadro_o_con_sand_rooks:
                rook_2_0.cambio(cuadro_2_0.coordsx_get(),cuadro_2_0.coordsy_get(),mesa[2][0],7)
            if mesa[2][0] == cuadro_o_con_water_rooks:
                rook_2_0.cambio(cuadro_2_0.coordsx_get(),cuadro_2_0.coordsy_get(),mesa[2][0],16)
            if mesa[2][0] == cuadro_o_con_fire_rooks:
                rook_2_0.cambio(cuadro_2_0.coordsx_get(),cuadro_2_0.coordsy_get(),mesa[2][0],16)
            if mesa[2][0] == cuadro_o_con_rock_rooks:
                rook_2_0.cambio(cuadro_2_0.coordsx_get(),cuadro_2_0.coordsy_get(),mesa[2][0],14)
        if mesa[2][0] == cuadro_oscuro:
            banderas[2][0] = 0
            rook_2_0.cambio(-200,-200,mesa[2][0],0)
        #rook_2_1
        if mesa[2][1] != cuadro_oscuro and banderas[2][1] == 0:
            pone_rooks_2_1()
            banderas[2][1] = 1
            if mesa[2][1] == cuadro_o_con_sand_rooks:
                rook_2_1.cambio(cuadro_2_1.coordsx_get(),cuadro_2_1.coordsy_get(),mesa[2][1],7)
            if mesa[2][1] == cuadro_o_con_water_rooks:
                rook_2_1.cambio(cuadro_2_1.coordsx_get(),cuadro_2_1.coordsy_get(),mesa[2][1],16)
            if mesa[2][1] == cuadro_o_con_fire_rooks:
                rook_2_1.cambio(cuadro_2_1.coordsx_get(),cuadro_2_1.coordsy_get(),mesa[2][1],16)
            if mesa[2][1] == cuadro_o_con_rock_rooks:
                rook_2_1.cambio(cuadro_2_1.coordsx_get(),cuadro_2_1.coordsy_get(),mesa[2][1],14)
        if mesa[2][1] == cuadro_oscuro:
            banderas[2][1] = 0
            rook_2_1.cambio(-200,-200,mesa[2][1],0)
        #rook_2_2    
        if mesa[2][2] != cuadro_oscuro and banderas[2][2] == 0:
            pone_rooks_2_2()
            banderas[2][2] = 1
            if mesa[2][2] == cuadro_o_con_sand_rooks:
                rook_2_2.cambio(cuadro_2_2.coordsx_get(),cuadro_2_2.coordsy_get(),mesa[2][2],7)
            if mesa[2][2] == cuadro_o_con_water_rooks:
                rook_2_2.cambio(cuadro_2_2.coordsx_get(),cuadro_2_2.coordsy_get(),mesa[2][2],16)
            if mesa[2][2] == cuadro_o_con_fire_rooks:
                rook_2_2.cambio(cuadro_2_2.coordsx_get(),cuadro_2_2.coordsy_get(),mesa[2][2],16)
            if mesa[2][2] == cuadro_o_con_rock_rooks:
                rook_2_2.cambio(cuadro_2_2.coordsx_get(),cuadro_2_2.coordsy_get(),mesa[2][2],14)
        if mesa[2][2] == cuadro_oscuro:
            banderas[2][2] = 0
            rook_2_2.cambio(-200,-200,mesa[2][2],0)
        #rook_2_3
        if mesa[2][3] != cuadro_oscuro and banderas[2][3] == 0:
            pone_rooks_2_3()
            banderas[2][3] = 1
            if mesa[2][3] == cuadro_o_con_sand_rooks:
                rook_2_3.cambio(cuadro_2_3.coordsx_get(),cuadro_2_3.coordsy_get(),mesa[2][3],7)
            if mesa[2][3] == cuadro_o_con_water_rooks:
                rook_2_3.cambio(cuadro_2_3.coordsx_get(),cuadro_2_3.coordsy_get(),mesa[2][3],16)
            if mesa[2][3] == cuadro_o_con_fire_rooks:
                rook_2_3.cambio(cuadro_2_3.coordsx_get(),cuadro_2_3.coordsy_get(),mesa[2][3],16)
            if mesa[2][3] == cuadro_o_con_rock_rooks:
                rook_2_3.cambio(cuadro_2_3.coordsx_get(),cuadro_2_3.coordsy_get(),mesa[2][3],14)
        if mesa[2][3] == cuadro_oscuro:
            banderas[2][3] = 0
            rook_2_3.cambio(-200,-200,mesa[2][3],0)
        #rook_2_4
        if mesa[2][4] != cuadro_oscuro and banderas[2][4] == 0:
            pone_rooks_2_4()
            banderas[2][4] = 1
            if mesa[2][4] == cuadro_o_con_sand_rooks:
                rook_2_4.cambio(cuadro_2_4.coordsx_get(),cuadro_2_4.coordsy_get(),mesa[2][4],7)
            if mesa[2][4] == cuadro_o_con_water_rooks:
                rook_2_4.cambio(cuadro_2_4.coordsx_get(),cuadro_2_4.coordsy_get(),mesa[2][4],16)
            if mesa[2][4] == cuadro_o_con_fire_rooks:
                rook_2_4.cambio(cuadro_2_4.coordsx_get(),cuadro_2_4.coordsy_get(),mesa[2][4],16)
            if mesa[2][4] == cuadro_o_con_rock_rooks:
                rook_2_4.cambio(cuadro_2_4.coordsx_get(),cuadro_2_4.coordsy_get(),mesa[2][4],14)
        if mesa[2][4] == cuadro_oscuro:
            banderas[2][4] = 0
            rook_2_4.cambio(-200,-200,mesa[2][4],0)
        ########################################
        #fila3
        #rook_3_0    
        if mesa[3][0] != cuadro_oscuro and banderas[3][0] == 0:
            pone_rooks_3_0()
            banderas[3][0] = 1
            if mesa[3][0] == cuadro_o_con_sand_rooks:
                rook_3_0.cambio(cuadro_3_0.coordsx_get(),cuadro_3_0.coordsy_get(),mesa[3][0],7)
            if mesa[3][0] == cuadro_o_con_water_rooks:
                rook_3_0.cambio(cuadro_3_0.coordsx_get(),cuadro_3_0.coordsy_get(),mesa[3][0],16)
            if mesa[3][0] == cuadro_o_con_fire_rooks:
                rook_3_0.cambio(cuadro_3_0.coordsx_get(),cuadro_3_0.coordsy_get(),mesa[3][0],16)
            if mesa[3][0] == cuadro_o_con_rock_rooks:
                rook_3_0.cambio(cuadro_3_0.coordsx_get(),cuadro_3_0.coordsy_get(),mesa[3][0],14)
        if mesa[3][0] == cuadro_oscuro:
            banderas[3][0] = 0
            rook_3_0.cambio(-200,-200,mesa[3][0],0)
        #rook_3_1
        if mesa[3][1] != cuadro_oscuro and banderas[3][1] == 0:
            pone_rooks_3_1()
            banderas[3][1] = 1
            if mesa[3][1] == cuadro_o_con_sand_rooks:
                rook_3_1.cambio(cuadro_3_1.coordsx_get(),cuadro_3_1.coordsy_get(),mesa[3][1],7)
            if mesa[3][1] == cuadro_o_con_water_rooks:
                rook_3_1.cambio(cuadro_3_1.coordsx_get(),cuadro_3_1.coordsy_get(),mesa[3][1],16)
            if mesa[3][1] == cuadro_o_con_fire_rooks:
                rook_3_1.cambio(cuadro_3_1.coordsx_get(),cuadro_3_1.coordsy_get(),mesa[3][1],16)
            if mesa[3][1] == cuadro_o_con_rock_rooks:
                rook_3_1.cambio(cuadro_3_1.coordsx_get(),cuadro_3_1.coordsy_get(),mesa[3][1],14)
        if mesa[3][1] == cuadro_oscuro:
            banderas[3][1] = 0
            rook_3_1.cambio(-200,-200,mesa[3][1],0)
        #rook_3_2    
        if mesa[3][2] != cuadro_oscuro and banderas[3][2] == 0:
            pone_rooks_3_2()
            banderas[3][2] = 1
            if mesa[3][2] == cuadro_o_con_sand_rooks:
                rook_3_2.cambio(cuadro_3_2.coordsx_get(),cuadro_3_2.coordsy_get(),mesa[3][2],7)
            if mesa[3][2] == cuadro_o_con_water_rooks:
                rook_3_2.cambio(cuadro_3_2.coordsx_get(),cuadro_3_2.coordsy_get(),mesa[3][2],16)
            if mesa[3][2] == cuadro_o_con_fire_rooks:
                rook_3_2.cambio(cuadro_3_2.coordsx_get(),cuadro_3_2.coordsy_get(),mesa[3][2],16)
            if mesa[3][2] == cuadro_o_con_rock_rooks:
                rook_3_2.cambio(cuadro_3_2.coordsx_get(),cuadro_3_2.coordsy_get(),mesa[3][2],14)
        if mesa[3][2] == cuadro_oscuro:
            banderas[3][2] = 0
            rook_3_2.cambio(-200,-200,mesa[3][2],0)
        #rook_3_3    
        if mesa[3][3] != cuadro_oscuro and banderas[3][3] == 0:
            pone_rooks_3_3()
            banderas[3][3] = 1
            if mesa[3][3] == cuadro_o_con_sand_rooks:
                rook_3_3.cambio(cuadro_3_3.coordsx_get(),cuadro_3_3.coordsy_get(),mesa[3][3],7)
            if mesa[3][3] == cuadro_o_con_water_rooks:
                rook_3_3.cambio(cuadro_3_3.coordsx_get(),cuadro_3_3.coordsy_get(),mesa[3][3],16)
            if mesa[3][3] == cuadro_o_con_fire_rooks:
                rook_3_3.cambio(cuadro_3_3.coordsx_get(),cuadro_3_3.coordsy_get(),mesa[3][3],16)
            if mesa[3][3] == cuadro_o_con_rock_rooks:
                rook_3_3.cambio(cuadro_3_3.coordsx_get(),cuadro_3_3.coordsy_get(),mesa[3][3],14)
        if mesa[3][3] == cuadro_oscuro:
            banderas[3][3] = 0
            rook_3_3.cambio(-200,-200,mesa[3][3],0)

        #rook_3_4
        if mesa[3][4] != cuadro_oscuro and banderas[3][4] == 0:
            pone_rooks_3_4()
            banderas[3][4] = 1
            if mesa[3][4] == cuadro_o_con_sand_rooks:
                rook_3_4.cambio(cuadro_3_4.coordsx_get(),cuadro_3_4.coordsy_get(),mesa[3][4],7)
            if mesa[3][4] == cuadro_o_con_water_rooks:
                rook_3_4.cambio(cuadro_3_4.coordsx_get(),cuadro_3_4.coordsy_get(),mesa[3][4],16)
            if mesa[3][4] == cuadro_o_con_fire_rooks:
                rook_3_4.cambio(cuadro_3_4.coordsx_get(),cuadro_3_4.coordsy_get(),mesa[3][4],16)
            if mesa[3][4] == cuadro_o_con_rock_rooks:
                rook_3_4.cambio(cuadro_3_4.coordsx_get(),cuadro_3_4.coordsy_get(),mesa[3][4],14)
        if mesa[3][4] == cuadro_oscuro:
            banderas[3][4] = 0
            rook_3_4.cambio(-200,-200,mesa[3][4],0)
        ##########################################################
        #fila4
        #rook_4_0    
        if mesa[4][0] != cuadro_oscuro and banderas[4][0] == 0:
            pone_rooks_4_0()
            banderas[4][0] = 1
            if mesa[4][0] == cuadro_o_con_sand_rooks:
                rook_4_0.cambio(cuadro_4_0.coordsx_get(),cuadro_4_0.coordsy_get(),mesa[4][0],7)
            if mesa[4][0] == cuadro_o_con_water_rooks:
                rook_4_0.cambio(cuadro_4_0.coordsx_get(),cuadro_4_0.coordsy_get(),mesa[4][0],16)
            if mesa[4][0] == cuadro_o_con_fire_rooks:
                rook_4_0.cambio(cuadro_4_0.coordsx_get(),cuadro_4_0.coordsy_get(),mesa[4][0],16)
            if mesa[4][0] == cuadro_o_con_rock_rooks:
                rook_4_0.cambio(cuadro_4_0.coordsx_get(),cuadro_4_0.coordsy_get(),mesa[4][0],14)
        if mesa[4][0] == cuadro_oscuro:
            banderas[4][0] = 0
            rook_4_0.cambio(-200,-200,mesa[4][0],0)
        #rook_4_1
        if mesa[4][1] != cuadro_oscuro and banderas[4][1] == 0:
            pone_rooks_4_1()
            banderas[4][1] = 1
            if mesa[4][1] == cuadro_o_con_sand_rooks:
                rook_4_1.cambio(cuadro_4_1.coordsx_get(),cuadro_4_1.coordsy_get(),mesa[4][1],7)
            if mesa[4][1] == cuadro_o_con_water_rooks:
                rook_4_1.cambio(cuadro_4_1.coordsx_get(),cuadro_4_1.coordsy_get(),mesa[4][1],16)
            if mesa[4][1] == cuadro_o_con_fire_rooks:
                rook_4_1.cambio(cuadro_4_1.coordsx_get(),cuadro_4_1.coordsy_get(),mesa[4][1],16)
            if mesa[4][1] == cuadro_o_con_rock_rooks:
                rook_4_1.cambio(cuadro_4_1.coordsx_get(),cuadro_4_1.coordsy_get(),mesa[4][1],14)
        if mesa[4][1] == cuadro_oscuro:
            banderas[4][1] = 0
            rook_4_1.cambio(-200,-200,mesa[4][1],0)
        #rook_4_2    
        if mesa[4][2] != cuadro_oscuro and banderas[4][2] == 0:
            pone_rooks_4_2()
            banderas[4][2] = 1
            if mesa[4][2] == cuadro_o_con_sand_rooks:
                rook_4_2.cambio(cuadro_4_2.coordsx_get(),cuadro_4_2.coordsy_get(),mesa[4][2],7)
            if mesa[4][2] == cuadro_o_con_water_rooks:
                rook_4_2.cambio(cuadro_4_2.coordsx_get(),cuadro_4_2.coordsy_get(),mesa[4][2],16)
            if mesa[4][2] == cuadro_o_con_fire_rooks:
                rook_4_2.cambio(cuadro_4_2.coordsx_get(),cuadro_4_2.coordsy_get(),mesa[4][2],16)
            if mesa[4][2] == cuadro_o_con_rock_rooks:
                rook_4_2.cambio(cuadro_4_2.coordsx_get(),cuadro_4_2.coordsy_get(),mesa[4][2],14)
        if mesa[4][2] == cuadro_oscuro:
            banderas[4][2] = 0
            rook_4_2.cambio(-200,-200,mesa[4][2],0)
        #rook_4_3
        if mesa[4][3] != cuadro_oscuro and banderas[4][3] == 0:
            pone_rooks_4_3()
            banderas[4][3] = 1
            if mesa[4][3] == cuadro_o_con_sand_rooks:
                rook_4_3.cambio(cuadro_4_3.coordsx_get(),cuadro_4_3.coordsy_get(),mesa[4][3],7)
            if mesa[4][3] == cuadro_o_con_water_rooks:
                rook_4_3.cambio(cuadro_4_3.coordsx_get(),cuadro_4_3.coordsy_get(),mesa[4][3],16)
            if mesa[4][3] == cuadro_o_con_fire_rooks:
                rook_4_3.cambio(cuadro_4_3.coordsx_get(),cuadro_4_3.coordsy_get(),mesa[4][3],16)
            if mesa[4][3] == cuadro_o_con_rock_rooks:
                rook_4_3.cambio(cuadro_4_3.coordsx_get(),cuadro_4_3.coordsy_get(),mesa[4][3],14)
        if mesa[4][3] == cuadro_oscuro:
            banderas[4][3] = 0
            rook_4_3.cambio(-200,-200,mesa[4][3],0)
        #rook_4_4
        if mesa[4][4] != cuadro_oscuro and banderas[4][4] == 0:
            pone_rooks_4_4()
            banderas[4][4] = 1
            if mesa[4][4] == cuadro_o_con_sand_rooks:
                rook_4_4.cambio(cuadro_4_4.coordsx_get(),cuadro_4_4.coordsy_get(),mesa[4][4],7)
            if mesa[4][4] == cuadro_o_con_water_rooks:
                rook_4_4.cambio(cuadro_4_4.coordsx_get(),cuadro_4_4.coordsy_get(),mesa[4][4],16)
            if mesa[4][4] == cuadro_o_con_fire_rooks:
                rook_4_4.cambio(cuadro_4_4.coordsx_get(),cuadro_4_4.coordsy_get(),mesa[4][4],16)
            if mesa[4][4] == cuadro_o_con_rock_rooks:
                rook_4_4.cambio(cuadro_4_4.coordsx_get(),cuadro_4_4.coordsy_get(),mesa[4][4],14)
        if mesa[4][4] == cuadro_oscuro:
            banderas[4][4] = 0
            rook_4_4.cambio(-200,-200,mesa[4][4],0)
        ########################################
        #fila5
        #rook_5_0    
        if mesa[5][0] != cuadro_oscuro and banderas[5][0] == 0:
            pone_rooks_5_0()
            banderas[5][0] = 1
            if mesa[5][0] == cuadro_o_con_sand_rooks:
                rook_5_0.cambio(cuadro_5_0.coordsx_get(),cuadro_5_0.coordsy_get(),mesa[5][0],7)
            if mesa[5][0] == cuadro_o_con_water_rooks:
                rook_5_0.cambio(cuadro_5_0.coordsx_get(),cuadro_5_0.coordsy_get(),mesa[5][0],16)
            if mesa[5][0] == cuadro_o_con_fire_rooks:
                rook_5_0.cambio(cuadro_5_0.coordsx_get(),cuadro_5_0.coordsy_get(),mesa[5][0],16)
            if mesa[5][0] == cuadro_o_con_rock_rooks:
                rook_5_0.cambio(cuadro_5_0.coordsx_get(),cuadro_5_0.coordsy_get(),mesa[5][0],14)
        if mesa[5][0] == cuadro_oscuro:
            banderas[5][0] = 0
            rook_5_0.cambio(-200,-200,mesa[5][0],0)
        #rook_5_1
        if mesa[5][1] != cuadro_oscuro and banderas[5][1] == 0:
            pone_rooks_5_1()
            banderas[5][1] = 1
            if mesa[5][1] == cuadro_o_con_sand_rooks:
                rook_5_1.cambio(cuadro_5_1.coordsx_get(),cuadro_5_1.coordsy_get(),mesa[5][1],7)
            if mesa[5][1] == cuadro_o_con_water_rooks:
                rook_5_1.cambio(cuadro_5_1.coordsx_get(),cuadro_5_1.coordsy_get(),mesa[5][1],16)
            if mesa[5][1] == cuadro_o_con_fire_rooks:
                rook_5_1.cambio(cuadro_5_1.coordsx_get(),cuadro_5_1.coordsy_get(),mesa[5][1],16)
            if mesa[5][1] == cuadro_o_con_rock_rooks:
                rook_5_1.cambio(cuadro_5_1.coordsx_get(),cuadro_5_1.coordsy_get(),mesa[5][1],14)
        if mesa[5][1] == cuadro_oscuro:
            cuenta_5_1 = 0
            rook_5_1.cambio(-200,-200,mesa[5][1],0)
        #rook_5_2    
        if mesa[5][2] != cuadro_oscuro and banderas[5][2] == 0:
            pone_rooks_5_2()
            banderas[5][2] = 1
            if mesa[5][2] == cuadro_o_con_sand_rooks:
                rook_5_2.cambio(cuadro_5_2.coordsx_get(),cuadro_5_2.coordsy_get(),mesa[5][2],7)
            if mesa[5][2] == cuadro_o_con_water_rooks:
                rook_5_2.cambio(cuadro_5_2.coordsx_get(),cuadro_5_2.coordsy_get(),mesa[5][2],16)
            if mesa[5][2] == cuadro_o_con_fire_rooks:
                rook_5_2.cambio(cuadro_5_2.coordsx_get(),cuadro_5_2.coordsy_get(),mesa[5][2],16)
            if mesa[5][2] == cuadro_o_con_rock_rooks:
                rook_5_2.cambio(cuadro_5_2.coordsx_get(),cuadro_5_2.coordsy_get(),mesa[5][2],14)
        if mesa[5][2] == cuadro_oscuro:
            banderas[5][2] = 0
            rook_5_2.cambio(-200,-200,mesa[5][2],0)
        #rook_5_3    
        if mesa[5][3] != cuadro_oscuro and banderas[5][3] == 0:
            pone_rooks_5_3()
            banderas[5][3] = 1
            if mesa[5][3] == cuadro_o_con_sand_rooks:
                rook_5_3.cambio(cuadro_5_3.coordsx_get(),cuadro_5_3.coordsy_get(),mesa[5][3],7)
            if mesa[5][3] == cuadro_o_con_water_rooks:
                rook_5_3.cambio(cuadro_5_3.coordsx_get(),cuadro_5_3.coordsy_get(),mesa[5][3],16)
            if mesa[5][3] == cuadro_o_con_fire_rooks:
                rook_5_3.cambio(cuadro_5_3.coordsx_get(),cuadro_5_3.coordsy_get(),mesa[5][3],16)
            if mesa[5][3] == cuadro_o_con_rock_rooks:
                rook_5_3.cambio(cuadro_5_3.coordsx_get(),cuadro_5_3.coordsy_get(),mesa[5][3],14)
        if mesa[5][3] == cuadro_oscuro:
            banderas[5][3] = 0
            rook_5_3.cambio(-200,-200,mesa[5][3],0)

        #rook_5_4
        if mesa[5][4] != cuadro_oscuro and banderas[5][4] == 0:
            pone_rooks_5_4()
            banderas[5][4] = 1
            if mesa[5][4] == cuadro_o_con_sand_rooks:
                rook_5_4.cambio(cuadro_5_4.coordsx_get(),cuadro_5_4.coordsy_get(),mesa[5][4],7)
            if mesa[5][4] == cuadro_o_con_water_rooks:
                rook_5_4.cambio(cuadro_5_4.coordsx_get(),cuadro_5_4.coordsy_get(),mesa[5][4],16)
            if mesa[5][4] == cuadro_o_con_fire_rooks:
                rook_5_4.cambio(cuadro_5_4.coordsx_get(),cuadro_5_4.coordsy_get(),mesa[5][4],16)
            if mesa[5][4] == cuadro_o_con_rock_rooks:
                rook_5_4.cambio(cuadro_5_4.coordsx_get(),cuadro_5_4.coordsy_get(),mesa[5][4],14)
        if mesa[5][4] == cuadro_oscuro:
            banderas[5][4] = 0
            rook_5_4.cambio(-200,-200,mesa[5][4],0)
        ##########################################################3##
        #fila6
        #rook_6_0    
        if mesa[6][0] != cuadro_oscuro and banderas[6][0] == 0:
            pone_rooks_6_0()
            banderas[6][0] = 1
            if mesa[6][0] == cuadro_o_con_sand_rooks:
                rook_6_0.cambio(cuadro_6_0.coordsx_get(),cuadro_6_0.coordsy_get(),mesa[6][0],7)
            if mesa[6][0] == cuadro_o_con_water_rooks:
                rook_6_0.cambio(cuadro_6_0.coordsx_get(),cuadro_6_0.coordsy_get(),mesa[6][0],16)
            if mesa[6][0] == cuadro_o_con_fire_rooks:
                rook_6_0.cambio(cuadro_6_0.coordsx_get(),cuadro_6_0.coordsy_get(),mesa[6][0],16)
            if mesa[6][0] == cuadro_o_con_rock_rooks:
                rook_6_0.cambio(cuadro_6_0.coordsx_get(),cuadro_6_0.coordsy_get(),mesa[6][0],14)
        if mesa[6][0] == cuadro_oscuro:
            banderas[6][0] = 0
            rook_6_0.cambio(-200,-200,mesa[6][0],0)
        #rook_6_1
        if mesa[6][1] != cuadro_oscuro and banderas[6][1] == 0:
            pone_rooks_6_1()
            banderas[6][1] = 1
            if mesa[6][1] == cuadro_o_con_sand_rooks:
                rook_6_1.cambio(cuadro_6_1.coordsx_get(),cuadro_6_1.coordsy_get(),mesa[6][1],7)
            if mesa[6][1] == cuadro_o_con_water_rooks:
                rook_6_1.cambio(cuadro_6_1.coordsx_get(),cuadro_6_1.coordsy_get(),mesa[6][1],16)
            if mesa[6][1] == cuadro_o_con_fire_rooks:
                rook_6_1.cambio(cuadro_6_1.coordsx_get(),cuadro_6_1.coordsy_get(),mesa[6][1],16)
            if mesa[6][1] == cuadro_o_con_rock_rooks:
                rook_6_1.cambio(cuadro_6_1.coordsx_get(),cuadro_6_1.coordsy_get(),mesa[6][1],14)
        if mesa[6][1] == cuadro_oscuro:
            banderas[6][1] = 0
            rook_6_1.cambio(-200,-200,mesa[6][1],0)
        #rook_6_2    
        if mesa[6][2] != cuadro_oscuro and banderas[6][2] == 0:
            pone_rooks_6_2()
            banderas[6][2] = 1
            if mesa[6][2] == cuadro_o_con_sand_rooks:
                rook_6_2.cambio(cuadro_6_2.coordsx_get(),cuadro_6_2.coordsy_get(),mesa[6][2],7)
            if mesa[6][2] == cuadro_o_con_water_rooks:
                rook_6_2.cambio(cuadro_6_2.coordsx_get(),cuadro_6_2.coordsy_get(),mesa[6][2],16)
            if mesa[6][2] == cuadro_o_con_fire_rooks:
                rook_6_2.cambio(cuadro_6_2.coordsx_get(),cuadro_6_2.coordsy_get(),mesa[6][2],16)
            if mesa[6][2] == cuadro_o_con_rock_rooks:
                rook_6_2.cambio(cuadro_6_2.coordsx_get(),cuadro_6_2.coordsy_get(),mesa[6][2],14)
        if mesa[6][2] == cuadro_oscuro:
            banderas[6][2] = 0
            rook_6_2.cambio(-200,-200,mesa[6][2],0)
        #rook_6_3
        if mesa[6][3] != cuadro_oscuro and banderas[6][3] == 0:
            pone_rooks_6_3()
            banderas[6][3] = 1
            if mesa[6][3] == cuadro_o_con_sand_rooks:
                rook_6_3.cambio(cuadro_6_3.coordsx_get(),cuadro_6_3.coordsy_get(),mesa[6][3],7)
            if mesa[6][3] == cuadro_o_con_water_rooks:
                rook_6_3.cambio(cuadro_6_3.coordsx_get(),cuadro_6_3.coordsy_get(),mesa[6][3],16)
            if mesa[6][3] == cuadro_o_con_fire_rooks:
                rook_6_3.cambio(cuadro_6_3.coordsx_get(),cuadro_6_3.coordsy_get(),mesa[6][3],16)
            if mesa[6][3] == cuadro_o_con_rock_rooks:
                rook_6_3.cambio(cuadro_6_3.coordsx_get(),cuadro_6_3.coordsy_get(),mesa[6][3],14)
        if mesa[6][3] == cuadro_oscuro:
            banderas[6][3] = 0
            rook_6_3.cambio(-200,-200,mesa[6][3],0)
        #rook_6_4
        if mesa[6][4] != cuadro_oscuro and banderas[6][4] == 0:
            pone_rooks_6_4()
            banderas[6][4] = 1
            if mesa[6][4] == cuadro_o_con_sand_rooks:
                rook_6_4.cambio(cuadro_6_4.coordsx_get(),cuadro_6_4.coordsy_get(),mesa[6][4],7)
            if mesa[6][4] == cuadro_o_con_water_rooks:
                rook_6_4.cambio(cuadro_6_4.coordsx_get(),cuadro_6_4.coordsy_get(),mesa[6][4],16)
            if mesa[6][4] == cuadro_o_con_fire_rooks:
                rook_6_4.cambio(cuadro_6_4.coordsx_get(),cuadro_6_4.coordsy_get(),mesa[6][4],16)
            if mesa[6][4] == cuadro_o_con_rock_rooks:
                rook_6_4.cambio(cuadro_6_4.coordsx_get(),cuadro_6_4.coordsy_get(),mesa[6][4],14)
        if mesa[6][4] == cuadro_oscuro:
            banderas[6][4] = 0
            rook_6_4.cambio(-200,-200,mesa[6][4],0)
        ########################################
        #fila7
        #rook_7_0    
        if mesa[7][0] != cuadro_oscuro and banderas[7][0] == 0:
            pone_rooks_7_0()
            banderas[7][0] = 1
            if mesa[7][0] == cuadro_o_con_sand_rooks:
                rook_7_0.cambio(cuadro_7_0.coordsx_get(),cuadro_7_0.coordsy_get(),mesa[7][0],7)
            if mesa[7][0] == cuadro_o_con_water_rooks:
                rook_7_0.cambio(cuadro_7_0.coordsx_get(),cuadro_7_0.coordsy_get(),mesa[7][0],16)
            if mesa[7][0] == cuadro_o_con_fire_rooks:
                rook_7_0.cambio(cuadro_7_0.coordsx_get(),cuadro_7_0.coordsy_get(),mesa[7][0],16)
            if mesa[7][0] == cuadro_o_con_rock_rooks:
                rook_7_0.cambio(cuadro_7_0.coordsx_get(),cuadro_7_0.coordsy_get(),mesa[7][0],14)
        if mesa[7][0] == cuadro_oscuro:
            banderas[7][0] = 0
            rook_7_0.cambio(-200,-200,mesa[7][0],0)
        #rook_7_1
        if mesa[7][1] != cuadro_oscuro and banderas[7][1] == 0:
            pone_rooks_7_1()
            banderas[7][1] = 1
            if mesa[7][1] == cuadro_o_con_sand_rooks:
                rook_7_1.cambio(cuadro_7_1.coordsx_get(),cuadro_7_1.coordsy_get(),mesa[7][1],7)
            if mesa[7][1] == cuadro_o_con_water_rooks:
                rook_7_1.cambio(cuadro_7_1.coordsx_get(),cuadro_7_1.coordsy_get(),mesa[7][1],16)
            if mesa[7][1] == cuadro_o_con_fire_rooks:
                rook_7_1.cambio(cuadro_7_1.coordsx_get(),cuadro_7_1.coordsy_get(),mesa[7][1],16)
            if mesa[7][1] == cuadro_o_con_rock_rooks:
                rook_7_1.cambio(cuadro_7_1.coordsx_get(),cuadro_7_1.coordsy_get(),mesa[7][1],14)
        if mesa[7][1] == cuadro_oscuro:
            banderas[7][1] = 0
            rook_7_1.cambio(-200,-200,mesa[7][1],0)
        #rook_7_2    
        if mesa[7][2] != cuadro_oscuro and banderas[7][2] == 0:
            pone_rooks_7_2()
            banderas[7][2] = 1
            if mesa[7][2] == cuadro_o_con_sand_rooks:
                rook_7_2.cambio(cuadro_7_2.coordsx_get(),cuadro_7_2.coordsy_get(),mesa[7][2],7)
            if mesa[7][2] == cuadro_o_con_water_rooks:
                rook_7_2.cambio(cuadro_7_2.coordsx_get(),cuadro_7_2.coordsy_get(),mesa[7][2],16)
            if mesa[7][2] == cuadro_o_con_fire_rooks:
                rook_7_2.cambio(cuadro_7_2.coordsx_get(),cuadro_7_2.coordsy_get(),mesa[7][2],16)
            if mesa[7][2] == cuadro_o_con_rock_rooks:
                rook_7_2.cambio(cuadro_7_2.coordsx_get(),cuadro_7_2.coordsy_get(),mesa[7][2],14)
        if mesa[7][2] == cuadro_oscuro:
            banderas[7][2] = 0
            rook_7_2.cambio(-200,-200,mesa[7][2],0)
        #rook_7_3    
        if mesa[7][3] != cuadro_oscuro and banderas[7][3] == 0:
            pone_rooks_7_3()
            banderas[7][3] = 1
            if mesa[7][3] == cuadro_o_con_sand_rooks:
                rook_7_3.cambio(cuadro_7_3.coordsx_get(),cuadro_7_3.coordsy_get(),mesa[7][3],7)
            if mesa[7][3] == cuadro_o_con_water_rooks:
                rook_7_3.cambio(cuadro_7_3.coordsx_get(),cuadro_7_3.coordsy_get(),mesa[7][3],16)
            if mesa[7][3] == cuadro_o_con_fire_rooks:
                rook_7_3.cambio(cuadro_7_3.coordsx_get(),cuadro_7_3.coordsy_get(),mesa[7][3],16)
            if mesa[7][3] == cuadro_o_con_rock_rooks:
                rook_7_3.cambio(cuadro_7_3.coordsx_get(),cuadro_7_3.coordsy_get(),mesa[7][3],14)
        if mesa[7][3] == cuadro_oscuro:
            banderas[7][3] = 0
            rook_7_3.cambio(-200,-200,mesa[7][3],0)

        #rook_7_4
        if mesa[7][4] != cuadro_oscuro and banderas[7][4] == 0:
            pone_rooks_7_4()
            banderas[7][4] = 1
            if mesa[7][4] == cuadro_o_con_sand_rooks:
                rook_7_4.cambio(cuadro_7_4.coordsx_get(),cuadro_7_4.coordsy_get(),mesa[7][4],7)
            if mesa[7][4] == cuadro_o_con_water_rooks:
                rook_7_4.cambio(cuadro_7_4.coordsx_get(),cuadro_7_4.coordsy_get(),mesa[7][4],16)
            if mesa[7][4] == cuadro_o_con_fire_rooks:
                rook_7_4.cambio(cuadro_7_4.coordsx_get(),cuadro_7_4.coordsy_get(),mesa[7][4],16)
            if mesa[7][4] == cuadro_o_con_rock_rooks:
                rook_7_4.cambio(cuadro_7_4.coordsx_get(),cuadro_7_4.coordsy_get(),mesa[7][4],14)
        if mesa[7][4] == cuadro_oscuro:
            banderas[7][4] = 0
            rook_7_4.cambio(-200,-200,mesa[7][4],0)
        ##########################################################
        global activo
        if activo == True:
            aparecen_avatares()
            activo = False
        segundos = localtime()
        if contadorI == True:
            if len(poner_avatares) > 0:
                for ele in poner_avatares:
                    ele.comportamiento(segundos[5])
                    ele.aparece(ventana)
                    ele.camina(segundos[5])
        #############################################################
        #proyectiles
        if contadorI == True:
            for a in rooks_puestos:
                #if len(a.lista_disparo)>0:
                 #   if a.y == coord_x:
                       # print('bien')
                        for ele in a.lista_disparo:
                            ele.direccion('abajo') 
                            ele.disparo(ventana)

                            if ele.rect.top > 400:
                                a.lista_disparo.remove(ele)
                            for i in  lista_avatares:
                                if ele.chocan(i.rect.left,i.rect.top) == True:
                                    if ele.get_tipo() == bola_de_agua:
                                        monedas_para_comprar +=int(i.golpe(8))
                                    if ele.get_tipo() == bola_de_arena:
                                        monedas_para_comprar +=int(i.golpe(2))
                                    if ele.get_tipo() == bola_de_fuego:
                                        monedas_para_comprar +=int(i.golpe(8))
                                    if ele.get_tipo() == bola_de_roca:
                                        monedas_para_comprar +=int(i.golpe(4))
                                    if ele in a.lista_disparo:
                                        a.lista_disparo.remove(ele)
                    #else:
                        #print('mal')
                        #a.lista_disparo = []
        if contadorI == True:
            for a in lista_avatares:
                if a.get_tipo() == arquero1:
                    if len(a.lista_disparo)>0:
                        for ele in a.lista_disparo:
                                ele.direccion('arriba') 
                                ele.disparo(ventana)

                                if ele.rect.top < 100:
                                    a.lista_disparo.remove(ele)
                                for i in  rooks_puestos:
                                    if ele.chocan(i.x,i.y) == True:
                                        i.golpe(2)
                                        a.lista_disparo.remove(ele)

        if contadorI == True:
            for a in lista_avatares:
                if a.get_tipo() != arquero1:
                    if len(a.lista_disparo)>0:
                        for ele in a.lista_disparo:
                                ele.direccion('arriba') 
                                ele.disparo(ventana)

                                if ele.rect.top < 100:
                                    a.lista_disparo.remove(ele)
                                for i in  rooks_puestos:
                                    if ele.chocan(i.x,i.y) == True:
                                        if ele.get_tipo() == espada:
                                            i.golpe(3)
                                        if ele.get_tipo() == hacha:
                                            i.golpe(9)
                                        if ele.get_tipo() == garrote:
                                            i.golpe(12)
                                        a.lista_disparo.remove(ele)
                                    
        for avatar in lista_avatares:
            for rooks in rooks_puestos:
                if avatar.coords() == rooks.coords():
                    avatar.dañar = True

                    
        for avatar in lista_avatares:            
            if avatar.rect.top == 101:
                contadorI=False
                ventana.blit(perdiste,(0,101))                                   
        #############################################################
        #fondo de la monedas para comprar
        ventana.blit(fondo_monedas3,(215,97))
        #boton para recoger monedas
        boton_recoger_monedas.seleccion(ventana,cursor1)
        #monedas para comprar
        monedas_para_comprar_ = Fuenteti.render(str(monedas_para_comprar),0,(255,255,255))
        ventana.blit(monedas_para_comprar_,(220,100))
        #monedas para recolectar
        monedas_para_retirar = Fuenteti.render(str(monedas),0,(255,255,255))
        ventana.blit(monedas_para_retirar,(220,400))
        #contador en pantalla
        contador = Fuenteti.render("Tiempo : "+str(aux),0,(255,255,255))
        ventana.blit(contador,(0,415))

        for avatar in lista_avatares:
            if avatar.vida <= 0:
                muertos += 1
                lista_avatares.remove(avatar)
                
        
        volumen.seleccion(ventana,cursor1)
        
        #llama al cursor
        cursor1.sigue()
        
        #actualiza la pantalla
        pygame.display.flip()

        
