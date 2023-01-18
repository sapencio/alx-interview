#!/usr/bin/env python3

import sys

# counters for status codes
code200 = 0
code301 = 0
code400 = 0
code401 = 0
code403 = 0
code404 = 0
code405 = 0
code500 = 0
total_size = 0 # total file size of all files

counter = 0 # counter to print out metrics every 10 lines
for line in sys.stdin:
    line_split = line.split(' ')
    # Skip if not correct format
    if len(line_split) != 8:
        continue
    counter += 1
    status_code = line_split[6]
    file_size = int(line_split[7])
    total_size += file_size
    count_num = 0
    # Count number of codes
    if status_code == '200':
        code200 += 1
        count_num = code200
    elif status_code == '301':
        code301 += 1
        count_num = code301
    elif status_code == '400':
        code400 += 1
        count_num = code400
    elif status_code == '401':
        code401 += 1
        count_num = code401
    elif status_code == '403':
        code403 += 1
        count_num = code403
    elif status_code == '404':
        code404 += 1
        count_num = code404
    elif status_code == '405':
        code405 += 1
        count_num = code405
    elif status_code == '500':
        code500 += 1
        count_num = code500
    else:
        continue


    # Print metrics every 10 lines or when CTRL+C
    if counter % 10 == 0: 
        # print number of lines by status code
        if 200 in line_split: 
            print('200: ' + str(code200))
        if 301 in line_split:
            print('301: ' + str(code301))
        if 400 in line_split:
            print('400: ' + str(code400))
        if 401 in line_split:
            print('401: ' + str(code401))
        if 403 in line_split:
            print('403: ' + str(code403))
        if 404 in line_split:
            print('404: ' + str(code404))
        if 405 in line_split:
            print('405: ' + str(code405))
        if 500 in line_split:
            print('500: ' + str(code500))
        # print total file size of all files
        print('File size: ' + str(total_size))
