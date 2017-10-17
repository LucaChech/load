import numpy as np
import pandas as pd
from random import random

cols = [u'cat_4', u'cat_5', u'tone_hz', u'tone_onset', u'cat_1', u'cat_2',
       u'cat_3', u'keys', u'space', u'question', u'image_name', u'load',
       u'present_absent', u'block_number', u'RT_VS', u'exemplar', u'trueskill',
       u'RT_TO', u'trial_type', u'image_number', u'useless', u'valid',
       u'correct_vs', u'restricted_correct_tone', u'correct_tone', u'sdt']
def range_from_1(n):
    return np.arange(1,n+1)

def gen_test_1():
    n = 400
    
    keys = range_from_1(n)
    df = pd.DataFrame(index=keys, columns = cols)
    
    mean = 450
    sd = 50
    
    for t in keys:
        if random() > 0.5:
            df.loc[t, 'load'] = 'high'
        else:
            df.loc[t, 'load'] = 'low'
        
        if random() > 0.5:
            df.loc[t, 'trial_type'] = 'Critical'
        else:
            df.loc[t, 'trial_type'] = 'Normal'
        
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
        
        df.loc[t,'keys'] = keys
        df.loc[t,'present_absent'] = present_absent
    return df


def gen_test_2():
    #Accuracy - tone detection
    
    n = 4000
    
    keys = range_from_1(n)
    df = pd.DataFrame(index=keys, columns = cols)
    
    to_accuracy_high = .2
    to_accuracy_low = .8
    to_rt_high = 450
    to_rt_low = 200
    sd = 50
    mean = 300
    
    
    
    for t in keys:
        if random() > 0.5:
            df.loc[t, 'load'] = 'high'
        else:
            df.loc[t, 'load'] = 'low'
        
        
        if (df.loc[max(1,t-1), 'trial_type'] != 'Critical') and (df.loc[max(1,t-2), 'trial_type'] != 'Critical'):
            follower = False
            if random() > 0.5:
                df.loc[t, 'trial_type'] = 'Critical'
            else:
                df.loc[t, 'trial_type'] = 'Normal'
        else:
            follower = True
            df.loc[t, 'trial_type'] = 'Normal'
                
        df.loc[t, 'tone_onset'] = 0
        
        rt_vs = mean + sd*random()
        if df.loc[t,'load'] == 'high':
            if random()< to_accuracy_high:
                #Correct
                if df.loc[t, 'trial_type'] == 'Critical':
                    rt_to = to_rt_high
                else:
                    rt_to = None
            else:
                #Incorrect
                if df.loc[t, 'trial_type'] == 'Critical':
                    rt_to = None
                else:
                    rt_to = to_rt_high                 
        elif df.loc[t,'load'] == 'low':
            if random()< to_accuracy_low:
                #Correct
                if df.loc[t, 'trial_type'] == 'Critical':
                    rt_to = to_rt_low
                else:
                    rt_to = None
            else:
                #Incorrect
                if df.loc[t, 'trial_type'] == 'Critical':
                    rt_to = None
                else:
                    rt_to = to_rt_low
                    
        # Follower trials have no response
        if follower:
            rt_to = None
        
        if t in [10,20,30,40,50,60]:
            rt_vs = 600
        if t in [15,25,35,45,55,65]:
            rt_vs = 200
        
        df.loc[t, 'RT_VS'] = rt_vs
        df.loc[t, 'RT_TO'] = rt_to
        
        if random() < 0.5:
            present_absent = 'Target Present'
        else:
            present_absent = 'Target Absent'
        
    
        
        if random() < 0.5:
            keys = 'q'
        else:
            keys = 'p'
        
        df.loc[t,'keys'] = keys
        df.loc[t,'present_absent'] = present_absent
    return df