import pygame
from Heroes.Penguato import Penguato
from Heroes.Peixorro import Peixorro
import time


from LibCG.LibCG import (
    Window,
    Resources,
    Shape,
    Texture,
    TextureShape,

)
#CORES
white = (255, 255, 255)
sea_blue = (51, 97, 127)
sea_blue2 = (77, 146, 189)
red_wine = (110, 0, 0)
blue_pastel = (159, 174, 214)


pixels = Window(700, 700)
FPS = 45


def bolhas():
    pixels.bresenham_circle(55, 635, 20, white)
    pixels.bresenham_circle(70, 600, 15, white)
    pixels.bresenham_circle(52, 573, 10, white)
    pixels.bresenham_circle(74, 570, 7, white)
    pixels.bresenham_circle(67, 550, 7, white)
    
    pixels.bresenham_circle(550, 635, 24, white)
    pixels.bresenham_circle(340, 340, 30, white)
    pixels.bresenham_circle(35, 73, 13, white)
    pixels.bresenham_circle(100, 200, 9, white)
    pixels.bresenham_circle(670, 530, 7, white)
    
    pixels.bresenham_circle(43, 63, 20, white)
    pixels.bresenham_circle(230, 350, 15, white)
    pixels.bresenham_circle(27, 635, 10, white)
    pixels.bresenham_circle(74, 480, 7, white)
    pixels.bresenham_circle(451, 55, 7, white)
    
    pixels.bresenham_circle(342, 63, 20, white)
    pixels.bresenham_circle(534, 75, 15, white)
    pixels.bresenham_circle(270, 93, 10, white)
    pixels.bresenham_circle(128, 40, 35, white)
    pixels.bresenham_circle(100, 55, 21, white)
    pixels.bresenham_circle(320, 655, 25, white)
    pixels.bresenham_circle(655, 340, 25, white)

def menu(pixels):
    penguatoVSpeixorro_logo = TextureShape(
        [                    
            [100,   650, 0, 0],
            [100,   350, 0, 1],
            [600,   350, 1, 1],
            [600,   650, 1, 0],
        
        ]
    )
    penguatoVSpeixorro_tex = Texture.import_texture("Logo2.png")
    pixels.surface.fill(sea_blue2)
    
    #ENQUADRAMENTOS
    #BRESENHAM
    pixels.bresenham(20, 675, 680, 675, red_wine)
    pixels.bresenham(20, 25, 680, 25, red_wine)
    pixels.bresenham(20, 25, 20, 675, red_wine)
    pixels.bresenham(680, 25, 680, 675, red_wine)
    
    pixels.bresenham(40, 45, 40, 350, red_wine)
    pixels.bresenham(40, 45, 660, 45, red_wine)
    pixels.bresenham(660, 45, 660, 350, red_wine)
    pixels.bresenham(40, 350, 660, 350, red_wine)
    
    #FLOOD_FILL
    pixels.flood_fill(red_wine, 43, 300)
    
    #BOLHAS
    #CIRCUNFERENCIA
    pixels.bresenham_circle(55, 635, 20, white)
    pixels.bresenham_circle(70, 600, 15, white)
    pixels.bresenham_circle(52, 573, 10, white)
    pixels.bresenham_circle(74, 570, 7, white)
    pixels.bresenham_circle(67, 550, 7, white)
    
    penguatoVSpeixorro_instrucoes = TextureShape(
        [                    
            [60,   330, 0, 0],
            [60,   50, 0, 1],
            [600,   50, 1, 1],
            [600,   330, 1, 0],
        
        ]
    )
    
    penguatoVSpeixorroInstrucoes_tex = Texture.import_texture("Instruções2.png")
     
    pixels.scanline_Tex(penguatoVSpeixorro_logo, penguatoVSpeixorro_tex)
    pixels.scanline_Tex(penguatoVSpeixorro_instrucoes, penguatoVSpeixorroInstrucoes_tex)

    pygame.display.update()
    
    running = True
    while running:        
        keys = pygame.key.get_pressed() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if keys[pygame.K_p]:
                running = False

def win_screen(pixels):
    penguatoWins = TextureShape(
        [                    
            [100,   500, 0, 0],
            [100,   200, 0, 1],
            [600,   200, 1, 1],
            [600,   500, 1, 0],
        
        ]
    )
    penguatoWins_tex = Texture.import_texture("PenguatoWins.png")
    
    pixels.surface.fill(sea_blue2)
    pixels.scanline_Tex(penguatoWins, penguatoWins_tex)
    
    #ENQUADRAMENTOS
    #BRESENHAM
    pixels.bresenham(20, 675, 680, 675, red_wine)
    pixels.bresenham(20, 25, 680, 25, red_wine)
    pixels.bresenham(20, 25, 20, 675, red_wine)
    pixels.bresenham(680, 25, 680, 675, red_wine)
    
    bolhas()
    pygame.display.update()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        time.sleep(5)
        pygame.quit()
    
def lose_screen(pixels):
    penguatoLose = TextureShape(
        [                    
            [100,   500, 0, 0],
            [100,   200, 0, 1],
            [600,   200, 1, 1],
            [600,   500, 1, 0],
        
        ]
    )
    
    penguatoLose_tex = Texture.import_texture("PeixorroWin.png")
    
    pixels.surface.fill(sea_blue2)
    pixels.scanline_Tex(penguatoLose, penguatoLose_tex)
    
    #ENQUADRAMENTOS
    #BRESENHAM
    pixels.bresenham(20, 675, 680, 675, red_wine)
    pixels.bresenham(20, 25, 680, 25, red_wine)
    pixels.bresenham(20, 25, 20, 675, red_wine)
    pixels.bresenham(680, 25, 680, 675, red_wine)
    
    pixels.bresenham_ellipse(90, 620, 20, 40, white)
    
    #POLIGONO BASE
    square = Shape()
    square.insert_Point(600, 50)
    square.insert_Point(600, 100)
    square.insert_Point(650, 100)
    square.insert_Point(650, 50)
    
    pixels.draw_shape(square, white)
    
    pixels.scanline(square, white)
    
    bolhas()
    pygame.display.update()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        time.sleep(5)
        pygame.quit()
    
menu(pixels)


#JOGO 

#VIEWPORTS
window_game = [0, 0, 700, 700]
viewport_game = [0, 0, 700, 700]

viewport_mini_map = [610, 0, 700, 90]
window_mini_map = [0, 0, 700, 700]

window = [window_game, window_mini_map]
viewports = [viewport_game, viewport_mini_map]

peixorros =[]
peixorros_desviados = 0
penguato = Penguato(pixels, window, viewports)

pygame.init()
clock = pygame.time.Clock()
peixorro_Showtime = 1000
last_ShownPeixorro = 0

    
while True:
    current_time = pygame.time.get_ticks()
    if pygame.event.get(pygame.QUIT): 
        break
    pygame.event.pump()
    keys = pygame.key.get_pressed()    
    
    if keys[pygame.K_LEFT]:
        if penguato.is_notlimitLEFT():
            penguato.to_Left(1)
        
    if keys[pygame.K_RIGHT]:
        if penguato.is_notlimitRIGHT():
            penguato.to_Right(1)
        
    if keys[pygame.K_UP]:
        if penguato.is_notlimitUP():
            penguato.to_Up(1)
        
    if keys[pygame.K_DOWN]:
        if penguato.is_notlimitDOWN():
            penguato.to_Down(1)  
            
    if current_time - last_ShownPeixorro >= peixorro_Showtime and len(peixorros) < 5:
        
        peixorros.append(Peixorro(pixels, window, viewports))
        last_ShownPeixorro = current_time
    
    for i in range(len(peixorros)):
        if any(penguato.shape.check_collision(peixorro.shape) for peixorro in peixorros):
            lose_screen(pixels)   
        peixorros[i].to_Left(1)
    
    pixels.surface.fill(sea_blue)
    bolhas()
    
    #MINI MAPA
    pixels.bresenham(610, 0, 610, 90, white)
    pixels.bresenham(610, 90, 700, 90, white)
    
    for peixorro in peixorros:
        if peixorro.is_limit():
            peixorros.pop(0)
            peixorros_desviados += 1
            
            del(peixorro)
            
            if peixorros_desviados == 20:
                win_screen(pixels)
        else:
            peixorro.show()

    penguato.show()  
    pygame.display.flip()
    clock.tick(FPS)