import math
import random

def distance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)


def generate_random_point_inside_triangle():
    # Equilateral triangle vertices
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 0.5, math.sqrt(3) / 2

    # Generate random barycentric coordinates
    a = random.uniform(0, 1)
    b = random.uniform(0, 1 - a)
    c = 1 - a - b

    # Calculate the point inside the triangle using barycentric coordinates
    x = a * x1 + b * x2 + c * x3
    y = a * y1 + b * y2 + c * y3

    return x, y