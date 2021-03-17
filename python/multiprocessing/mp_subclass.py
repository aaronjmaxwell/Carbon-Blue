"""
The process module can also be used as a base class, rather than passing
a target function.
"""
import multiprocessing as mp

class Worker(mp.Process):
    def run(self):
        print('In {}'.format(self.name))
        return


if (__name__ == '__main__'):
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    
    for j in jobs:
        j.join()
