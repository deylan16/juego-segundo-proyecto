import pygame,sys 
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
    while True:

        ventana.fill((0,170,228))
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
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#Definicion de la ventana del juego
def juego():
    empieza('ninguno')

#Definicion de la ventana de configuracion 
def config():
    running = True
    while running:
        ventana.fill((0,0,0))
        
        escribir('configuracion', fuente,(255,0,0),ventana,20,20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False


        pygame.display.update()
        mainClock.tick(60)

#Definicion de la ventana del salon de la fama
def famehall():
    running = True
    while running:
        ventana.fill((0,0,0))
        
        escribir('Salon', fuente,(255,0,0),ventana,20,20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False


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
        escribir(' que se te acabe y no puedas defender un avatar.', fuente4,(10,10,10),ventana,5,285)
        escribir('un avatar.', fuente4,(10,10,10),ventana,5,300)
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
