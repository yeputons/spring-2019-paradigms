#!/usr/bin/env python3
import sys
from collections import defaultdict

acc_balance = defaultdict(int)
footer = None
max_acc_len = 7

i = 1
while i < len(sys.argv):
    if sys.argv[i] == "--input":
        i += 1
        with open(sys.argv[i]) as f:
            for line in f:
                acc_from, acc_to, amount = line.split("\t")
                amount = int(amount)
                acc_balance[acc_from] -= amount
                acc_balance[acc_to] += amount
                max_acc_len = max(max_acc_len, len(acc_from))
                max_acc_len = max(max_acc_len, len(acc_to))
    elif sys.argv[i] == "--header":
        i += 1
        print("== " + sys.argv[i] + " ==")
    elif sys.argv[i] == "--footer":
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
for name in ["Account", "Balance"]:
    sys.stdout.write(" " * (1 + max(0, (max_acc_len - 7) // 2)))
    sys.stdout.write(name)
    sys.stdout.write(" " * (1 + max(0, (max_acc_len - 7) // 2)))
    sys.stdout.write("|")
print()

for account, balance in acc_balance.items():
    line = "| " + account + " " * (max_acc_len - len(account)) + " | "
    line += str(balance) + " " * (max_balance_len - len(str(balance))) + " |"
    print(line)


if footer:
    print(footer)
