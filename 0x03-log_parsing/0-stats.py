#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys


def print_metrics(dict_code, total_size):
    """
    Args:
        dict_code: dictionary of status code
        total_size: total of the file
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(dict_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
code = 0
counter = 0
dict_code = {"200": 0,
             "301": 0,
             "400": 0,
             "401": 0,
             "403": 0,
             "404": 0,
             "405": 0,
             "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_code.keys()):
                    dict_code[code] += 1

            if (counter == 10):
                print_metrics(dict_code, total_size)
                counter = 0

finally:
    print_metrics(dict_code, total_size)
