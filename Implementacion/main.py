#!/usr/bin/python3

# Docs: https://docs.python.org/3.6/library/sqlite3.html
import sqlite3
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.shortcuts import prompt
from populate import *

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Creación de tablas desde init.sql
with open("init.sql",'r') as init:
  init_data = init.read()
  c.executescript(init_data)
  conn.commit()

# Rellena la tabla con los datos de populate.py
c.executemany('INSERT INTO productoCulturalPadre VALUES (?,?,?,?,?)', productoCulturalPadre)
c.executemany('INSERT INTO entidadCreadora VALUES (?,?)', entidadCreadora)
c.executemany('INSERT INTO creadoPor VALUES (?,?,?)', creadoPor)
c.executemany('INSERT INTO asociadoA VALUES (?,?,?)', asociadoA)
c.executemany('INSERT INTO generoSupergenero VALUES (?,?,?)', generoSupergenero)
c.executemany('INSERT INTO perteneceA VALUES (?,?)', perteneceA)
c.executemany('INSERT INTO premiadaPor VALUES (?,?,?)', premiadaPor)

conn.close()



commands_completer = WordCompleter([
    'Ver-Productos',
    'Ver-Creadores',
  ], ignore_case=True)

if __name__ == '__main__':
  # Input command
  ic = prompt('Comando: ', completer=commands_completer)
  if ic == "Ver-Products":
    c.execute("")
  
  print('Comando: %s' % inputcommand)
