'''
Q: How can more than one worker access a resource at the same time, but not all workers at once?
A: Semaphore.
'''
import random
import multiprocessing as mp
import time

class ActivePool:
    def __init__(self):
        super(ActivePool, self).__init__()
        self.manager = mp.Manager()
        self.active = self.manager.list()
        self.lock = mp.Lock()

    def MakeActive(self, name):
        with self.lock:
            self.active.append(name)

    def MakeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)

def worker(s, pool):
    name = mp.current_process().name
    with s:
        pool.MakeActive(name)
        print ('activating {} now running {}'.format(name, pool))
        time.sleep(random.random())
        pool.MakeInactive(name)

if (__name__ == '__main__'):
    pool = ActivePool()
    s = mp.Semaphore(3)
    jobs = [mp.Process(target = worker, name = str(i), args = (s, pool)) for i in range(10)]

    for job in jobs:
        job.start()

    while True:
        alive = 0
        for job in jobs:
            if (job.is_alive()):
                alive += 1
                job.join(timeout = 0.1)
                print('Now running {}'.format(pool))
        if (alive == 0):
            break
