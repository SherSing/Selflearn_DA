import numpy as np

import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('Raw Data/testdata.csv')
print(df.head(5))

x=df['LN_IC50' [:20]]
y=df['AUC' [:20]]
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(slope,intercept,r, p, std_err)
def predict(x):
    """Return the predicted value of y given x."""
    return slope * x + intercept

mymodel = list(map(predict, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

