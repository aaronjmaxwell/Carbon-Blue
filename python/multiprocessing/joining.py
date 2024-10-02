"""Joining processes.

Waiting until a process has successfully completed its work and exited
is performed using the join method.
"""
import multiprocessing as mp

import workers


if (__name__ == '__main__'):
    d = mp.Process(name="slow-walker", target=workers.sleepy, daemon=True, args=(8, True, False,),)
    w = mp.Process(name="fast-walker", target=workers.sleepy, daemon=False, args=(2, True, False,),)
    h = mp.Process(name="walker", target=workers.sleepy, daemon=False, args=(4, True, False,),)
    h.start()
    h.join()
    d.start()
    w.start()
    d.join()
    w.join()
    print("both walkers have been destroyed")
