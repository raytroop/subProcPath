import os
import sys
import datetime

print(os.getcwd())

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
assert count == 1, 'One directory name is NEEDED'

if os.path.isdir(sys.argv[1]):
    pass
else:
    timestr = datetime.datetime.now().strftime("%H:%M:%S.%f")
    os.mkdir(sys.argv[1]+timestr)