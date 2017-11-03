from psychopy import visual
from psychopy import core, event



def print_instructions(win,noise_example,tone1,tone2):
    print 1
    print '!A'
    Instructions_screen_1 = visual.TextStim(win,
    '                                INSTRUCTIONS \n'
    '\n'
    '     You will be presented with a series of brief images.\n'
    '\n'
    '           Your task is to carefully examine each image.\n'
    '              Sometimes, you will be asked whether\n'
    '   a specific object (e.g. a chair) was present in the image.\n'
    '\n'
    '              Please reply as accurately as possible \n'
    '                                    by pressing:\n'
    '                        Q if the object was present\n'
    '                         P if the object was absent\n'
    '\n'
    'The experiment is run in short blocks with a break after \n'
    '                                    each block.\n'
    '\n'
    '  Please keep your fingers on the Q and P keys throughout \n'
    '                                      a block.\n'
    '\n'
    '                      press ENTER to continue'
    ,
    alignHoriz='center',
    alignVert='center',
    height= 0.08,
    wrapWidth=2 )
    print '!B'


    Instructions_screen_2 = visual.TextStim(win,
    '                               INSTRUCTIONS \n'
    '\n'
    '\n'
    '  Each image will be accompanied by a constant noise. \n'
    '\n'
    '\n'
    '\n'
    '      Press ENTER to hear an example of the noise. \n'
    ,
    alignHoriz='center',
    alignVert='center',
    height= 0.08,
    wrapWidth=2 )



    Instructions_screen_3 = visual.TextStim(win,
    '                               INSTRUCTIONS \n'
    '\n'
    '\n'
    'Sometimes, in addition to the noise, you will also hear a\n'
    '                                      sound. \n'
    '\n'
    '\n'
    '\n'
    '       Press ENTER to hear a few examples of the \n'
    '                                     sounds. \n'
    ,
    alignHoriz='center',
    alignVert='center',
    height= 0.08,
    wrapWidth=2 )


    Instructions_screen_4 = visual.TextStim(win,
    '           INSTRUCTIONS \n'
    '\n'
    '\n'
    '   If you hear any sound, press\n'
    '\n'
    '               SPACEBAR\n'
    '\n'
    '\n'
    '\n'
    '\n'
    '    Press ENTER to continue.\n'
    '\n'
    ,
    alignHoriz='center',
    alignVert='center',
    height= 0.08,
    wrapWidth=2 )


    Instructions_screen_5 = visual.TextStim(win,
    '                                             INSTRUCTIONS\n'
    '\n'

    '                Remember, you primary task is to examine the images\n'
    '       and make a correct response regarding the presence or absence\n'
    '                                         of the probed object.\n'
    '\n'
    '         You will be awarded with a bonus if you earn 768 or more points\n'
    '             Points are only allocated when you make a correct response\n'
    '                                          to the probed object.\n'
    '\n'
    '\n'
    '                                          Press ENTER to start.'
    ,
    alignHoriz='center',
    alignVert='center',
    height= 0.08,
    wrapWidth=2 )


    Instructions_screen_1.draw()
    win.flip()
    event.waitKeys(keyList=['return'])
    Instructions_screen_2.draw()
    win.flip()
    event.waitKeys(keyList=['return'])
    noise_example.play()
    core.wait(2)
    Instructions_screen_3.draw()
    win.flip()
    event.waitKeys(keyList=['return'])
    core.wait(2)
    tone1.play()
    core.wait(2)
    tone2.play()
    core.wait(2)
    Instructions_screen_4.draw()
    win.flip()
    event.waitKeys(keyList=['return'])
    Instructions_screen_5.draw()
    win.flip()
    event.waitKeys(keyList=['return'])
    core.wait(1)
