from LibCG.LibCG import (Texture, TextureShape, Transformations)

class Penguato:
    
    def __init__(self, image):
        
        self.Texture = Texture.import_texture("PenguatoFundo.png")
        self.image = image
        self.shape = TextureShape(
                [
                    [150, 230, 0, 0],
                    [150, 150, 0, 1],
                    [180, 150, 1, 1],
                    [180, 230, 1, 0]
                ]
        )
        
    def show(self, image):
        
        Texture.scanline_with_texture(image, self.shape, self.Texture)
        
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