from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual
from psychopy import prefs
prefs.general['audioLib'] = ['pyo']

from setup import *
from functions_old import *
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

run_blocks(trials,noise,visual,win,event,i_counter,expInfo,incorrect,tone1,tone2,experiment_details,allPoints)

win.close()
core.quit()