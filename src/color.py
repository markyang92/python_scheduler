#!/usr/bin/python3

# Define "from <where is this file>.color import *" in Other python files
"""
# ================================
# -*- This py can control color on colsole
#
# Other file:
# 1. from src.color import *
#
# 2. print(Colors.BOLD+"Hello"+Colors.RESET)
"""


# -*- coding: utf-8 -*- 
BRIGHT_BLACK = '\033[90m' 
BRIGHT_RED = '\033[91m' 
BRIGHT_GREEN = '\033[92m' 
BRIGHT_YELLOW = '\033[93m' 
BRIGHT_BLUE = '\033[94m' 
BRIGHT_MAGENTA = '\033[95m' 
BRIGHT_CYAN = '\033[96m' 
BRIGHT_WHITE = '\033[97m' 
BRIGHT_END = '\033[0m' 

class Colors: 
    BLACK = '\033[30m' 
    RED = '\033[31m' 
    GREEN = '\033[32m' 
    YELLOW = '\033[33m' 
    BLUE = '\033[34m' 
    MAGENTA = '\033[35m' 
    CYAN = '\033[36m' 
    WHITE = '\033[37m' 
    UNDERLINE = '\033[4m' 
    RESET = '\033[0m' 
    BOLD = '\033[1m'


if __name__ == '__main__': 
    print(Colors.BOLD + Colors.RED + 'TEST' + Colors.RESET) 
    print(BRIGHT_YELLOW + 'TEST' + BRIGHT_END) 
    print(Colors.RED + 'TE' + Colors.BLUE + 'ST' + Colors.RESET)
