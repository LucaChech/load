#IMPORTING LIBRARIES
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual
from psychopy import prefs
prefs.general['audioLib'] = ['pyo']
from psychopy import locale_setup, core, data, event, logging, sound, gui
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

mypath = 'C:/Users/KeK/OneDrive - University College London/Random_probes_last/Luca/'

#RECREATING exp_dict
df = pd.DataFrame.from_csv(mypath + 'randomization_1_2.csv')

df.reset_index(drop=False,) 
image_names = df.index.tolist()
cat1 = df['Cat.1'].tolist()
cat2 = df['Cat.2'].tolist()
cat3 = df['Cat.3'].tolist()
cat4 = df['Cat.4'].tolist()
cat5 = df['Cat.5'].tolist()
ts = df['TS'].tolist()
load = df['Load'].tolist()
exemplar = df['exemplar'].tolist()
question = df['question'].tolist()
trial_type = df['present_absent'].tolist()
critical = df['trial_type'].tolist()
my_dict ={z[0]:list(z[1:]) for z in zip(image_names,cat1,cat2,cat3,cat4,cat5,ts,load,exemplar,question,trial_type,critical)}

blocks_final = []
with open('filename.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        #print ', '.join(row)
        blocks_final.append(row)

low_one = blocks_final[0]
low_two = blocks_final[1]
low_three = blocks_final[2]
low_four = blocks_final[3]
low_five = blocks_final[4]
low_six = blocks_final[5]
low_seven = blocks_final[6]
low_eight = blocks_final[7]
high_one = blocks_final[8]
high_two = blocks_final[9]
high_three = blocks_final[10]
high_four = blocks_final[11]
high_five = blocks_final[12]
high_six = blocks_final[13]
high_seven = blocks_final[14]
high_eight = blocks_final[15]

low_one = [x.strip() for x in low_one[0].split(',')]
low_two = [x.strip() for x in low_two[0].split(',')]
low_three = [x.strip() for x in low_three[0].split(',')]
low_four = [x.strip() for x in low_four[0].split(',')]
low_five = [x.strip() for x in low_five[0].split(',')]
low_six = [x.strip() for x in low_six[0].split(',')]
low_seven = [x.strip() for x in low_seven[0].split(',')]
low_eight = [x.strip() for x in low_eight[0].split(',')]
high_one = [x.strip() for x in high_one[0].split(',')]
high_two = [x.strip() for x in high_two[0].split(',')]
high_three = [x.strip() for x in high_three[0].split(',')]
high_four = [x.strip() for x in high_four[0].split(',')]
high_five = [x.strip() for x in high_five[0].split(',')]
high_six = [x.strip() for x in high_six[0].split(',')]
high_seven = [x.strip() for x in high_seven[0].split(',')]
high_eight = [x.strip() for x in high_eight[0].split(',')]

blocks_final = [low_one, low_two, low_three, low_four, high_one, high_two, high_three, high_four, low_five, low_six, low_seven, low_eight, high_five, high_six, high_seven, high_eight]

#-----------------------------------------------------------------------------------------------------------------------------------------------------
sequences = []
with open('filename2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        #print ', '.join(row)
        sequences.append(row)
print sequences

list_low_one = sequences[0]
list_low_two = sequences[1]
list_low_three = sequences[2]
list_low_four = sequences[3]
list_low_five = sequences[4]
list_low_six = sequences[5]
list_low_seven = sequences[6]
list_low_eight = sequences[7]
list_high_one = sequences[8]
list_high_two = sequences[9]
list_high_three = sequences[10]
list_high_four = sequences[11]
list_high_five = sequences[12]
list_high_six = sequences[13]
list_high_seven = sequences[14]
list_high_eight = sequences[15]



list_low_one = [x.strip() for x in list_low_one[0].split(',')]
list_low_two = [x.strip() for x in list_low_two[0].split(',')]
list_low_three = [x.strip() for x in list_low_three[0].split(',')]
list_low_four = [x.strip() for x in list_low_four[0].split(',')]
list_low_five = [x.strip() for x in list_low_five[0].split(',')]
list_low_six = [x.strip() for x in list_low_six[0].split(',')]
list_low_seven = [x.strip() for x in list_low_seven[0].split(',')]
list_low_eight = [x.strip() for x in list_low_eight[0].split(',')]
list_high_one = [x.strip() for x in list_high_one[0].split(',')]
list_high_two = [x.strip() for x in list_high_two[0].split(',')]
list_high_three = [x.strip() for x in list_high_three[0].split(',')]
list_high_four = [x.strip() for x in list_high_four[0].split(',')]
list_high_five = [x.strip() for x in list_high_five[0].split(',')]
list_high_six = [x.strip() for x in list_high_six[0].split(',')]
list_high_seven = [x.strip() for x in list_high_seven[0].split(',')]
list_high_eight = [x.strip() for x in list_high_eight[0].split(',')]

sequences = [list_low_one, list_low_two, list_low_three, list_low_four, list_high_one, list_high_two, list_high_three, list_high_four, list_low_five, list_low_six, list_low_seven, list_low_eight, list_high_five, list_high_six, list_high_seven, list_high_eight]


blocks_final_index = 0
#-------------------------------------------------------------------------------------------
expName = 'participant info'  
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  
expInfo['date'] = data.getDateStr()  
expInfo['expName'] = expName


# CREATING TRIAL OBJECTS

#WINDOW
win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# FIXATION CROSS
cross = visual.TextStim(win, '+', color='black')

#SOUND
noise = sound.Sound(mypath + 'noise_exp_low.wav', secs=1)
noise_example = sound.Sound(mypath + 'noise_example_low.wav', secs=1)
tone1 = sound.Sound(mypath + 'tonesUpdated2/Luca/tones/Subject '+expInfo['participant']+'.1'+'/PureTone_F500_t50.wav', secs=0.05)
tone2 = sound.Sound(mypath + 'tonesUpdated2/Luca/tones/Subject '+expInfo['participant']+'.2'+'/PureTone_F1000_t50.wav', secs=0.05)
tone3 = sound.Sound(mypath + 'tonesUpdated2/Luca/tones/Subject '+expInfo['participant']+'.3'+'/PureTone_F1500_t50.wav', secs=0.05)
tone4 = sound.Sound(mypath + 'tonesUpdated2/Luca/tones/Subject '+expInfo['participant']+'.4'+'/PureTone_F2000_t50.wav', secs=0.05)
incorrect = sound.Sound(mypath + 'wrong_buzzer.wav', secs=1)
# INSTRUCTIONS
Instructions_screen_1 = visual.TextStim(win, 
'                                INSTRUCTIONS \n'
'\n'
'   You will be presented with a series of briefly displayed\n'
'                                       images.\n'
'           Your task is to carefully examine each image.\n'
'              Sometimes, you will be asked whether\n'
'   a specific object (e.g. a chair) was present in the image.\n'
'       Please reply as quickly and accurately as possible \n'
'                                    by pressing:\n'
'                        P if the object was present\n'
'                         Q if the object was absent\n'
'   The experiment is run in short blocks with a break after \n'
'                                    each block.\n'
'  Please keep your fingers on the Q and P keys throughout \n'
'                                      a block.\n'
'                     press SPACEBAR to continue'
,
alignHoriz='center',
alignVert='center',
height= 0.10,
wrapWidth=2 )

Instructions_screen_2 = visual.TextStim(win,
'  Each image will be accompanied by a constant noise. \n'
'\n'
'\n'
'\n'
'   Press SPACEBAR to hear an example of the noise. \n'
,
alignHoriz='center',
alignVert='center',
height= 0.10,
wrapWidth=2 )

Instructions_screen_3 = visual.TextStim(win,
'Sometimes, in addition to the noise, you will also hear a\n'
'                                      sound. \n'
'\n'
'\n'
'\n'
'   Press SPACEBAR to hear a few examples of the \n'
'                                     sounds. \n' 
,
alignHoriz='center',
alignVert='center',
height= 0.10,
wrapWidth=2 )

Instructions_screen_4 = visual.TextStim(win,
'   If you hear any sound, press\n' 
'               SPACEBAR\n'
'        as quickly as possible, \n'
'      and only afterwards reply \n'
'   to the image-related question\n'
'           by pressing either \n'
'Q if the target object was absent \n'
'                       or \n'
'P if the target object was present \n'
'\n'
'\n' 
'     Press SPACEBAR to start.'
,
alignHoriz='center',
alignVert='center',
height= 0.10,
wrapWidth=2 )


#END OF EXPERIMENT MESSAGE
############################
############################
end_of_exp = visual.TextStim(win, 
'The experiment is over.\n'
'\n'
'\n'
'\n'
'          Thank you.',
height=0.12)

#Empty message
empty = visual.TextStim(win,'')
blank =visual.Rect(win, width=0.5, height=0.5,fillColor='Black')
####################################################################################
sound_onset = []
for i in range(80):
    a = random.uniform(0, 1)
    a = str(a)[0:5]
    a = float(a)
    sound_onset.append(a)
sound_onset = random.sample(sound_onset, len(sound_onset))

sound_Hz_1 = ['tone1'] * 10 + ['tone2'] * 10 + ['tone3'] * 10 + ['tone4'] * 10
sound_Hz_2 = ['tone1'] * 10 + ['tone2'] * 10 + ['tone3'] * 10 + ['tone4'] * 10
sound_Hz_1 = random.sample(sound_Hz_1, len(sound_Hz_1))
sound_Hz_2 = random.sample(sound_Hz_2, len(sound_Hz_2))
sound_Hz = sound_Hz_1 + sound_Hz_2
onset_counter = 0
hz_counter = 0
trial_n = 0
print len(sound_onset), len(sound_Hz)
######################################################################################
trial_counter = 0
tempo = core.Clock()
stopwatch = core.Clock()
def routine(play, block_name):
     global stimulus, sound_onset, sound_Hz, onset_counter, hz_counter , sequences, sequences_index, trial_counter, blocks_final, blocks_final_index
     block = blocks_final[blocks_final_index]
     image = visual.ImageStim(win=win, image= mypath + 'exp_images/'+ block[stimulus][1:-1])
     image.draw()
     win.flip()
     image.setAutoDraw(False)
     tempo.reset()
     stopwatch.reset()
     space_pressed = False
     late_press = []
     while tempo.getTime()  <=1 :
        space_rt = event.getKeys(keyList=['space'],timeStamped=tempo)
        if space_rt != [] and space_pressed == False:
            #print space_rt, tempo.getTime()
            my_dict[block[stimulus][1:-1]].append(space_rt)
            space_pressed = True
        if play:
            which_sound = sound_Hz[hz_counter]
            if sound_onset[onset_counter] - 0.005 <  tempo.getTime() <  sound_onset[onset_counter] + 0.005:
                if which_sound == 'tone1':
                    tone1.play()
                    #tempo.reset()
                elif which_sound == 'tone2':
                    tone2.play()
                    #tempo.reset()
                elif which_sound == 'tone3':
                    tone3.play()
                    #tempo.reset()
                elif which_sound == 'tone4':
                    tone4.play()
                    #tempo.reset()
     #image.setAutoDraw(False)
     win.flip()
     #core.wait(0.3, hogCPUperiod=0.3)
     #if space_pressed == 0:
     #   late_press = event.waitKeys(maxWait = 0.3,keyList=['space'],timeStamped=stopwatch)
     #if late_press != []:
     #   my_dict[block[stimulus]].append(late_press)
     if space_pressed == 0: #and late_press == []:
        my_dict[block[stimulus][1:-1]].append('None')

##########################################################################
     if trial_counter not in sequences[sequences_index]:
        my_dict[block[stimulus]][2:-2].append('Na')
        my_dict[block[stimulus][2:-2]].append('Na')
        #stopwatch.reset()
        if play:
            my_dict[block[stimulus]][1:-1].append(sound_onset[onset_counter])
            my_dict[block[stimulus][1:-1]].append(sound_Hz[hz_counter])
            onset_counter = onset_counter + 1
            hz_counter = hz_counter + 1
        if not play:
            my_dict[block[stimulus][1:-1]].append('None')
            my_dict[block[stimulus][1:-1]].append('None')
        my_dict[block[stimulus][1:-1]].append(trial_counter)
        print 'stimulus '+ str(stimulus) +'   trial counter ' + str(trial_counter)
        print 'stimulus ' + str(my_dict[block[stimulus][1:-1]])
        #stopwatch.reset()
        tempo.reset()
##########################################################################
     if trial_counter in sequences[sequences_index]:
        #core.wait(1)
        print tempo.getTime()
        name=my_dict[block[stimulus]][8] 
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
        #stopwatch.reset()
        keys = event.waitKeys(keyList=['q','p','space'],timeStamped=tempo)
        rt_space = -999
        wait = True
        for k in keys:
            if k[0] == 'space':
                rt_space = [k[0],k[1]]
            if k[0] == 'q' or k[0] == 'p':
                wait = False
        while wait:
            keys = event.waitKeys(keyList=['q','p'],timeStamped=tempo)
            letters = [t[0] for t in keys]
            if ('p' in letters) or ('q' in letters):
                wait = False

        my_dict[block[stimulus][1:-1]].append(keys)
        my_dict[block[stimulus][1:-1]].append(rt_space)
        #stopwatch.reset()
        if play:
            my_dict[block[stimulus][1:-1]].append(sound_onset[onset_counter])
            my_dict[block[stimulus][1:-1]].append(sound_Hz[hz_counter])
            onset_counter = onset_counter + 1
            hz_counter = hz_counter + 1
        if not play:
            my_dict[block[stimulus][1:-1]].append('None')
            my_dict[block[stimulus][1:-1]].append('None')
        my_dict[block[stimulus][1:-1]].append(trial_counter)
        #stopwatch.reset()
        
        if 'Target Present' in my_dict[block[stimulus]]:
            if 'q'in my_dict[block[stimulus]][-5][0]:
                incorrect.play()
                vs_performance.append(0)
            elif 'p'in my_dict[block[stimulus]][-5][0]:
                vs_performance.append(1)
            core.wait(1)
        elif 'Target Absent' in my_dict[block[stimulus]]:
            if 'p'in my_dict[block[stimulus]][-5][0]:
                incorrect.play()
                vs_performance.append(0)
            elif 'q'in my_dict[block[stimulus]][-5][0]:
                vs_performance.append(1)
            core.wait(1)
        tempo.reset()
### REWARD PROCEDURE ###
        #mean_performance = str(sum(vs_performance)/len(vs_performance)*100)
        #if all_same(vs_performance) == True:
        #    mean_performance = '0'
        #elif mean_performance[2] == '.':
        #    mean_performance = mean_performance[0:2]
        #elif mean_performance[3] == '.':
        #    mean_performance = mean_performance[0:3]
        #accuracy = visual.TextStim(win, 
        #'Your accuracy is ' + mean_performance + '%',
        #alignHoriz='center',
        #alignVert='center',
        #height= 0.14,
        #wrapWidth=2 )
        #accuracy.draw()
        #win.flip()
        #core.wait(2)
########################
        print'stimulus '+ str(stimulus) + '   trial counter ' + str(trial_counter)
        print 'stimulus ' +str(my_dict[block[stimulus]])
#######################################################################
#CONSTANTS
response = []
reaction_t = []
sequences_length = []
absent_question = []
#stopwatch = core.Clock()
i = 0
#######################################################################
#Instructions_screen_1.draw()
#win.flip()
#event.waitKeys(keyList=['space'])
#Instructions_screen_2.draw()
#win.flip()
#event.waitKeys(keyList=['space'])
#noise_example.play()
#core.wait(2)
#Instructions_screen_3.draw()
#win.flip()
#event.waitKeys(keyList=['space'])
#core.wait(1)
#tone1.play()
#core.wait(2)
#tone2.play()
#core.wait(2)
#tone3.play()
#core.wait(2)
#tone4.play()
#core.wait(2)
#Instructions_screen_4.draw()
#win.flip()
#event.waitKeys(keyList=['space'])
vs_performance = []
block_number = 1
sequences_index = 0
print len(low_one)
for element in sequences[sequences_index]:
    print element
def block_handler(block_name):
    global stimulus, onset_counter, hz_counter, sound_Hz, sound_onset, block_number, vs_performance, mean_performance, sequences, sequences_index, trial_counter, blocks_final, blocks_final_index, trial_n
    block = blocks_final[blocks_final_index]
    print 'Len of current block (inside block_handler:)', len(blocks_final[blocks_final_index])
    random.shuffle(sound_onset)
    random.shuffle(sound_Hz)
    onset_counter = 0
    hz_counter = 0
    stimulus = 0
    trial_counter = 0
    noise.play()
    print sequences[sequences_index]
    for each in range(len(block)):
        #stopwatch = core.Clock()
        event.clearEvents()
        if 'No Target' in my_dict[block[stimulus][1:-1]] and 'Critical' in my_dict[block[stimulus][1:-1]]:
            routine(True, block_name)
            if 'q' in my_dict[block[stimulus]][-5][0]:
                core.wait(1)
            my_dict[block[stimulus]].append(trial_n)
            trial_n = trial_n + 1
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'No Target' in my_dict[block[stimulus]] and 'Normal' in my_dict[block[stimulus]]:
            routine(False,  block_name)
            if 'q' in my_dict[block[stimulus]][-5][0]:
                core.wait(1)
            my_dict[block[stimulus]].append(trial_n)
            trial_n = trial_n + 1
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Present' in my_dict[block[stimulus]] and 'Critical' in my_dict[block[stimulus]]:
            routine(True, block_name)
            if 'q' in my_dict[block[stimulus]][-5][0]:
                event.waitKeys(keyList = ['f'])
                core.wait(1)
            my_dict[block[stimulus]].append(trial_n)
            trial_n = trial_n + 1
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Present' in my_dict[block[stimulus]] and 'Normal' in my_dict[block[stimulus]]:
            routine(False, block_name)
            if 'q' in my_dict[block[stimulus]][-5][0]:
                event.waitKeys(keyList = ['f'])
                core.wait(1)
            my_dict[block[stimulus]].append(trial_n)
            trial_n = trial_n + 1
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Absent' in my_dict[block[stimulus]] and 'Critical' in my_dict[block[stimulus]]:
            routine(True, block_name)
            if 'p' in my_dict[block[stimulus]][-5][0]:
                event.waitKeys(keyList = ['f'])
                core.wait(1)
            my_dict[block[stimulus]].append(trial_n)
            trial_n = trial_n + 1
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        elif 'Target Absent' in my_dict[block[stimulus]] and 'Normal' in my_dict[block[stimulus]]:
            routine(False, block_name)
            if 'p' in my_dict[block[stimulus]][-5][0]:
                event.waitKeys(keyList = ['f'])
                core.wait(1)
            my_dict[block[stimulus]].append(trial_n)
            trial_n = trial_n + 1
            stimulus = stimulus + 1
            trial_counter = trial_counter + 1
        if each in sequences[sequences_index]:
            print vs_performance
    sequences_index = sequences_index + 1
    if block_number <= 7:
        end_of_block = visual.TextStim(win, 
        'End of block ' + str(block_number),
        alignHoriz='center',
        alignVert='center',
        height= 0.14,
        wrapWidth=2 )
        end_of_block.draw()
        win.flip()
        core.wait(2)
        block_number = block_number + 1
#-------------------------------------------------------------------
        waiting_list = [i for i in range(10,0,-1)]
        for i in range(len(waiting_list)):
            waiting = visual.TextStim(win, 
        'Block '+str(block_number)+' beginning in '+str(waiting_list[i]) ,
        alignHoriz='center',
        alignVert='center',
        height= 0.14,
        wrapWidth=2 )
            waiting.draw()
            win.flip()
            core.wait(1)
#-------------------------------------------------------------------
        blocks_final_index = blocks_final_index + 1
        win.flip()
#-------------------------------------------------------------------
def all_same(items):
    if 0 in items:
        return all(x == items[0] for x in items) 
block_handler('low_one')
block_handler('high_one')
block_handler('high_two')
block_handler('low_two')
block_handler('high_three')
block_handler('low_three')
block_handler('low_four')
block_handler('high_four')
end_of_exp.draw()
win.flip()
core.wait(3)
win.close()

#dict_small1 = {key:my_dict[key] for key in low_one}
#dict_small2 = {key:my_dict[key] for key in high_one}
#z = dict_small1.copy()
#z.update(dict_small2)
#df = pd.DataFrame(z) 
#df = df.T
#df.reset_index(inplace=True)
#df.columns = ['Image Name','Cat. 1', 'Cat. 2','Cat. 3','Cat. 4','Cat. 5','True Skill Rating', 'Load','Exemplar','To be asked', 'Trial Type','Audio','RT to TO', 'RT VS', 'RT to TO','Sound Onset','Sound Hz','Trial Counter','trial_n']
#df.to_csv('Participant_'+expInfo['participant']+'_experiment.csv') 
print df
### SAVING .CSV
df = pd.DataFrame(my_dict) 
df = df.T
df.reset_index(inplace=True)
df.columns = ['Image Name','Cat. 1', 'Cat. 2','Cat. 3','Cat. 4','Cat. 5','True Skill Rating', 'Load','Exemplar of','To be asked', 'Trial Type','Audio','RT to TO', 'RT VS', 'RT to TO','Sound Onset','Sound Hz', 'Trial N.','trial_n']

df.to_csv('Participant_'+expInfo['participant']+'_experiment.csv')
core.quit()