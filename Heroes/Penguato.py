from LibCG.LibCG import (Texture, TextureShape, Transformations, Window)

class Penguato:
    
    def __init__(self, image, windows, viewports):
        
        self.image = image
        self.windows = windows
        self.viewports = viewports
        
        self.penguato_texture = Texture.import_texture("PenguatoFundo.png")
        
        self.shape = TextureShape(
                [
                    [150, -230, 0, 1],
                    [150, -150, 0, 0],
                    [180, -150, 1, 0],
                    [180, -230, 1, 1]
                ]
        )
        
    def show(self):
        shape = self.image.map_window(self.shape, self.windows[0], self.viewports[0])
        self.image.scanline_with_texture(shape, self.penguato_texture)
        
        shape = self.image.map_window(self.shape, self.windows[1], self.viewports[1])
        self.image.scanline_with_texture(shape, self.penguato_texture)
    
    def is_notlimitLEFT(self):
        return self.shape.x_min() != 0
    
    def is_notlimitRIGHT(self):
        return self.shape.x_max() < 700
    
    def is_notlimitUP(self):
        return self.shape.y_max() < 0 
    
    def is_notlimitDOWN(self):
        return self.shape.y_min() > -700
    
    def to_Left(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, -10*a, 0)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
        
    def to_Right(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, 10*a, 0)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
    
    def to_Up(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, 0, 10*a)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
    
    def to_Down(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, 0, -10*a)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
    
    def rotate(self, ang):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_rotation(matrix, ang)
        self.shape = Transformations.apply_transformation(self.shape, matrix)