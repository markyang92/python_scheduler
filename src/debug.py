#!/usr/bin/env python3
import sys
import os

sys.path.append(os.getcwd())
from color import Colors

from inspect import currentframe, getframeinfo

"""
* =========================================
* -*- If you want to output 'Debug File, Debug Name' -*-
* Other Py:
* 1. from <PATH>.src.debug import debugPrint
*
* 2. debugPrint(getframeinfo(currentframe()))
*
* =========================================
"""

def debugPrint(frameinfo):
    print("{:s}".format(frameinfo.filename),\
        Colors.BOLD+Colors.RED+" line: {:d}".format(frameinfo.lineno)\
            +Colors.RESET)

if __name__ == "__main__":
    debugPrint(getframeinfo(currentframe()))