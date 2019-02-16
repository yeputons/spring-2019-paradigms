#!/usr/bin/env python3
import collections
import sys
from datetime import date

Person = collections.namedtuple('Person', ['first_name', 'last_name', 'birth_date', 'area'])
people = [
    Person(first_name='Albert', last_name='Einstein', birth_date=date(year=1879, month=3, day=14), area='physics'),
    Person(first_name='Alan', last_name='Turing', birth_date=date(year=1912, month=6, day=23), area='cs'),
    Person(first_name='Edsger', last_name='Dijkstra', birth_date=date(year=1930, month=5, day=11), area='cs'),
    Person(first_name='Niels', last_name='Bohr', birth_date=date(year=1885, month=10, day=7), area='physics'),
    Person(first_name='Leslie', last_name='Lamport', birth_date=date(year=1941, month=2, day=7), area='cs'),
]


def format_person(p):
    return '{}. {}, born on {}'.format(p.first_name[:1], p.last_name, p.birth_date)


def print_table(title, people):
    print('--- {} ---'.format(title))
    for p in people:
        print('* ' + format_person(p))
    print('Total: {}'.format(len(people)))


print_table('Physics', [p for p in people if p.area == 'physics'])
print()
print_table('Computer Science', [p for p in people if p.area == 'cs'])

oldest = min(people, key=lambda p: p.birth_date)
print('Oldest person: ' + format_person(oldest))
