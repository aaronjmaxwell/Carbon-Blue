'''
The logger object can be manipulated directly rather than passing a logging object at init.
'''
import multiprocessing as mp
import logging
import sys

def worker():
    print('little black submarines')
    sys.stdout.flush()

if (__name__ == '__main__'):
    mp.log_to_stderr()
    logger = mp.get_logger()
    logger.setLevel(logging.INFO)
    p = mp.Process(target = worker)
    p.start()
    p.join()
