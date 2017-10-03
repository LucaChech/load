import csv
import pdb
import pickle
from psychopy import locale_setup, core, data, event, logging, sound, gui

test = True

def run_blocks(blocks,noise,timer,visual,win,my_dict,event,i_counter,probes_position_list,probes_position_index,block_number,expInfo,incorrect,tone1,tone2,experiment_details,allPoints,trial_number):
    for block in blocks:
        bPoints = 0
        for pic in block:
            print 'IMAGE ', i_counter
            trial_details = {}
            probe_response = 't'
            #noise.play()
            timer.reset()
            image = visual.ImageStim(win=win, image=  '../load-data/exp_images/'+ pic[1:-1])
            responded = False
            start_frame = ((int(my_dict[pic[1:-1]][12]) + 17 // 2) // 17) -1 # final -1 is to compensate for lag
            #CHANGE 17 WITH ACTUAL FRAMERATE
            if test:
                n_frames = 1
            else:
                n_frames = 60
            for frameN in range(n_frames):
 
                if 'tone1' in my_dict[pic[1:-1]] and frameN == start_frame :
                    tone1.play()
                    print start_frame, my_dict[pic[1:-1]][12]
                elif 'tone2' in my_dict[pic[1:-1]] and frameN == start_frame:
                    tone2.play()
                    print start_frame, my_dict[pic[1:-1]][12]
                image.draw()
                win.flip()
            for frameN in range(20):

                win.flip()
            if not test:
                response = event.getKeys(keyList = ['space'], timeStamped = timer)
            else:
                response = [['space',6.666]]
#            if 'c' in response[0][0]:
#                win.close()
#                core.quit()

            #Write the existing trial info
            T = my_dict[pic[1:-1]]
            
#            print T
            
            trial_details['image_name'] = pic[1:-1]
            trial_details['cat_1'] = T[0]
            trial_details['cat_2'] = T[1]
            trial_details['cat_3'] = T[2]
            trial_details['cat_4'] = T[3]
            trial_details['cat_5'] = T[4]
            trial_details['trueskill'] = T[5]
            trial_details['load'] = T[6]
            trial_details['exemplar'] = T[7]
            trial_details['question'] =  T[8]
            trial_details['present_absent'] = T[9]
            trial_details['trial_type'] = T[10]
            trial_details['tone_hz'] = T[11]
            trial_details['tone_onset'] = T[12]
            
            if len(response) == 0:
                my_dict[pic[1:-1]].append(None)
                my_dict[pic[1:-1]].append(None)
                trial_details['space'] = None
                trial_details['RT_TO'] = None
            if len(response) >= 1:
                my_dict[pic[1:-1]].append(response[0][0])
                my_dict[pic[1:-1]].append(response[0][1])
                trial_details['space'] = response[0][0]
                trial_details['RT_TO'] = response[0][1]
                
            print 'A'

            trial_details['keys'] = None
            trial_details['RT_VS'] = None
            trial_details['useless'] = None


            if i_counter in probes_position_list[probes_position_index]:
                print 'pic',pic
                name=my_dict[pic[1:-1]][8]
                
                print 'counter:',i_counter
                print 'probes_position_index:',probes_position_index
                print 'block',block_number
                print 'image_in_block',block[1]
                print 'block_list,',block

                print 'line:',my_dict[pic[1:-1]]
                
                if 'pottedplant' in name:
                    name = 'potted plant'
                print name
        
                search_text = visual.TextStim(win, name , wrapWidth=2, height=0.16)
                search_text.draw()
                
                win.flip()
                
                if test:
                    keys = [['q',6.66]]
                else:
                    keys = event.waitKeys(keyList=['q','p','space','r'],timeStamped=timer)
                    
                rt_space = -999
                wait = True
                for k in keys:
                    if k[0] == 'r':
                        win.close()
                        core.quit()
                    if k[0] == 'space':
                        rt_space = [k[0],k[1]]
                    if k[0] == 'q' or k[0] == 'p':
                        wait = False
                while wait:
                    keys = event.waitKeys(keyList=['q','p'],timeStamped=timer)
                    letters = [t[0] for t in keys]
                    if ('p' in letters) or ('q' in letters):
                        wait = False
                my_dict[pic[1:-1]].append(keys[0][0])
                my_dict[pic[1:-1]].append(str(keys[0][1]))
                my_dict[pic[1:-1]].append(rt_space)
                my_dict[pic[1:-1]][16] = float(my_dict[pic[1:-1]][16][0:5])
                
                trial_details['keys'] = keys[0][0]
                trial_details['RT_VS'] = keys[0][1]
                trial_details['useless'] = rt_space
               
                
               
      
                if 'Target Present' in my_dict[pic[1:-1]] and 'p' in my_dict[pic[1:-1]][15]:
                    incorrect.play()
                elif 'Target Absent' in my_dict[pic[1:-1]] and 'q' in my_dict[pic[1:-1]][15]:
                    incorrect.play()
                else:
                    RT = my_dict[pic[1:-1]][16] - 1.3
                    #tPoints = round(pointval - (decay*RT))
                    tPoints = 3
                    bPoints = bPoints + tPoints
                    allPoints =  allPoints + tPoints
                    print tPoints
                    print RT
                    print bPoints
                    #if tPoints >= trialthresh:
                    #    for frameN in range(20):
                    #        happy.draw()
                    #        win.flip()
                win.flip()
                core.wait(1.5)
     
            if i_counter not in probes_position_list[probes_position_index]:
                my_dict[pic[1:-1]].append('Na')
                my_dict[pic[1:-1]].append('Na')
                my_dict[pic[1:-1]].append('Na')
            my_dict[pic[1:-1]].append(i_counter)
            my_dict[pic[1:-1]].append(block_number)
            trial_details['image_number'] = i_counter
            trial_details['block_number'] = block_number
            i_counter = i_counter + 1

            
            experiment_details[trial_number] = trial_details
            trial_number += 1
            
            data_to_dump = {'observer_details': expInfo, 'experiment_details':experiment_details}

            with open('output/participant_'+expInfo['Participant no.']+'.pik','wb') as file:
                pickle.dump(data_to_dump, file)
            
#            w = csv.writer(open('Participant_'+expInfo['participant']+'_1st_half.csv', 'w'))
#            
#            for key, val in my_dict.items():
#                w.writerow([key, val])
        if probes_position_index < 15:
            end_of_block = visual.TextStim(win, 
            'You have earned a total of ' + str(bPoints) + ' points in this block and ' + str(allPoints) + ' points in total.\n'
            '\n'
            'Try to earn an average of 24 points per block to get the bonus!\n'
            '\n'
            '\n'
            'Press ENTER to start block ' + str(block_number+1)+ '.\n',
            height=0.10)
            end_of_block.draw()
            win.flip()
            if not test:
                event.waitKeys(keyList=['return'])
        if probes_position_index == 15:
            end_of_experiment.draw()
            win.flip()
            core.wait(5)
            win.close()
            core.quit()

        block_number = block_number + 1
        i_counter = 0
        probes_position_index = probes_position_index + 1
        
        print my_dict[pic[1:-1]]
        
        bPoints = 0
    return i_counter,probes_position_index,block_number,experiment_details,allPoints,trial_number