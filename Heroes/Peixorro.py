from LibCG.LibCG import (Texture, TextureShape, Transformations)
import random
import numpy as np

class Peixorro:
    
    def __init__(self, image):
        
        self.Texture = Texture.import_texture("PeixorroFundo.png")
        self.image = image
        self.width = 100
        self.height = 30
        self.x = image.get_width() - 100  
        self.y = random.randint(0, image.get_height() - 30)  
        
        self.shape = TextureShape(
                [
                    [self.x + 100, self.y     , 1, 1],
                    [self.x      , self.y     , 0, 1],
                    [self.x      , self.y + 30, 0, 0],
                    [self.x + 100, self.y + 30, 1, 0]
                ]
        )
    
    def show(self, image):       
        Texture.scanline_with_texture(image, self.shape, self.Texture)

    def to_Left(self, a):
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, -5*a, 0)
        self.shape = Transformations.apply_transformation(self.shape, matrix)

    def is_limit(self):
        return self.shape.x_min() == 0

'''    def check_for_colision(self, penguato):
        return any(
            penguato.shape.check_collision(peixorro) for peixorro, _, _, _ in self.polygons
        )'''


