#!/usr/bin/env python3
# ./01-report-bad.py --header Header --input 01-a.in --footer footer
from collections import namedtuple
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', nargs='+')
parser.add_argument('--header')
parser.add_argument('--footer')
args = parsers.parse_args()


Transaction = collections.namedtuple('Transaction', ['acc_from', 'acc_to', 'amount'])


def read_transactions(f):
    result = []
    with open(f) as f:
        for line in f:
            acc_from, acc_to, amount = line.split("\t")
            result.append(Transaction(acc_from, acc_to, amount))
    return result


transactions = []
for fname in args['input']:
    transactions += read_transactions(fname)


def get_balaces(t):
    acc_balance = collections.defaultdict(int)
    acc_balance[t.acc_from] -= t.amount
    acc_balance[t.acc_to] += t.amount
    return acc_balance


acc_balances = get_balances(transactions)

if args['header']:
    print("== " + args['header'] + " ==")

# TODO
max_balance_len = 7
for balance in acc_balance.values():  # max + list comprehension
    max_balance_len = max(max_balance_len, len(str(balance)))

# Вывод таблички с центровкой и подсчёт данных в ячейках стоит разделить
sys.stdout.write("|")
for i in ["Account", "Balance"]:
    # Не стоит сразу выводить на экран - так не протестировать.
    # Например, тут есть баг и зависимость len("Account") == len("Balance") == 7.
    sys.stdout.write(" " * (1 + max(0, (max_acc_len - 7) // 2)))
    sys.stdout.write(i)
    sys.stdout.write(" " * (1 + max(0, (max_acc_len - 7) // 2)))
    sys.stdout.write("|")
print()

for account in acc_balance:
    line = "| " + account + " " * (max_acc_len - len(account)) + " | "
    line += str(acc_balance[account]) + " " * (max_balance_len - len(str(acc_balance[account]))) + " |"
    print(line)


if args['footer']:
    print(args['footer'])
