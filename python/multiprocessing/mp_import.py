"""
Target functions do not have reside in the same file as __main__.
However, the main work must still be shielded inside __main__.
"""
import multiprocessing as mp
import mp_import_worker
if (__name__ == '__main__'):
    jobs = []
    for i in range(5):
        p = mp.Process(target = mp_import_worker.worker,)
        jobs.append(p)
        p.start()
