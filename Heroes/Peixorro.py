from LibCG.LibCG import (Texture, TextureShape, Transformations, Window)
import random
import numpy as np

class Peixorro:
    
    def __init__(self, image, windows, viewports):
        
        self.image = image
        self.windows = windows
        self.viewports = viewports
        
        self.width = 100
        self.height = 30
        self.x = self.image.width - 100  
        self.y = random.randint(0, self.image.height - 30)
        
        self.peixorro_texture = Texture.import_texture("PeixorroFundo.png") 
        self.shape = TextureShape(
                [
                    [self.x + 100, -(self.y)     , 1, 0],
                    [self.x      , -(self.y)     , 0, 0],
                    [self.x      , -(self.y) - 30, 0, 1],
                    [self.x + 100, -(self.y) - 30, 1, 1] 
                ]
        )
    
    def show(self):
        shape = self.image.map_window(self.shape, self.windows[0], self.viewports[0])
        self.image.scanline_with_texture(shape, self.peixorro_texture)
        
        shape = self.image.map_window(self.shape, self.windows[1], self.viewports[1])
        self.image.scanline_with_texture(shape, self.peixorro_texture)
        
    #def show(self, image):       
        #Texture.scanline_with_texture(image, self.shape, self.Texture)

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


