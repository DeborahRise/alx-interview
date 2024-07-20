#!/usr/bin/python3
""" A script that, reads the stdin, checks the correct input format and
generates a given metrics"""

import sys
import re

""" Initialize important variables"""
total_size = 0
line_count = 0

""" First step: compile the regular expression pattern into an object"""

valid_input = re.compile(r'(\d+\.\d+\.\d+\.\d+\)\-\[d+.\] \\\"GET /projects/260 HTTP/1.1\\\" (\d+) (\d+)')

""" Compare the input with the approved regex """
for file_input in sys.stdin:
    matching = valid_input.match(file_input)
    if matching:
        if line_count % 10 == 0:
            
