"""Extending the simple example with arguments.

Passing arguments to the spawned process uses the `args` keyword. All
arguments passed between processes must be able to be serialized using
`pickle`.
"""
import multiprocessing as mp


def worker(n: int)->None:
    """Worker function receiving arguments."""
    print(f"Worker:  {n}")


if (__name__ == "__main__"):
    jobs = []
    for i in range(5):
        p = mp.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
