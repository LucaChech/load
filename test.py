from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, sound
from psychopy import prefs

prefs.general['audioLib'] = ['pyo']

from setup import *
from functions_old import *
from instructions import *

import unittest
import mock
import pickle

debug = True
timer = core.Clock()
i_counter = 0
block_number = 1
trial_number = 1

# REWARD PARAMETERS
decay = 10
trialthresh = 4
pointval = 10
allPoints = 0
bPoints = 0

if debug:
    expInfo = {u'session': u'-999', u'Participant no.': u'test'}
    expInfo['date'] = 'test'
    expInfo['expName'] = 'test'
else:
    expName = 'participant info'
    expInfo = {u'Age': u'1', u'Sex': u'', u'Right handed?': '1', u'Participant no.': '1'}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False: core.quit()
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName

if debug:
    win = visual.Window(size=(800, 600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
                        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                        blendMode='avg', useFBO=True,
                        )
else:
    win = visual.Window(size=(1920, 1080), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
                        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                        blendMode='avg', useFBO=True,
                        )

search_text = visual.TextStim(win, 'TEST', wrapWidth=2, height=0.16)

win.flip()

noise_example = sound.Sound('../load-data/noise_example_low.wav', secs=1)
incorrect = sound.Sound('../load-data/wrong_buzzer.wav', secs=1)
noise = sound.Sound('../load-data/noise_exp_low.wav', secs=1)
tone1 = sound.Sound('../load-data/PureTone_F1500_t50_low.wav', secs=0.05)
tone2 = sound.Sound('../load-data/PureTone_F2000_t50_low.wav', secs=0.05)

if not debug:
    print_instructions(win, noise_example, tone1, tone2)

class Test(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch('psychopy.event.getKeys')
    @mock.patch('psychopy.event.waitKeys')
    def test_1(self, mock_getKeys, mock_waitKeys):
        experiment_details = {}
        trials_new = {}
        n=2
        for k in trials.keys()[:n]:
            trials_new[k] = trials[k]
        mock_getKeys.return_value = [['space',0.1]]
        mock_waitKeys.return_value = [['q', 0.1]]
        run_blocks(trials_new,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,1,n)
        self.assertEqual(experiment_details[1]['RT_TO'], 0.1)

class TestWholeExperiment(unittest.TestCase):
    @mock.patch('keyboard.wait_keys')
    @mock.patch('keyboard.get_keys')
    @mock.patch('keyboard.wait_for_return')
    def runTest(self, mock_wait_for_return, mock_getKeys, mock_waitKeys):
        trial_file = 'config/randomization.pik'
        converted = False

        with open(trial_file, 'r') as of:
            trials_raw = pickle.load(of)

        trials = {}

        cols = ['cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5', 'TS', 'load', 'exemplar', 'question', 'present_absent',
                'trial_type', 'tone_hz', 'tone_onset', 'image_name', 'block']

        if converted:
            trials = trials_raw
        else:
            for k in trials_raw.keys():
                l = trials_raw[k]
                trial_dict = {}
                for i in range(len(l)):
                    trial_dict[cols[i]] = l[i]
                trials[k] = trial_dict

        experiment_details = {}
        mock_waitKeys.return_value = [['q', 0.1]]
        mock_getKeys.return_value = [['space',0.1]]
        mock_wait_for_return.return_value = True

        run_blocks(trials,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,32,60)


class ReactionTimeZero(unittest.TestCase):
    @mock.patch('keyboard.wait_keys')
    @mock.patch('keyboard.get_keys')
    def runTest(self, mock_get_keys, mock_wait_keys):
        experiment_details = {}
        trials_new = {}
        n = 5
        for k in trials.keys()[:n]:
            trials_new[k] = trials[k]
            trials_new[k]['trial_type'] = 'Critical'
            trials_new[k]['tone_hz'] = 'tone1'
            trials_new[k]['tone_onset'] = 500
        mock_wait_keys.return_value = [['q', 0]]
        mock_get_keys.return_value = [['space', 0]]

        D = run_blocks(trials,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,1,n)
        for k in D.keys():
            t = D[k]
            print t
            self.assertEqual(t['RT_TO'], 0)
            self.assertEqual(t['tone_sdt'], 'HI')

class test_reply_in_next_trial(unittest.TestCase):
    @mock.patch('keyboard.wait_keys')
    @mock.patch('keyboard.get_keys')
    def runTest(self, mock_get_keys, mock_wait_keys):
        n = 2
        experiment_details = {}
        trials_new = {}
        trials_new[1] = trials[1]
        trials_new[1]['trial_type'] = 'Critical'
        trials_new[1]['tone_hz'] = 'tone1'
        trials_new[1]['tone_onset'] = 500

        trials_new[2] = trials[2]
        trials_new[2]['trial_type'] = 'Normal'


        mock_get_keys.side_effect = [ [],[['space', 1]] ]

        D = run_blocks(trials,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,1,n)

        self.assertEqual(D[1]['RT_TO'], 1)
        self.assertEqual(D[1]['tone_sdt'], 'HI')

        self.assertIsNone(D[2]['RT_TO'])
        self.assertIsNone(D[2]['tone_sdt'])
        self.assertEqual(D[2]['moved_space_in_this_trial'], True)

class test_visual_search_question(unittest.TestCase):
    @mock.patch('keyboard.wait_keys')
    @mock.patch('keyboard.get_keys')
    def runTest(self, mock_get_keys, mock_wait_keys):
        n = 1
        experiment_details = {}
        trials_new = {}
        trials_new[1] = trials[1]
        trials_new[1]['trial_type'] = 'Critical'
        trials_new[1]['tone_hz'] = 'tone1'
        trials_new[1]['tone_onset'] = 500
        trials_new[1]['present_or_absent'] = 'Target Present'

        mock_get_keys.return_value = [['space', 1]]
        mock_wait_keys.return_value = [['q',1]]

        D = run_blocks(trials,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,1,n)

        self.assertEqual(D[1]['RT_TO'], 1)
        self.assertEqual(D[1]['tone_sdt'], 'HI')
        self.assertEqual(D[1]['keys'], 'q')

class test_visual_search_question_2(unittest.TestCase):
    @mock.patch('keyboard.wait_keys')
    @mock.patch('keyboard.get_keys')
    @mock.patch('psychopy.core.Clock.getTime')
    def runTest(self, mock_tone_timer, mock_get_keys, mock_wait_keys):
        n = 1
        experiment_details = {}
        trials_new = {}
        trials_new[1] = trials[1]
        trials_new[1]['trial_type'] = 'Critical'
        trials_new[1]['tone_hz'] = 'tone1'
        trials_new[1]['tone_onset'] = 500
        trials_new[1]['present_or_absent'] = 'Target Present'

        mock_get_keys.return_value = [['space', 1]]

        mock_wait_keys.side_effect = [    [['space', 2]], [['q',2.2]]    ]
        mock_tone_timer.return_value = 1

        D = run_blocks(trials,noise,win,expInfo, incorrect, tone1, tone2, experiment_details,allPoints,1,n)

        self.assertEqual(D[1]['RT_TO'], 3)
        self.assertEqual(D[1]['tone_sdt'], 'FA')
        self.assertEqual(D[1]['keys'], 'q')
        self.assertEqual(D[1]['RT_VS'], 2.2)



if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestSuite()
    test = test_visual_search_question_2
    suite.addTest(test())

    unittest.TextTestRunner().run(suite)

