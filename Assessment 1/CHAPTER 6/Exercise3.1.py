import matplotlib.pyplot as plt

# Define the coordinates
x_values = [1, 6]  # X-coordinates: 1 and 6
y_values = [2, 8]  # Y-coordinates: 2 and 8

# Plot the line
plt.plot(x_values, y_values)

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line from (1, 2) to (6, 8)')

# Show the plot
plt.show()