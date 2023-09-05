import threading
from sampler import Sampler
from program import *
from multiprocessing import Process
import os

if __name__ == '__main__':
    p = threading.Thread(target=main, args=())
    p.start()
    profiler = Sampler(p.ident)
    profiler.start()
    p.join()
    profiler.stop()