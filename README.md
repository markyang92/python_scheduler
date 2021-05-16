# scripts
- Author: Mark.yang@lge.com

1. User descibed each scenario and script will be executed using Thread.
2. Several Commands will be composed of each process
3. One Scenario is controlled by The one Scenario Task.

## DebugTool
- DebugTool is in `src/debug.py`

### Debugmode
- You can execute script in debugmode, When you pass `-d` or `--debug` option
`./run_script.py -s <SENARIO> -d`

### How to use debug print at your code.
1. Check the definition 
- `from src.debug import *`

2. `debugPrint(getframeinfo(currentframe()))`