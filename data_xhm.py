# %%

import numpy as np 
import pandas as pd 

df = pd.read_csv('data_xhm.csv', sep=',', skiprows=0, names=['t','i','j','W'])
print(df.head(5))

# %%
T = np.max(df['t'])
N = np.max(df['i']) # number of workers
M = np.max(df['j']) 

print('{} periods, {} workers and {} firms.'.format(T,N,M))

# %%

i = 0
W_i = df.loc[df['i']==i+1]

print(Wt)

# %%
for t in range(T):
    Wt = df[df['t']==t+1]