"""
Waiting until a process has successfully completed its work and exited
is performed using the join method
"""
import multiprocessing as mp
import time
import sys


def worker(n):
    p = mp.current_process()
    print ('starting', p.name)
    time.sleep(n)
    print ('exiting', p.name)

if (__name__ == '__main__'):
    d = mp.Process(name = 'slow-walker', target = worker, daemon = True, args = (8, ))
    w = mp.Process(name = 'fast-walker', target = worker, daemon = False, args = (2, ))
    d.start()
    d.join()
    
    w.start()
    w.join()
    print ('both walkers have been destroyed')
