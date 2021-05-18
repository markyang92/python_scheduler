#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2021 MarkYang

All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: pllpokko@alumni.kaist.ac.kr

Description: This script is used for executing specific script.
"""

import sys
import os
sys.path.append(os.getcwd()+'/src')
from parser import *
from AppRunner import AppRunner
from debug import *
from color import *
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
    


def run_expr(schedule,log):
    run_apps(schedule,log)


if __name__ == "__main__":
    scenario1 = parser.parsing()
    
    run_expr(scenario1.schedule,scenario1.log)

    print(Colors.GREEN+"The Scheduling Program is sucessfully terminated\nreturn code 0."+Colors.RESET)
    sys.exit(0)
