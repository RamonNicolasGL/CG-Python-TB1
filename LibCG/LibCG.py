import pygame
import math
import os
import numpy as np
from PIL import Image

#image related methods
class Window:

    def create_Image(image_width, image_height):
        return pygame.display.set_mode((image_width, image_height))
    
    
    def show_Image(image):
        pygame.display.update()
        
    
    def get_pixel_with_texture(texture, x, y):
        
        num_rows, num_cols, _ = texture.shape

        x = max(min(x, 1), 0)
        y = max(min(y, 1), 0)

        x = int(x * (num_cols - 1))
        y = int(y * (num_rows - 1))

        color = texture[y][x]

        return (color[0], color[1], color[2])


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
        
        

#Drawing related methods
class Draw:

    def set_Pixel(image, x, y, color):
        
        y = image.get_height() - y 
    
        if x < 0:   
            x = 0   
        if y < 0:   
            y = 0   
        
        if x >= image.get_width(): 
            x = image.get_width() - 1  
        if y >= image.get_height():    
            y = image.get_height() - 1 
        
        image.set_at((x, y), color)     
    
        
    def dda(image, initial_x, initial_y, final_x, final_y, color):
        
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

        Draw.set_Pixel(image, round(x), round(y), color)

        for _ in range(int(steps)):
            
            x = x + steps_x
            y = y + steps_y
            Draw.set_Pixel(image, round(x), round(y), color) 
    
    
    #dont work (TypeError: 'int' object is not iterable)
    def dda_aa(image, xi, yi, xf, yf, intensity):
        
        dx = xf-xi
        dy = yf-yi
        
        if (abs(dx) > abs(dy)):
            passos = abs(dx)
        else:
            passos = abs(dy)

        passo_x = dx/passos
        passo_y = dy/passos

        x = xi
        y = yi

        intensity = tuple(intensity)
        Draw.set_Pixel(image, x, y, intensity)
        
        for p in range (0, passos):
            
            x = x + passo_x
            y = y + passo_y
            if passo_x == 1:
                
                proporcao = abs(y - math.floor(y))
                color = [round((1-proporcao)*intensity[0]), round((1-proporcao)*intensity[1]), round((1-proporcao)*intensity[2])]
                color_tuple = tuple(color)
                Draw.set_Pixel(image, math.floor(x), math.floor(y), color_tuple)
                color2 = [round((proporcao)*intensity[0]), round((proporcao)*intensity[1]), round((proporcao)*intensity[2])]
                color_tuple2 = tuple(color2)

                Draw.set_Pixel(image, math.floor(x), math.floor(y + Resources.sign(passo_y)), color_tuple2)
                
            else:
                
                proporcao = abs(x - math.floor(x))
                color = [round((1-proporcao)*intensity[0]), round((1-proporcao)*intensity[1]), round((1-proporcao)*intensity[2])]
                color_tuple = tuple(color)
                Draw.set_Pixel(image, math.floor(x), math.floor(y), color_tuple)
                color2 = [round((proporcao)*intensity[0]), round((proporcao)*intensity[1]), round((proporcao)*intensity[2])]
                color_tuple2 = tuple(color2)

                Draw.set_Pixel(image, math.floor(x + Resources.sign(passo_x)), math.floor(y), color_tuple2)
                
    def bresenham(pixels, xi, yi, xf, yf, intensity):
    
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

        p = dx -dy2

        for x in range(0, dx):
            if p < 0:
                p = p - dy2dx2
                y = y + 1
            else:
                p = p - dy2

            if aux == 0:
                Draw.set_Pixel(pixels, xi +x, yi + s*y, intensity)
            else:
                Draw.set_Pixel(pixels, xi +y, yi + s*x, intensity)
                
                
    def polygon(pixels, pol, intensity):
        
        if len(pol.points) < 2: 
            print ("less than two sides")
            return
    
        for i in range(0, len(pol.points) - 1):
           Draw.bresenham(pixels, pol.points[i][0], pol.points[i][1], pol.points[i + 1][0], pol.points[i + 1][1], intensity)

        Draw.bresenham(pixels, pol.points[-1][0], pol.points[-1][1], pol.points[0][0], pol.points[0][1], intensity)
        
        
    def circle(pixels, xc, yc, r, intensidade):
        c = []

        for ang in Resources.frange(0, 2*math.pi, 0.025):
            Shape.insert_Point(c, math.floor(xc + r*math.cos(ang)), math.floor(yc + r*math.sin(ang)))
        Shape.polygono(pixels, c, intensidade)


    def intersecao(y, pi, pf):

        if pi[1] == pf[1]:
            return -1
            
        if pi[1] > pf[1]:
            aux = pi
            pi = pf
            pf = aux
            
        t = (y - pi[1])/(pf[1] - pi[1])
        
        if (t <= 0) or (t > 1) :
            return -1
            
        x = pi[0] + t*(pf[0] - pi[0])

        return (x,y)


    
    def print_scan(screen, p_int, intensidade):
    
        p_int = sorted(p_int, key=lambda x: x[0])

        y = p_int[0][1]
        
        for i in range(0, len(p_int) - 1, 2):
                x1 = p_int[i][0]
                x2 = p_int[i + 1][0]  
                
                for x in range(round(x1), round(x2) + 1):  
                    Draw.set_Pixel(screen, round(x), y, intensidade)


    ##
    def scanline(screen, pol, intensidade):

        #y min e max
        y_min = min(p[1] for p in pol.points)
        y_max = max(p[1] for p in pol.points)

        for y in range(y_min, y_max + 1):

            p_int = []

            pi = pol.points[0]

            for p in pol.points[1:]:
                pf = p
                
                intersec = Draw.intersecao(y, pi, pf)

                if intersec != -1:

                    p_int.append(intersec)

                pi = pf

            aux = pol.points[0]

            intersec = Draw.intersecao(y, pi, aux)
            if intersec != -1:

                p_int.append(intersec)

            if len(p_int) != 0:
                Draw.print_scan(screen, p_int, intensidade)

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

class TextureShape:
    
    def __init__(self, points=[]):
        self.points = points

    def insert_points(self, points):
        self.points += points

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
    
#Texture
class Texture:
    
    def import_texture(img_name):
        cg_Tb1 = os.getcwd()
        return np.asarray(Image.open(os.path.join(cg_Tb1, "Heroes", img_name)))
    

    def scanline_with_texture(screen, polygon, texture):
        y_min = polygon.y_min()
        y_max = polygon.y_max()

        for y in range(y_min, y_max + 1):
            intersections = []

            for p in range(len(polygon.points)):
                pi = polygon.points[p]
                pf = polygon.points[(p + 1) % len(polygon.points)]

                intersection = Texture.__intersection_with_texture(y, [pi, pf])

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

                    color = Window.get_pixel_with_texture(texture, tx, ty)

                    Draw.set_Pixel(screen, xk, y, color)
                    

    def __intersection_with_texture(y, segment):
        pi = segment[0]
        pf = segment[1]

        # Horizontal segment (has no intersection)
        if pi[1] == pf[1]:
            return [-1, 0, 0, 0]

        # Secure starting point on top
        if pi[1] > pf[1]:
            pi, pf = pf, pi

        t = (y - pi[1]) / (pf[1] - pi[1])

        if t > 0 and t <= 1:
            x = pi[0] + t * (pf[0] - pi[0])

            tx = pi[2] + t * (pf[2] - pi[2])
            ty = pi[3] + t * (pf[3] - pi[3])

            return [x, y, tx, ty]

        return [-1, 0, 0, 0]


class Transformations:
    
    def create_transformation_matrix():
        return np.identity(3)

    def compose_translation(matrix, tx, ty):
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

    def compose_scale(matrix, sx, sy):
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

    def compose_rotation(matrix, ang):
        ang = (ang * np.pi)/180

        return np.array(
            [
                [np.cos(ang), -np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]
            ]
            @ matrix
        )

    #bugando
    def compose_mirroring(matrix):
        return (
            np.array(
                [
                    [-1, 0, 0],
                    [0, -1, 0],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )

    def compose_shear(matrix, cx, cy):
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

    def apply_transformation(polygon, matrix):
        
        points = []

        for i in range(len(polygon.points)):
            
            pt = polygon.points[i][:2]
            pt.append(1)
            pt = np.transpose(pt)

            transformed_pt = matrix @ pt

            transformed_pt = np.transpose(transformed_pt)
            points.append(transformed_pt[:2].tolist())

            for j in range(2, len(polygon.points[i])):
                
                points[i].append(polygon.points[i][j])

        if type(polygon) is Shape:
            return Shape(points)
        return TextureShape(points)