"""Simple example of how multiprocessing works.

A worker function is launched from the main script. Child processes must
be able to import worker functions so the spawn is wrapped in __main__
which is shielded.
"""
import multiprocessing as mp


def worker():
    """Worker function."""
    print("Worker")

if (__name__ == "__main__"):
    jobs = []
    for i in range(5):
        p = mp.Process(target=worker)
        jobs.append(p)
        p.start()
