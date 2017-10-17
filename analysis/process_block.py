import pickle
import pandas as pd
import numpy as np

from pdb import set_trace

def range_from_1(n):
    return np.arange(1,n+1)

def preprocess(df):
        #Split into blocks
    #Split into blocks
    fix_reaction_times(df)
    
   
    # Outlier rejection for TO
    
    si, sj = df.shape
    mean_TO = df['RT_TO'].mean()
    print 'MEAN TO: ',mean_TO
    sd_TO = df['RT_TO'].std()
    low = mean_TO - 2.5 * sd_TO
    high = mean_TO + 2.5 * sd_TO
    TO_outliers = df[df['RT_TO'].between(low, high, inclusive=False)]
    new_mean_TO = TO_outliers['RT_TO'].mean()
    print 'TO WINDOW: ',low,high
    
    counter_TO = 0
    RT_TO_outliers = []
    for i in range_from_1(si):
        if not pd.isnull(df.loc[i,'RT_TO']):
            if not (low < df.loc[i,'RT_TO'] < high):
                df.loc[i,'RT_TO'] = new_mean_TO
                counter_TO += 1
                
                
    print 'TO rejects n: ',counter_TO            
    #notes['rejects_TO'] = [counter_TO, TO_outliers]
                
    
    # Outlier rejection for VS
    
    mean_VS = df['RT_VS'].mean()
    sd_VS = df['RT_VS'].std()
    low = mean_VS - 2.5 * sd_VS
    high = mean_VS + 2.5 * sd_VS
    VS_outliers = df[df['RT_VS'].between(low, high, inclusive=False)]
    new_mean_VS = VS_outliers['RT_VS'].mean()    
        
   
    
    counter_VS = 0
    RT_VS_outliers = []
    for i in range_from_1(si):
        if not pd.isnull(df.loc[i,'RT_VS']):
            if not (low < df.loc[i,'RT_VS'] < high):
                df.loc[i,'RT_VS'] = new_mean_VS
                counter_VS += 1
                
   
    print 'VS rejects N: ',counter_VS            
    #notes['rejects_VS'] = counter_VS, VS_outliers
    
    # RT adjustment - VS
    
    for i in range_from_1(si):
        if (df.loc[i,'present_absent'] == 'Target Present' or df.loc[i,'present_absent'] == 'Target Absent') and not pd.isnull(df.loc[i,'RT_VS']):
            df.loc[i,'RT_VS'] = df.loc[i,'RT_VS'] - 1.3
            
    # RT adjustment - tone
    
    for i in range_from_1(si):
        if df.loc[i,'trial_type'] == 'Critical' and (not pd.isnull(df.loc[i,'RT_TO'])) and df.loc[i,'tone_onset'] != -999:
            df.loc[i,'RT_TO'] = df.loc[i,'RT_TO'] - df.loc[i,'tone_onset']
    

def process_block(df):
    si, sj = df.shape
    notes = {}
    df.loc[:,'valid'] = 1

    #fix_reaction_times(df)
    
   
    # Outlier rejection for TO
    
  
            
    # RT adjustment - tone
    

    
    #Correctness for Visual-search task
    #Accuracy for the visual-search task: we want trials:
    #- with a target (either present or absent) : 'trial_type' == 'Target Present' or 'trial_type' == 'Target Absent'
    #- without false alarms to the tone: pd.isnull(df.loc[i,'RT_TO'])
    #- without the tone : df.loc[i,'trial_type'] == 'Normal'
    #tone-detection task
    df.loc[1,'correct_vs'] = None
    
    

    
    for i in range_from_1(si):
        if df.loc[i,'trial_type'] == 'Normal' and pd.isnull(df.loc[i,'RT_TO']):
            if df.loc[i,'present_absent'] == 'Target Present'  and df.loc[i,'keys'] == 'q':
                df.loc[i,'correct_vs'] = 1
            if df.loc[i,'present_absent'] == 'Target Present' and df.loc[i,'keys'] == 'p':
                df.loc[i,'correct_vs'] = 0
            if df.loc[i,'present_absent'] == 'Target Absent'  and df.loc[i,'keys'] == 'p':
                df.loc[i,'correct_vs'] = 1   
            if df.loc[i,'present_absent'] == 'Target Absent'  and df.loc[i,'keys'] == 'q':
                df.loc[i,'correct_vs'] = 0
    
    n_corrects_vs = len(df[df['correct_vs'] == 1])
    print 'CORRECT VS: ',n_corrects_vs
    
    
    ### This is for calculating Accuracy (properly hit rate) for the detection task
    df.loc[:,'restricted_correct_tone'] = None
    
    for i in range_from_1(si):
        # Here we only care about trials which have a tone (Critical) and which also either have no VS target
        # or the VS was right.
        #correct_tone will not be filled out for all normal trials!!
        no_vis_target_or_right = (df.loc[i,'present_absent'] == 'Target Absent' or df.loc[i,'correct_vs'] == 1)
        if df.loc[i,'trial_type'] == 'Critical' and no_vis_target_or_right:
            if df.loc[i, 'trial_type'] == 'Critical' and pd.isnull(df.loc[i,'RT_TO']):
                df.loc[i,'restricted_correct_tone'] = 0
            if df.loc[i, 'trial_type'] == 'Critical' and not pd.isnull(df.loc[i,'RT_TO']):
                df.loc[i,'restricted_correct_tone'] = 1
                
         
    df.loc[:,'correct_tone'] = None    
        
    for i in range_from_1(si):
        if df.loc[i, 'trial_type'] == 'Critical' and pd.isnull(df.loc[i,'RT_TO']):
            df.loc[i,'correct_tone'] = 0
        if df.loc[i, 'trial_type'] == 'Critical' and not pd.isnull(df.loc[i,'RT_TO']) :
            df.loc[i,'correct_tone'] = 1
        if df.loc[i, 'trial_type'] == 'Normal' and  pd.isnull(df.loc[i,'RT_TO']):
            df.loc[i,'correct_tone'] = 1
        if df.loc[i, 'trial_type'] == 'Normal' and not pd.isnull(df.loc[i,'RT_TO']):
            df.loc[i,'correct_tone'] = 0

                
    df.loc[:,'sdt'] = None
             # 1 HIT
             # 2 MISS
             # 3 FA
             # 4 CR
    for i in range_from_1(si):
        # We don't care about trials which have an audio probe and the VS was wrong.
        if not ( df.loc[i,'trial_type'] == 'Critical' and df.loc[i,'correct_vs'] == 0):
            if df.loc[i,'trial_type'] == 'Critical' and df.loc[i,'correct_tone'] == 1:
                df.loc[i,'sdt'] = 1
            if df.loc[i,'trial_type'] == 'Critical' and df.loc[i,'correct_tone'] == 0:
                df.loc[i,'sdt'] = 2
            if df.loc[i,'trial_type'] == 'Normal' and df.loc[i,'correct_tone'] == 0:
                df.loc[i,'sdt'] = 3
            if df.loc[i,'trial_type'] == 'Normal' and df.loc[i,'correct_tone'] == 1:
                df.loc[i,'sdt'] = 4
        else:
            print 'EXCLUDED FROM SDT'
                
    n_valid_sdt_high = len(df[pd.notnull(df['sdt']) & (df['load'] == 'high')])
    n_present_high = len(df[df['sdt'].notnull() & (df['trial_type'] == 'Critical') & (df['load'] == 'high')])
    n_hit_high = len(df[df['sdt'] == 1 & (df['load'] == 'high')])
    hit_rate_high = float(n_hit_high) / n_present_high
    
    n_valid_sdt_low = len(df[pd.notnull(df['sdt']) & (df['load'] == 'low')])
    n_present_low = len(df[df['sdt'].notnull() & (df['trial_type'] == 'Critical') & (df['load'] == 'low')])
    n_hit_low = len(df[df['sdt'] == 1 & (df['load'] == 'low')])
    hit_rate_low = float(n_hit_low) / n_present_low
    tone_detection_diff = hit_rate_low - hit_rate_high
    
    notes['tone_n_present_high'] = n_present_high
    notes['tone_n_hit_high'] = n_hit_high
    
  
    
    #Accuracy for the visual-search task: we want trials:
    #- with a target (either present or absent) : 'trial_type' == 'Target Present' or 'trial_type' == 'Target Absent'
    #- without false alarms to the tone
    #- without the tone
    #tone-detection task
    
    #High load
    n_vs_trials_with_target_high = len(df[(df['present_absent'] != 'No Target') & (df['trial_type'] == 'Normal') & (pd.isnull(df['RT_TO'])) & (df['load']=='high')])
    n_vs_trials_correct_high = len(df[(df['load']=='high') & (df['correct_vs']==1)])
    if n_vs_trials_with_target_high != 0:
        accuracy_vs_high = float(n_vs_trials_correct_high) / float(n_vs_trials_with_target_high)
    else:
        accuracy_vs_high = np.NaN
    #
    #Low load
    n_vs_trials_with_target_low = len(df[(df['present_absent'] != 'No Target') & (df['trial_type'] == 'Normal') & (pd.isnull(df['RT_TO'])) & (df['load']=='low')])
    n_vs_trials_correct_low = len(df[(df['load']=='low') & (df['correct_vs']==1)])
    if n_vs_trials_with_target_low != 0:    
        accuracy_vs_low = float(n_vs_trials_correct_low) / float(n_vs_trials_with_target_low)
    else:
        accuracy_vs_low = np.NaN
        
    accuracy_vs_diff = accuracy_vs_low - accuracy_vs_high
    
    ### Calculating absolute number of false alarms for the detection task
    
    #High load
    fa_high = len(df[(df['trial_type']=='Normal') & (df['RT_TO'].notnull()) & (df['load']=='high')])
    fa_low = len(df[(df['trial_type']=='Normal') & (df['RT_TO'].notnull()) & (df['load']=='low')])
    
    
    
    
    for i in range_from_1(si):
        if df.loc[i,'valid'] == 0:
            df.loc[i,'sdt'] = 0    
            
    #Result storage
    notes['vs_accuracy_high'] = accuracy_vs_high
    notes['vs_accuracy_low'] = accuracy_vs_low
    notes['vs_accuracy_diff'] = accuracy_vs_diff
    notes['tone_detection_accuracy_high'] = hit_rate_high
    notes['tone_detection_accuracy_low'] = hit_rate_low
    notes['tone_detection_accuracy_diff'] = tone_detection_diff
    notes['false_alarms_high'] = int(fa_high)
    notes['false_alarms_low'] = int(fa_low)
    

    #print notes
    return [df, notes]


def fix_reaction_times(df):
    invalid_count = 0
    n = df.shape[0]
    print n
    
    for i in np.arange(1,n+1):
        
        trial_type = df['trial_type'][i]
        rt_sound = df['RT_TO'][i]
        #if trial_type == 'Critical' and  rt_sound == 'nan':
        if trial_type == 'Critical' and  pd.isnull(rt_sound):
           # print 'DIRTY!',i
            go = True
            c = i+1
            if c <=n and df.loc[c,'trial_type'] == 'Normal' and not pd.isnull(df.loc[c,'RT_TO']):
              #  print 'FOUND RT IN FIRST', c
                invalid_count += 1
                df.loc[c,'valid'] = 0
                df.loc[i,'RT_TO'] = float(df.loc[c,'RT_TO']) + 1.3*1000
                df.loc[i,'space'] = 'space'
                df.loc[c,'RT_TO'] = np.NaN 
                df.loc[c,'space'] = None 
                go = False
            c = i+2
            if go==True and c <=n and df.loc[c,'trial_type'] == 'Normal' and not pd.isnull(df.loc[c,'RT_TO']):
              #  print 'FOUND RT IN SECOND',c
                invalid_count += 2
                df.loc[c,'valid'] = 0
                df.loc[c-1,'valid'] = 0
                df.loc[i,'RT_TO'] = float(df.loc[c,'RT_TO']) + 2.6*1000
                df.loc[i,'space'] = 'space'
                df.loc[c,'RT_TO'] = np.NaN 
                df.loc[c,'space'] = None 
            
                
    return invalid_count
