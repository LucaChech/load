import numpy as np
import pandas as pd
from random import random

cols = ['Image_Name','Cat.1','Cat.2','Cat.3','Cat.4','Cat.5','TS','Load','exemplar','question','present_absent','trial_type','tone_Hz','tone_onset','space','RT_TO','keys','RT_VS','useless','Trial_N_Block','Block']
def range_from_1(n):
    return np.arange(1,n+1)

def gen_test():
    n = 400
    
    keys = range_from_1(n)
    df = pd.DataFrame(index=keys, columns = cols)
    
    mean = 450
    sd = 50
    
    for t in keys:
        
        rt_vs = mean + sd*random()
        rt_to = mean + sd*random()
        
        if t in [10,20,30,40,50,60]:
            rt_vs = 600
        if t in [15,25,35,45,55,65]:
            rt_vs = 200
        
        df.loc[t, 'RT_VS'] = rt_vs
        df.loc[t, 'RT_TO'] = rt_vs
        
        if random() < 0.5:
            present_absent = 'Target Present'
        else:
            present_absent = 'Target Absent'
        if random() < 0.5:
            keys = 'q'
        else:
            keys = 'p'
        df.loc[t,'trial_type'] = 'Normal'
        df.loc[t,'keys'] = keys
        df.loc[t,'present_absent'] = present_absent
    return df