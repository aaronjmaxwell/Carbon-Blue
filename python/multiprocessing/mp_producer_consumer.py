'''
Multiple workers can consume data from a JoinableQueue and pass back to the parent.  A poison pill
technique stops the worker by adding one stop value per worker to the job queue.  The main process
uses join to wait for all tasks to complete.
'''
import multiprocessing as mp
import time

class Consumer(mp.Process):
    def __init__(self, task_q, result_q):
        mp.Process.__init__(self)
        self.task_q = task_q
        self.result_q = result_q

    def run(self):
        name = self.name
        while True:
            next_task = self.task_q.get()
            if next_task is None:
                print('{}: swallowing the poison pill'.format(name))
                self.task_q.task_done()
                break
            print ('{}: {}'.format(name, next_task))
            answer = next_task()
            self.task_q.task_done()
            self.result_q.put(answer)
class Task:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)
        return '{self.a} * {self.b} = {product}'.format(self = self, product = self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self = self)

if (__name__ == '__main__'):
    tasks = mp.JoinableQueue()
    results = mp.Queue()
    num = mp.cpu_count() * 2
    print('Creating {} consumers'.format(num))
    consumers = [Consumer(tasks, results) for i in range(num)]
    
    for w in consumers:
        w.start()
    
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))
    
    for i in range(num):
        tasks.put(None)

    tasks.join()
    tasks.close()

    while num_jobs:
        result = results.get()
        print ('Result:', result)
        num_jobs -= 1
