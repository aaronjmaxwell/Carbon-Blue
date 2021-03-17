"""
Each spawned process has a name attribute that can be changed upon
creation using the name kwarg.  Naming helps to keep track of processes,
although they possess defaults.
"""
import multiprocessing as mp
import time

def worker():
    """
    A sleepy named worker.
    """
    name = mp.current_process().name
    print(name, 'starting')
    time.sleep(2)
    print(name, 'exiting')

def my_service():
    """
    A lazy service.
    """
    name = mp.current_process().name
    print(name, 'starting')
    time.sleep(3)
    print (name, 'exiting')

if (__name__ == '__main__'):
    service = mp.Process(name = 'my_service', target = my_service,)
    worker1 = mp.Process(target = worker,)
    worker1.name = 'worker 1'
    worker2 = mp.Process(target = worker,)
    worker1.start()
    worker2.start()
    service.start()
