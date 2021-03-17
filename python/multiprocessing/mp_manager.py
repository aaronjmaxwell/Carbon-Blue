'''
In the previous example, the active processes were maintained centrally in a list object created by
the Manager method.  It is responsible for coordinating shared informmation between all users.
Dictionaries are also supported through the Manger().dict() class.
'''
import multiprocessing as mp
import pprint

def worker(d, key, value):
    d[key] = value

if (__name__ == '__main__'):
    mgr = mp.Manager()
    d = mgr.dict()
    jobs = [mp.Process(target = worker, args = (d, i, i * 2)) for i in range(10)]
    
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print('results: ', d)
