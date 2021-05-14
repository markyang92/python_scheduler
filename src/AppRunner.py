#!/usr/bin/python3
import subprocess
import time
import threading
import shlex
import os

import src.parser
################### debug ####################
from inspect import currentframe, getframeinfo
def debugPrint(frameinfo):
    print("{} line: {}".format(frameinfo.filename,frameinfo.lineno),end=' ')
# debugPrint(getframeinfo(currentframe()))
############################################
class ExperimentKillError(Exception):
    def __init__(self, proc):
        self.proc = proc
        self.proc.kill()
    def __str__(self):
        return "{:s} is killed because experiment is done".format(self.proc)

class AppRunner(threading.Thread):
    def __init__(self, schedule, absolute_time=0):
        threading.Thread.__init__(self)

        self.schedule=schedule
        self.app, self.start_time, self.end_time, self.env, self.app_message= self.schedule


        self.proc = None
        self.app_cmd=shlex.split(self.app)  
        self.absolute_time=absolute_time
        self.debug=src.parser.debug
        self._return=None
        
    def run(self):
        # starts app at desgined time
        self.wait_till(self.start_time) # Sleep app at 0.5 seconds until start time

        # After start time, App will wake up!

        # execute app
        if self.debug:
            print("[Info] [{:s}] is executed".format(self.app))
        
        # start time
        start_time=time.time()

        # App is created and start as process instance in THIS THREAD
        try:
            self.proc=subprocess.Popen(self.app_cmd, env=self.env, stdout=self.proc.PIPE)
        except Exception as e:
            debugPrint(getframeinfo(currentframe()))
            print(e)

        self.set_timeout(self.end_time)
        out, err=self.proc.communicate()    
        if self.debug:
            print(out)
        if err != None: # if err get not None, Then Some Error Occured!
            print(err)

    def set_timeout(self, timeout):
        try:
            if self.debug:
                print(self.proc)
            if timeout == float("inf"):
                self.proc.wait(timeout=float("inf"))
            else:
                self.proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            # In this case, App will killed by end_time 
            self.kill_by_raise()
        
        else:
            # In this case, App will be finished Before end_time
            pass
        

    def kill_by_raise(self):
        if self.is_alive():
            raise ExperimentKillError(self.proc)

    def wait_till(self, t, interval=0.5):
        if t == 0:
            return
        while self.get_elapsed_time() < t:
            time.sleep(interval)

    def get_elapsed_time(self):
        return time.time() - self.absolute_time

    def join(self):
        threading.Thread.join(self)
        return self._return