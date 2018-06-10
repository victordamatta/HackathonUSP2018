import sys
for line in sys.stdin.readlines():
    print(' '.join(map(lambda w: w.lower(), line.split())))
