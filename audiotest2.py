import sys
sys.path.append('C:\pyo\Python27\Lib\site-packages')
from psychopy import prefs
prefs.general['audioLib'] = ['pyo']
from psychopy import locale_setup, core, data, event, logging, sound, gui
print sound.__file__
f = sound.Sound('..\load-data\PureTone_F1500_t50.wav', secs=0.15)
f.play()
import time
time.sleep(5)