"""
By default, the main program will not exit until all child processes
have exited.  By setting a multiprocess' daemon attribute, __main__
can successfully exit even if a daemon hangs.  However, upon exiting,
all daemons are destroyed.
"""
import multiprocessing as mp
import time
import sys

def demon():
    """
    A hanging background process.
    """
    p = mp.current_process()
    print ('starting ', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(100)
    print ('we never get here because worker finishes before ', p.name, p.pid)
    sys.stdout.flush()

def worker():
    """
    A prompt worker.
    """
    p = mp.current_process()
    print ('starting ', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(10)
    print ('exiting ', p.name, p.pid)
    sys.stdout.flush()

if (__name__ == '__main__'):
    d = mp.Process(name = 'daemon', target = demon)
    d.daemon = True # Set after calling.
    w = mp.Process(name = 'worker', target = worker, daemon = False)
    d.start()
    time.sleep(1)
    w.start()
