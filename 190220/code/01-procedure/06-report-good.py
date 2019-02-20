#!/usr/bin/env python3
import sys
import collections
import argparse

Transaction = collections.namedtuple(
    'Transaction',
    ['acc_from', 'acc_to', 'amount']
)


def read_transactions(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f.read().split('\n'):
            if not line:
                continue  # Early return/continue
            acc_from, acc_to, amount = line.split('\t')
            result.append(Transaction(
                acc_from,
                acc_to,
                int(amount)
            ))
    return result


parser = argparse.ArgumentParser()
parser.add_argument('--input', nargs='+')
parser.add_argument('--header')
parser.add_argument('--footer')
args = parser.parse_args()

if args.header:
    print('== ' + args.header + ' ==')

transactions = []
for filename in args.input:
    transactions += read_transactions(filename)

# TODO: extract into a separate procedure because transactions processing
# may become a hard problem
acc_balance = collections.defaultdict(int)
for t in transactions:
    acc_balance[t.acc_from] -= t.amount
    acc_balance[t.acc_to] += t.amount

# TODO: use a sane library instead (Google it!)
ACCOUNT_HEADER = 'Account'
BALANCE_HEADER = 'Balance'

max_acc_len = max(len(ACCOUNT_HEADER), *[len(acc) for acc in acc_balance])
# max_acc_len = max(7, *map(len, acc_balance))
max_balance_len = max(len(BALANCE_HEADER), *[len(str(balance)) for balance in acc_balance.values()])

def format_header(titles, width):
    result = '|'
    for title, width in zip(titles, width):
        title_formatter = '{:^' + str(width + 2) + '}'
        result += title_formatter.format(title)
        result += '|'
    return result

print(format_header([ACCOUNT_HEADER, BALANCE_HEADER],
                    [max_acc_len, max_balance_len]))

for account in acc_balance:
    # TODO: refactor this like format_header()
    line = '| ' + account + ' ' * (max_acc_len - len(account)) + ' | '
    line += str(acc_balance[account]) + ' ' * (max_balance_len - len(str(acc_balance[account]))) + ' |'
    print(line)


if args.footer:
    print(args.footer)
