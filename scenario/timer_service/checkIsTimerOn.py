#!/usr/bin/env python3
import subprocess
import shlex
import sys
import time

# Check Is chromium-browser.timer in Active mode?

# 1. Write Shell-Command in raw_cmd
raw_cmd="systemctl --user status chromium-browser.timer"

# 2. Shell-Command have to formatted by shlex.split() method
cmd=shlex.split(raw_cmd)


while True:
    # Exception Handle
    try:
        # 3. Run Process
        proc=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        print("Exception Occured")
        exit(1)

    # Wait for proc
    # out <- stdout msg from proc. You can see it using "print(out)"
    # err <- stderr msg from proc. You can see it using "print(err)"
    out, err = proc.communicate()

    """
    # ===========================================================================
    # -*- systemctl status case -*-
    # $ systemctl --user status chromium-brower.timer
    #
    # Case 1. The Service is active (waiting)
    ● chromium-browser.timer - Execute chromium.service
        Loaded: loaded (/home/dhyang/.config/systemd/user/chromium-browser.timer; static; vendor preset: enabled)
        Active: active (waiting) since Mon 2021-05-17 14:29:15 KST; 3min 37s ago
        Trigger: Tue 2021-05-18 09:32:00 KST; 18h left
    Triggers: ● chromium.service

    5월 17 14:29:15 dhyang systemd[931]: Started Execute chromium.service.

    # ===========================================================================
    #
    # Case 2. The Service is inactive (dead)
    ● chromium-browser.timer - Execute chromium.service
        Loaded: loaded (/home/dhyang/.config/systemd/user/chromium-browser.timer; static; vendor preset: enabled)
        Active: inactive (dead)
        Trigger: n/a
    Triggers: ● chromium.service

    """

    # ==================================================
    # -*- refine output string -*-
    #
    # 1. split output line by line
    out=out.split("\n")

    # service_info dictionary is made for saving service info that I want
    service_info={'Service': None, 'Loaded': None, 'Active': [], 
            'Trigger': None, 'Triggers': None,
            'Log':[]}

    # 2. Refine
    for idx, var in enumerate(out):
        out[idx]=out[idx].strip()
        if out[idx] == "":
            del out[idx]

    # 2-1. double stripper to get inocecent string
    for idx, var in enumerate(out):
        out[idx]=out[idx].strip()


    # 3. each value pass into each 'key' in service_info
    for idx, var in enumerate(out):
        refined_this_line=var.split(' ')
        # separator
        sep = refined_this_line
        if sep[0] == '●':
            # sep : ['●', 'chromium-browser.timer', '-', 'Execute', 'chromium.service']
            # Insert Service name into 'service_info['Service']'
            service_info['Service']=sep[1]
            # -*- debug -*- 
            # print(service_info['Service'])
        elif sep[0] == 'Loaded:':
            service_info['Loaded']=sep[1]
            # -*- debug -*-
            # print(service_info['Loaded'])
        elif sep[0] == 'Active:':
            service_info['Active'].append(sep[1])
            service_info['Active'].append(sep[2])
        elif sep[0] == 'Trigger:':
            service_info['Trigger']=sep[1:]
            # -*- debug -*-
            # print(service_info['Trigger'])
        elif sep[0] == 'Triggers:':
            service_info['Triggers']=sep[2]
            # -*- debug -*-
            # print(service_info['Triggers'])
        else:
            # this is log
            # e.g. 5월 17 14:29:15 dhyang systemd[931]: Started Execute chromium.service.
            logs=var.split('\n')
            for idx, var in enumerate(logs):
                service_info['Log'].append(var)
            # -*- debug -*-
            # print(service_info['Log'])


    if service_info['Active'][0] != 'active':
        print("{}".format(service_info['Active']))
        print("execute {}".format(service_info['Service']))
        # Execute start service
        start_cmd="systemctl --user start chromium-browser.timer"
        start_cmd=shlex.split(start_cmd)
        timer_proc=subprocess.Popen(start_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(5)

    elif service_info['Active'][0] == 'active':
        print("{}".format(service_info['Active']))
        break
        

sys.exit(0)