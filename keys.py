from psychopy import core
#from psychopy import event
import time


c = core.Clock()

print c.getTime()
time.sleep(5)
c.reset()
print c.getTime()
time.sleep(5)
print c.getTime()