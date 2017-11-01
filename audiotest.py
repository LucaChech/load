import sys
sys.path.append('C:\pyo\Python27\Lib\site-packages')
from pyo import *
s=Server(sr=44100, nchnls=2, buffersize=256, duplex=1, audio='portaudio', jackname='pyo', ichnls=None, winhost='asio')
s.boot()
print 'B'
s.start()
a = Sine(mul=0.01).out()
import time
time.sleep(5)
print 'C'