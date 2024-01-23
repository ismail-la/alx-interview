#!/usr/bin/python3
'''Module for log parsing script.
Write a script that reads stdin line by line and computes metrics:

-Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
-After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    ->Total file size: File size: <total size>
    ->where <total size> is the sum of all previous <file size> (see input format above)
    ->Number of lines by status code:
      -possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
      -if a status code doesn’t appear or is not an integer, don’t print anything for this status code
      -format: <status code>: <number>
      -status codes should be printed in ascending order

'''


import sys

codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

size_total = 0
count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            code_status = line_list[-2]
            size_file = int(line_list[-1])

            if code_status in codes_dict.keys():
                codes_dict[code_status] += 1

            size_total += size_file
            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(size_total))

            for key, value in sorted(codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size_total))
    for key, value in sorted(codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
