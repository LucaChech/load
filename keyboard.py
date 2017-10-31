from psychopy import event, core

def get_keys(keyList, timeStamped):
    return event.getKeys(keyList=keyList, timeStamped=timeStamped)

def wait_keys(keyList, timeStamped):
    return event.waitKeys(keyList=keyList, timeStamped=timeStamped)

def get_keys_after_image(tone_timer):
    RT_TO = None
    response = get_keys(keyList=['space'], timeStamped=tone_timer)
    if len(response):
        RT_TO = response[0][1]
        print 'RT_TO inside first function: ', RT_TO
    event.clearEvents()
    return RT_TO

def get_keys_after_visual_search_question(tone_timer, vs_timer):
    #If space comes first, log it and then listen for q or p
    RT_TO = None
    RT_VS = None
    p_or_q = None
    t = core.Clock()
    t.reset()
    t_start_from_tone = tone_timer.getTime()
    t_start_from_vs = vs_timer.getTime()

    #print 'since vs:', t_start_from_vs
    keys = wait_keys(keyList=['q', 'p', 'space'], timeStamped=t)


    wait = True
    for k in keys:
        if k[0] == 'space':
            stamp =  k[1]
            rt_space = stamp + t_start_from_tone
            RT_TO = rt_space
        if k[0] == 'q' or k[0] == 'p':
            print 'Here'
            wait = False
            stamp = k[1]
            RT_VS = stamp + t_start_from_vs
            print RT_VS
            q_or_p = k[0]
    while wait:
        print 'wait'
        keys = wait_keys(keyList=['q', 'p'], timeStamped=vs_timer)
        print vs_timer
        letters = [t[0] for t in keys]
        if ('p' in letters) or ('q' in letters):
            wait = False
            RT_VS = keys[0][1]
            print RT_VS
            q_or_p = keys[0][0]
    event.clearEvents()
    return RT_TO, RT_VS, q_or_p