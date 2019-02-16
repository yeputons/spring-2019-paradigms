#!/usr/bin/env python3
# ./01-report-bad.py --header Header --input 01-a.in --footer footer
import sys
from collections import defaultdict

acc_balance = defaultdict(int)
footer = None
max_acc_len = 7

i = 1
while i < len(sys.argv):
    if sys.argv[i][0] == "-" and sys.argv[i][2] == "i":  # --input
        i += 1
        f = open(sys.argv[i])
        for line in f.read().split("\n"):
            if len(line.split("\t")) > 2:
                acc = line.split("\t")[0]
                amount = line.split("\t")[2]
                acc_balance[acc] -= int(amount)
                max_acc_len = max(max_acc_len, len(acc))
                acc = line.split("\t")[1]

                acc_balance[acc] += int(amount)
                max_acc_len = max(max_acc_len, len(acc))
    elif sys.argv[i][0] == "-" and sys.argv[i][2] == "h":  # --header
        i += 1
        print("== " + sys.argv[i] + " ==")
    elif sys.argv[i][0] == "-" and sys.argv[i][2] == "f":  # --footer
        i += 1
        footer = sys.argv[i]
    else:
        sys.stderr.write("Unknown argument: {}".format(sys.argv[i]))
        sys.exit(1)
    i += 1

max_balance_len = 7
for balance in acc_balance.values():
    max_balance_len = max(max_balance_len, len(str(balance)))

sys.stdout.write("|")
for i in ["Account", "Balance"]:
    sys.stdout.write(" " * (1 + max(0, (max_acc_len - 7) // 2)))
    sys.stdout.write(i)
    sys.stdout.write(" " * (1 + max(0, (max_acc_len - 7) // 2)))
    sys.stdout.write("|")
print()

for account in acc_balance:
    line = "| " + account + " " * (max_acc_len - len(account)) + " | "
    line += str(acc_balance[account]) + " " * (max_balance_len - len(str(acc_balance[account]))) + " |"
    print(line)


if footer:
    print(footer)
