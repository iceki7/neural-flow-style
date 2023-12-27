import os 
import numpy as np
import argparse
import sys
# dir=r'F:\yzx-2\neural-flow-style-FORK\neural-flow-style\data\smokegun'
# with np.load(dir+r'\d_low\\'+'118.npz') as data:  
#     dlow = data['x']
# with np.load(dir+r'\v_low\\'+'118.npz') as data:  
#     vlow = data['x'] 
# print(dlow.shape)  
# print(vlow.shape)  


dir=r'C:\Users\yzx\Downloads\1225_054811_test\1225_054811_test'
with np.load(dir+r'\039.npz') as data:  
    res = data['x']



print(res.shape)  
