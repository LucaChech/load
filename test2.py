from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual
from psychopy import prefs
prefs.general['audioLib'] = ['pyo']
from psychopy import locale_setup, core, data, event, logging, sound, gui
import time


noise_example = sound.Sound( '../load-data/noise_example_low.wav', secs=1)
incorrect = sound.Sound( '../load-data/wrong_buzzer.wav', secs=1)
noise = sound.Sound( '../load-data/noise_exp_low.wav', secs=1)
tone1 = sound.Sound( '../load-data/PureTone_F1500_t50_low.wav', secs=0.05)
tone2 = sound.Sound( '../load-data/PureTone_F2000_t50_low.wav', secs=0.05)

noise.play()

time.sleep(1)

tone1.play()
time.sleep(1)
tone2.play()
time.sleep(1)
noise_example.play()
time.sleep(1)
incorrect.play()