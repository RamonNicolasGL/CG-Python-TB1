import pygame

from LibGC import (
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

Square = TextureShape(
            [
                [50,  150, 0, 0],
                [50,   50, 0, 1],
                [150,  50, 1, 1],
                [150, 150, 1, 0]
            ]
)

#Draw.polygon(pixels, Square, (255, 255, 255))

Catguin = Texture.import_texture("Catguin.jpeg")

transformation = Transformations.create_transformation_matrix()

transformation = Transformations.compose_translation(transformation, 100, 300)

Square = Transformations.apply_transformation(Square, transformation)

Texture.scanline_with_texture(pixels, Square, Catguin)

#Draw.scanline(pixels, Square, (255, 255, 255))

#Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    #Atualiza o display
    Window.show_Image(pixels)

# Encerre o Pygame
pygame.quit()