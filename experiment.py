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
import pickle

from setup import *
from functions import *
from instructions import *

#import functions
#functions.myfunction()
# myfunction()

debug = False


#RECREATING exp_dict
df = pd.DataFrame.from_csv('config/randomization_1.csv')

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


blocks_final_index = 0
probes_position_index = 0
#block = blocks_final[blocks_final_index]
timer = core.Clock()
i_counter = 0
block_number = 1
trial_number = 1

experiment_details = {}

#REWARD PARAMETERS
decay = 10
trialthresh = 4
pointval = 10
allPoints=0
bPoints=0


if debug:
    expInfo ={u'session': u'-999', u'Participant no.': u'test'}
    expInfo['date'] = 'test'
    expInfo['expName'] = 'test'
else:
    expName = 'participant info'  
    expInfo = {u'Age': u'1', u'Sex': u'', u'Right handed?':'1', u'Participant no.':'1'}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False: core.quit()  
    expInfo['date'] = data.getDateStr()  
    expInfo['expName'] = expName

if debug:
    win = visual.Window(size=(800, 600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
else:
    win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        )
    
    
search_text = visual.TextStim(win, 'TEST' , wrapWidth=2, height=0.16)
 
win.flip()

noise_example = sound.Sound( '../load-data/noise_example_low.wav', secs=1)
incorrect = sound.Sound( '../load-data/wrong_buzzer.wav', secs=1)
noise = sound.Sound( '../load-data/noise_exp_low.wav', secs=1)
tone1 = sound.Sound( '../load-data/PureTone_F1500_t50_low.wav', secs=0.05)
tone2 = sound.Sound( '../load-data/PureTone_F2000_t50_low.wav', secs=0.05)

if not debug:
    print_instructions(win,noise_example,tone1,tone2)


i_counter,probes_position_index,block_number,experiment_details,allPoints,trial_number = run_blocks(blocks_final[0:8],noise,timer,visual,win,my_dict,event,i_counter,probes_position_list,probes_position_index,block_number,expInfo,incorrect,tone1,tone2,experiment_details,allPoints,trial_number)


print allPoints


#RECREATING exp_dict
df = pd.DataFrame.from_csv( 'config/randomization_2.csv')

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


i_counter,probes_position_index,block_number,experiment_details,allPoints,trial_number = run_blocks(blocks_final[8:],noise,timer,visual,win,my_dict,event,i_counter,probes_position_list,probes_position_index,block_number,expInfo,incorrect,tone1,tone2,experiment_details,allPoints,trial_number)


win.close()
core.quit()