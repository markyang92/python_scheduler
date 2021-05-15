#!/usr/bin/env python3
import subprocess
import shlex


# 1. Write Shell-Command in raw_cmd
raw_cmd="echo \"Hello World!\""

# 2. Shell-Command have to formatted by shlex.split() method
cmd=shlex.split(raw_cmd)

# Exception Handle
try:
    # 3. Run Process
    proc=subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    # -*- Do not need to save stdout message in variable -*- #
    # proc=subprocess.Popen(cmd)
except Exception as e:
    print(e)
    exit(1)

# Wait for proc
# out <- stdout msg from proc. You can show it using "print(out)"
# err <- stderr msg from proc. You can show it using "print(err)"
out, err = proc.communicate()

print(out)

