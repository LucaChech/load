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

#WINDOW
win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )



Instructions_screen_5 = visual.TextStim(win, 
'                                             INSTRUCTIONS\n'
'\n'

'                Remember, you primary task is to examine the images\n'
'       and make a correct response regarding the presence or absence\n'
'                                         of the probed object.\n'
'\n'
'         You will be awarded with a bonus if you earn 384 or more points\n'
'             Points are only allocated when you make a correct response\n'
'                                          to the probed object.\n'
'\n'
'\n'
'                                          Press ENTER to start.'
,
alignHoriz='center',
alignVert='center',
height= 0.08,
wrapWidth=2 )

Instructions_screen_5.draw()
win.flip()
event.waitKeys(keyList = ['space'])
win.close()
core.quit()
