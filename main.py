import pygame

from Heroes.Penguato import Penguato

from LibCG.LibCG import (
    Window,
    Draw,
    Resources,
    Shape,
    Texture,
    TextureShape,
    Transformations
)



# Inicialize o Pygame
pygame.init()

FPS = 30
clock = pygame.time.Clock()



#Cria janela com altura e largura especificadas
pixels = Window.create_Image(500,500)



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

penguato = Penguato(pixels)

FPS = 30
clock = pygame.time.Clock()

while True:
    
    #if pygame.event.get(pygame.QUIT): break
    #pygame.event.pump()
        
    #Draw.polygon(pixels, Square, (255, 255, 255))
    transformation = Transformations.create_transformation_matrix()

    transformation = Transformations.compose_translation(transformation, 1, 3)

    penguato.shape = Transformations.apply_transformation(penguato.shape, transformation)
    
    pixels.fill((255, 255, 255))

    Texture.scanline_with_texture(pixels, penguato.shape, penguato.Texture)
    
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