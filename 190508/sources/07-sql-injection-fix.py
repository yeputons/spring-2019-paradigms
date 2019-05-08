#!/usr/bin/env python3
import sqlite3

with sqlite3.Connection("sql-injection.sqlite3") as db:
  key = input('Text key: ')
  cursor = db.execute("""SELECT * FROM Text
                         WHERE owner='user' AND key='{}'"""
                         .format(key))
  print(list(cursor))
