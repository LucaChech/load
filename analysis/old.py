def process_observer(obs):
    f = '../output/participant_'+obs+'.pik'
    import pickle
    with open(f,'r') as of:
        D = pickle.load(of)
    df = dataframe_from_dict(D['experiment_details'])
    
    
       
    df['valid'] = df['Block']
    df['valid'] = 1
    df['sdt'] = 0
    df.drop(['Image_Name','
             Cat.1','Cat.2','Cat.3','Cat.4','Cat.5','TS','exemplar','question','space','useless'], axis=1, inplace=True)
    invalid_count = fix_reaction_times(df)
    
    RT_TO = df['RT_TO'].tolist()
    RT_VS = df['RT_VS'].tolist()
    Audio = df['trial_type'].tolist()
    Present_absent = df['present_absent'].tolist()
    Audio = df['trial_type'].tolist()
    Keys = df['keys'].tolist()
    Tone_onset = df['tone_onset'].tolist()

#     RT_TO = [str('NaN') if n == 'No timing' else float(n[0:5]) for n in RT_TO]
#     RT_VS = [str('NaN') if n == None else float(n[0:5])-1.3 for n in RT_VS]
#     Keys = [str(n[2:-1]) for n in Keys]
    RT_TO_floats = [n for n in RT_TO if type(n) == float]
    sd_TO = np.std(RT_TO_floats)
    mean_TO = np.mean(RT_TO_floats)

    #Getting rid of outliers for TO RT (outliers are replaced with mean)
    RT_TO_no_outliers = []
    counter_TO = 0
    RT_TO_outliers = []
    for i in RT_TO:
        if type(i) != float:
            RT_TO_no_outliers.append(i)
        elif type(i) == float:
            if (mean_TO - 2.5 * sd_TO) < i < (mean_TO + 2.5 * sd_TO):
                RT_TO_no_outliers.append(i)
            else:
                counter_TO = counter_TO + 1
                #print 'Outlier ' + str(counter_TO) + ': ' + str(i) 
                RT_TO_no_outliers.append(mean_TO)
                RT_TO_outliers.append(i)
    RT_TO = RT_TO_no_outliers

    Tone_onset = [int(n) for n in Tone_onset]
    for i in range(len(Tone_onset)):
        if Tone_onset[i] != -999:
            Tone_onset[i] = float(Tone_onset[i])/1000
            if type(RT_TO[i]) == float:
                #print RT_TO[i], '-', Tone_onset[i] 
                RT_TO[i] = RT_TO[i] - Tone_onset[i]
                #print RT_TO[i]


    RT_VS_floats = [n for n in RT_VS if type(n) == float]
    sd_VS = np.std(RT_VS_floats)
    mean_VS = np.mean(RT_VS_floats)

    #Getting rid of outliers for TO RT (outliers are replaced with mean)
    RT_VS_no_outliers = []
    counter_VS = 0
    RT_VS_outliers = []
    for i in RT_VS:
        if type(i) != float:
            RT_VS_no_outliers.append(i)
        elif type(i) == float:
            if (mean_VS - 2.5 * sd_VS) < i < (mean_VS + 2.5 * sd_VS):
                RT_VS_no_outliers.append(i)
            else:
                counter_VS = counter_VS + 1
                #print 'Outlier ' + str(counter_TO) + ': ' + str(i) 
                RT_VS_no_outliers.append(mean_VS)
                RT_VS_outliers.append(i)
    RT_VS = RT_VS_no_outliers

    print 'Take Over:'
    print 'mean RT: ', mean_TO
    print 'SD: ', sd_TO
    print 'Outliers: ', len(RT_TO_outliers)
    for i in RT_TO_outliers:
        print i

    print 'Visual Search:'
    print 'mean RT: ', mean_VS
    print 'SD: ', sd_VS
    print 'Outliers: ', len(RT_VS_outliers)
    for i in RT_VS_outliers:
        print i


    #######
    Acc_VS = []
    for i in range(960):
        if 'Critical' in Audio[i]:
            #print i
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

    #print len(Acc_VS)
    #######

    #######
    # CREATING Acc_DT (1 = included for analysis; 0 = excluded from analysis)
    Acc_DT = []
    for i in range(960):
        if 'Critical' in Audio[i] and type(RT_TO[i]) != str:
            # Was visual search correct?
            if 'Target Present' in Present_absent[i] and 'q' in Keys[i]:
                Acc_DT.append(1)
                df.loc[i,'sdt'] = 1
            elif 'Target Absent' in Present_absent[i] and 'p' in Keys[i]:
                Acc_DT.append(1)
                df.loc[i,'sdt'] = 1
            elif 'Target Present' in Present_absent[i] and 'p' in Keys[i]:
             #Wrong VS
                Acc_DT.append(999)
                df.loc[i,'sdt'] = 0
            elif 'Target Absent' in Present_absent[i] and 'q' in Keys[i]:
             #Wrong VS
                Acc_DT.append(999)
                df.loc[i,'sdt'] = 0
            elif 'No Target' in Present_absent[i]:
                Acc_DT.append(1)
                df.loc[i,'sdt'] = 1
             1 HIT
             2 MISS
             3 FA
             4 CR
        # Incorrect on tone
        elif 'Critical' in Audio[i] and type(RT_TO[i]) == str:
            Acc_DT.append(0)
            df.loc[i,'sdt'] = 2
        #Throw out normal trials
        elif 'Normal' in Audio[i] and type(RT_TO[i]) != str:
            Acc_DT.append(666) # 666 are false alarms
            df.loc[i,'sdt'] = 3
        elif 'Normal' in Audio[i] and type(RT_TO[i]) == str:
            Acc_DT.append(999)
            df.loc[i,'sdt'] = 4
    for i in range(960):
        if df.loc[i,'valid'] == 0:
            df.loc[i,'sdt'] = 0
    #print len(Acc_DT) 

    correct_response_counter = len([n for n in Acc_DT if n == 1])
    incorrect_response_counter = len([n for n in Acc_DT if n == 0])
    incorrect_response_counter

    n_present = correct_response_counter + incorrect_response_counter
    hit_rate = float(correct_response_counter) / (n_present - invalid_count)
    print hit_rate

    # Converting lists into pandas.series...
    RT_TO = pd.Series(data=RT_TO)
    RT_VS = pd.Series(data=RT_VS)
    Acc_VS = pd.Series(data=Acc_VS)
    Acc_DT = pd.Series(data=Acc_DT)
    #False_Alarms = pd.Series(data=False_Alarms)
    # ...and combining them into a pandas dataframe

    df.drop(['RT_TO','RT_VS'], axis = 1, inplace = True)
    df['RT_TO'] = RT_TO.values
    df['RT_VS'] = RT_VS.values
    df['Acc_VS'] = Acc_VS.values
    df['Acc_DT'] = Acc_DT.values

    df[['RT_TO','RT_VS']] = df[['RT_TO','RT_VS']].astype('float')
    df[['Acc_VS','Acc_DT']] = df[['Acc_VS','Acc_DT']].astype('int')
    print df.dtypes

    df_low = df[df['Load'].str.contains("low")]
    df_high = df[df['Load'].str.contains("high")]

    counts = df['sdt'].value_counts()
    counts_low = df_low['sdt'].value_counts()
    counts_high = df_high['sdt'].value_counts()
    
    result['vs_accuracy_low'] = calc_vs_accuracy(df, 'low')
    result['vs_accuracy_high'] = calc_vs_accuracy(df, 'high')
    calc_vs_accuracy_both(df)
    
    print counts
    print '---------'
    print counts_low
    print '---------'
    print counts_high

    n_h = float(counts[1])
    n_m = float(counts[2])
    try:
        n_fa = float(counts[3])
    except:
        n_fa = 0
    n_cr = float(counts[4])

    h_rate = n_h / (n_h + n_m)
    fa_rate = n_fa / (n_cr + n_fa)
    h_rate

    n_h_low = float(counts_low[1])
    try:
        n_m_low = float(counts_low[2])
    except:
        n_m_low = 0
    try:
        n_fa_low = float(counts_low[3])
    except:
        n_fa_low = 0
    n_cr_low = float(counts_low[4])

    h_rate_low = n_h_low / (n_h_low + n_m_low)
    fa_rate_low = n_fa_low / (n_cr_low + n_fa_low)
    
    result['h_rate_low_detection'] = h_rate_low

    n_h_high = float(counts_high[1])
    try:
        n_m_high = float(counts_high[2])
    except:
        n_m_high = 0
    try:
        n_fa_high = float(counts_high[3])
    except:
        n_fa_high = 0
    n_cr_high = float(counts_high[4])

    h_rate_high = n_h_high / (n_h_high + n_m_high)
    fa_rate_high = n_fa_high / (n_cr_high + n_fa_high)
    
    result['h_rate_high_detection'] = h_rate_high

    print d_prime(n_h_low, n_m_low, n_fa_low, n_cr_low)
    print d_prime(n_h_high, n_m_high, n_fa_high, n_cr_high)

    #TABLE 1
    print df.groupby(['Load','Acc_VS']).RT_VS.mean()
    print df.groupby(['Load','Acc_VS']).RT_VS.count()

    # TABLE 2
    #print df.groupby(['Load','Acc_VS','present_absent']).RT_VS.mean()
    #print df.groupby(['Load','Acc_VS','present_absent']).RT_VS.count()

    #TABLE 3
    print df.groupby(['Load','trial_type','Acc_DT']).RT_TO.mean()
    print df.groupby(['Load','trial_type','Acc_DT']).Acc_DT.count()
    
    return result