import pickle
import pandas as pd
import numpy as np
from IPython.core.debugger import Tracer


cols = ['Image_Name','Cat.1','Cat.2','Cat.3','Cat.4','Cat.5','TS','Load','exemplar','question','present_absent','trial_type','tone_Hz','tone_onset','space','RT_TO','keys','RT_VS','useless','Trial_N_Block','Block']

def range_from_1(n):
    return np.arange(1,n+1)

def process_observer(obs):  
    f = '../output/participant_'+obs+'.pik'
    import pickle
    with open(f,'r') as of:
        D = pickle.load(of)
    df = pd.DataFrame.from_dict(D['experiment_details'],orient='index')
    #df = dataframe_from_dict(D['experiment_details'])
    return process(df)

def process(df):
    notes = {}
    #fix_reaction_times(df)
    
    # Outlier rejection for TO
    
    si, sj = df.shape
    mean_TO = df['RT_TO'].mean()
    print 'MEAN TO: ',mean_TO
    sd_TO = df['RT_TO'].std()
    low = mean_TO - 2.5 * sd_TO
    high = mean_TO + 2.5 * sd_TO
    TO_outliers = df[df['RT_TO'].between(low, high, inclusive=False)]
    new_mean_TO = TO_outliers['RT_TO'].mean()
    print 'WINDOW: ',low,high
    
    #Tracer()()
    
    counter_TO = 0
    RT_TO_outliers = []
    for i in range_from_1(si):
        if df.loc[i,'RT_TO'] != None:
            if not (low < df.loc[i,'RT_TO'] < high):
                df.loc[i,'RT_TO'] = new_mean_TO
                counter_TO += 1
                
                
    print 'TO rejects n: ',counter_TO            
    notes['rejects_TO'] = [counter_TO, TO_outliers]
                
    # Outlier rejection for VS
    
    mean_VS = df['RT_VS'].mean()
    sd_VS = df['RT_VS'].std()
    low = mean_VS - 2.5 * sd_VS
    high = mean_VS + 2.5 * sd_VS
    VS_outliers = df[df['RT_VS'].between(low, high, inclusive=False)]
    new_mean_VS = VS_outliers['RT_VS'].mean()    
        
    #Tracer()()
    
    counter_VS = 0
    RT_VS_outliers = []
    for i in range_from_1(si):
        if df.loc[i,'RT_VS'] != None:
            if not (low < df.loc[i,'RT_VS'] < high):
                df.loc[i,'RT_VS'] = new_mean_VS
                counter_VS += 1
                
    print 'VS rejects N: ',counter_VS            
    notes['rejects_VS'] = counter_VS, VS_outliers
    
    #Correctness
    
    df['correct'] = None
    
    for i in range_from_1(si):
        if df['trial_type'] == :
            Acc_VS.append('999')
        elif 'Normal' in Audio[i] and RT_TO[i] != 'NaN':
            Acc_VS.append('666')
        elif 'Target Present' in Present_absent[i] and 'q' in Keys[i]:
            Acc_VS.append(1)
        elif 'Target Present' in Present_absent[i] and 'p' in Keys[i]:
            Acc_VS.append(0)
        elif 'Target Absent' in Present_absent[i] and 'p' in Keys[i]:
            Acc_VS.append(1)   
        elif 'Target Absent' in Present_absent[i] and 'q' in Keys[i]:
            Acc_VS.append(0)
        elif 'No Target' in Present_absent[i]:
            Acc_VS.append('999')
    #print notes
    return [df, notes]

def test():
    print 400
    
def dataframe_from_dict(DE):
    df = pd.DataFrame(index=DE.keys(), columns = cols)

    for t in DE.keys():
        row = [DE[t]['image_name'], 
            DE[t]['cat_1'],
               DE[t]['cat_2'],
               DE[t]['cat_3'],
               DE[t]['cat_4'],
               DE[t]['cat_5'],
               DE[t]['trueskill'],
               DE[t]['load'],
               DE[t]['exemplar'],
               DE[t]['question'],
               DE[t]['present_absent'],
               DE[t]['trial_type'],
               DE[t]['tone_hz'],
               DE[t]['tone_onset'],
               DE[t]['space'],
               DE[t]['RT_TO'],
               DE[t]['keys'],
               DE[t]['RT_VS'],
               DE[t]['useless'],
               0,
               DE[t]['block_number'],

        ]
        df.loc[t] = row
    return df



def fix_reaction_times(df):
#     df = pd.DataFrame.from_csv(path, header = None)
#     df.reset_index(inplace = True)
#     df.columns = ['Image_Name','Cat.1','Cat.2','Cat.3','Cat.4','Cat.5','TS','Load','exemplar','question','present_absent','trial_type','tone_Hz','tone_onset','space','RT_TO','keys','RT_VS','useless','Trial_N_Block','Block']
    invalid_count = 0
    n = df.shape[0]
    
    for i in np.arange(1,n+1):
        
        trial_type = df['trial_type'][i]
        rt_sound = df['RT_TO'][i]
        if 'Critical' in trial_type and  rt_sound == 'No timing':
            print 'DIRTY!',i
            go = True
            c = i+1
    #         set_trace()
            if c<n and 'Normal' in df['trial_type'][c] and  'No timing' not in df['RT_TO'][c]:

                print 'FOUND RT IN FIRST', c
                invalid_count += 1
                df.loc[c,'valid'] = 0
                df.loc[i,'RT_TO'] = str(float(df.loc[c,'RT_TO']) + 1.3)
                df.loc[i,'space'] = 'space'
                df.loc[c,'RT_TO'] = 'No timing'
                df.loc[c,'space'] = 'No space' 
                go = False
            c = i+2
            if go and c<n and 'Normal' in df['trial_type'][c] and  'No timing' not in df['RT_TO'][c]:
                print 'FOUND RT IN SECOND',c
                invalid_count += 2
                df.loc[c,'valid'] = 0
                df.loc[c-1,'valid'] = 0
                df.loc[i,'RT_TO'] = str(float(df.loc[c,'RT_TO']) + 2.6)
                df.loc[i,'space'] = 'space'
                df.loc[c,'RT_TO'] = 'No timing'
                df.loc[c,'space'] = 'No space'
            
                
    return invalid_count

        
            
        