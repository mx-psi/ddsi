#!/usr/bin/python3

# Docs: https://docs.python.org/3.6/library/sqlite3.html
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

with open("init.sql",'r') as init:
  init_data = init.read()
  c.executescript(init_data)
  conn.commit()

c.executemany('INSERT INTO productoCulturalPadre VALUES (?,?,?,?,?)', productos)
conn.close()
