"""Child classes.

The process module can also be used as a base class, rather than passing
a target function.
"""
import multiprocessing as mp

from workers import Worker


if (__name__ == "__main__"):
    jobs = []
    for j in range(5):
        p = Worker()
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()
