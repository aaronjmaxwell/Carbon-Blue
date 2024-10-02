"""Using timeouts.

By default, `~mp.Process.join` method blocks indefinitely. By passing a
timeout via *args (type float) representing the number of seconds to
wait, we can limit how long __main__ must wait before continuing on.
"""
import multiprocessing as mp

import workers
import services


if (__name__ == "__main__"):
    d = mp.Process(name="daemon", target=services.demon, daemon=True, args=(2, False))
    w = mp.Process(name="worker", target=workers.sleepy, daemon=False, args=(0, True, False))
    d.start()
    d.join(1.0)  # Note less than sleep time.
    print(f"have we timed out? {d.is_alive()}")
    w.start()
    w.join()
