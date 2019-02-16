#!/usr/bin/env python3
# ./01-report-bad.py --header Header --input 01-a.in --footer footer
import sys

acc_balance = {}  # defaultdict
footer = None
max_acc_len = 7

i = 1
while i < len(sys.argv):  # Используйте argparse
    # Сравнивайте строчку целиком
    if sys.argv[i][0] == "-" and sys.argv[i][2] == "i":  # --input
        i += 1
        f = open(sys.argv[i])  # Закрывайте файлы конструкцией `with`
        for line in f.read().split("\n"):  # Можно итерироваться сразу по файлу
            if len(line.split("\t")) > 2:  # Проверяйте конкретный случай (пустая строка), а не ставьте заглушку
                acc = line.split("\t")[0]  # Используйте распаковку
                amount = line.split("\t")[2]
                if acc not in acc_balance: acc_balance[acc] = 0
                acc_balance[acc] -= int(amount)  # int() должен быть при чтении amount
                max_acc_len = max(max_acc_len, len(acc))  # Вычисления должы быть отделены от чтения

                acc = line.split("\t")[1]  # Не переиспользуйте переменные
                if acc not in acc_balance: acc_balance[acc] = 0
                acc_balance[acc] += int(amount)
                max_acc_len = max(max_acc_len, len(acc))
    elif sys.argv[i][0] == "-" and sys.argv[i][2] == "h":  # --header
        i += 1
        print("== " + sys.argv[i] + " ==")  # Вывод должен быть отделён от вычислений и чтения
    elif sys.argv[i][0] == "-" and sys.argv[i][2] == "f":  # --footer
        i += 1
        footer = sys.argv[i]
    else:
        sys.stderr.write("Unknown argument: {}".format(sys.argv[i]))
        sys.exit(1)
    i += 1

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


if footer:
    print(footer)
