from __future__ import print_function
import threading
from time import sleep
import traceback
import sys
import sys, traceback

class Sampler:
    def __init__(self, tid) -> None:
        self.tid = tid
        self.t= threading.Thread(target=self.sample, args=())
        self.active = True
        
        
    def start(self):
        self.active = True
        self.t.start()

    
    def stop(self):
        self.active = False
        
    def printStackTrace(self):
        for thread_id, frame in sys._current_frames().items():
            if thread_id == self.tid :
                print('Stack for thread {}'.format(thread_id))
                print(frame.__class__)
                traceback.print_stack(frame) 
    
    def sample(self):
        while self.active:
            self.printStackTrace()
            sleep(1)