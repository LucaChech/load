from shared import * 
import numpy as np
import pandas as pd
##########################################################
df = pd.DataFrame.from_csv(shared['mypath']+'all_images_2.csv')

df.reset_index(drop=False)

image_names = df.index.tolist()
cat1 = df['0'].tolist()
cat2 = df['1'].tolist()
cat3 = df['2'].tolist()
cat4 = df['3'].tolist()
cat5 = df['4'].tolist()
ts = df['5'].tolist()
load = df['6'].tolist()
exemplar = df['7'].tolist()
possible_images_dict ={z[0]:list(z[1:]) for z in zip(image_names,cat1,cat2,cat3,cat4,cat5,ts,load,exemplar)}
lista = possible_images_dict.keys()
##########################################################

def target_present_probes_1():
    global categories, load
    for category in shared['categories']:
        for load in shared['p_load']:
            while True:
                trial = str(np.random.choice(lista, 1, replace= False))[2:-2]
                if category in possible_images_dict[trial][7] and load in possible_images_dict[trial] \
                    and trial not in shared['intermediate'] and trial not in shared['target_present']:
                    shared['intermediate'].append(trial)
                if len(shared['intermediate']) == 1:
                    for each in shared['intermediate']:
                        shared['target_present'].append(each)
                        possible_images_dict[each].append(category)
                    shared['intermediate'] = []
                    break
    print len(shared['target_present'])

    for category in shared['odd']:
        for load in shared['p_load']:
            while True:
                trial = str(np.random.choice(lista, 1, replace= False))[2:-2]
                if category in possible_images_dict[trial][7] and load in possible_images_dict[trial] \
                    and trial not in shared['intermediate'] and trial not in shared['target_present']:
                    shared['intermediate'].append(trial)
                if len(shared['intermediate']) == 1:
                    for each in shared['intermediate']:
                        shared['target_present'].append(each)
                        possible_images_dict[each].append(category)
                    shared['intermediate'] = []
                    break
    print len(shared['target_present'])
    for n in shared['target_present']:
        possible_images_dict[n].append('Target Present')

    target_present_counter = [n for n in lista if 'Target Present' in possible_images_dict[n]]
    shared['target_present_counter'] = target_present_counter
    print 'len(target_present_counter): ', len(target_present_counter)
    return

def block_low_1():
# Pick 4 present probes and 5 absent probes
    global critical_per_block,probes_per_block, present_used, absent_used, critical_used, normal_per_block, to_insert
    while len(probes_per_block) < 4:
        probe = str(np.random.choice(target_present,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in present_used and 'low' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    while 4 <= len(probes_per_block) < 9:
        probe = str(np.random.choice(target_absent,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in absent_used and 'low' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    
    for n in probes_per_block:
        print possible_images_dict[n]
        if 'Target Present' in possible_images_dict[n]:
            present_used.append(n)
        elif 'Target Absent' in possible_images_dict[n]:
            absent_used.append(n)
    
    probes.append(probes_per_block)
#------------------------------------------------------------------------------    
#Counting critical probes    
    critical_probes_counter = 0
    for n in probes_per_block:
        if 'Critical' in possible_images_dict[n]:
            critical_probes_counter = critical_probes_counter + 1
    #for n in probes_per_block:
    #    print possible_images_dict[n]
    print 'Present Used: ',len(present_used)
    print 'Absent Used ',len(absent_used)
    print 'Critical probes counter: ',critical_probes_counter
    
    modifier.append(critical_probes_counter)
#------------------------------------------------------------------------------
#Picking critical trials
    while len(critical_per_block) < (3-critical_probes_counter):
        image = str(np.random.choice(critical_trials,1,replace = False))[2:-2]
        if image not in critical_per_block and image not in critical_used \
            and 'No Target' in possible_images_dict[image] and 'low' in possible_images_dict[image]:
            critical_per_block.append(image) 
    print 'List of critical trials without probe: '
    for n in critical_per_block:
        critical_used.append(n)
        print possible_images_dict[n]
    #temp = []
    
    critical.append(critical_per_block)

#------------------------------------------------------------------------------
#Picking normal trials
    while len(normal_per_block) < 51 - (3 - critical_probes_counter):
        image = str(np.random.choice(normal_no_probe,1,replace = False))[2:-2]
        if image not in normal_per_block and image not in normal_no_probe_used and 'low' in possible_images_dict[image]:
            normal_per_block.append(image)
    for n in normal_per_block:
        normal_no_probe_used.append(n)
    print 'len(normal_no_probe_used): ',len(normal_no_probe_used)
    
    normal.append(normal_per_block)

#-----------------------------------------------------------------------------
    
    probes_per_block = []
    critical_per_block = []
    normal_per_block = []
    to_insert = []
    print 'Normal used:',len(normal_no_probe_used)
    print'---------------------------------------------------'
    return 


def block_low_2():
# Pick 5 present probes and 4 absent probes
    global critical_per_block,probes_per_block, present_used, absent_used, critical_used, normal_per_block, to_insert
    while len(probes_per_block) < 5:
        probe = str(np.random.choice(target_present,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in present_used and 'low' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    while 5 <= len(probes_per_block) < 9:
        probe = str(np.random.choice(target_absent,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in absent_used and 'low' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    
    for n in probes_per_block:
        print possible_images_dict[n]
        if 'Target Present' in possible_images_dict[n]:
            present_used.append(n)
        elif 'Target Absent' in possible_images_dict[n]:
            absent_used.append(n)
    
    probes.append(probes_per_block)
#------------------------------------------------------------------------------    
#Counting critical probes    
    critical_probes_counter = 0
    for n in probes_per_block:
        if 'Critical' in possible_images_dict[n]:
            critical_probes_counter = critical_probes_counter + 1
    #for n in probes_per_block:
    #    print possible_images_dict[n]
    print 'Present Used: ',len(present_used)
    print 'Absent Used ',len(absent_used)
    print 'Critical probes counter: ',critical_probes_counter
    
    modifier.append(critical_probes_counter)
#------------------------------------------------------------------------------
#Picking critical trials
    while len(critical_per_block) < (3-critical_probes_counter):
        image = str(np.random.choice(critical_trials,1,replace = False))[2:-2]
        if image not in critical_per_block and image not in critical_used \
            and 'No Target' in possible_images_dict[image] and 'low' in possible_images_dict[image]:
            critical_per_block.append(image) 
    print 'List of critical trials without probe: '
    for n in critical_per_block:
        critical_used.append(n)
        print possible_images_dict[n]
    #temp = []
    
    critical.append(critical_per_block)

#------------------------------------------------------------------------------
#Picking normal trials
    while len(normal_per_block) < 51 - (3 - critical_probes_counter):
        image = str(np.random.choice(normal_no_probe,1,replace = False))[2:-2]
        if image not in normal_per_block and image not in normal_no_probe_used and 'low' in possible_images_dict[image]:
            normal_per_block.append(image)
    for n in normal_per_block:
        normal_no_probe_used.append(n)
    print 'len(normal_no_probe_used): ',len(normal_no_probe_used)
    
    normal.append(normal_per_block)

#-----------------------------------------------------------------------------
   
    probes_per_block = []
    critical_per_block = []
    normal_per_block = []
    to_insert = []
    print 'Normal used:',len(normal_no_probe_used)
    print'---------------------------------------------------'
    return 



def block_high_1():
# Pick 4 present probes and 5 absent probes
    global critical_per_block,probes_per_block, present_used, absent_used, critical_used, normal_per_block, to_insert
    while len(probes_per_block) < 4:
        probe = str(np.random.choice(target_present,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in present_used and 'high' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    while 4 <= len(probes_per_block) < 9:
        probe = str(np.random.choice(target_absent,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in absent_used and 'high' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    
    for n in probes_per_block:
        print possible_images_dict[n]
        if 'Target Present' in possible_images_dict[n]:
            present_used.append(n)
        elif 'Target Absent' in possible_images_dict[n]:
            absent_used.append(n)
    
    probes.append(probes_per_block)
#------------------------------------------------------------------------------    
#Counting critical probes    
    critical_probes_counter = 0
    for n in probes_per_block:
        if 'Critical' in possible_images_dict[n]:
            critical_probes_counter = critical_probes_counter + 1
    #for n in probes_per_block:
    #    print possible_images_dict[n]
    print 'Present Used: ',len(present_used)
    print 'Absent Used ',len(absent_used)
    print 'Critical probes counter: ',critical_probes_counter
    
    modifier.append(critical_probes_counter)
#------------------------------------------------------------------------------
#Picking critical trials
    while len(critical_per_block) < (3-critical_probes_counter):
        image = str(np.random.choice(critical_trials,1,replace = False))[2:-2]
        if image not in critical_per_block and image not in critical_used \
            and 'No Target' in possible_images_dict[image] and 'high' in possible_images_dict[image]:
            critical_per_block.append(image) 
    print 'List of critical trials without probe: '
    for n in critical_per_block:
        critical_used.append(n)
        print possible_images_dict[n]
    #temp = []
    
    critical.append(critical_per_block)

#------------------------------------------------------------------------------
#Picking normal trials
    while len(normal_per_block) < 51 - (3 - critical_probes_counter):
        image = str(np.random.choice(normal_no_probe,1,replace = False))[2:-2]
        if image not in normal_per_block and image not in normal_no_probe_used and 'high' in possible_images_dict[image]:
            normal_per_block.append(image)
    for n in normal_per_block:
        normal_no_probe_used.append(n)
    print 'len(normal_no_probe_used): ',len(normal_no_probe_used)
    
    normal.append(normal_per_block)

#-----------------------------------------------------------------------------
   
    probes_per_block = []
    critical_per_block = []
    normal_per_block = []
    to_insert = []
    print 'Normal used:',len(normal_no_probe_used)
    print'---------------------------------------------------'
    return 


def block_high_2():
# Pick 4 present probes and 5 absent probes
    global critical_per_block,probes_per_block, present_used, absent_used, critical_used, normal_per_block, to_insert
    while len(probes_per_block) < 5:
        probe = str(np.random.choice(target_present,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in present_used and 'high' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    while 5 <= len(probes_per_block) < 9:
        probe = str(np.random.choice(target_absent,1,replace = False))[2:-2]
        if probe not in probes_per_block and probe not in absent_used and 'high' in possible_images_dict[probe]:
            probes_per_block.append(probe)
    
    for n in probes_per_block:
        print possible_images_dict[n]
        if 'Target Present' in possible_images_dict[n]:
            present_used.append(n)
        elif 'Target Absent' in possible_images_dict[n]:
            absent_used.append(n)
    
    probes.append(probes_per_block)
#------------------------------------------------------------------------------    
#Counting critical probes    
    critical_probes_counter = 0
    for n in probes_per_block:
        if 'Critical' in possible_images_dict[n]:
            critical_probes_counter = critical_probes_counter + 1
    #for n in probes_per_block:
    #    print possible_images_dict[n]
    print 'Present Used: ',len(present_used)
    print 'Absent Used ',len(absent_used)
    print 'Critical probes counter: ',critical_probes_counter
    
    modifier.append(critical_probes_counter)
#------------------------------------------------------------------------------
#Picking critical trials
    while len(critical_per_block) < (3-critical_probes_counter):
        image = str(np.random.choice(critical_trials,1,replace = False))[2:-2]
        if image not in critical_per_block and image not in critical_used \
            and 'No Target' in possible_images_dict[image] and 'high' in possible_images_dict[image]:
            critical_per_block.append(image) 
    print 'List of critical trials without probe: '
    for n in critical_per_block:
        critical_used.append(n)
        print possible_images_dict[n]
    #temp = []
    
    critical.append(critical_per_block)

#------------------------------------------------------------------------------
#Picking normal trials
    while len(normal_per_block) < 51 - (3 - critical_probes_counter):
        image = str(np.random.choice(normal_no_probe,1,replace = False))[2:-2]
        if image not in normal_per_block and image not in normal_no_probe_used and 'high' in possible_images_dict[image]:
            normal_per_block.append(image)
    for n in normal_per_block:
        normal_no_probe_used.append(n)
    print 'len(normal_no_probe_used): ',len(normal_no_probe_used)
    
    normal.append(normal_per_block)

#-----------------------------------------------------------------------------
   
    probes_per_block = []
    critical_per_block = []
    normal_per_block = []
    to_insert = []
    print 'Normal used:',len(normal_no_probe_used)
    print'---------------------------------------------------'
    return 

def building_the_church(w):
    while True:    
        while True:
            a = [random.randint(1,60) for r in xrange(9)]
            if sum(a) <= 60:
                break
        new_list_1 = []
        acc = 0
        for i in a:
            acc = acc + i
            new_list_1.append(acc)
        new_list_1 = [n - 1 for n in new_list_1]
        #print 'new_list_1: ',new_list_1
        #print sum(a)

        while True:
            while True:
                a = [random.randint(1,60) for r in xrange(3-w)]
                if sum(a) <= 60: 
                    break
            #print sum(a)
            new_list_2 = []
            acc = 0
            for i in a:
                acc = acc + i
                new_list_2.append(acc)
            #print new_list_2
            new_list_2 = [n - 1 for n in new_list_2]
            two_gap = []
            for i in range(2-w): # add "-w"
                two_gap.append(new_list_2[i+1] - new_list_2[i])
                #print two_gap
            if 1 not in two_gap and 2 not in two_gap:
                break
        #print new_list_2

        container = []
        for i in new_list_2:
            sequence = [i, i+1, i+2]
            #print sequence
            for element in sequence:
                if element in new_list_1:
                    container.append(element)
        #print len(container)
        #print new_list_2
        if len(container) == 0:
            break
    print '---------------------------'
    probe_series.append(new_list_1)
    critical_series.append(new_list_2)
    print new_list_1
    print new_list_2
    print '---------------------------'
    return 

def critical_trial(load_level):
    global critical_trials
    temp = []
    container = []
    for element in lista:
        if load_level in possible_images_dict[element]:
            container.append(element)
    for category in categories:
        while len(temp) <1 :
            intermediate = str(np.random.choice(container, 1, replace= False))[2:-2]
            if category in possible_images_dict[intermediate] \
                and intermediate not in temp and intermediate not in critical_trials:
                temp.append(intermediate)
        for each in temp:
            critical_trials.append(each)
        temp =[]
    print 'len(critical_trials): ', len(critical_trials)