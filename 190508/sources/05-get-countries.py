#!/usr/bin/env python3
import sqlite3

with sqlite3.Connection("literacy.sqlite3") as db:
  cursor = db.execute("SELECT * FROM Country LIMIT 3")
  print(cursor.description)
  print(list(cursor))
  print(list(cursor))
