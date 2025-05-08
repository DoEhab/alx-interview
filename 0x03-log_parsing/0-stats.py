#!/usr/bin/python3
import sys
from collections import defaultdict

"""
This script reads terminal input and print stats
"""


def print_stats(files_size, all_codes):
    """
    Print stats
    :param files_size: files size
    :param all_codes: all status codes
    :return:
    """
    print(f"File size: {files_size}")
    for code in sorted(all_codes.keys()):
        print(f"{code}: {all_codes[code]}")


total_size = 0
status_codes = defaultdict(int)
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
line_count = 0

try:
    for line in sys.stdin:
        parsed_input = line.strip().split()

        if len(parsed_input) < 7:
            continue

        try:
            file_size = int(parsed_input[-1])
            status_code = parsed_input[-2]
        except ValueError:
            continue

        if status_code in valid_codes:
            status_codes[status_code] += 1
        total_size += file_size

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)
            total_size = 0
            status_codes = defaultdict(int)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
