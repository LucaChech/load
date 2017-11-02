

 
#IMPORTING LIBRARIES

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
sys.path.append('C:\pyo\Python27\Lib\site-packages')
from psychopy import visual
from psychopy import prefs
prefs.general['audioLib'] = ['pyo']
from psychopy import locale_setup, core, event, logging, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding
from os import listdir
from os.path import isfile, join
from shutil import copyfile
from random import shuffle
import pandas as pd
import csv
import random 
import pyglet
import time
from pdb import set_trace
import random
import numpy as np


#RECREATING exp_dict

mypath = 'C:/Users/nilli lab/Desktop/load/practice/'

df = pd.DataFrame.from_csv(mypath + 'practice.csv')

df.reset_index(drop=False,)
image_names = df.index.tolist()
cat1 = df['Cat.1'].tolist()
cat2 = df['Cat.2'].tolist()
cat3 = df['Cat.3'].tolist()
cat4 = df['Cat.4'].tolist()
cat5 = df['Cat.5'].tolist()
ts = df['TS'].tolist()
load = df['Load'].tolist()
trial_type = df['present_absent'].tolist()
critical = df['trial_type'].tolist()
my_dict ={z[0]:list(z[1:]) for z in zip(image_names,cat1,cat2,cat3,cat4,cat5,ts,load,trial_type,critical)}


categories = [' bottle', ' horse', ' pottedplant', ' dog',' cat', ' person', ' aeroplane', ' car', ' chair', ' sofa', ' bird', ' boat']
p_load = ['low','high']

#-------------------------------------------------------------------------------------------
expInfo = {u'session': u'-999', u'Participant no.': u'test'}
expInfo['date'] = 'test'
expInfo['expName'] = 'test'

#WINDOW
win = visual.Window(size=(800, 600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
# INSTRUCTIONS #
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
Instructions_screen_1 = visual.TextStim(win, 
'                                INSTRUCTIONS \n'
'\n'
'     You will be presented with a series of brief images.\n'
'\n'
'           Your task is to carefully examine each image.\n'
'              Sometimes, you will be asked whether\n'
'   a specific object (e.g. a chair) was present in the image.\n'
'\n'
'              Please reply as accurately as possible \n'
'                                    by pressing:\n'
'                        Q if the object was present\n'
'                         P if the object was absent\n'
'\n'   
'The experiment is run in short blocks with a break after \n'
'                                    each block.\n'
'\n'
'  Please keep your fingers on the Q and P keys throughout \n'
'                                      a block.\n'
'\n'
'                      press ENTER to continue'
,
alignHoriz='center',
alignVert='center',
height= 0.08,
wrapWidth=2 )

Instructions_screen_2 = visual.TextStim(win,
'                               INSTRUCTIONS \n'
'\n'
'\n'
'  Each image will be accompanied by a constant noise. \n'
'\n'
'\n'
'\n'
'      Press ENTER to hear an example of the noise. \n'
,
alignHoriz='center',
alignVert='center',
height= 0.08,
wrapWidth=2 )

Instructions_screen_3 = visual.TextStim(win,
'                               INSTRUCTIONS \n'
'\n'
'\n'
'Sometimes, in addition to the noise, you will also hear a\n'
'                                      sound. \n'
'\n'
'\n'
'\n'
'       Press ENTER to hear a few examples of the \n'
'                                     sounds. \n' 
,
alignHoriz='center',
alignVert='center',
height= 0.08,
wrapWidth=2 )


Instructions_screen_4 = visual.TextStim(win,
'           INSTRUCTIONS \n'
'\n'
'\n'
'   If you hear any sound, press\n'
'\n'
'               SPACEBAR\n'
'\n'
'\n'
'\n'
'\n'
'       Press ENTER to start.\n'
'\n' 
,
alignHoriz='center',
alignVert='center',
height= 0.08,
wrapWidth=2 )

#END OF EXPERIMENT MESSAGE
############################
############################
end_of_exp = visual.TextStim(win, 
'End of practice session.',
height=0.12)
#-------------------------------------------------------------------------------------------
noise_example = sound.Sound(mypath + 'noise_example_low.wav', secs=1)
incorrect = sound.Sound(mypath + 'wrong_buzzer.wav', secs=1)
noise = sound.Sound(mypath + 'noise_exp_low.wav', secs=1)
tone1 = sound.Sound(mypath + 'PureTone_F1500_t50_low.wav', secs=0.05)
tone2 = sound.Sound(mypath + 'PureTone_F2000_t50_low.wav', secs=0.05)
#-------------------------------------------------------------------------------------------
def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    global sequences_length
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    sequences_length = [a - b for a, b in zip(dividers + [total], [0] + dividers)]
#-------------------------------------------------------------------------------------------
lista = my_dict.keys()
random.shuffle(lista)
#-------------------------------------------------------------------------------------------
probes = []
load_level = ['low','high']
present_absent = ['Target Present', 'Target Absent']
for load in load_level:
    for element in present_absent:
        names = []
        while len(names) < 4:
            temp_name = str(np.random.choice(lista, 1, replace= False))[2:-2]
            if element in my_dict[temp_name] and load in my_dict[temp_name] and temp_name not in names:
                names.append(temp_name)
        for each in names:
            probes.append(each)
print len(probes)
print len(lista)
for probe in probes:
    if probe in lista:
        lista.remove(probe)
print len(lista)
#-------------------------------------------------------------------------------------------
constrained_sum_sample_pos(16,160)
random.shuffle(probes)
acc = 0
new_list = []
for i in sequences_length:
    acc = acc + i
    new_list.append(acc - 1)
for i in range(len(probes)):
    lista.insert(new_list[i], probes[i])
print sequences_length
print new_list
#-------------------------------------------------------------------------------------------
critical_trials_counter = 0
for each in my_dict:
    if 'Critical' in my_dict[each]:
        critical_trials_counter = critical_trials_counter + 1
print critical_trials_counter
#-------------------------------------------------------------------------------------------
####################################################################################
sound_onset = []
for i in range(32):
    a = random.uniform(0, 0.2)
    a = str(a)[0:5]
    a = float(a)
    sound_onset.append(a)
sound_onset = random.sample(sound_onset, len(sound_onset))

sound_Hz_1 = ['tone1'] * 16 + ['tone2'] * 16
sound_Hz_1 = random.sample(sound_Hz_1, len(sound_Hz_1))
sound_Hz = sound_Hz_1 
onset_counter = 0
hz_counter = 0
print len(sound_onset), len(sound_Hz)
######################################################################################
trial_counter = 0
block_dict = {}
block_dict['lista'] = lista
noise_list = [0,40,80,120]
def routine(play, block_name):
     global stimulus, sound_onset, sound_Hz, onset_counter, hz_counter , sequences, sequences_index, trial_counter, blocks_final, blocks_final_index
     block = block_dict['lista']
     image = visual.ImageStim(win=win, image= mypath + 'practice_images/' + block[stimulus])
     image.draw()
     if trial_counter in noise_list:
        noise.play()
     win.flip()
     stopwatch.reset()
     if play:
        core.wait(sound_onset[onset_counter])
        which_sound = sound_Hz[hz_counter]
        if which_sound == 'tone1':
            tone1.play()
        elif which_sound == 'tone2':
            tone2.play()
        print onset_counter
     core.wait(1, hogCPUperiod=1)
     lista = event.getKeys(keyList=['space'], timeStamped=stopwatch)
     my_dict[block[stimulus]].append(lista)
     win.flip()
     core.wait(0.3,hogCPUperiod=0.3)
########################################################################
     if trial_counter not in new_list:
        my_dict[block[stimulus]].append('Na')
        my_dict[block[stimulus]].append('Na')
        stopwatch.reset()
        if play:
            my_dict[block[stimulus]].append(sound_onset[onset_counter])
            my_dict[block[stimulus]].append(sound_Hz[hz_counter])
            onset_counter = onset_counter + 1
            hz_counter = hz_counter + 1
        if not play:
            my_dict[block[stimulus]].append('None')
            my_dict[block[stimulus]].append('None')
        my_dict[block[stimulus]].append(trial_counter)
        print 'stimulus '+ str(stimulus) +'   trial counter ' + str(trial_counter)
        print 'stimulus ' + str(my_dict[block[stimulus]])
        stopwatch.reset()
##########################################################################
     if trial_counter in new_list:
        if 'Target Present' in my_dict[block[stimulus]]:
            name = my_dict[block[stimulus]][0]
        elif 'Target Absent' in my_dict[block[stimulus]]:
            absent_categories = [category for category in categories if category not in my_dict[block[stimulus]]]
            name = str(np.random.choice(absent_categories,1))[2:-2]
        if 'pottedplant' in name:
            search_text = visual.TextStim(win, 'potted plant',
        wrapWidth=2,
        height=0.16)
        else:
            search_text = visual.TextStim(win, name ,
        wrapWidth=2,
        height=0.16)
        search_text.draw()
        win.flip()
        stopwatch.reset()
        keys = event.waitKeys(keyList=['q','p','space'],timeStamped=stopwatch)
        rt_space = -999
        wait = True
        for k in keys:
            if k[0] == 'space':
                rt_space = [k[0],k[1]]
            if k[0] == 'q' or k[0] == 'p':
                wait = False
        while wait:
            keys = event.waitKeys(keyList=['q','p'],timeStamped=stopwatch)
            letters = [t[0] for t in keys]
            if ('p' in letters) or ('q' in letters):
                wait = False
        
        my_dict[block[stimulus]].append(keys)
        my_dict[block[stimulus]].append(rt_space)
        stopwatch.reset()
        if play:
            my_dict[block[stimulus]].append(sound_onset[onset_counter])
            my_dict[block[stimulus]].append(sound_Hz[hz_counter])
            onset_counter = onset_counter + 1
            hz_counter = hz_counter + 1
        if not play:
            my_dict[block[stimulus]].append('None')
            my_dict[block[stimulus]].append('None')
        my_dict[block[stimulus]].append(trial_counter)
        stopwatch.reset()
##################################################################
        if 'Target Present' in my_dict[block[stimulus]]:
            if 'p'in my_dict[block[stimulus]][-5][0]:
                incorrect.play()
                vs_performance.append(0)
            elif 'q'in my_dict[block[stimulus]][-5][0]:
                vs_performance.append(1)
            core.wait(1)
        elif 'Target Absent' in my_dict[block[stimulus]]:
            if 'q'in my_dict[block[stimulus]][-5][0]:
                incorrect.play()
                vs_performance.append(0)
            elif 'p'in my_dict[block[stimulus]][-5][0]:
                vs_performance.append(1)
            core.wait(1)
        mean_performance = str(sum(vs_performance)/len(vs_performance)*100)
 
        if all_same(vs_performance) == True:
            mean_performance = '0'
        elif mean_performance[2] == '.':
            mean_performance = mean_performance[0:2]
        elif mean_performance[3] == '.':
            mean_performance = mean_performance[0:3]
        accuracy = visual.TextStim(win, 
        'Your accuracy is ' + mean_performance + '%',
        alignHoriz='center',
        alignVert='center',
        height= 0.14,
        wrapWidth=2 )
        accuracy.draw()
        win.flip()
        core.wait(2)
        print'stimulus '+ str(stimulus) + '   trial counter ' + str(trial_counter)
        print 'stimulus ' +str(my_dict[block[stimulus]])
#######################################################################
#CONSTANTS
response = []
reaction_t = []
sequences_length = []
absent_question = []
stopwatch = core.Clock()
i = 0
#######################################################################
Instructions_screen_1.draw()
win.flip()
event.waitKeys(keyList=['return'])
Instructions_screen_2.draw()
win.flip()
event.waitKeys(keyList=['return'])
noise_example.play()
core.wait(2)
Instructions_screen_3.draw()
win.flip()
event.waitKeys(keyList=['return'])
core.wait(1)
tone1.play()
core.wait(2)
tone2.play()
core.wait(2)
Instructions_screen_4.draw()
win.flip()
event.waitKeys(keyList=['return'])
#######################################################################
vs_performance = []
block_number = 1
sequences_index = 0

for element in new_list:
    print element
def block_handler(block_name):
    global stimulus, onset_counter, hz_counter, sound_Hz, sound_onset, block_number, vs_performance, mean_performance, sequences, sequences_index, trial_counter, blocks_final, blocks_final_index
    block = block_dict['lista']
    random.shuffle(sound_onset)
    random.shuffle(sound_Hz)
    onset_counter = 0
    hz_counter = 0
    stimulus = 0
    trial_counter = 0
    #noise.play()
    for each in range(len(block)):
        #stopwatch = core.Clock()
        event.clearEvents()
        if 'Target Present' in my_dict[block[stimulus]] and 'Critical' in my_dict[block[stimulus]]:
            routine(True, block_name)
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Present' in my_dict[block[stimulus]] and 'Normal' in my_dict[block[stimulus]]:
            routine(False, block_name)
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Absent' in my_dict[block[stimulus]] and 'Critical' in my_dict[block[stimulus]]:
            routine(True, block_name)
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Absent' in my_dict[block[stimulus]] and 'Normal' in my_dict[block[stimulus]]:
            routine(False, block_name)
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        if each in new_list:
            print vs_performance
    
def all_same(items):
    if 0 in items:
        return all(x == items[0] for x in items)
block_handler('lista')

end_of_exp.draw()
win.flip()
event.waitKeys()
win.close()

 
print df
### SAVING .CSV
df = pd.DataFrame(my_dict) 
df = df.T
df.reset_index(inplace=True)
df.columns = ['Image Name','Cat. 1', 'Cat. 2','Cat. 3','Cat. 4','Cat. 5','True Skill Rating', 'Load', 'Trial Type','Audio','RT to TO', 'RT VS', 'RT to TO','Sound Onset','Sound Hz', 'Trial N.']

df.to_csv('Participant_'+expInfo['participant']+'_practice.csv')
core.quit()

