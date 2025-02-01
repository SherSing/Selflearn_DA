import numpy as np

#Standard Deviation

import pandas as pd
from scipy import stats

df = pd.read_csv('Raw Data/testdata.csv')
print(df.head(5))

stdLN_IC50=np.std(df['LN_IC50'])
print(stdLN_IC50)
