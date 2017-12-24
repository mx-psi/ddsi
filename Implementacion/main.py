#!/usr/bin/python3

# Docs: https://docs.python.org/3.6/library/sqlite3.html
import sqlite3
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from populate import *


def load(conn, filename):
  with open(filename,'r') as f:
    data = f.read()
    c = conn.cursor()
    c.executescript(data)
    conn.commit()

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Carga creación de tablas y disparadores
load(conn,"init.sql")
load(conn, "triggers.sql")

# Rellena la tabla con los datos de populate.py
c.executemany('INSERT INTO productoCulturalPadre VALUES (?,?,?,?,?)', productoCulturalPadre)
c.executemany('INSERT INTO entidadCreadora VALUES (?,?)', entidadCreadora)
c.executemany('INSERT INTO creadoPor VALUES (?,?,?)', creadoPor)
c.executemany('INSERT INTO asociadoA VALUES (?,?,?)', asociadoA)
c.executemany('INSERT INTO generoSupergenero VALUES (?,?,?)', generoSupergenero)
c.executemany('INSERT INTO perteneceA VALUES (?,?)', perteneceA)
c.executemany('INSERT INTO premiadaPor VALUES (?,?,?)', premiadaPor)
c.executemany('INSERT INTO usuario VALUES (?,?,?,?,?,?)', usuario)
c.executemany('INSERT INTO leGusta VALUES (?,?)', leGusta)




commands_completer = WordCompleter([
    'Ver-Productos',
    'Ver-Creadores',
    'Añadir-Productos',
    'Salir',
  ], ignore_case=True)


if __name__ == '__main__':
  quitar = False

  while not quitar:
    # Bucle de lectura de comandos
    print('')
    ic = prompt('Comando: ', completer=commands_completer)
    print('')

    if ic == "Salir":
      quitar = True
  
    elif ic == "Ver-Productos":
      c.execute("SELECT * FROM productoCulturalPadre")
      print(tabulate(c.fetchall(), headers=['Id','Título','Fecha','Tipo','Inspirado en']))
  
  
    elif ic == "Ver-Creadores":
      c.execute("SELECT * FROM entidadCreadora")
      print(tabulate(c.fetchall(), headers=['Nombre','Tipo']))

    elif ic == "Añadir-Productos":
      print('Añadiendo un producto cultural.')
      prod_nombre = prompt('Nombre del producto: ')
      prod_fecha = prompt('Fecha de creación: ')
      prod_tipo = prompt('Tipo del producto: ')
      prod_inspirado = prompt('Inspirado en: ')
      c.execute('INSERT INTO productoCulturalPadre VALUES (?, ?, ?, ?, ?)',
                (12,prod_nombre,prod_fecha,prod_tipo,prod_inspirado))
      
    else:
      print('El comando introducido no es válido')

  conn.close()
