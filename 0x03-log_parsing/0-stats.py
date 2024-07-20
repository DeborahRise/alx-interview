#!/usr/bin/python3
""" A script that, reads the stdin, checks the correct input format and
generates a given metrics"""

import sys
import re
from collections import defaultdict

""" Initialize important variables"""
total_size = 0
line_count = 0
statuscode_count = defaultdict(int)

""" First step: compile the regular expression pattern into an object"""

valid_input = re.compile(r'(\d+\.\d+\.\d+\.\d+\)\-\[.+?\] \\"GET /projects/260 HTTP/1.1\\" (\d+) (\d+)')

"""The function to print the metrics"""


def print_metrics():
    """ Establish the print format"""
    print(f"file size: {total_size}")
    for status in sorted(statuscode_count.keys()):
        if statuscode_count[status] > 0:
            print(f"{status}: {statuscode_count[status]}")


""" Compare the input with the approved regex """
try:
    for file_input in sys.stdin:
        matching = valid_input.match(file_input)
        if matching:
            statuscode = matching.group(2)
            file_size = int(matching.group(3))
            total_size += file_size
            statuscode_count[statuscode] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
    sys.exit()

print_metrics()
