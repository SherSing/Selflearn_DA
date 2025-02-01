import numpy as np
#Mean-Median-Mode
import pandas as pd
from scipy import stats

df = pd.read_csv('Raw Data/testdata.csv')
print(df.head(5))

meanLN_IC50=np.mean(df['LN_IC50'])
print(meanLN_IC50)

medianLN_IC50=np.median(df['LN_IC50'])
print(medianLN_IC50)


mode = stats.mode(df['LN_IC50'])
print(mode.mode)
