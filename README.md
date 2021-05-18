# scripts
- Author: Mark.yang@lge.com

1. User descibed each scenario and script will be executed using Thread.
2. Several Commands will be composed of each Thread

## file tree
```python
├── LICENSE
├── README.md
├── run_script.py           # run script
├── scenario
│   ├── sample_scenario     # scenario
│   └── timer_service
│        ├── checkIsTimerOn.py      # simple check shell 1
│        ├── expr_schedule          # to be scheduled
│        └── log
│ 
└── src
```

---

# Usage
- `run_script.py -s <Senario Path What You want to execute> [-d]`
- `run_script.py --scenario <Scenario Path>  [--debug]`

**e.g.**
- `run_script.py -s ./scenario/sample_scenario -d`

---
# Make Own Schedule
1. create your schedule dir (You want to create a scenario named 'timer_service') <br>
`$ cp -r ./scenario/sample_scenario ./scenario/timer_service`

2. expr_schedule will create "each thread" using line by line
- I suggest that 
    1. Long Command or Complicated Command: Makes another schedule.py
    - e.g,
        - write `checkIsTimerOn.py # complicated schedule program`
        - In **expr_schedule**
            -  `/home/dhyang/.../scripts/scenario/timer_service/checkIsTimerOn.py   5   10  none    "Log"`
    2. Simple Command: Just enter cmd in expr_schedule
    - e.g.
        - `/usr/bin/echo "Hello World!" 5   10  none    "Hello World log"`