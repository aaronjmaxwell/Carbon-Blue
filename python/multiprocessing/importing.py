"""Using imports in processes.

Target functions do not have reside in the same file as __main__.
However, the main work must still be shielded inside __main__.
"""
import multiprocessing as mp
import workers


if (__name__ == "__main__"):
    jobs = []
    for i in range(5):
        p = mp.Process(target=workers.dummy,)
        jobs.append(p)
        p.start()
