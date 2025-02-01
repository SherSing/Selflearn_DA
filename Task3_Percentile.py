import numpy as np
#Percentile
import pandas as pd

df = pd.read_csv('Raw Data/testdata.csv')
print(df.head(5))

percentile25=np.percentile(df['LN_IC50'],25)
print(percentile25)

percentile50=np.percentile(df['LN_IC50'],50)
print(percentile50)

percentile75=np.percentile(df['LN_IC50'],75)
print(percentile75) 


