import pygame
from pygame.locals import *
import sys
from time import *
from threading import Thread
from rooks import *
from cursor import *
from cuadros import *


pygame.init()
# creamos la ventana y le indicamos un titulo:
ventana = pygame.display.set_mode((267,440))
pygame.display.set_caption("juego")
##########################################3#######
#imagenes de los proyectiles
agua = pygame.image.load("bala.png")
#proyectiles
c = [cuadro_0_0,cuadro_0_1,cuadro_0_2,cuadro_0_3,cuadro_0_4,cuadro_1_0,cuadro_1_1,cuadro_1_2,cuadro_1_3,cuadro_1_4,cuadro_2_0,cuadro_2_1,cuadro_2_2,
                        cuadro_2_3,cuadro_2_4,cuadro_3_0,cuadro_3_1,cuadro_3_2,cuadro_3_3,cuadro_3_4,cuadro_4_0,cuadro_4_1,cuadro_4_2,cuadro_4_3,cuadro_4_4,cuadro_5_0,
                        cuadro_5_1,cuadro_5_2,cuadro_5_3,cuadro_5_4,cuadro_6_0,cuadro_6_1,cuadro_6_2,cuadro_6_3,cuadro_6_4,cuadro_7_0,cuadro_7_1,cuadro_7_2,cuadro_7_3,
                        cuadro_7_4,cuadro_8_0,cuadro_8_1,cuadro_8_2,cuadro_8_3,cuadro_8_4]

y0 = c[0].coordsy_get()
x0 = c[0].coordsx_get()
y1 = c[1].coordsy_get()
x1 = c[1].coordsx_get()

def lanza_agua(estado,x,y):
    if estado.estado_get() == cuadro_o_con_water_rooks:
        ventana.blit(agua,(x,y))
        sleep(1)
        return lanza_agua(estado,x,y)
    else:
        return 0


#########################################################################################################################################################################
##########################################################################################################################################################################   
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
            #fila3
            if cursor1.colliderect(cuadro_3_0.rect):
                mesa[3][0]= escogido
                cuadro_3_0.cambio(mesa[3][0])
            if cursor1.colliderect(cuadro_3_1.rect):
                mesa[3][1]= escogido
                cuadro_3_1.cambio(mesa[3][1])
            if cursor1.colliderect(cuadro_3_2.rect):
                mesa[3][2]= escogido
                cuadro_3_2.cambio(mesa[3][2])
            if cursor1.colliderect(cuadro_3_3.rect):
                mesa[3][3]= escogido
                cuadro_3_3.cambio(mesa[3][3])
            if cursor1.colliderect(cuadro_3_4.rect):
                mesa[3][4]= escogido
                cuadro_3_4.cambio(mesa[3][4])
            #fila4
            if cursor1.colliderect(cuadro_4_0.rect):
                mesa[4][0]= escogido
                cuadro_4_0.cambio(mesa[4][0])
            if cursor1.colliderect(cuadro_4_1.rect):
                mesa[4][1]= escogido
                cuadro_4_1.cambio(mesa[4][1])
            if cursor1.colliderect(cuadro_4_2.rect):
                mesa[4][2]= escogido
                cuadro_4_2.cambio(mesa[4][2])
            if cursor1.colliderect(cuadro_4_3.rect):
                mesa[4][3]= escogido
                cuadro_4_3.cambio(mesa[4][3])
            if cursor1.colliderect(cuadro_4_4.rect):
                mesa[4][4]= escogido
                cuadro_4_4.cambio(mesa[4][4])
            #fila5
            if cursor1.colliderect(cuadro_5_0.rect):
                mesa[5][0]= escogido
                cuadro_5_0.cambio(mesa[5][0])
            if cursor1.colliderect(cuadro_5_1.rect):
                mesa[5][1]= escogido
                cuadro_5_1.cambio(mesa[5][1])
            if cursor1.colliderect(cuadro_5_2.rect):
                mesa[5][2]= escogido
                cuadro_5_2.cambio(mesa[5][2])
            if cursor1.colliderect(cuadro_5_3.rect):
                mesa[5][3]= escogido
                cuadro_5_3.cambio(mesa[5][3])
            if cursor1.colliderect(cuadro_5_4.rect):
                mesa[5][4]= escogido
                cuadro_5_4.cambio(mesa[5][4])
            #fila6
            if cursor1.colliderect(cuadro_6_0.rect):
                mesa[6][0]= escogido
                cuadro_6_0.cambio(mesa[6][0])
            if cursor1.colliderect(cuadro_6_1.rect):
                mesa[6][1]= escogido
                cuadro_6_1.cambio(mesa[6][1])
            if cursor1.colliderect(cuadro_6_2.rect):
                mesa[6][2]= escogido
                cuadro_6_2.cambio(mesa[6][2])
            if cursor1.colliderect(cuadro_6_3.rect):
                mesa[6][3]= escogido
                cuadro_6_3.cambio(mesa[6][3])
            if cursor1.colliderect(cuadro_6_4.rect):
                mesa[6][4]= escogido
                cuadro_6_4.cambio(mesa[6][4])
            #fila7
            if cursor1.colliderect(cuadro_7_0.rect):
                mesa[7][0]= escogido
                cuadro_7_0.cambio(mesa[7][0])
            if cursor1.colliderect(cuadro_7_1.rect):
                mesa[7][1]= escogido
                cuadro_7_1.cambio(mesa[7][1])
            if cursor1.colliderect(cuadro_7_2.rect):
                mesa[7][2]= escogido
                cuadro_7_2.cambio(mesa[7][2])
            if cursor1.colliderect(cuadro_7_3.rect):
                mesa[7][3]= escogido
                cuadro_7_3.cambio(mesa[7][3])
            if cursor1.colliderect(cuadro_7_4.rect):
                mesa[7][4]= escogido
                cuadro_7_4.cambio(mesa[7][4])
            #fila8
            if cursor1.colliderect(cuadro_8_0.rect):
                mesa[8][0]= escogido
                cuadro_8_0.cambio(mesa[8][0])
            if cursor1.colliderect(cuadro_8_1.rect):
                mesa[8][1]= escogido
                cuadro_8_1.cambio(mesa[8][1])
            if cursor1.colliderect(cuadro_8_2.rect):
                mesa[8][2]= escogido
                cuadro_8_2.cambio(mesa[8][2])
            if cursor1.colliderect(cuadro_8_3.rect):
                mesa[8][3]= escogido
                cuadro_8_3.cambio(mesa[8][3])
            if cursor1.colliderect(cuadro_8_4.rect):
                mesa[8][4]= escogido
                cuadro_8_4.cambio(mesa[8][4])
                
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
    #############################################
    #proyectiles
    if c[0].estado_get() == cuadro_o_con_water_rooks:
        estado = c[0]
        if y0 < 400:
            y0 +=1
            hilo2 = Thread(target=lanza_agua, args=(estado,x0, y0))
            hilo2.start()       
    if c[0].estado_get() == cuadro_oscuro:
        y0 = c[0].coordsy_get()
    if c[1].estado_get() == cuadro_o_con_water_rooks:
        estado = c[1]
        if y1 < 400:
            y1 +=1
            hilo2 = Thread(target=lanza_agua, args=(estado,x1, y1))
            hilo2.start()       
    if c[1].estado_get() == cuadro_oscuro:
        y1 = c[1].coordsy_get()

    
    
    #llama al cursor
    cursor1.sigue()
    #actualiza la pantalla
    pygame.display.flip()

