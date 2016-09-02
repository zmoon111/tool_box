#!/usr/bin/env python
import traceback 
import sys
import time

if len(sys.argv) != 2:
    print "usage: py token_mem.py <number-of-megabytes>"
    sys.exit()

try:
    count = int(sys.argv[1])
    megabyte = (0,) * (1024 * 1024 / 8)
    data = megabyte * count
except Exception,e:
    print "here"
    traceback.print_exc()

while True:
    time.sleep(1)


