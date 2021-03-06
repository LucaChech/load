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


debug = True

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
#else:
   # win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
   #     monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
   #     blendMode='avg', useFBO=True,
    #    )
    
    
#search_text = visual.TextStim(win, 'TEST' , wrapWidth=2, height=0.16)
 
#win.flip()

#
if not debug:
    print_instructions(win,noise_example,tone1,tone2)
    
c=core.Clock()
c2=core.Clock()
print 'k1'
core.wait(10, hogCPUperiod=10)
c.reset()
c2.reset()
#r = event.getKeys(keyList=['space'], timeStamped=c)
from keyboard import *
print 'keys?'
RT_TO, RT_VS, q_or_p = get_keys_after_visual_search_question(c,c2)
print RT_TO,RT_VS, q_or_p

print 'k'
