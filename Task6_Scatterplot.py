##A scatter plot is a diagram where each value in the data set is represented by a dot.
# it needs 2 arrays of same length
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(5.0, 1.0, 10)
y = numpy.random.uniform(10.0, 2.0, 10)

plt.scatter(x, y)
plt.show()
