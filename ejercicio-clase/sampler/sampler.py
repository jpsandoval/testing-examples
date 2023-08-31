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
        for thread_id, frames in sys._current_frames().items():
            if thread_id == self.tid :
                print('Stack for thread {}'.format(thread_id))
                stack = traceback.walk_stack(frames)
                for frame, _ in stack:  # pragma: no branch
                    code = frame.f_code.co_name
                    locals = frame.f_locals
                    print(code)
                #traceback.print_stack(frame) 
    
    def sample(self):
        while self.active:
            self.printStackTrace()
            sleep(1)