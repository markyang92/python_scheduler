#!/usr/bin/env python3
import subprocess
import shlex


# 1. Write Shell-Command in raw_cmd
raw_cmd="echo \"Hello World!\""

# 2. Shell-Command have to formatted by shlex.split() method
cmd=shlex.split(raw_cmd)

# Exception Handle
try:
    proc=subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
except Exception as e:
    print(e)
    exit(1)

out, err = proc.communicate()
print(out)




