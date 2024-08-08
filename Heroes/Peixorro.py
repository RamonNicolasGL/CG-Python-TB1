from LibCG.LibCG import (Texture, TextureShape, Transformations)
import random
import numpy as np

class Peixorro:
    
    def __init__(self, image):
        
        self.Texture = Texture.import_texture("PeixorroFundo.png")
        self.image = image
        
        x = image.get_width() - 100  # Fixar o retângulo na lateral direita
        y = random.randint(0, image.get_height() - 30)  # Gerar y aleatoriamente
        
        self.shape = TextureShape(
                [
                    [x + 100, y     , 1, 1],
                    [x      , y     , 0, 1],
                    [x      , y + 30, 0, 0],
                    [x + 100, y + 30, 1, 0]
                ]
        )
    
    def show(self, image):
        
        Texture.scanline_with_texture(image, self.shape, self.Texture)

    def to_Left(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, -5*a, 0)
        self.shape = Transformations.apply_transformation(self.shape, matrix)

    def create_RandomPeixorro(self, image):
        
        x = image.get_width() - 100  # Fixar o retângulo na lateral direita
        y = random.randint(0, image.get_height() - 30)  # Gerar y aleatoriamente
        
        return np.array([
            [x + 100, y, 1, 1],
            [x, y, 0, 1],
            [x, y + 30, 0, 0],
            [x + 100, y + 30, 1, 0]
    ])




        
    '''def to_Right(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, 5*a, 0)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
    
    def to_Up(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, 0, 5*a)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
    
    def to_Down(self, a):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_translation(matrix, 0, -5*a)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
    
    def rotate(self, ang):
        
        matrix = Transformations.create_transformation_matrix()
        matrix = Transformations.compose_rotation(matrix, ang)
        self.shape = Transformations.apply_transformation(self.shape, matrix)
        
        
    import pygame
import random
import numpy as np

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Retângulos Aleatórios na Lateral Direita")

# Define a cor do polígono
polygon_color = (255, 0, 0)  # Vermelho

# Função para gerar um retângulo de 150x80 em uma posição aleatória na lateral direita da tela

def generate_random_rectangle(screen_width, screen_height, rect_width=150, rect_height=80):
    x = screen_width - rect_width  # Fixar o retângulo na lateral direita
    y = random.randint(0, screen_height - rect_height)  # Gerar y aleatoriamente
    return np.array([
        [x + rect_width, y, 1, 1],
        [x, y, 0, 1],
        [x, y + rect_height, 0, 0],
        [x + rect_width, y + rect_height, 1, 0]
    ])

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche o fundo com preto
    screen.fill((0, 0, 0))
    
    # Gera um retângulo aleatório e desenha na tela
    rectangle = generate_random_rectangle(screen_width, screen_height)
    pygame.draw.polygon(screen, polygon_color, rectangle[:, :2])
    
    # Atualiza a tela
    pygame.display.flip()
    pygame.time.delay(500)  # Atraso para ver o retângulo antes de desenhar o próximo

# Encerra o Pygame
pygame.quit()    
    '''