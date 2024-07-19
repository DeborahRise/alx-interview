#!/usr/bin/python3
""" A script that, reads the stdin, checks the correct input format and
generates a given metrics"""

import sys
import re

if len(sys.argv) > 1:
    log_input = sys.argv[1]
    valid_format = 