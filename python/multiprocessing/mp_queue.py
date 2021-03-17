"""
Common usage for multiprocessing is to divide a job among several
workers and run them in parallel.  This requires communication between
the workers, which can be done simply using the Queue class. Any object
that can be pickled can pass through the Queue, one at a time.
"""
import multiprocessing as mp
from random import randint as rnd
import time

class Constitution:
    def __init__(self, name):
        self.name = name
    def red_alert(self):
        proc = mp.current_process()
        print ('{} has raised shields in {}!'.format(self.name, proc.name))


def worker(q, n):
    obj = q.get()
    time.sleep(n)
    obj.red_alert()

if (__name__ == '__main__'):
    q = mp.Queue()
    # Even if only `~mp.Queue` object is passed, an error will be raised if it does not have a
    # trailing comma in the args `tuple`.  Always safest to leave the trailing comma when using
    # the multiprocessing library.
    P = [mp.Process(target = worker, args = (q, rnd(1, 3)), name = "red alert") for _ in range(10)]
    S = ["Enterprise", "Defiant", "Yorktown", "Excaliber", "Intrepid", "Constitution",
        "Constellation", "Exeter", "Farragut", "Hood"]
    
    for p, s in zip(P, S):
        p.start()
        q.put(Constitution(s))
    
    q.close()
    q.join_thread()
    
