
import pickle
from psychopy import locale_setup, core, data, event, logging, sound, gui
import numpy as np
from keyboard_luca import *

timer_from_trial_start = core.Clock()

vs_timer = core.Clock()
def run_blocks(trials,noise,timer,visual,win,event,i_counter,expInfo,incorrect,tone1,tone2,experiment_details,allPoints):
    last_tone_trial_no = None
    responded_to_last_tone = False
    trials_waited_for_tone = 0
    n_blocks = 32
    blocks = np.arange(1, n_blocks+1)  # 1 to 16
    trial_number = 1
    trials_per_block = 60
    for block in blocks:
        timer_from_block_start = core.Clock()
        time_so_far = timer_from_block_start.getTime()
        bPoints = 0
        trial_numbers_in_block = np.arange(1, trials_per_block+1)
        time_at_end_of_trial = 0
        for trial_number_in_block in trial_numbers_in_block:
            time_from_start = timer_from_block_start.getTime()
            print 'time_so_far: ', time_so_far
            print 'beginning: ', time_from_start
            print 'time at end of previous trial (if it is a no probe trial)', time_at_end_of_trial
            print 'time_from_start - time_at_end_of_trial',time_from_start - time_at_end_of_trial
            print 'difference: ',time_from_start - (time_from_start - time_at_end_of_trial)

            this_trial = trials[trial_number]
            trial_details = this_trial
            trial_details['keys'] = None # CAN ONLY BE Q OR P, NOT SPACE
            trial_details['RT_VS'] = None
            trial_details['RT_TO'] = None
            RT_VS = None
            RT_TO = None
            print 'IMAGE ', i_counter
            noise.play()
            timer_from_trial_start.reset()
            image = visual.ImageStim(win=win, image=  '../load-data/exp_images/'+ this_trial['image_name'])
            start_frame = ((int(this_trial['tone_onset']) + 17 // 2) // 17) -1 # final -1 is to compensate for lag
            # CHANGE 17 WITH ACTUAL FRAMERATE
            n_frames = 60

            for frameN in range(n_frames):
                if this_trial['tone_hz'] == 'tone1' and frameN == start_frame :
                    tone1.play()
                elif this_trial['tone_hz'] == 'tone2' and frameN == start_frame:
                    tone2.play()
                image.draw()
                win.flip()

            for frameN in range(20):
                win.flip()

            RT_TO_before_check = event.getKeys(keyList=['space'], timeStamped=timer_from_trial_start)
            if len(RT_TO_before_check):
                RT_TO = RT_TO_before_check[0][1]
            time_at_end_of_trial = timer_from_trial_start.getTime()
            print time_at_end_of_trial

            if this_trial['present_absent'] != 'No Target':
                #If this is a critical trial (tone present)
                print timer_from_trial_start.getTime()
                name = this_trial['question']

                if 'pottedplant' in name:
                    name = 'potted plant'
                print name
        
                search_text = visual.TextStim(win, name , wrapWidth=2, height=0.16)
                search_text.draw()
                win.flip()

                timer_from_probe = core.Clock()
                timer_from_probe.add(timer_from_trial_start.getTime())
                print 'timer', timer_from_probe.getTime()
                vs_timer.reset()
                print 'VS: ' ,vs_timer.getTime()
                RT_TO, RT_VS, q_or_p = get_keys_after_visual_search_question(tone_timer, vs_timer)

                trial_details['keys'] = q_or_p
                trial_details['RT_VS'] = RT_VS



                if  this_trial['present_absent'] == 'Target Present' and q_or_p == 'p':
                    incorrect.play()
                elif this_trial['present_absent'] == 'Target Absent'  and q_or_p == 'q':
                    incorrect.play()
                else:
                    tPoints = 3
                    bPoints = bPoints + tPoints
                    allPoints =  allPoints + tPoints
                win.flip()
                core.wait(1.5)

            i_counter = i_counter + 1



            trial_details['RT_TO'] = RT_TO
            experiment_details[trial_number] = trial_details
            # print 'keys', experiment_details[trial_number]['keys']
            print 'RT_TO', experiment_details[trial_number]['RT_TO']
            #print 'RT_vs', experiment_details[trial_number]['RT_VS']
            trial_number += 1
            #last_tone_trial_no = None
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
