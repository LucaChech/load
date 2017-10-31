import pickle
import numpy as np
from keyboard import *

t_from_trial_start = core.Clock()
tone_timer = core.Clock()
vs_timer = core.Clock()

def run_blocks(trials,noise,visual,win,event,i_counter,expInfo,incorrect,tone1,tone2,experiment_details,allPoints):
    last_tone_trial_no = None
    time_since_previous_tone = None
    responded_to_last_tone = False
    trials_waited_for_tone = 0
    # tone_timer = core.Clock()
    # vs_timer = core.Clock()
    n_blocks = 32
    blocks = np.arange(1, n_blocks+1)
    trial_number = 1
    trials_per_block = 60
    for block in blocks:
        bPoints = 0
        trial_numbers_in_block = np.arange(1, trials_per_block+1)
        for trial_number_in_block in trial_numbers_in_block:
            event.clearEvents()
            #This is OK as we have checked possible dead zones in the last trial
            this_trial = trials[trial_number]
            trial_details = this_trial
            trial_details['keys'] = None
            trial_details['RT_VS'] = None
            trial_details['useless'] = None
            trial_details['RT_TO'] = None
            trial_details['tone_sdt'] = None
            trial_details['space_before_tone'] = False

            RT_VS = None
            RT_TO = None
            print 'IMAGE ', i_counter
            #noise.play()
            #t_from_trial_start.reset()
            image = visual.ImageStim(win=win, image=  '../load-data/exp_images/'+ this_trial['image_name'])
            responded = False
            start_frame = ((int(this_trial['tone_onset']) + 17 // 2) // 17) -1 # final -1 is to compensate for lag
            n_frames = 60



            for frameN in range(n_frames):
                if this_trial['tone_hz'] == 'tone1' and frameN == start_frame :
                    tone1.play()
                    tone_timer.reset()
                    last_tone_trial_no = trial_number
                    responded_to_last_tone = False
                elif this_trial['tone_hz'] == 'tone2' and frameN == start_frame:
                    tone2.play()
                    tone_timer.reset()
                    last_tone_trial_no = trial_number
                    responded_to_last_tone = False
                image.draw()
                win.flip()

            for frameN in range(20):
                win.flip()

            #First keyboard call
            RT_TO = get_keys_after_image(tone_timer)
            print RT_TO

            if RT_TO < 0:
                #Space was pressed before the tone played
                #Must be a false alarm for this trial, since tone played
                #And previous tone must have been more than 2 seconds ago
                trial_details['space_before_tone'] = True

            elif RT_TO > 2:
                #Belongs to this trial
                #FA because no tone in this trial
                trial_details['RT_TO'] = RT_TO
                trial_details['tone_sdt'] = 'FA'
            else:
                #Shorter than 2
                if last_tone_trial_no != None and responded_to_last_tone == False:
                    #Hit for last tone trial
                    if RT_TO != None:
                        responded_to_last_tone = True
                        if last_tone_trial_no == trial_number:
                            trial_details['RT_TO'] = RT_TO
                            trial_details['tone_sdt'] = 'HI'
                            responded_to_last_tone = True
                        else:
                            experiment_details[last_tone_trial_no]['RT_TO'] = RT_TO
                            experiment_details[last_tone_trial_no]['tone_sdt'] = 'HI'
                            responded_to_last_tone = True
                elif last_tone_trial_no is None:
                    #responded to last tone must be false
                    #No tone yet so this must be FA for current trial
                    trial_details['tone_sdt'] = 'FA'
                elif responded_to_last_tone == True:
                    trial_details['tone_sdt'] = 'FA'

            if this_trial['present_absent'] != 'No Target':
                #If this is a visual search question trial

                name = this_trial['question']

                if 'pottedplant' in name:
                    name = 'potted plant'
                print name
        
                search_text = visual.TextStim(win, name , wrapWidth=2, height=0.16)
                search_text.draw()
                win.flip()

                vs_timer.reset()
                print 'VS: ' ,vs_timer.getTime()
                RT_TO, RT_VS, q_or_p = get_keys_after_visual_search_question(tone_timer, vs_timer)

                trial_details['keys'] = q_or_p
                trial_details['RT_VS'] = RT_VS

                if RT_TO > 2 and trial_details['RT_TO'] != None:
                    #Reaction time greater than 2
                    #Must be an FA for the current trial
                    trial_details['RT_TO'] = RT_TO
                    trial_details['tone_sdt'] = 'FA'
                else:
                    #Reaction time less than 2
                    #Could be hit for this trial
                    #Or hit for previous trial
                    if last_tone_trial_no is not None:
                        #We have had the tone
                        if last_tone_trial_no == trial_number:
                            #Tone was on current trial
                            if trial_details['RT_TO'] is None:
                                trial_details['RT_TO'] = RT_TO
                                trial_details['tone_sdt'] = 'HI'
                                responded_to_last_tone = True
                        else:
                            #Tone was on previous trial
                            if responded_to_last_tone == False and experiment_details[last_tone_trial_no]['RT_TO'] == None:
                                if RT_TO != None:
                                    responded_to_last_tone = True
                                    experiment_details[last_tone_trial_no]['RT_TO'] = RT_TO
                                    experiment_details[last_tone_trial_no]['tone_sdt'] = 'HI'
                                    responded_to_last_tone = True

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
            dz_timer = core.Clock()
            trial_details['image_number'] = i_counter
            trial_details['block_number'] = block
            i_counter = i_counter + 1

            experiment_details[trial_number] = trial_details
            # print 'keys', experiment_details[trial_number]['keys']
            # print 'RT_TO', experiment_details[trial_number]['RT_TO']
            print 'RT_vs', experiment_details[trial_number]['RT_VS']
            trial_number += 1


            print 'RT_TO: ', trial_details['RT_TO']
            print 'RT_VS: ', trial_details['RT_VS']
            print 'keys: ', trial_details['keys']
            print 'tone_sdt: ', trial_details['tone_sdt']


            print 'DZ: ', dz_timer.getTime()

        data_to_dump = {'observer_details': expInfo, 'experiment_details': experiment_details}
        with open('output/participant_' + expInfo['Participant no.'] + '.pik', 'wb') as file:
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
