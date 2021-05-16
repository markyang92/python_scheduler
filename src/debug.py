#!/usr/bin/env python3
import sys
from src.color import *
from inspect import currentframe, getframeinfo
# -*- Use colored console -*- 
#
# print(Colors.Bold+Colors.RED+"msgs"+Colors.RESET)

def debugPrint(frameinfo):
    print("{:s}".format(frameinfo.filename),\
        Colors.BOLD+Colors.RED+" line: {:d}".format(frameinfo.lineno)\
            +Colors.RESET)

if __name__ == "__main__":
    debugPrint(getframeinfo(currentframe()))