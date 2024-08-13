#viewports

import pygame
from Heroes.Penguato import Penguato
from Heroes.Peixorro import Peixorro


from LibCG.LibCG import (
    Window,
    Draw,
    Resources,
    Shape,
    Texture,
    TextureShape,
    Transformations
)
sea_blue = (51, 97, 127)
sea_blue2 = (77, 146, 189)
blue_pastel = (159, 174, 214)
FPS = 45




pixels = Window(700, 700)

def menu(pixels):
    penguatoVSpeixorro_logo = TextureShape(
        [                    
            [150,   650, 0, 0],
            [150,   400, 0, 1],
            [550,   400, 1, 1],
            [550,   650, 1, 0],
        
        ]
    )
    
    penguatoVSpeixorro_tex = Texture.import_texture("Logo.png")
    
    
    
    running = True

    while running:
        
        
        pygame.display.update()
        
        pixels.surface.fill(sea_blue2)
        
        pixels.scanline_with_texture(penguatoVSpeixorro_logo, penguatoVSpeixorro_tex)
        
        keys = pygame.key.get_pressed() 
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if keys[pygame.K_p]:
                running = False

    
    
    
menu(pixels)
# Inicialize o Pygame
window_game = [0, 0, 700, 700]
viewport_game = [0, 0, 700, 700]

viewport_mini_map = [610, 0, 700, 90]
window_mini_map = [0, 0, 700, 700]

'''window_game = [0, 0, 500, 550]
viewport_game = [0, 0, 500, 550]

viewport_mini_map = [450, 0, 500, 55]
window_mini_map = [0, 0, 150, 250]'''

'''window_game = [0, 0, 900, 600]
viewport_game = [0, 0, 900, 600]

viewport_mini_map = [600, 0, 900, 300]
window_mini_map = [0, 0, 900, 600]'''

window = [window_game, window_mini_map]
viewports = [viewport_game, viewport_mini_map]


pygame.init()


peixorros =[]
penguato = Penguato(pixels, window, viewports)
clock = pygame.time.Clock()
peixorro_Showtime = 2000
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
            print(penguato.shape.x_min())
            #print(penguato.shape.y_max())
            print(penguato.shape.y_min())
        
    if keys[pygame.K_RIGHT]:
        if penguato.is_notlimitRIGHT():
            penguato.to_Right(1)
            print(penguato.shape.x_min())
            #print(penguato.shape.y_max())
            print(penguato.shape.y_min())
        
    if keys[pygame.K_UP]:
        if penguato.is_notlimitUP():
            penguato.to_Up(1)
            print(penguato.shape.x_min())
            #print(penguato.shape.y_max())
            print(penguato.shape.y_min())
        
    if keys[pygame.K_DOWN]:
        if penguato.is_notlimitDOWN():
            penguato.to_Down(1)  
            print(penguato.shape.x_min())
            #print(penguato.shape.y_max())
            print(penguato.shape.y_min())

    #if keys[pygame.K_SPACE]:
    #    Penguato.rotate(penguato, 1)
    
    if current_time - last_ShownPeixorro >= peixorro_Showtime and len(peixorros) < 5:
        
        peixorros.append(Peixorro(pixels, window, viewports))
        last_ShownPeixorro = current_time
        
    #pixels.fill(sea_blue)
    
    for i in range(len(peixorros)):
        if any(penguato.shape.check_collision(peixorro.shape) for peixorro in peixorros):
            #aqui
            break    
        peixorros[i].to_Left(1)
    pixels.surface.fill(sea_blue)
    
    # Desenha todos os polígonos armazenados na lista
    #remove os que possuem limite menor
    for peixorro in peixorros:
        if peixorro.is_limit():
            peixorros.pop(0)
            del(peixorro)
        else:
            peixorro.show()

    penguato.show()  
        
    
    pygame.display.flip()
    
    clock.tick(FPS)

#Loop principal
'''executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    #Atualiza o display
    Window.show_Image(pixels)

# Encerre o Pygame
pygame.quit()'''