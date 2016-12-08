import sys

def conv():
    for line in sys.stdin:
        line = line[:-1]
        line = line.replace('\\n', '\n')
        line = line.replace('\\"', '"')
        line = line.replace('\\t', '\t')
        print line

conv()
