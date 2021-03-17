'''
multiprocessing has a module-level function to set up a logging object and pass it to stderr.
'''
import multiprocessing as mp
import logging
import sys

def worker():
    print('gold on the ceiling')
    sys.stdout.flush()

if (__name__ == '__main__'):
    mp.log_to_stderr(logging.DEBUG)
    p = mp.Process(target = worker)
    p.start()
    p.join()
