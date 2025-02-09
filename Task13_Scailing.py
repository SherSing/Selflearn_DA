import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv('Raw Data/data_MRegression.csv')

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)