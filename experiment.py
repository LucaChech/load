from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
sys.path.append('C:\pyo\Python27\Lib\site-packages')
from psychopy import prefs, sound
prefs.general['audioLib'] = ['pyo']

from setup import *
from functions_old import *
from instructions import *



debug = False
timer = core.Clock()
i_counter = 0
block_number = 1
trial_number = 1



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
    expInfo = {u'session': u'-999', u'Participant no.': u'test'}
    expInfo['date'] = 'test666'
    expInfo['expName'] = 'test'
    # from psychopy import gui
    # from psychopy import data
    # expName = 'participant info'
    # expInfo = {u'Age': u'1', u'Sex': u'', u'Right handed?':'1', u'Participant no.':'1'}
    # dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    # if dlg.OK == False: core.quit()
    # expInfo['date'] = data.getDateStr()
    # expInfo['expName'] = expName

if debug:
    win = visual.Window(size=(800, 600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
else:
    win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True)

# search_text = visual.TextStim(win, 'TEST' , wrapWidth=2, height=0.16)
# win.flip()
#This stopped (or caused) a TextStim crash

noise_example = sound.Sound( '../load-data/noise_example_low.wav', secs=1)
incorrect = sound.Sound( '../load-data/wrong_buzzer.wav', secs=1)
noise = sound.Sound( '../load-data/noise_exp_low.wav', secs=1)
tone1 = sound.Sound( '../load-data/PureTone_F1500_t50_low.wav', secs=0.05)
tone2 = sound.Sound( '../load-data/PureTone_F2000_t50_low.wav', secs=0.05)

if not debug:
    print_instructions(win,noise_example,tone1,tone2)

n_blocks = 32
trials_per_block = 60
experiment_details = {}
D = run_blocks(trials,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,n_blocks,trials_per_block)

win.close()
core.quit()