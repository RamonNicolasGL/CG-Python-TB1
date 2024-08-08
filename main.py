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


#Cria janela com altura e largura especificadas
pixels = Window.create_Image(900,600)

# Inicialize o Pygame
pygame.init()

peixorros =[]
penguato = Penguato(pixels)

sea_blue = (51, 97, 127)
blue_pastel = (159, 174, 214)
FPS = 45
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
        penguato.to_Left(1)
        
    if keys[pygame.K_RIGHT]:
        penguato.to_Right(1)
        
    if keys[pygame.K_UP]:
        penguato.to_Up(1)
        
    if keys[pygame.K_DOWN]:
        penguato.to_Down(1)  
    
    #if keys[pygame.K_SPACE]:
    #    Penguato.rotate(penguato, 1)
    
    if current_time - last_ShownPeixorro >= peixorro_Showtime:
        
        peixorros.append(Peixorro(pixels))
        last_ShownPeixorro = current_time
        
    pixels.fill(sea_blue)
    
    for i in range(len(peixorros)):
        if any(penguato.shape.check_collision(peixorro.shape) for peixorro in peixorros):
            break    
        peixorros[i].to_Left(1)
    
    # Desenha todos os polígonos armazenados na lista
    #remove os que possuem limite menor
    for peixorro in peixorros:
        if peixorro.is_limit():
            peixorros.pop(0)
            del(peixorro)
        else:
            peixorro.show(pixels)

    penguato.show(pixels)           
    
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