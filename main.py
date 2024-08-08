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

#testes

#Draw.set_Pixel(pixels, 250, 250, 255)

#Draw.dda(pixels,270, 270, 350, 350, 255)

#Draw.dda_aa(pixels, 270, 270, 350, 350, 255)

#Draw.bresenham(pixels, 270, 270, 300, 350, 255)

#Square = TextureShape() 
#Square.insert_Point(50,50)
#Square.insert_Point(50,200)
#Square.insert_Point(200, 200)
#Square.insert_Point(200, 50)

#Cria janela com altura e largura especificadas
pixels = Window.create_Image(900,600)

# Inicialize o Pygame
pygame.init()

peixorros =[]
penguato = Penguato(pixels)
peixorro = Peixorro(pixels)

sea_blue = (51, 97, 127)
blue_pastel = (159, 174, 214)
FPS = 45
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
        penguato.to_Left(1)
        
    if keys[pygame.K_RIGHT]:
        penguato.to_Right(1)
        
    if keys[pygame.K_UP]:
        penguato.to_Up(1)
        
    if keys[pygame.K_DOWN]:
        penguato.to_Down(1)  
        
    peixorro.to_Left( 1)
    
    #if keys[pygame.K_SPACE]:
    #    Penguato.rotate(penguato, 1)
    
    if current_time - last_ShownPeixorro >= peixorro_Showtime:
        
        peixorros.append(Peixorro(pixels))
        last_ShownPeixorro = current_time
        
    pixels.fill(sea_blue)
    
    for i in range(len(peixorros)):
        peixorros[i].to_Left(1)

    # Desenha todos os polígonos armazenados na lista
    for peixorro in peixorros:
        peixorro.show(pixels)
    
    peixorro.show(pixels)
    penguato.show(pixels)           
    #Texture.scanline_with_texture(pixels, penguato.shape, penguato.Texture)
    
    pygame.display.flip()
    
    clock.tick(60)

#Draw.scanline(pixels, Square, (255, 255, 255))

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