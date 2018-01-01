#!/usr/bin/python3


import sqlite3 # Interacción base de datos
from prompt_toolkit.contrib.completers import WordCompleter # Interfaz
from prompt_toolkit.shortcuts import prompt # Interfaz
from prompt_toolkit.history import InMemoryHistory # Historia
from tabulate import tabulate # Tabulado de datos

from populate import * # Inicialización de la base de datos

# Subsistemas
import productos
import entidades
import valoraciones



def load(conn, filename):
  with open(filename,'r') as f:
    data = f.read()
    c = conn.cursor()
    c.executescript(data)
    conn.commit()

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Activa comprobación de claves externas
c.execute("PRAGMA foreign_keys = ON")

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
c.executemany('INSERT INTO valoracionValora VALUES (?,?,?,?)', valoracionValora)
c.executemany('INSERT INTO puntua VALUES (?,?,?,?)', puntua)
c.executemany('INSERT INTO reporta VALUES (?,?,?)', reporta)


def ayuda(c):
  """Muestra posibles comandos"""
  l = sorted(map(lambda nom: [nom, comandos[nom].__doc__], comandos.keys()))
  print(tabulate(l, tablefmt="plain"))

def salir(c):
  """Termina la ejecución"""
  raise EOFError

comandos = {"Ayuda": ayuda, "Salir": salir}
comandos.update(productos.comandos)
comandos.update(entidades.comandos)
comandos.update(valoraciones.comandos)
commands_completer = WordCompleter(comandos.keys(), ignore_case = True)

if __name__ == '__main__':
  history = InMemoryHistory()
  print("Introduce \"Ayuda\" para ver los posibles comandos")
  try:
    while True:
      # Bucle de lectura de comandos
      print('')
      ic = prompt('Comando: ', completer=commands_completer, history=history)
      if ic in comandos: comandos[ic](c)
      else: print('Comando no válido. Introduce \"Ayuda\" para ver los posibles comandos')
  except (KeyboardInterrupt, EOFError):
    pass
  finally:
    conn.close()
