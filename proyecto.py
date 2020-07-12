import pygame
from pygame.locals import *
import sys
from time import *
from threading import Thread
from rooks import *
from cursor import *
from cuadros import *


def empieza():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    ventana = pygame.display.set_mode((267,440))
    pygame.display.set_caption("juego")



    #########################################################################################################################################################################
    cuenta_0_0 = 0                 
    cuenta_0_1 = 0
    cuenta_0_2 = 0
    cuenta_0_3 = 0
    cuenta_0_4 = 0
    cuenta_1_0 = 0                 
    cuenta_1_1 = 0
    cuenta_1_2 = 0
    cuenta_1_3 = 0
    cuenta_1_4 = 0
    cuenta_2_0 = 0                 
    cuenta_2_1 = 0
    cuenta_2_2 = 0
    cuenta_2_3 = 0
    cuenta_2_4 = 0
    cuenta_3_0 = 0                 
    cuenta_3_1 = 0
    cuenta_3_2 = 0
    cuenta_3_3 = 0
    cuenta_3_4 = 0

    ##########################################################################################################################################################################   
    # el bucle principal del juego
    hola = True
    while hola:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            #cierra el programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        hola = False
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

    
         #########################################
        #cambia el estado de la matriz principal
        if event.type == pygame.MOUSEBUTTONDOWN:
            #fila0
            if cursor1.colliderect(cuadro_0_0.rect):
                    cambio_mesa(0,0,escogido)
            if cursor1.colliderect(cuadro_0_1.rect):
                    cambio_mesa(0,1,escogido)
            if cursor1.colliderect(cuadro_0_2.rect):
                    cambio_mesa(0,2,escogido)
            if cursor1.colliderect(cuadro_0_3.rect):
                    cambio_mesa(0,3,escogido)
            if cursor1.colliderect(cuadro_0_4.rect):
                    cambio_mesa(0,4,escogido)
            #fila1
            if cursor1.colliderect(cuadro_1_0.rect):
                    cambio_mesa(1,0,escogido)
            if cursor1.colliderect(cuadro_1_1.rect):
                    cambio_mesa(1,1,escogido)
            if cursor1.colliderect(cuadro_1_2.rect):
                    cambio_mesa(1,2,escogido)
            if cursor1.colliderect(cuadro_1_3.rect):
                    cambio_mesa(1,3,escogido)
            if cursor1.colliderect(cuadro_1_4.rect):
                    cambio_mesa(1,4,escogido)
            #fila2
            if cursor1.colliderect(cuadro_2_0.rect):
                    cambio_mesa(2,0,escogido)
            if cursor1.colliderect(cuadro_2_1.rect):
                    cambio_mesa(2,1,escogido)
            if cursor1.colliderect(cuadro_2_2.rect):
                    cambio_mesa(2,2,escogido)
            if cursor1.colliderect(cuadro_2_3.rect):
                    cambio_mesa(2,3,escogido)
            if cursor1.colliderect(cuadro_2_4.rect):
                    cambio_mesa(2,4,escogido)
            #fila3
            if cursor1.colliderect(cuadro_3_0.rect):
                    cambio_mesa(3,0,escogido)
            if cursor1.colliderect(cuadro_3_1.rect):
                    cambio_mesa(3,1,escogido)
            if cursor1.colliderect(cuadro_3_2.rect):
                    cambio_mesa(3,2,escogido)
            if cursor1.colliderect(cuadro_3_3.rect):
                    cambio_mesa(3,3,escogido)
            if cursor1.colliderect(cuadro_3_4.rect):
                    cambio_mesa(3,4,escogido)
            #fila4
            if cursor1.colliderect(cuadro_4_0.rect):
                    cambio_mesa(4,0,escogido)
            if cursor1.colliderect(cuadro_4_1.rect):
                    cambio_mesa(4,1,escogido)
            if cursor1.colliderect(cuadro_4_2.rect):
                    cambio_mesa(4,2,escogido)
            if cursor1.colliderect(cuadro_4_3.rect):
                    cambio_mesa(4,3,escogido)
            if cursor1.colliderect(cuadro_4_4.rect):
                    cambio_mesa(4,4,escogido)
            #fila5
            if cursor1.colliderect(cuadro_5_0.rect):
                    cambio_mesa(5,0,escogido)
            if cursor1.colliderect(cuadro_5_1.rect):
                    cambio_mesa(5,1,escogido)
            if cursor1.colliderect(cuadro_5_2.rect):
                    cambio_mesa(5,2,escogido)
            if cursor1.colliderect(cuadro_5_3.rect):
                    cambio_mesa(5,3,escogido)
            if cursor1.colliderect(cuadro_5_4.rect):
                    cambio_mesa(5,4,escogido)
            #fila6
            if cursor1.colliderect(cuadro_6_0.rect):
                    cambio_mesa(6,0,escogido)
            if cursor1.colliderect(cuadro_6_1.rect):
                    cambio_mesa(6,1,escogido)
            if cursor1.colliderect(cuadro_6_2.rect):
                    cambio_mesa(6,2,escogido)
            if cursor1.colliderect(cuadro_6_3.rect):
                    cambio_mesa(6,3,escogido)
            if cursor1.colliderect(cuadro_6_4.rect):
                    cambio_mesa(6,4,escogido)
            #fila7
            if cursor1.colliderect(cuadro_7_0.rect):
                    cambio_mesa(7,0,escogido)
            if cursor1.colliderect(cuadro_7_1.rect):
                    cambio_mesa(7,1,escogido)
            if cursor1.colliderect(cuadro_7_2.rect):
                    cambio_mesa(7,2,escogido)
            if cursor1.colliderect(cuadro_7_3.rect):
                    cambio_mesa(7,3,escogido)
            if cursor1.colliderect(cuadro_7_4.rect):
                    cambio_mesa(7,4,escogido)
            #fila8
            if cursor1.colliderect(cuadro_8_0.rect):
                    cambio_mesa(8,0,escogido)
            if cursor1.colliderect(cuadro_8_1.rect):
                    cambio_mesa(8,1,escogido)
            if cursor1.colliderect(cuadro_8_2.rect):
                    cambio_mesa(8,2,escogido)
            if cursor1.colliderect(cuadro_8_3.rect):
                    cambio_mesa(8,3,escogido)
            if cursor1.colliderect(cuadro_8_4.rect):
                    cambio_mesa(8,4,escogido)


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
       
        #verifica la matriz principal y pone los roocks
        ########################################
        #fila0
        #rook_0_0    
        if mesa[0][0] != cuadro_oscuro and cuenta_0_0 == 0:
            pone_rooks_0_0()
            cuenta_0_0 = 1
            rook_0_0.cambio(cuadro_0_0.coordsx_get(),cuadro_0_0.coordsy_get(),mesa[0][0])
        if mesa[0][0] == cuadro_oscuro:
            cuenta_0_0 = 0
            rook_0_0.cambio(-200,-200,mesa[0][0])
        #rook_0_1
        if mesa[0][1] != cuadro_oscuro and cuenta_0_1 == 0:
            pone_rooks_0_1()
            cuenta_0_1 = 1
            rook_0_1.cambio(cuadro_0_1.coordsx_get(),cuadro_0_1.coordsy_get(),mesa[0][1])
        if mesa[0][1] == cuadro_oscuro:
            cuenta_0_1 = 0
            rook_0_1.cambio(-200,-200,mesa[0][1])
        #rook_0_2    
        if mesa[0][2] != cuadro_oscuro and cuenta_0_2 == 0:
            pone_rooks_0_2()
            cuenta_0_2 = 1
            rook_0_2.cambio(cuadro_0_2.coordsx_get(),cuadro_0_2.coordsy_get(),mesa[0][2])
        if mesa[0][2] == cuadro_oscuro:
            cuenta_0_2 = 0
            rook_0_2.cambio(-200,-200,mesa[0][2])
        #rook_0_3
        if mesa[0][3] != cuadro_oscuro and cuenta_0_3 == 0:
            pone_rooks_0_3()
            cuenta_0_3 = 1
            rook_0_3.cambio(cuadro_0_3.coordsx_get(),cuadro_0_3.coordsy_get(),mesa[0][3])
        if mesa[0][3] == cuadro_oscuro:
            cuenta_0_3 = 0
            rook_0_3.cambio(-200,-200,mesa[0][3])
        #rook_0_4
        if mesa[0][4] != cuadro_oscuro and cuenta_0_4 == 0:
            pone_rooks_0_4()
            cuenta_0_4 = 1
            rook_0_4.cambio(cuadro_0_4.coordsx_get(),cuadro_0_4.coordsy_get(),mesa[0][4])
        if mesa[0][4] == cuadro_oscuro:
            cuenta_0_4 = 0
            rook_0_4.cambio(-200,-200,mesa[0][4])
        ########################################
        #fila1
        #rook_1_0    
        if mesa[1][0] != cuadro_oscuro and cuenta_1_0 == 0:
            pone_rooks_1_0()
            cuenta_1_0 = 1
            rook_1_0.cambio(cuadro_1_0.coordsx_get(),cuadro_1_0.coordsy_get(),mesa[1][0])
        if mesa[1][0] == cuadro_oscuro:
            cuenta_1_0 = 0
            rook_1_0.cambio(-200,-200,mesa[1][0])
        #rook_1_1
        if mesa[1][1] != cuadro_oscuro and cuenta_1_1 == 0:
            pone_rooks_1_1()
            cuenta_1_1 = 1
            rook_1_1.cambio(cuadro_1_1.coordsx_get(),cuadro_1_1.coordsy_get(),mesa[1][1])
        if mesa[1][1] == cuadro_oscuro:
            cuenta_1_1 = 0
            rook_1_1.cambio(-200,-200,mesa[1][1])
        #rook_1_2    
        if mesa[1][2] != cuadro_oscuro and cuenta_1_2 == 0:
            pone_rooks_1_2()
            cuenta_1_2 = 1
            rook_1_2.cambio(cuadro_1_2.coordsx_get(),cuadro_1_2.coordsy_get(),mesa[1][2])
        if mesa[1][2] == cuadro_oscuro:
            cuenta_1_2 = 0
            rook_1_2.cambio(-200,-200,mesa[1][2])
        #rook_1_3    
        if mesa[1][3] != cuadro_oscuro and cuenta_1_3 == 0:
            pone_rooks_1_3()
            cuenta_1_3 = 1
            rook_1_3.cambio(cuadro_1_3.coordsx_get(),cuadro_1_3.coordsy_get(),mesa[1][3])
        if mesa[1][3] == cuadro_oscuro:
            cuenta_1_3 = 0
            rook_1_3.cambio(-200,-200,mesa[1][3])

        #rook_1_4
        if mesa[1][4] != cuadro_oscuro and cuenta_1_4 == 0:
            pone_rooks_1_4()
            cuenta_1_4 = 1
            rook_1_4.cambio(cuadro_1_4.coordsx_get(),cuadro_1_4.coordsy_get(),mesa[1][4])
        if mesa[1][4] == cuadro_oscuro:
            cuenta_1_4 = 0
            rook_1_4.cambio(-200,-200,mesa[1][4])
        ########################################    
        #fila0
        #rook_2_0    
        if mesa[2][0] != cuadro_oscuro and cuenta_2_0 == 0:
            pone_rooks_2_0()
            cuenta_2_0 = 1
            rook_2_0.cambio(cuadro_2_0.coordsx_get(),cuadro_2_0.coordsy_get(),mesa[2][0])
        if mesa[2][0] == cuadro_oscuro:
            cuenta_2_0 = 0
            rook_2_0.cambio(-200,-200,mesa[2][0])
        #rook_2_1
        if mesa[2][1] != cuadro_oscuro and cuenta_2_1 == 0:
            pone_rooks_2_1()
            cuenta_2_1 = 1
            rook_2_1.cambio(cuadro_2_1.coordsx_get(),cuadro_2_1.coordsy_get(),mesa[2][1])
        if mesa[2][1] == cuadro_oscuro:
            cuenta_2_1 = 0
            rook_2_1.cambio(-200,-200,mesa[2][1])
        #rook_2_2    
        if mesa[2][2] != cuadro_oscuro and cuenta_2_2 == 0:
            pone_rooks_2_2()
            cuenta_2_2 = 1
            rook_2_2.cambio(cuadro_2_2.coordsx_get(),cuadro_2_2.coordsy_get(),mesa[2][2])
        if mesa[2][2] == cuadro_oscuro:
            cuenta_2_2 = 0
            rook_2_2.cambio(-200,-200,mesa[2][2])
        #rook_2_3
        if mesa[2][3] != cuadro_oscuro and cuenta_2_3 == 0:
            pone_rooks_2_3()
            cuenta_2_3 = 1
            rook_2_3.cambio(cuadro_2_3.coordsx_get(),cuadro_2_3.coordsy_get(),mesa[2][3])
        if mesa[2][3] == cuadro_oscuro:
            cuenta_2_3 = 0
            rook_2_3.cambio(-200,-200,mesa[2][3])
        #rook_2_4
        if mesa[2][4] != cuadro_oscuro and cuenta_2_4 == 0:
            pone_rooks_2_4()
            cuenta_2_4 = 1
            rook_2_4.cambio(cuadro_2_4.coordsx_get(),cuadro_2_4.coordsy_get(),mesa[2][4])
        if mesa[2][4] == cuadro_oscuro:
            cuenta_2_4 = 0
            rook_2_4.cambio(-200,-200,mesa[2][4])
        ########################################
        #fila1
        #rook_3_0    
        if mesa[3][0] != cuadro_oscuro and cuenta_3_0 == 0:
            pone_rooks_3_0()
            cuenta_3_0 = 1
            rook_3_0.cambio(cuadro_3_0.coordsx_get(),cuadro_3_0.coordsy_get(),mesa[3][0])
        if mesa[3][0] == cuadro_oscuro:
            cuenta_3_0 = 0
            rook_3_0.cambio(-200,-200,mesa[3][0])
        #rook_3_1
        if mesa[3][1] != cuadro_oscuro and cuenta_3_1 == 0:
            pone_rooks_3_1()
            cuenta_3_1 = 1
            rook_3_1.cambio(cuadro_3_1.coordsx_get(),cuadro_3_1.coordsy_get(),mesa[3][1])
        if mesa[3][1] == cuadro_oscuro:
            cuenta_3_1 = 0
            rook_3_1.cambio(-200,-200,mesa[3][1])
        #rook_3_2    
        if mesa[3][2] != cuadro_oscuro and cuenta_3_2 == 0:
            pone_rooks_3_2()
            cuenta_3_2 = 1
            rook_3_2.cambio(cuadro_3_2.coordsx_get(),cuadro_3_2.coordsy_get(),mesa[3][2])
        if mesa[3][2] == cuadro_oscuro:
            cuenta_3_2 = 0
            rook_3_2.cambio(-200,-200,mesa[3][2])
        #rook_3_3    
        if mesa[3][3] != cuadro_oscuro and cuenta_3_3 == 0:
            pone_rooks_3_3()
            cuenta_3_3 = 1
            rook_3_3.cambio(cuadro_3_3.coordsx_get(),cuadro_3_3.coordsy_get(),mesa[3][3])
        if mesa[3][3] == cuadro_oscuro:
            cuenta_3_3 = 0
            rook_3_3.cambio(-200,-200,mesa[3][3])

        #rook_3_4
        if mesa[3][4] != cuadro_oscuro and cuenta_3_4 == 0:
            pone_rooks_3_4()
            cuenta_3_4 = 1
            rook_3_4.cambio(cuadro_3_4.coordsx_get(),cuadro_3_4.coordsy_get(),mesa[3][4])
        if mesa[3][4] == cuadro_oscuro:
            cuenta_3_4 = 0
            rook_3_4.cambio(-200,-200,mesa[3][4])
        #############################################################
        #proyectiles
        for a in rooks_puestos:
            if len(a.lista_disparo)>0:
                for ele in a.lista_disparo:
                        ele.direccion() 
                        ele.disparo(ventana)

                        if ele.rect.top > 400:
                            a.lista_disparo.remove(ele)

        
        
        #llama al cursor
        cursor1.sigue()
        #actualiza la pantalla
        pygame.display.flip()

empieza()
