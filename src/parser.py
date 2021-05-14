#!/usr/bin/python3
import argparse
import os.path
import sys

### for Debug ###
debug=False
from inspect import currentframe, getframeinfo
def debugPrint(frameinfo):
    print("{} line: {}".format(frameinfo.filename,frameinfo.lineno),end=' ')
# debugPrint(getframeinfo(currentframe()))
#################

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scenario", help="Execute scenario path. e.g., --scenario ./scenario/timer_service",required=True)
    parser.add_argument("-d", "--debug", help="Debug log for experiment script", action="store_true")

    args = parser.parse_args()

    ### Formatter args.scenario ###
    try:
        os.path.exists(args.scenario)
    except Exception as e:
        print(e)
        print("scenario directory doesn't exist!")
    else:
        print("scenario directory: " + args.scenario)
    scenario=os.path.normpath(os.path.abspath(args.scenario))
    schedule=scenario+'/expr_schedule'

    ### Formatter args.debug ###
    if args.debug:
        print(args.debug)
        global debug
        debug=True

    ### Formatter log ###
    log=scenario+'/log'

    return Scenario(scenario=scenario,
             schedule=schedule,
             log=log)


class Scenario:
    def __init__(self,scenario,schedule,log):
        self.scenario_path=scenario
        self.schedule_path=schedule
        self.log_path=log
        self.schedule=None  # schedule list
        self.log=None       # log list
        self.scheduleParser()
        self.logParser()

    
    def scheduleParser(self):
        schedule_file=open(self.schedule_path, 'r')
        schedule_list=[]
        while True:
            line=schedule_file.readline()
            if not line:
                break
            if line[0]=='#':    # In Expr_schedule, # Character is comment
                continue
            line=line.split('\t')
            schedule_list_now_line=[]
            for idx, var in enumerate(line):
                schedule_list_now_line.append(var.strip())


            schedule_list.append(schedule_list_now_line)

        schedule_file.close()

        self.schedule=schedule_list
        if debug == True:
            debugPrint(getframeinfo(currentframe()))
            print(self.schedule)
    
    def logParser(self):
        log_file=open(self.log_path)
        log_list=[]
        while True:
            line=log_file.readline()
            if not line:
                break
            if line[0]=='#':    # In log, # Character is comment
                continue
            line=line.split('\t')
            log_list_now_line=[]
            for idx, var in enumerate(line):
                log_list_now_line.append(var.strip())
            
            log_list.append(log_list_now_line)
        
        log_file.close()

        self.log=log_list
        if debug == True:
            debugPrint(getframeinfo(currentframe()))
            print(self.log)

