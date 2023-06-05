import matplotlib.pyplot as plt
from utils import distance, generate_random_point_inside_triangle
import math
from random import randint

sqrt32 = math.sqrt(3) / 2
N=100000
# Define the vertices of the equilateral triangle
x = [0, 1, 0.5]
y = [0, 0, sqrt32]

choice_x = [0, 1, 0.5]
choice_y = [0, 0, sqrt32]


# Generate a random point inside the triangle
x1, y1 = generate_random_point_inside_triangle()
x.append(x1)
y.append(y1)
for _ in range(N):
    index=randint(0,2)
    x1 = (choice_x[index]+x1)/2
    y1 = (choice_y[index]+y1)/2 
    x.append(x1)
    y.append(y1)


# Create a scatter plot with small points
plt.plot(x, y, marker='.', linestyle='',color ='red')
plt.gca().set_facecolor('black')

# Set labels for the x and y axes
plt.xlabel('X')
plt.ylabel('Y')

# Set the plot title
plt.title('Equilateral Triangle with Random Point')

# Display the plot
plt.show()
