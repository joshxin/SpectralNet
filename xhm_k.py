# testing spectral-net using data imported from xhm
# jianhong, 1/19


# %%
import pandas as pd
import numpy as np
import scipy.io as sio
import tensorflow as tf
import keras.backend as K 


# %% load types

types = sio.loadmat('types.mat')

i2x = types['i2x']

# num
n = {}
n['i'] = len(i2x)

k = {}
k['i'] = np.max(i2x)

print('There are {} workers in {} types.'.format(n['i'], k['i']))

j2cj = types['j2cj']
n['j'], _ = j2cj.shape

cj2y = types['cj2y']
_, n['f'] = cj2y.shape
k['f'] = np.max(cj2y)


print('There are {} firms in {} types.'.format(n['f'], k['f']))

# %% load affinity matrix

a = sio.loadmat('a.mat')

A = {}
A['ii'] = np.array(a['A_ii'])

print('The shape of the affinity matrix A: {}'.format(A['ii'].shape))

# %% load sufficient stats

ss = sio.loadmat('ss.mat')

G = ss['G_if']
H = ss['H_if']
H_ss = ss['H_ss_if']
W_s = ss['W_s_if']
W_ss = ss['W_ss_if']
W_ssb = ss['W_ssb_if']
W_ssw = ss['W_ssw_if']

S = {}
S['if'] = {'G': G, 'H': H, 'H_ss': H_ss,
           'W_s': W_s, 'W_ssb': W_ssb, 'W_ssw': W_ssw}


print('The shape of the matrix S: {}'.format(G.shape))

# %% load estimators

e = sio.loadmat('e.mat')

W_m = e['W_m_if']     # average wage (i,f)
W_se = e['W_se_if']   # std err for average wage (i,f)
z_se = e['z_se_if']   # std err for match spec shock (i,f)

E = {}
E['if'] = {'W_m': W_m, 'W_se': W_se, 'z_se': z_se}

W_se = e['W_se']
E['11'] = {'W_se': W_se}

print(W_se)
w =  W_m / W_se # t stat
print(w[:50,0])
print('The shape of the matrix E: {}'.format(W_m.shape))
# %%

A2 = np.sum((np.abs(w[:1000,np.newaxis,:1000] - w[:1000,:1000])<2),axis=-1)
# %%
print(A['ii'][:10,:10]*256)
print(A2[:10,:10])

#%%
