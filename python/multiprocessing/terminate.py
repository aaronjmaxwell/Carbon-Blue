"""
A hung process can be killed using the terminate method.  Terminated
processes must still be joined back to main in order to give the process
manager time to update.
"""
import multiprocessing as mp
import time

def worker():
    print('started')
    time.sleep(0.1)
    print('finished')

if (__name__ == '__main__'):
    p = mp.Process(target = worker)
    print('BEFORE:', p.name, 'is alive?', p.is_alive())
    p.start()
    print('DURING:', p.name, 'is alive?', p.is_alive())
    p.terminate()
    print('TERMINATED:', p.name, 'is alive?', p.is_alive())
    p.join()
    print('JOINED:', p.name, 'is alive?', p.is_alive())
