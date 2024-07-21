#!/usr/bin/python3
""" the log parsing task"""

import sys
import re
from collections import defaultdict

"""Compile the regex pattern to match the log format"""
pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+)'    # IP Address
    r' - \[.+?\] '              # Date in square brackets
    r'"GET /projects/260 HTTP/1.1" '
    r'(\d+) '                   # Status code
    r'(\d+)'                    # File size
)

"""Initialize variables"""
total_size = 0
status_counts = defaultdict(int)
line_count = 0

"""Define a function to print the metrics"""


def print_metrics():
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


"""Read from standard input line by line"""
try:
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            """Extract the status code and file size"""
            status_code = match.group(2)
            file_size = int(match.group(3))
            # Update the total file size and status code count
            total_size += file_size
            status_counts[status_code] += 1
        line_count += 1
        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    # Print final metrics if interrupted
    print_metrics()
    sys.exit()

# Final print after reading all lines
print_metrics()
