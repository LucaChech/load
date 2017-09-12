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

probes_position_list = [list_low_one, list_low_two, list_low_three, list_low_four, list_high_one, list_high_two, list_high_three, list_high_four, list_low_five, list_low_six, list_low_seven, list_low_eight, list_high_five, list_high_six, list_high_seven, list_high_eight]
blocks_final_index = 0
probes_position_list_index = 0

block = blocks_final[blocks_final_index]


#WINDOW
win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

for pic in block[0:10]:
    image = visual.ImageStim(win=win, image= mypath + 'exp_images/'+ pic[1:-1])
    for frameN in range(60):
        image.draw()
        win.flip()
    for frameN in range(30):
        win.flip()
    if 
    #print my_dict[pic[1:-1]]
core.quit()

