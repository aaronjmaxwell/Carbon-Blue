"""
By default, a `~mp.Process.join` method blocks indefinitely.  By passing
a timeout argument (type float) representing the number of seconds to
wait, we can limit how long __main__ must wait before continuing on.
"""
import multiprocessing as mp
import time
import sys

def daemon():
    """A sleepy daemon"""
    p = mp.current_process()
    print ('starting ', p.name)
    time.sleep(2)
    print ('exiting ', p.name)

def worker():
    """A fast worker"""
    p = mp.current_process()
    print ('starting ', p.name)
    print ('exiting ', p.name)

if (__name__ == '__main__'):
    d = mp.Process(name = 'daemon', target = daemon, daemon = True)
    w = mp.Process(name = 'worker', target = worker, daemon = False)
    d.start()
    d.join(1)
    print ('have we timed out?', d.is_alive())
    w.start()
    w.join()
