from keyboard import *

from psychopy import core, event
import time

c = core.Clock()
c2 = core.Clock()

c.reset()
c2.reset(0)

print 1

#r = get_keys_after_image(c)
RT_TO, RT_VS, q_or_p = get_keys_after_visual_search_question(c,c2)
print RT_TO,RT_VS, q_or_p