#!/usr/bin/python3
import subprocess
import time
import threading
import shlex
import os

class ExperimentKillError(Exception):
    def __init__(self, cmd):
        self.cmd = cmd
    def __str__(self):
        return "{:s} is killed because experiment is done".format(self.cmd)

class AppRunner(threading.Thread):
    def __init__(self, schedule, absolute_time=0, debug=False):
        threading.Thread.__init__(self)

        self.proc = None
        self.schedule=schedule
        self.app, self.start_time, self.execution_time, self.env, \
            self.app_type, self.how_many = schedule
        self.app_cmd=shlex.split(self.app)
        self.absolute_time=absolute_time
        self.debug=debug
        self._return=None
    
    def run(self):
        # starts app at desgined time
        if self.debug:
            print("[Info] [{:s}] wait till {:f}".format(self.app, self.start_time))
        self.wait_till(self.start_time)

        # execute app
        if self.debug:
            print("[Info] [{:s}] is executed".format(self.app))
        
        # start time
        start_time=time.time()
        if(self.)