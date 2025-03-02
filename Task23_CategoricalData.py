import pandas as pd
from sklearn import linear_model


cars = pd.read_csv('Raw Data/data_MRegression.csv')
one_hot_encoding_cars = pd.get_dummies(cars[['Car']])
# one_hot_encoding_model = pd.get_dummies(cars[['Model']])

# print(one_hot_encoding_cars.head())

X = pd.concat([cars[['Volume', 'Weight']], one_hot_encoding_cars], axis=1)
print(X.head())
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X,y)

##predict the CO2 emission of a VW where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])

print(predictedCO2)