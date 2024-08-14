import pygame
from pygame import gfxdraw
import math
import os
import numpy as np
from PIL import Image

class Window:
    
    def __init__(self, window_height, window_width):
        self.height = window_height
        self.width = window_width
        
        self.surface = pygame.display.set_mode((window_width, window_height))
        self.surface.fill((0, 0, 0))
    
    def get_pixel(self, x, y):
        color = self.surface.get_at((x, y))

        return (color[0], color[1], color[2], color[3])
        
    
    def set_Pixel(self, x, y, color):
        
        y = self.height - y 
    
        if x < 0:   
            x = 0   
        if y < 0:   
            y = 0   
        
        if x >= self.height: 
            x = self.width - 1  
        if y >= self.height:    
            y = self.width - 1 
        
        self.surface.set_at((x, y), color) 
        
    def create_Image(image_width, image_height):
        return pygame.display.set_mode((image_width, image_height))
        
    def show_Image(image):
        pygame.display.update()
            
    def get_pixel_with_texture(self, texture, x, y):
        
        num_rows, num_cols, _ = texture.shape

        x = max(min(x, 1), 0)
        y = max(min(y, 1), 0)

        x = int(x * (num_cols - 1))
        y = int(y * (num_rows - 1))

        color = texture[y][x]

        return (color[0], color[1], color[2])
    
    def flood_fill(self, intensity, x, y):

        initial_color = self.surface.get_at((x,y))
        
        if initial_color == intensity:
            return

        stack = [(x, y)]

        while stack:
            
            x, y = stack.pop()
            if self.surface.get_at((x,y)) != initial_color:
                continue
            
            self.surface.set_at((x, y), intensity)

            if x + 1 < self.width:
                stack.append((x + 1, y))

            if x >= 1:
                stack.append((x - 1, y))

            if y + 1 < self.height:
                stack.append((x, y + 1))
            
            if y >= 1:
                stack.append((x, y - 1))
                       
    
    def dda(self, initial_x, initial_y, final_x, final_y, color):
        
        dx = final_x - initial_x
        dy = final_y - initial_y

        if abs(dx) > abs(dy):
            
            steps = abs(dx)
        else:
            
            steps = abs(dy)

        steps_x = dx/steps
        steps_y = dy/steps

        x = initial_x
        y = initial_y

        self.set_Pixel(round(x), round(y), color)

        for _ in range(int(steps)):
            
            x = x + steps_x
            y = y + steps_y
            self.set_Pixel(round(x), round(y), color)
            
    def bresenham(self, xi, yi, xf, yf, intensity):
    
        if xf < xi:
            aux = xf
            xf = xi
            xi = aux

            aux = yf
            yf = yi
            yi = aux

        dx = abs(xf - xi)
        dy = abs(yf - yi)
        aux = 0 
        
        if dy>dx:
            aux = dx
            dx = dy
            dy = aux
            aux = 1

        y = 0
        dy2 = 2*dy
        dy2dx2 = dy2 - 2*dx
        s = Resources.sign(yf-yi)

        p = dx - dy2

        for x in range(0, dx):
            if p < 0:
                p = p - dy2dx2
                y = y + 1
            else:
                p = p - dy2

            if aux == 0:
                self.set_Pixel(xi +x, yi + s*y, intensity)
            else:
                self.set_Pixel(xi +y, yi + s*x, intensity)
                
    
    def draw_polygon(self, pol, intensity):
        
        if len(pol) < 2: 
            print ("less than two sides")
            return
    
        for i in range(0, len(pol) - 1):
           self.bresenham(pol[i][0], pol[i][1], pol[i + 1][0], pol[i + 1][1], intensity)

        self.bresenham(pol[-1][0], pol[-1][1], pol[0][0], pol[0][1], intensity)
    
    #Circunferencia implementada pelo professor (Os arredondamentos deixam ela relativamente torta)
    def circle(self, xc, yc, r, intensidade):
        c = Shape()

        for ang in np.arange(0, 2 * np.pi, 0.25):
            c.insert_Point(math.floor(xc + r*math.cos(ang)), math.floor(yc + r*math.sin(ang)))
            
        self.draw_polygon(c.points, intensidade)
    
    #Circunferencia usando bresenham
    def bresenham_circle(self, xc, yc, r, intensidade):
        x = 0
        y = r
        quadrantes = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        p = 3 - 2 * r

        while y >= x:
            x_aux, y_aux = y, x

            for x_signal, y_signal in quadrantes:
                self.set_Pixel(xc + x_signal * x, yc + y_signal * y, intensidade)
                self.set_Pixel(xc + x_signal * x_aux, yc + y_signal * y_aux, intensidade)

            x += 1

            if p > 0:
                y -= 1
                p += 4 * (x - y) + 10
            else:
                p += 4 * x + 6
    
    def map_window(self, pol, window, viewport):
        x_ini_vp = viewport[0]
        y_ini_vp = viewport[1]
        x_fin_vp = viewport[2]
        y_fin_vp = viewport[3]
        
        x_ini = window[0]
        y_ini = window[1]
        x_fin = window[2]
        y_fin = window[3]

        a = (x_fin_vp - x_ini_vp) / (x_fin - x_ini)
        b = (y_fin_vp - y_ini_vp) / (y_fin - y_ini)

        matrix = np.array(
            [
                [a, 0, x_ini_vp - a * x_ini],
                [0, b, y_fin_vp - b * y_ini],
                [0, 0,                    1],
            ]
        )

        return self.apply_transformation(pol, matrix)
    
    def intersection_with_texture(self, y, segment):
        pi = segment[0]
        pf = segment[1]

        # Horizontal segment (has no intersection)
        if pi[1] == pf[1]:
            return [-1, 0, 0, 0]

        if pi[1] > pf[1]:
            pi, pf = pf, pi

        t = (y - pi[1]) / (pf[1] - pi[1])

        if t > 0 and t <= 1:
            x = pi[0] + t * (pf[0] - pi[0])

            tx = pi[2] + t * (pf[2] - pi[2])
            ty = pi[3] + t * (pf[3] - pi[3])

            return [x, y, tx, ty]

        return [-1, 0, 0, 0]
    
    def scanline_Tex(self, shape, texture):
        y_min = shape.y_min()
        y_max = shape.y_max()

        for y in range(y_min, y_max + 1):
            intersections = []

            for p in range(len(shape.points)):
                pi = shape.points[p]
                pf = shape.points[(p + 1) % len(shape.points)]

                intersection = self.intersection_with_texture(y, [pi, pf])

                if intersection[0] >= 0:
                    intersections.append(intersection)

            intersections.sort(key=lambda intersection: intersection[0])
            
            
            for pi in range(0, len(intersections), 2):
                p1 = intersections[pi]
                p2 = intersections[pi + 1]

                x1 = p1[0]
                x2 = p2[0]

                if x1 == x2:
                    continue

                if x2 < x1:
                    p1, p2 = p2, p1

                for xk in range(int(p1[0]), int(p2[0]) + 1):
                    pc = (xk - p1[0]) / (p2[0] - p1[0])

                    tx = p1[2] + pc * (p2[2] - p1[2])
                    ty = p1[3] + pc * (p2[3] - p1[3])

                    color = self.get_pixel_with_texture(texture, tx, ty)

                    self.set_Pixel(xk, y, color)
                    
    def create_transformation_matrix(self):
        return np.identity(3)

    def translation(self, matrix, tx, ty):
        return (
            np.array(
                [
                    [1, 0, tx],
                    [0, 1, ty],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )

    def scale(self, matrix, sx, sy):
        return (
            np.array(
                [
                    [sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )

    def rotation(self, matrix, ang):
        ang = (ang * np.pi)/180

        return np.array(
            [
                [np.cos(ang), -np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]
            ]
            @ matrix
        )


    def shear(self, matrix, cx, cy):
        return (
            np.array(
                [
                    [1, cx, 0],
                    [cy, 1, 0],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )

    def apply_transformation(self, shape, matrix):
        
        points = []

        for i in range(len(shape.points)):
            
            pt = shape.points[i][:2]
            pt.append(1)
            pt = np.transpose(pt)

            transformed_pt = matrix @ pt

            transformed_pt = np.transpose(transformed_pt)
            points.append(transformed_pt[:2].tolist())

            for j in range(2, len(shape.points[i])):
                
                points[i].append(shape.points[i][j])

        if type(shape) is Shape:
            return Shape(points)
        return TextureShape(points)


#aditional resoucers methods
class Resources:
    
    def sign(number):
        if number <0:
            return -1
        elif (number == 0):
            return 0
        else:
            return 1
    
    def frange (start, stop=None, step=None):
        
        start = float(start)
        if stop == None:
            stop = start + 0.0
            start = 0.0
        if step == None:
            step = 1.0

        count = 0
        while True:
            temp = float (start + count * step)
            if step > 0 and temp >=stop:
                break
            elif step < 0 and temp <= stop:
                break
            yield temp
            count +=1


#Shapes
class Shape:
    
    def __init__(self, points=[]):
        self.points = points
    
    def insert_Point(self, x, y):
        self.points.append((x, y))
        
    def y_min(self):
        return min(int(row[1]) for row in self.points)

    def y_max(self):
        return max(int(row[1]) for row in self.points)
    
    def get_rectangle_bounds(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]

        x1 = min(x_coords)
        y1 = min(y_coords)
        x2 = max(x_coords)
        y2 = max(y_coords)

        return x1, y1, x2, y2

class TextureShape:
    
    def __init__(self, points=[]):
        self.points = points

    def insert_points(self, points):
        self.points += points
        
    def x_min(self):
        return min(int(row[0]) for row in self.points)

    def x_max(self):
        return max(int(row[0]) for row in self.points)

    def y_min(self):
        return min(int(row[1]) for row in self.points)

    def y_max(self):
        return max(int(row[1]) for row in self.points)

    def center(self):
        
        x_sum = sum(row[0] for row in self.points)
        y_sum = sum(row[1] for row in self.points)
        num_points = len(self.points)

        center_x = int(x_sum / num_points)
        center_y = int(y_sum / num_points)

        return center_x, center_y
    
    def get_bounds(self):
        x = [point[0] for point in self.points]
        y = [point[1] for point in self.points]

        x1 = min(x)
        y1 = min(y)
        x2 = max(x)
        y2 = max(y)

        return x1, y1, x2, y2
    
    def check_collision(self, shape):
        shape1_x1, shape1_y1, shape1_x2, shape1_y2 = self.get_bounds()
        shape2_x1, shape2_y1, shape2_x2, shape2_y2 = shape.get_bounds()

        return (
            shape1_x1 <= shape2_x2
            and shape1_x2 >= shape2_x1
            and shape1_y1 <= shape2_y2
            and shape1_y2 >= shape2_y1
        )
    
class Texture:
    
    def import_texture(img_name):
        cg_Tb1 = os.getcwd()
        return np.asarray(Image.open(os.path.join(cg_Tb1, "Heroes", img_name)))

