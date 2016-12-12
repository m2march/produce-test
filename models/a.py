import sys

with open(sys.argv[1]) as f:
    for l in f:
        print int(l) * 2
