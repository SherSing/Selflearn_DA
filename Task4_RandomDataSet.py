import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 50.0, 250)         

print(x)

plt.hist(x, 10, facecolor='green', edgecolor='black',label='Random Data')
plt.show()