#!/usr/bin/env python3
import argparse
import os
import sys
sys.path.append(os.getcwd())
from color import *
from debug import *
import glob

debug=False

def isThereCorrectFiles(path):
    found_files=glob.glob(path+'/*')
    schedule_file_flag=False
    log_file_flag=False
    for idx,var in enumerate(found_files):
        if os.path.basename(var) == "expr_schedule":
            schedule_file_flag=True
        elif os.path.basename(var) == "log":
            log_file_flag=True
    
    if schedule_file_flag and log_file_flag:
        return 
    else:
        if not schedule_file_flag:
            print(Colors.RED+Colors.BOLD+"[ERROR] File Not Found: expr_schedule"+Colors.RESET)
            sys.stderr.write("[ERROR] File Not Found: expr_schedule")
        if not log_file_flag:
            print(Colors.RED+Colors.BOLD+"[ERROR] File Not Found: log"+Colors.RESET)
            sys.stderr.write("[ERROR] File Not Found: log")
        sys.exit(1)

def parsing():
    parser = argparse.ArgumentParser(usage="{} --scenario <SCENARIO_PATH> [--debug]".format(sys.argv[0]),
                                     description="{} -- <SCENARIO_PATH> [-d]".format(sys.argv[0]))
    parser.add_argument("-s", "--scenario", 
                        help="Pass the scenario path that will execute.")
    parser.add_argument("-d", "--debug", help="Debug log for experiment script", action="store_true")

    args = parser.parse_args()

    ### Formatter args.scenario ###
    try:
        os.path.exists(args.scenario)
    except FileNotFoundError:
        print(Colors.RED+Colors.BOLD+"[ERROR] scenario directory doesn't exist!"+Colors.RESET)
        sys.exit(1)
    else:
        print(Colors.BOLD+Colors.BLUE+"scenario: {}".format(args.scenario)+Colors.RESET)
    scenario_path=os.path.normpath(os.path.abspath(args.scenario))
    schedule=scenario_path+'/expr_schedule'

    ## Check "is there 'expr_schedule' file exist?""
    try:
        isThereCorrectFiles(scenario_path)
    except:
        pass

    ### Formatter expr_schedule,log ###
    expr_schedule=scenario_path+'/expr_scenario'
    log=scenario_path+'/log'

    ### Formatter args.debug ###
    if args.debug:
        print(Colors.BOLD + Colors.RED + "This Program will be executed in Debug mode" + Colors.RESET)
        global debug
        debug=True


    return Scenario(scenario=expr_schedule,
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
                # CMD:str   start:float end:float   env:str message:str
                if idx == 1 or idx == 2:
                    schedule_list_now_line.append(float(var.strip()))
                elif idx == 3:
                    if (var.strip()).lower() == "none":
                        schedule_list_now_line.append(None)
                else:
                    schedule_list_now_line.append(var.strip())


            schedule_list.append(schedule_list_now_line)

        schedule_file.close()

        self.schedule=schedule_list
        if debug == True:
            debugPrint(getframeinfo(currentframe()))
            if len(self.schedule) == 0:
                print(Colors.BOLD+Colors.RED+"Schedule isn't parsed"+Colors.RESET)
            else:
                print(Colors.BOLD+Colors.YELLOW+"Schedule is parsed"+Colors.RESET)
                for idx, var in enumerate(self.schedule):
                    print("{} Pased line: {}".format(idx,var))


    
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
            if len(self.log) == 0:
                print(Colors.BOLD+Colors.RED+"Log isn't parsed"+Colors.RESET)
            else:
                print(Colors.BOLD+Colors.YELLOW+"Log is parsed"+Colors.RESET)
                for idx,var in enumerate(self.log):
                    print("{} Parsed line: {}".format(idx,var))

