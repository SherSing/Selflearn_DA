import pandas
from sklearn.linear_model import LinearRegression

import warnings

# Disable the warning
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")


df = pandas.read_csv('Raw Data/data_MRegression.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)