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

#mypath = 'C:/Users/KeK/OneDrive - University College London/Random_probes_last/Luca/'
mypath = 'E:/OneDrive - University College London/Random_probes_last/Luca/'

#RECREATING exp_dict
df = pd.DataFrame.from_csv(mypath + 'randomization_1.csv')

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
tone_Hz = df['tone_Hz'].tolist()
tone_onset = df['tone_onset'].tolist()

my_dict ={z[0]:list(z[1:]) for z in zip(image_names,cat1,cat2,cat3,cat4,cat5,ts,load,exemplar,question,trial_type,critical,tone_Hz,tone_onset)}

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

blocks_final = [low_one, high_one, high_two, low_two, high_three, low_three, low_four, high_four, low_five, high_five, high_six, low_six, high_seven, low_seven, low_eight, high_eight]

#-----------------------------------------------------------------------------------------------------------------------------------------------------
probes_position_list = []
with open('filename2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        probes_position_list.append(row)

list_low_one = probes_position_list[0]
list_low_two = probes_position_list[1]
list_low_three = probes_position_list[2]
list_low_four = probes_position_list[3]
list_low_five = probes_position_list[4]
list_low_six = probes_position_list[5]
list_low_seven = probes_position_list[6]
list_low_eight = probes_position_list[7]
list_high_one = probes_position_list[8]
list_high_two = probes_position_list[9]
list_high_three = probes_position_list[10]
list_high_four = probes_position_list[11]
list_high_five = probes_position_list[12]
list_high_six = probes_position_list[13]
list_high_seven = probes_position_list[14]
list_high_eight = probes_position_list[15]



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

list_low_one = [int(n[1:-1]) for n in list_low_one ]
list_low_two = [int(n[1:-1]) for n in list_low_two]
list_low_three = [int(n[1:-1]) for n in list_low_three ]
list_low_four = [int(n[1:-1]) for n in list_low_four ]
list_low_five = [int(n[1:-1]) for n in list_high_five ]
list_low_six = [int(n[1:-1]) for n in list_low_six ]
list_low_seven = [int(n[1:-1]) for n in list_low_seven ]
list_low_eight = [int(n[1:-1]) for n in list_low_eight ]
list_high_one = [int(n[1:-1]) for n in list_high_one ]
list_high_two = [int(n[1:-1]) for n in list_high_two ]
list_high_three= [int(n[1:-1]) for n in list_high_three]
list_high_four = [int(n[1:-1]) for n in list_high_four ]
list_high_five = [int(n[1:-1]) for n in list_high_five ]
list_high_six = [int(n[1:-1]) for n in list_high_six ]
list_high_seven = [int(n[1:-1]) for n in list_high_seven ]
list_high_eight= [int(n[1:-1]) for n in list_high_eight ]

probes_position_list = [list_low_one, list_high_one, list_high_two, list_low_two, list_high_three, list_low_three, list_low_four, list_high_four, list_low_five, list_high_five, list_high_six, list_low_six, list_high_seven, list_low_seven, list_low_eight, list_high_eight]
#-------------------------------------------------------------------------------------------
blocks_final_index = 0
probes_position_index = 0
#block = blocks_final[blocks_final_index]
timer = core.Clock()
i_counter = 0
block_number = 1
#-------------------------------------------------------------------------------------------
#REWARD PARAMETERS
decay = 10
trialthresh = 4
pointval = 10
allPoints=0
bPoints=0
#-------------------------------------------------------------------------------------------
#expName = 'participant info'  
#expInfo = {u'session': u'001', u'participant': u''}
#dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
#if dlg.OK == False: core.quit()  
#expInfo['date'] = data.getDateStr()  
#expInfo['expName'] = expName

#WINDOW
win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
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
'          Please reply as quickly and accurately as possible \n'
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
'        as quickly as possible. \n'
'\n'
'\n'
'    Press ENTER to continue.\n'
'\n' 
,
alignHoriz='center',
alignVert='center',
height= 0.08,
wrapWidth=2 )


Instructions_screen_5 = visual.TextStim(win, 
'                                                       INSTRUCTIONS\n'
'\n'

'                        Remember, you primary task is to examine the images\n'
'               and make a correct response regarding the presence or absence\n'
'                                                   of the probed object.\n'
'\n'
'           You will be awarded with a bonus if you earn XXX or more points\n'
'                   Points are only allocated when you make a correct response\n'
'                                                  to the probed object.\n'
'\n'
'\n'
'                                                   Press ENTER to start.'
,
alignHoriz='center',
alignVert='center',
height= 0.08,
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

happy = visual.ImageStim(win, image='Happy.bmp', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, name=None, autoLog=None, maskParams=None)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#SOUNDS
noise_example = sound.Sound(mypath + 'noise_example_low.wav', secs=1)
incorrect = sound.Sound(mypath + 'wrong_buzzer.wav', secs=1)
noise = sound.Sound(mypath + 'noise_exp_low.wav', secs=1)
tone1 = sound.Sound(mypath + 'PureTone_F1500_t50_low.wav', secs=0.05)
tone2 = sound.Sound(mypath + 'PureTone_F2000_t50_low.wav', secs=0.05)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
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
Instructions_screen_5.draw()
win.flip()
event.waitKeys(keyList=['return'])
core.wait(1)

#a = 0
#print probes_position_list[probes_position_index]
#for pic in block:
#     print a, my_dict[pic[1:-1]][12], type(my_dict[pic[1:-1]][12])
#    if 'Critical' in my_dict[pic[1:-1]]:
#        print a, my_dict[pic[1:-1]]
#    a = a+1
for block in blocks_final:
    for pic in block:
        probe_response = 't'
        noise.play()
        timer.reset()
        image = visual.ImageStim(win=win, image= mypath + 'exp_images/'+ pic[1:-1])
        responded = False
        start_frame = ((int(my_dict[pic[1:-1]][12]) + 17 // 2) // 17) -1 # final -1 is to compensate for lag
        #CHANGE 17 WITH ACTUAL FRAMERATE
        for frameN in range(60):
            if 'tone1' in my_dict[pic[1:-1]] and frameN == start_frame :
                tone1.play()
                print start_frame, my_dict[pic[1:-1]][12]
            elif 'tone2' in my_dict[pic[1:-1]] and frameN == start_frame:
                tone2.play()
                print start_frame, my_dict[pic[1:-1]][12]
            elif 'tone3' in my_dict[pic[1:-1]] and frameN == start_frame:
                tone3.play()
                print start_frame, my_dict[pic[1:-1]][12]
            elif 'tone4' in my_dict[pic[1:-1]] and frameN == start_frame:
                tone4.play()
                print start_frame, my_dict[pic[1:-1]][12]
            image.draw()
            win.flip()
        for frameN in range(20):
            win.flip()
        response = event.getKeys(keyList = ['space','c'], timeStamped = timer)
        if 'c' in response:
            win.close()
            core.quit()
        #NOT WORKING
        if len(response) == 0:
            my_dict[pic[1:-1]].append('No spacebar')
            my_dict[pic[1:-1]].append('No timing')
        if len(response) >= 1:
            my_dict[pic[1:-1]].append(response[0][0])
            my_dict[pic[1:-1]].append(response[0][1])
            
        if i_counter in probes_position_list[probes_position_index]:
            name=my_dict[pic[1:-1]][8]
            if 'pottedplant' in name:
                name = 'potted plant'
            search_text = visual.TextStim(win, name , wrapWidth=2, height=0.16)
            search_text.draw()
            win.flip()
            keys = event.waitKeys(keyList=['q','p','space'],timeStamped=timer)
            #core.wait(1)
            rt_space = -999
            wait = True
            for k in keys:
                if k[0] == 'space':
                    rt_space = [k[0],k[1]]
                if k[0] == 'q' or k[0] == 'p':
                    wait = False
            while wait:
                keys = event.waitKeys(keyList=['q','p'],timeStamped=timer)
                letters = [t[0] for t in keys]
                if ('p' in letters) or ('q' in letters):
                    wait = False
            my_dict[pic[1:-1]].append(keys[0][0])
            my_dict[pic[1:-1]].append(str(keys[0][1]))
            my_dict[pic[1:-1]].append(rt_space)
            my_dict[pic[1:-1]][16] = float(my_dict[pic[1:-1]][16][0:5])
            if 'Target Present' in my_dict[pic[1:-1]] and 'p' in my_dict[pic[1:-1]][15]:
                incorrect.play()
            elif 'Target Absent' in my_dict[pic[1:-1]] and 'q' in my_dict[pic[1:-1]][15]:
                incorrect.play()
            else:
                RT = my_dict[pic[1:-1]][16] - 1.3
                #tPoints = round(pointval - (decay*RT))
                tPoints = 3
                bPoints = bPoints + tPoints
                allPoints =  allPoints + tPoints
                print tPoints
                print RT
                print bPoints
                #if tPoints >= trialthresh:
                #    for frameN in range(20):
                #        happy.draw()
                #        win.flip()
            win.flip()
            core.wait(1.5)
        if i_counter not in probes_position_list[probes_position_index]:
            my_dict[pic[1:-1]].append('Na')
            my_dict[pic[1:-1]].append('Na')
            my_dict[pic[1:-1]].append('Na')
        my_dict[pic[1:-1]].append(i_counter)
        my_dict[pic[1:-1]].append(block_number)
        i_counter = i_counter + 1
        
        w = csv.writer(open('output.csv', 'w'))
        for key, val in my_dict.items():
            w.writerow([key, val])
    if probes_position_index < 15:
        end_of_block = visual.TextStim(win, 
        'You have earned a total of ' + str(bPoints) + ' points in this block.\n'
        '\n'
        'Try to earn an average of 24 per each block to get the bonus!\n'
        '\n'
        '\n'
        'Press ENTER to start the next block.\n',
        height=0.10)
        end_of_block.draw()
        win.flip()
        event.waitKeys(keyList=['return'])
    if probes_position_index == 15:
        end_of_experiment.draw()
        win.flip()
        core.wait(5)
        win.close()
        core.quit()

    block_number = block_number + 1
    i_counter = 0
    probes_position_index = probes_position_index + 1
    
    print my_dict[pic[1:-1]]
    #print response
    #print len(response)
    #END OF BLOCK MESSAGE
############################
############################
    
    bPoints = 0
print allPoints
win.close()
core.quit()

