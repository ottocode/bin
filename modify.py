import sys
import fileinput
from string import *

fname = sys.argv[1]
newf = sys.argv[2]
which = sys.argv[3]
mover = sys.argv[4]

f = open(fname)
newf = open(newf, 'w+')

print int(mover)

for line in f.readlines():
    l = line #.rstrip('\n')
    n = ''
    for c in l:
        if( int(which) == 1):
            n += chr(ord(c) + int(mover))
        else:
            n += chr(ord(c) - int(mover))
    newf.write(n)
