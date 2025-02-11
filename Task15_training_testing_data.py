##Creating dataset
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# plt.scatter(x, y)
# plt.show()

# Split Into Train/Test
# The training set should be a random selection of 80% of the original data.
# The testing set should be the remaining 20%

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# plot training set
# plt.scatter(train_x, train_y)
# plt.show()
# #Plot testing set
# plt.scatter(test_x, test_y)
# plt.show()

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))
print(r2)


# myline = numpy.linspace(0, 6, 100)
# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()


##Bring in the Testing Set
r2_test = r2_score(test_y, mymodel(test_x))
print(r2_test)

# myline = numpy.linspace(0, 6, 100)
# plt.scatter(test_x, test_y)
# plt.plot(myline, mymodel(myline))
# plt.show()

#Predicitng value
print(mymodel(5))
