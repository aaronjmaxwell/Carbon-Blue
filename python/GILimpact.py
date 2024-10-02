"""Understanding the GIL's impact."""
import threading
import time


def dummy_counter():
    c = 0
    for i in range(10000000):
        c+=1
    print(f"Task completed with count = {c}")


def dummy_numbers():
    for n in range(10):
        print(f"Number {n}")
        time.sleep(1)


def dummy_letters():
    for l in "abcdefghij":
        print(f"Letter {l}")
        time.sleep(1)


def serial(tasks):
    t = time.time()
    for task in tasks:
        task()
    print(f"Executing {len(tasks)} times in serial: {time.time()-t} s.")


def threaded(tasks):
    threads = [threading.Thread(target=task) for task in tasks]
    t = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Executing {len(tasks)} threads: {time.time()-t} s.")



if __name__ == "__main__":
    serial([dummy_counter, dummy_counter])
    threaded([dummy_counter, dummy_counter])
    threaded([dummy_numbers, dummy_letters])
