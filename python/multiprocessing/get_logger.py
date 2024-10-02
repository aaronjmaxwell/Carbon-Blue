"""Manipulating the logger

The logger object can be manipulated directly rather than passing a
logging object at init.
"""
import logging
import multiprocessing as mp

import workers


if (__name__ == "__main__"):
    mp.log_to_stderr()
    logger = mp.get_logger()
    logger.setLevel(logging.INFO)
    p = mp.Process(target=workers.sleepy, args=(0, False, True, "little black submarines"),)
    p.start()
    p.join()
