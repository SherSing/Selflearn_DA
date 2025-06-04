import numpy as np
#Mean-Median-Mode
import pandas as pd
from scipy import stats

def calculate_statistics(df, column):
    mean_val = np.mean(df[column])
    median_val = np.median(df[column])
    mode_val = stats.mode(df[column], keepdims=True).mode[0]
    return mean_val, median_val, mode_val

df = pd.read_csv('Raw Data/testdata.csv')
print(df.head(5))

meanLN_IC50, medianLN_IC50, modeLN_IC50 = calculate_statistics(df, 'LN_IC50')
print(meanLN_IC50)
print(medianLN_IC50)
print(modeLN_IC50)
