from psychopy import event

def get_keys_after_image(tone_timer):
    RT_TO = None
    response = event.getKeys(keyList=['space'], timeStamped=tone_timer)

    if len(response) and response[0][1] <= 2:
        RT_TO = response[0][1]
    return RT_TO

def get_keys_after_visual_search_question(tone_timer, vs_timer):
    keys = event.waitKeys(keyList=['q', 'p', 'space'], timeStamped=tone_timer)

    rt_space = -999
    wait = True
    for k in keys:
        if k[0] == 'space':
            rt_space = [k[0], k[1]]
            if rt_space <= 2:
                RT_TO = rt_space
        if k[0] == 'q' or k[0] == 'p':
            wait = False
            RT_VS = k[0][1]
            RT_VS = RT_VS - (vs_timer - tone_timer)
            q_or_p = k[0]
    while wait:
        keys = event.waitKeys(keyList=['q', 'p'], timeStamped=vs_timer)
        letters = [t[0] for t in keys]
        if ('p' in letters) or ('q' in letters):
            wait = False
            RT_VS = keys[0][1]
            q_or_p = keys[0][0]

    return RT_TO, RT_VS, q_or_p