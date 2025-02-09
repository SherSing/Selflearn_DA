import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(100)
y = np.random.rand(100)

# Create a scatter plot
plt.scatter(x, y, c='blue')

# Add a regression line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")

# Label a single point with a yellow line
plt.annotate('Point of Interest', xy=(x[50], y[50]), xytext=(x[50], y[50]+0.1), 
             arrowprops=dict(facecolor='yellow', shrink=0.05),
             horizontalalignment='center', verticalalignment='bottom')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression Graph')

# Show the plot
plt.show()