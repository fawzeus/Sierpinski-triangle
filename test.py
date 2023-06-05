import matplotlib.pyplot as plt
import random

# Define the three vertices of the equilateral triangle
vertices = [(0, 0), (1, 0), (0.5, 0.866)]

# Define the number of iterations
num_iterations = [10, 50, 100, 500, 750, 1000, 10000, 100000]

# Sort the num_iterations list in ascending order
num_iterations.sort()

# Create a figure with subplots to display the results
fig, axs = plt.subplots(2, 4, figsize=(12, 8))

# Iterate over each number of iterations
for i, n in enumerate(num_iterations):
    # Initialize the list of points with a random point inside the triangle
    points = [random.choice(vertices)]

    # Iterate for the specified number of iterations
    for _ in range(n):
        # Choose a random vertex
        vertex = random.choice(vertices)

        # Get the last point in the list
        last_point = points[-1]

        # Calculate the midpoint between the last point and the chosen vertex
        midpoint = ((last_point[0] + vertex[0]) / 2, (last_point[1] + vertex[1]) / 2)

        # Add the midpoint to the list of points
        points.append(midpoint)

    # Extract the x and y coordinates of the points
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    # Plot the points
    ax = axs[i // 4, i % 4]
    ax.plot(x, y, '.', markersize=1)

    # Set the aspect ratio to equal and remove the axes
    ax.set_aspect('equal')
    ax.axis('off')

    # Set the title of the subplot
    ax.set_title(f'After {n} iteration')

# Set the window title
fig.canvas.manager.set_window_title('Sierpiński Triangle')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
