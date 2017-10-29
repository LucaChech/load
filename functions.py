import csv
import pdb
import pickle
from psychopy import locale_setup, core, data, event, logging, sound, gui
import numpy as np
from keyboard_luca import *

def run_blocks(trials,noise,timer,visual,win,event,i_counter,expInfo,incorrect,tone1,tone2,experiment_details,allPoints):
    last_tone_trial_no = 0
    tone_timer = core.Clock()
    n_blocks = 16
    blocks = np.arange(1, n_blocks+1)  # 1 to 16
    trial_number = 1
    trials_per_block = 60
    for block in blocks:
        bPoints = 0
        trial_numbers_in_block = np.arange(1, trials_per_block+1)
        for trial_number_in_block in trial_numbers_in_block:
            this_trial = trials[trial_number]
            RT_VS = None
            RT_TO = None
            print 'IMAGE ', i_counter
            trial_details = {}
            probe_response = 't'
            noise.play()
            timer.reset()
            image = visual.ImageStim(win=win, image=  '../load-data/exp_images/'+ this_trial['image_name'])
            responded = False
            start_frame = ((int(this_trial['tone_onset']) + 17 // 2) // 17) -1 # final -1 is to compensate for lag
            #CHANGE 17 WITH ACTUAL FRAMERATE
            n_frames = 60

            for frameN in range(n_frames):
                if this_trial['tone_hz'] == 'tone1' and frameN == start_frame :
                    tone1.play()
                    tone_timer.reset()
                elif this_trial['tone_hz'] == 'tone2' and frameN == start_frame:
                    tone2.play()
                    tone_timer.reset()
                image.draw()
                win.flip()
            for frameN in range(20):
                win.flip()

            RT_TO = get_keys_after_image
            (tone_timer)

            trial_details = this_trial
            
            trial_details['RT_TO'] = RT_TO
            trial_details['keys'] = None
            trial_details['RT_VS'] = None
            trial_details['useless'] = None

            if this_trial['present_absent'] != 'No Target':
                #If this is a critical trial (tone present)

                name = this_trial['question']

                if 'pottedplant' in name:
                    name = 'potted plant'
                print name
        
                search_text = visual.TextStim(win, name , wrapWidth=2, height=0.16)
                search_text.draw()
                vs_timer = core.Clock()
                win.flip()

                vs_timer.reset()

                RT_TO, RT_VS, q_or_p = get_keys_after_visual_search_question(tone_timer, vs_timer)

                trial_details['keys'] = q_or_p
                trial_details['RT_VS'] = RT_VS
                trial_details['RT_TO'] = RT_TO

                if  this_trial['present_absent'] == 'Target Present' and q_or_p == 'p':
                    incorrect.play()
                elif this_trial['present_absent'] == 'Target Absent'  and q_or_p == 'q':
                    incorrect.play()
                else:
                    #RT = my_dict[pic[1:-1]][16] - 1.3 #I'm not sure if it's bad to comment this line out
                    #tPoints = round(pointval - (decay*RT))
                    tPoints = 3
                    bPoints = bPoints + tPoints
                    allPoints =  allPoints + tPoints
 
                    #if tPoints >= trialthresh:
                    #    for frameN in range(20):
                    #        happy.draw()
                    #        win.flip()
                win.flip()
                core.wait(1.5)

            trial_details['image_number'] = i_counter
            trial_details['block_number'] = block
            i_counter = i_counter + 1

            experiment_details[trial_number] = trial_details
            print 'keys', experiment_details[trial_number]['keys']
            print 'RT_TO', experiment_details[trial_number]['RT_TO']
            print 'RT_VS', trial_details['RT_VS'] 
            print 'useless', trial_details['useless']
            trial_number += 1
            data_to_dump = {'observer_details': expInfo, 'experiment_details':experiment_details}
            
            with open('output/participant_'+expInfo['Participant no.']+'.pik','wb') as file:
                pickle.dump(data_to_dump, file)

        if block < n_blocks:
            end_of_block = visual.TextStim(win, 
            'You have earned a total of ' + str(bPoints) + ' points in this block and ' + str(allPoints) + ' points in total.\n'
            '\n'
            'Try to earn an average of 24 points per block to get the bonus!\n'
            '\n'
            '\n'
            'Press ENTER to start block ' + str(block+1)+ '.\n',
            height=0.10)
            end_of_block.draw()
            win.flip()
            event.waitKeys(keyList=['return'])
        if block == n_blocks:
            end_of_experiment = visual.TextStim(win, 
            'You have earned a total of ' + str(allPoints) + ' points.\n'
            '\n'
            '\n'
            '\n'
            'The experiment is over, thank you!\n'
            '\n'
            '\n'
            ,
            height=0.10)
            end_of_experiment.draw()
            win.flip()
            core.wait(100)
            win.close()
            core.quit()


        bPoints = 0
