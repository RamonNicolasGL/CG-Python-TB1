from LibCG.LibCG import (Texture, TextureShape)

class Penguato:
    
    def __init__(self, image):
        
        self.Texture = Texture.import_texture("Penguato.jpeg")
        self.image = image
        self.shape = TextureShape(
                [
                    [50,  150, 0, 0],
                    [50,   50, 0, 1],
                    [150,  50, 1, 1],
                    [150, 150, 1, 0]
                ]
        )

