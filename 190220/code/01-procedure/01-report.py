#!/usr/bin/env python3
import sys
from collections import defaultdict

acc_balance = defaultdict(int)
footer = None

i = 1
while i < len(sys.argv):
    if sys.argv[i] == "--input":
        i += 1
        with open(sys.argv[i]) as f:
            for line in f:
                acc_from, acc_to, amount = line.split("\t")
                acc_balance[acc_from] -= amount
                acc_balance[acc_to] += amount
    elif sys.argv[i] == "--header":
        i += 1
        print("== " + argv[i] + " ==")
    elif sys.argv[i] == "--footer":
        i += 1
        footer = sys.argv[i]
    else:
        sys.stderr.write("Unknown argument: {}".format(sys.argv[i])
        sys.exit(1)
    i += 1

# TODO

if footer:
    print(">> " + footer + " <<")
