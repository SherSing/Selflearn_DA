import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(10.0, 2.0, 10000)


print(x)

plt.hist(x, 100, facecolor='green')
plt.show()
