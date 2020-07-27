import shelve
import pygame,sys,os
from proyecto import *
#ventana de pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Battle: Avatars vs Rooks')
ventana = pygame.display.set_mode((267,440),0,32)

fuente = pygame.font.SysFont(None,50)
fuente2 = pygame.font.SysFont(None,40)
fuente3 = pygame.font.SysFont(None,30)
fuente4 = pygame.font.SysFont(None,18)
fuente5 = pygame.font.SysFont(None,26)
fuente6 = pygame.font.SysFont(None,22)

def escribir(texto, fuente, color, superficie,x,y):
    textobj = fuente.render(texto,1,color)
    textorect = textobj.get_rect()
    textorect.topleft=(x,y)
    superficie.blit(textobj,textorect)

click = False

#Definicio de la ventana incial
def menu_inicio():
    nombre_usuario = 'Tu Nombre!'

    input_rect = pygame.Rect(150, 0,185,25)
    color_activo = pygame.Color('lightskyblue3')
    color_pasivo = pygame.Color('gray15')
    color = color_pasivo

    activo = False
    
    running = True
    while running:

        ventana.fill((0,170,228))

        if activo:
            color = color_activo
        else:
            color = color_pasivo
        
        escribir('Battle:', fuente,(255,0,0),ventana,20,20)
        escribir('Avatars', fuente2,(255,255,0),ventana,20,50)
        escribir('vs', fuente2,(10,10,10),ventana,130,50)
        escribir('Rooks', fuente2,(128,64,0),ventana,170,50)
        escribir('version alpha 1.0', fuente4,(10,10,10),ventana,10,420)
        texto1 = fuente2.render("Iniciar",0,(10,10,10))
        texto2 = fuente3.render("Configuracion",0,(10,10,10))
        texto3 = fuente3.render("Salon de la fama",0,(10,10,10))
        texto4 = fuente2.render("Ayuda",0,(10,10,10))
        texto5 = fuente4.render("Creditos",0,(10,10,10))
        texto6 = fuente4.render("Salir",0,(10,10,10))

        mx,my = pygame.mouse.get_pos()

        boton1 = pygame.Rect(35, 100, 185, 50)
        boton2 = pygame.Rect(35, 170, 185, 50)
        boton3 = pygame.Rect(35, 240, 185, 50)
        boton4 = pygame.Rect(35, 310, 185, 50)
        boton5 = pygame.Rect(120, 400, 70, 30)
        boton6 = pygame.Rect(200, 400, 60, 30)
        if boton1.collidepoint((mx,my)):
            if click:
                d = shelve.open('HoF')
                d['resultados'] += [nombre_usuario]
                d.close()
                juego()
        if boton2.collidepoint((mx,my)):
            if click:
                config()
        if boton3.collidepoint((mx,my)):
            if click:
                famehall()
        if boton4.collidepoint((mx,my)):
            if click:
                ayuda()
        if boton5.collidepoint((mx,my)):
            if click:
                creditos()
        if boton6.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(ventana,(57,255,20),boton1)
        ventana.blit(texto1,(85,110))
        pygame.draw.rect(ventana,(57,255,20),boton2)
        ventana.blit(texto2,(60,184))
        pygame.draw.rect(ventana,(57,255,20),boton3)
        ventana.blit(texto3,(46,257))
        pygame.draw.rect(ventana,(57,255,20),boton4)
        ventana.blit(texto4,(85,320))
        pygame.draw.rect(ventana,(57,255,20),boton5)
        ventana.blit(texto5,(130,410))
        pygame.draw.rect(ventana,(57,255,20),boton6)
        ventana.blit(texto6,(215,410))
  
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if activo:
                    if event.key == pygame.K_BACKSPACE:
                        nombre_usuario = nombre_usuario[:-1]
                    else:
                        nombre_usuario += event.unicode
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if input_rect.collidepoint(event.pos):
                    activo = True
                else:
                    activo = False

        pygame.draw.rect(ventana,color,input_rect,2)

    
        text_surface = fuente3.render(nombre_usuario,True,(10,10,10))
        ventana.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100,text_surface.get_width() + 10)
        

        pygame.display.update()
        mainClock.tick(60)

#Definicion de la ventana del juego
def juego():
    empieza('ninguno')

#Definicion de la ventana de configuracion 
def config():
    #se obtienen datos de la biblioteca
    d = shelve.open('configuraciones')
    atkspf = str(d['VAF'])
    mvspf = str(d['VMF'])
    atkspe = str(d['VAE'])
    mvspe = str(d['VME'])
    atkspl = str(d['VAL'])
    mvspl = str(d['VML'])
    atkspc = str(d['VAC'])
    mvspc = str(d['VMC'])
    atkspr = str(d['VAR'])
    d.close()
    
    

    input_rect = pygame.Rect(5, 110,185,25)
    input_rect1 = pygame.Rect(150, 110,185,25)
    input_rect2 = pygame.Rect(5, 160,185,25)
    input_rect3 = pygame.Rect(150, 160,185,25)
    input_rect4 = pygame.Rect(5, 210,185,25)
    input_rect5 = pygame.Rect(150, 210,185,25)
    input_rect6 = pygame.Rect(5, 260,185,25)
    input_rect7 = pygame.Rect(150, 260,185,25)
    input_rect8 = pygame.Rect(75, 320,185,25)
    color_activo = pygame.Color('lightskyblue3')
    color_pasivo = pygame.Color('gray15')
    color = color_pasivo

    activo = False
    activo1 = False
    activo2 = False
    activo3 = False
    activo4 = False
    activo5 = False
    activo6 = False
    activo7 = False
    activo8 = False
    
    running = True
    while running:
        ventana.fill((0,170,228))

        if activo:
            color = color_activo
        else:
            color = color_pasivo
        if activo1:
            color1 = color_activo
        else:
            color1 = color_pasivo
        if activo2:
            color2 = color_activo
        else:
            color2 = color_pasivo
        if activo3:
            color3 = color_activo
        else:
            color3 = color_pasivo
        if activo4:
            color4 = color_activo
        else:
            color4 = color_pasivo
        if activo5:
            color5 = color_activo
        else:
            color5 = color_pasivo
        if activo6:
            color6 = color_activo
        else:
            color6 = color_pasivo
        if activo7:
            color7 = color_activo
        else:
            color7 = color_pasivo
        if activo8:
            color8 = color_activo
        else:
            color8 = color_pasivo
        
        escribir('Configuración', fuente,(128,64,0),ventana,10,10)
        escribir('VA = Velocidad de Ataque', fuente4,(10,10,10),ventana,0,50)
        escribir('VM = Velocidad de Movimiento', fuente4,(10,10,10),ventana,0,65)
        escribir('----------------------------------------------------------------------------------------------------------------------', fuente4,(10,10,10),ventana,0,80)
        escribir('VA del flechador', fuente4,(10,10,10),ventana,0,95)
        escribir('VM del flechador', fuente4,(10,10,10),ventana,145,95)
        escribir('VA del escudero', fuente4,(10,10,10),ventana,0,145)
        escribir('VM del escudero', fuente4,(10,10,10),ventana,145,145)
        escribir('VA del leñador', fuente4,(10,10,10),ventana,0,195)
        escribir('VM del leñador', fuente4,(10,10,10),ventana,145,195)
        escribir('VA del canibal', fuente4,(10,10,10),ventana,0,245)
        escribir('VM del canibal', fuente4,(10,10,10),ventana,145,245)
        escribir('VA de los rooks', fuente5,(10,10,10),ventana,65,300)
        textoat3 = fuente4.render("Atrás",0,(10,10,10))

        mx,my = pygame.mouse.get_pos()

        botonat3 = pygame.Rect(20, 400, 60, 30)
        if botonat3.collidepoint((mx,my)):
            if click:
                d = shelve.open('configuraciones')
                d['VAF'] = int(atkspf)
                d['VMF'] = int(mvspf)
                d['VAE'] = int(atkspe)
                d['VME'] = int(mvspe)
                d['VAL'] = int(atkspl)
                d['VML'] = int(mvspl)
                d['VAC'] = int(atkspc)
                d['VMC'] = int(mvspc)
                d['VAR'] = int(atkspr)
                d.close()
                running = False
        pygame.draw.rect(ventana,(57,255,20),botonat3)
        ventana.blit(textoat3,(35,410))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    #Se guardan los datos en una biblioteca generado por python
                    d = shelve.open('configuraciones')
                    d['VAF'] = int(atkspf)
                    d['VMF'] = int(mvspf)
                    d['VAE'] = int(atkspe)
                    d['VME'] = int(mvspe)
                    d['VAL'] = int(atkspl)
                    d['VML'] = int(mvspl)
                    d['VAC'] = int(atkspc)
                    d['VMC'] = int(mvspc)
                    d['VAR'] = int(atkspr)
                    d.close()
                    running = False
                if activo:
                    if event.key == pygame.K_BACKSPACE:
                        atkspf = atkspf[:-1]
                    else:
                        atkspf += event.unicode
                elif activo1:
                    if event.key == pygame.K_BACKSPACE:
                        mvspf = mvspf[:-1]
                    else:
                        mvspf += event.unicode
                elif activo2:
                    if event.key == pygame.K_BACKSPACE:
                        atkspe = atkspe[:-1]
                    else:
                        atkspe += event.unicode
                elif activo3:
                    if event.key == pygame.K_BACKSPACE:
                        mvspe = mvspe[:-1]
                    else:
                        mvspe += event.unicode
                elif activo4:
                    if event.key == pygame.K_BACKSPACE:
                        atkspl = atkspl[:-1]
                    else:
                        atkspl += event.unicode
                elif activo5:
                    if event.key == pygame.K_BACKSPACE:
                        mvspl = mvspl[:-1]
                    else:
                        mvspl += event.unicode
                elif activo6:
                    if event.key == pygame.K_BACKSPACE:
                        atkspc = atkspc[:-1]
                    else:
                        atkspc += event.unicode
                elif activo7:
                    if event.key == pygame.K_BACKSPACE:
                        mvspc = mvspc[:-1]
                    else:
                        mvspc += event.unicode
                elif activo8:
                    if event.key == pygame.K_BACKSPACE:
                        atkspr = atkspr[:-1]
                    else:
                        atkspr += event.unicode
                    
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if input_rect.collidepoint(event.pos):
                    activo = True
                elif input_rect1.collidepoint(event.pos):
                    activo1 = True
                elif input_rect2.collidepoint(event.pos):
                    activo2 = True
                elif input_rect3.collidepoint(event.pos):
                    activo3 = True
                elif input_rect4.collidepoint(event.pos):
                    activo4 = True
                elif input_rect5.collidepoint(event.pos):
                    activo5 = True
                elif input_rect6.collidepoint(event.pos):
                    activo6 = True
                elif input_rect7.collidepoint(event.pos):
                    activo7 = True
                elif input_rect8.collidepoint(event.pos):
                    activo8 = True
                else:
                    activo = False
                    activo1 = False
                    activo2 = False
                    activo3 = False
                    activo4 = False
                    activo5 = False
                    activo6 = False
                    activo7 = False
                    activo8 = False

        pygame.draw.rect(ventana,color,input_rect,2)
        pygame.draw.rect(ventana,color1,input_rect1,2)
        pygame.draw.rect(ventana,color2,input_rect2,2)
        pygame.draw.rect(ventana,color3,input_rect3,2)
        pygame.draw.rect(ventana,color4,input_rect4,2)
        pygame.draw.rect(ventana,color5,input_rect5,2)
        pygame.draw.rect(ventana,color6,input_rect6,2)
        pygame.draw.rect(ventana,color7,input_rect7,2)
        pygame.draw.rect(ventana,color8,input_rect8,2)

        text_surface = fuente3.render(atkspf,True,(10,10,10))
        ventana.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        text_surface1 = fuente3.render(mvspf,True,(10,10,10))
        ventana.blit(text_surface1,(input_rect1.x + 5, input_rect1.y + 5))
        text_surface2 = fuente3.render(atkspe,True,(10,10,10))
        ventana.blit(text_surface2,(input_rect2.x + 5, input_rect2.y + 5))
        text_surface3 = fuente3.render(mvspe,True,(10,10,10))
        ventana.blit(text_surface3,(input_rect3.x + 5, input_rect3.y + 5))
        text_surface4 = fuente3.render(atkspl,True,(10,10,10))
        ventana.blit(text_surface4,(input_rect4.x + 5, input_rect4.y + 5))
        text_surface5 = fuente3.render(mvspl,True,(10,10,10))
        ventana.blit(text_surface5,(input_rect5.x + 5, input_rect5.y + 5))
        text_surface6 = fuente3.render(atkspc,True,(10,10,10))
        ventana.blit(text_surface6,(input_rect6.x + 5, input_rect6.y + 5))
        text_surface7 = fuente3.render(mvspc,True,(10,10,10))
        ventana.blit(text_surface7,(input_rect7.x + 5, input_rect7.y + 5))
        text_surface8 = fuente3.render(atkspr,True,(10,10,10))
        ventana.blit(text_surface8,(input_rect8.x + 5, input_rect8.y + 5))

        input_rect.w = max(100,text_surface.get_width() + 10)
        input_rect1.w = max(100,text_surface1.get_width() + 10)
        input_rect2.w = max(100,text_surface2.get_width() + 10)
        input_rect3.w = max(100,text_surface2.get_width() + 10)
        input_rect4.w = max(100,text_surface4.get_width() + 10)
        input_rect5.w = max(100,text_surface5.get_width() + 10)
        input_rect6.w = max(100,text_surface6.get_width() + 10)
        input_rect7.w = max(100,text_surface7.get_width() + 10)
        input_rect8.w = max(100,text_surface8.get_width() + 10)


        pygame.display.update()
        mainClock.tick(60)

#Definicion de la ventana del salon de la fama
def famehall():
    running = True
    while running:
        ventana.fill((0,170,228))
        
        d = shelve.open('HoF')
        ganadores = d['resultados']
        d.close()
    
        escribir('Salon', fuente,(255,0,0),ventana,20,20)
        escribir('Ganadores!:', fuente3,(255,255,0),ventana,0,70)
      #  escribir(str(ganadores[0]), fuente5,(10,10,10),ventana,0,pos)
        textoat4 = fuente4.render("Atrás",0,(10,10,10))

        mx,my = pygame.mouse.get_pos()

        botonat4 = pygame.Rect(20, 400, 60, 30)

        pos=100
        while ganadores != []:
            escribir(str(ganadores[0]) + ' en ' + str(ganadores[1]) + ' segundos', fuente5,(10,10,10),ventana,0,pos)
            ganadores = ganadores[2:]
            pos+=30

            
        if botonat4.collidepoint((mx,my)):
            if click:
                running = False
        pygame.draw.rect(ventana,(57,255,20),botonat4)
        ventana.blit(textoat4,(35,410))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)

#Definicion de la ventana de ayuda
def ayuda():
    running = True
    while running:
        ventana.fill((0,170,228))
        
        escribir('Ayuda', fuente,(255,255,0),ventana,10,10)
        escribir('Idea del juego:', fuente3,(10,10,10),ventana,5,50)
        escribir('En este juego serás los rooks y deberas', fuente4,(10,10,10),ventana,5,80)
        escribir('evitar que los avatar lleguen a cruzar la', fuente4,(10,10,10),ventana,5,95)
        escribir('ultima linea, esto lo evitaras colocando torres', fuente4,(10,10,10),ventana,5,110)
        escribir('con las que te defenderas y eliminaras a todo Avatar', fuente4,(10,10,10),ventana,5,125)
        escribir('Avatar que intente entrar en tu base.', fuente4,(10,10,10),ventana,5,140)
        escribir('Pro tips:', fuente3,(10,10,10),ventana,5,180)
        escribir('+ Obtendras oro cada cierto tiempo y al', fuente4,(10,10,10),ventana,5,210)
        escribir('eliminar avatars. Recogelo!', fuente4,(10,10,10),ventana,5,225)
        escribir('+ Entre más valor tenga una torre más daño', fuente4,(10,10,10),ventana,5,240)
        escribir('infligirá.', fuente4,(10,10,10),ventana,5,255)
        escribir('+ Utiliza inteligentemente el oro, no vaya a ser', fuente4,(10,10,10),ventana,5,270)
        escribir('que se te acabe y no puedas defender un avatar.', fuente4,(10,10,10),ventana,5,285)
        escribir('un avatar.', fuente4,(10,10,10),ventana,5,300)
        escribir('+ Puedes quitar un Rook para colocar otro', fuente4,(10,10,10),ventana,5,315)
        escribir('mas fuerte', fuente4,(10,10,10),ventana,5,330)
        textoat1 = fuente4.render("Atrás",0,(10,10,10))

        mx,my = pygame.mouse.get_pos()

        botonat1 = pygame.Rect(20, 400, 60, 30)
        if botonat1.collidepoint((mx,my)):
            if click:
                running = False
        pygame.draw.rect(ventana,(57,255,20),botonat1)
        ventana.blit(textoat1,(35,410))
       
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#Definicion de la ventana de los creditos
def creditos():
    running = True
    while running:
        ventana.fill((0,170,228))
        
        escribir('Creditos', fuente,(128,64,0),ventana,10,10)
        escribir('Desarrolladores:', fuente3,(10,10,10),ventana,5,50)
        escribir('Deylan Sandoval Sánchez', fuente5,(10,10,10),ventana,5,80)
        escribir('Jose Carlos Umaña Rivera', fuente5,(10,10,10),ventana,5,100)
        escribir('Version:', fuente3,(10,10,10),ventana,5,130)
        escribir('version alpha 1.0', fuente5,(10,10,10),ventana,5,160)
        escribir('País:', fuente3,(10,10,10),ventana,5,190)
        escribir('Costa Rica', fuente5,(10,10,10),ventana,5,220)
        escribir('Institución:', fuente3,(10,10,10),ventana,5,250)
        escribir('Instituto Tecnológico de Costa Rica', fuente6,(10,10,10),ventana,5,280)
        textoat2 = fuente4.render("Atrás",0,(10,10,10))
        
        mx,my = pygame.mouse.get_pos()

        botonat2 = pygame.Rect(20, 400, 60, 30)
        if botonat2.collidepoint((mx,my)):
            if click:
                running = False
        pygame.draw.rect(ventana,(57,255,20),botonat2)
        ventana.blit(textoat2,(35,410))
       
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)

#Se llama al menu
menu_inicio()
