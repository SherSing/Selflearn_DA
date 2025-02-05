# Task to load diabetes dataset from sklearn

import numpy
import matplotlib.pyplot as plt
import pandas as pd
import sklearn 
from sklearn import linear_model
from sklearn.datasets import load_diabetes
from sklearn import linear_model

#https://www.youtube.com/watch?v=7d_HUVDD7k4

X,y= load_diabetes(return_X_y=True, as_frame=True)

print("Check data features \n",X.head(5))

print("Check target features \n",y.head(5))

# Concat variables together
all_vriables = pd.concat([X, y], axis=1)

# basic statistics of all_variables

print(all_vriables.describe())

print("**************")
# Plot histogram of bmi against sex

hist, bin_edges=all_vriables.hist(column='bmi', by='sex')
hist.plot().

plt.show()