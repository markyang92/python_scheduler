#!/usr/bin/env python3

import src.parser
from src.AppRunner import AppRunner
from src.debug import *
import time

def run_apps(schedule,log):
    # Get now time
    now = time.time()

    # Create app_runners list composed of AppRunner Class
    app_runners = []
    for i, now_schedule in enumerate(schedule):
        app_runners.append(AppRunner(now_schedule,now))
    
    # Execute app using thread in app_runners list
    for i,app in enumerate(app_runners):
        app.start() # thread start
    
    for i,app in enumerate(app_runners):
        app.join() # thread join
    
    print("This program is done!")


def run_expr(schedule,log):
    run_apps(schedule,log)


if __name__ == "__main__":
    scenario1 = src.parser.parsing()
    if src.parser.debug:
        print(scenario1.schedule)
        print(scenario1.log)
    
    run_expr(scenario1.schedule,scenario1.log)
