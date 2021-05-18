#!/usr/bin/env python3
import sys
import os
sys.path.append(os.getcwd())
import subprocess
import time
import threading
import shlex


from src.parser import *
from color import Colors
from debug import debugPrint
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
        self.debug=debug
        self._return=None
        
    def run(self):
        # At first, Go to sleep "self.app" until self.starttime
        self.wait_till(self.start_time) # Check Does app still get in sleep until self.starttime. check interval is just 0.5 sec.

        # After start time, App will wake up!

        # execute app
        if self.debug:
            print(Colors.MAGENTA+Colors.BOLD+"[Info] [{:s}] is executed".format(self.app)+Colors.RESET)
        

        # App is created and start as process instance in THIS THREAD
        try:
            self.proc=subprocess.Popen(self.app_cmd, env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        except FileNotFoundError:
            # 1. If Occured FileNotFoundError Exception, That will pass set_timeout method
            print(Colors.BOLD+Colors.RED+"[Error]: {} is not found! and Killed!".format(str(self.app_cmd))+Colors.RESET)
            # 2. It will be killed
            sys.exit(1)

        self.set_timeout(self.end_time)
        out, err=self.proc.communicate()    

        print("{}'s STDOUT: {}".format(self.app,out),end='')
        print("{}'s STDERR: {}".format(self.app,err),)
        print("{}'s return: {}".format(self.app,self.proc.returncode))
    def set_timeout(self, timeout):
        try:
            # Timeout is 'inf' then, this app.cmd will not be killed,
            # Before app.cmd will be done.
            if timeout == float("inf"):
                self.proc.wait(timeout=float("inf"))
            else:
                self.proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            # In this case, App will be killed by end_time, no matter Wheather or not this app isn't done.
            self.kill_by_raise()
        
        

    def kill_by_raise(self):
        if self.is_alive():
            raise ExperimentKillError(self.proc)

    def wait_till(self, start_time, interval=0.5):
        if start_time == 0:
            # If start_time is 0, self.app_cmd is executed as soon as Scheduler app is stated.
            return
        while self.get_elapsed_time() < start_time:
            # This task will get sleep mode until App Start time
            time.sleep(interval)

    def get_elapsed_time(self):
        return time.time() - self.absolute_time

    def join(self):
        if not threading.Thread.isAlive(self):
            threading.Thread.join(self)
            return 1
        
        threading.Thread.join(self)
        return 0