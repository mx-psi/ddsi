#!/usr/bin/python3

# Docs: https://docs.python.org/3.6/library/sqlite3.html
import sqlite3
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.shortcuts import prompt
from colorama import Fore
import colorama
import sphinx.quickstart
from tabulate import tabulate
from populate import *
colorama.init()


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
    'Añadir-Premios',
    'Consultar-Creadores',
    'Añadir-Género',
    'Consultar-Género',
    'Salir',
  ], ignore_case = True)

def leerEntidad(text):
  c.execute("SELECT nombre FROM entidadCreadora")
  return prompt(text, completer=WordCompleter([t[0] for t in c.fetchall()], ignore_case = True))

def leerGenero(text):
  c.execute("SELECT nombreGenero FROM generoSupergenero")
  return prompt(text, completer=WordCompleter([t[0] for t in c.fetchall()], ignore_case = True))

def leerProducto(text):
  c.execute("SELECT nombre FROM productoCulturalPadre")
  return prompt(text, completer=WordCompleter([t[0] for t in c.fetchall()], ignore_case = True))


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

    elif ic == "Añadir-Entidades":
      # RF-2.1. Añadir entidad creadora.  Esta función registra una
      # entidad creadora dentro del sistema a partir de su nombre y
      # tipo.
      print('Añadiendo una entidad creadora.')
      ent_nombre = prompt("Nombre: ")
      ent_tipo = prompt("Tipo: ")
      c.execute('INSERT INTO entidadCreadora VALUES (?, ?)',
                (ent_nombre,ent_tipo))

    elif ic == "Añadir-Premios":
      # RF-2.2. Registrar un premio asociado a la creación de una
      # entidad creadora.  Esta función añade un premio dada una
      # entidad creadora que lo recibe y un producto cultural por el
      # cual lo recibe.
      print('Añadiendo un premio')
      prm_entidad = prompt("Entidad que recibe el premio: ")
      prm_producto = prompt("ID del producto por el que recibe el premio: ")
      prm_nombre = prompt("Nombre del premio: ")
      c.execute('INSERT INTO premiadaPor VALUES (?, ?, ?)',
                (prm_entidad, prm_producto, prm_nombre))

    elif ic == "Consultar-Creadores":
      # RF-2.3. Consultar una entidad creadora.  Dado el nombre de una
      # entidad creadora, esta función muestra el nombre, tipo,
      # productos culturales creados y premios asociados a esas
      # creaciones, si los hubiere.
      ent = leerEntidad("Nombre: ")
      c.execute('SELECT * FROM entidadCreadora WHERE nombre=?', (ent,))
      print(tabulate(c.fetchall(), headers=['Nombre','Tipo']))
      c.execute(
        """SELECT rol, idProducto, nombre, tipo, fechaPublicacion 
        FROM creadoPor, productoCulturalPadre
        WHERE (idProducto=id AND nombreCreador=?)""", (ent,))
      print(tabulate(c.fetchall(), headers=['Rol','ID','Nombre', 'Tipo', 'Fecha']))

    elif ic == "Añadir-Género":
      # RF-2.4. Añadir un género
      # Esta función registra un género en el sistema a partir de un nombre,
      # un identificador, y, opcionalmente, un supergénero al que pertenece
      # como subgénero.
      gen_nombre = prompt("Nombre del género: ")
      gen_id = prompt("Identificador de género: ")
      gen_supg = prompt("Supergénero: ")

      c.execute('INSERT INTO generoSupergenero VALUES (?, ?, ?)',
                (gen_id, gen_nombre, gen_supg))

      # TODO: Restricción semántica

    elif ic == "Consultar-Género":
      # RF-2.5. Consultar un género por nombre.  Dado el nombre de un
      # género, esta función muestra su nombre, identificador,
      # supergénero, subgéneros asociados y productos culturales
      # asociados a ese género.
      gen_nombre = leerGenero("Nombre del género: ")

      # Datos
      c.execute('SELECT * FROM generoSupergenero WHERE nombreGenero = ?', (gen_nombre,))
      print('\nDatos del género')
      print(tabulate(c.fetchall(), headers=['ID', 'Nombre', 'Supergénero']))

      # Subgéneros
      c.execute(
        """SELECT genero.nombreGenero, subgenero.nombreGenero
        FROM generoSupergenero genero, generoSupergenero subgenero
        WHERE (subgenero.superGenero = ? AND genero.nombreGenero = ?)""",
        (gen_nombre, gen_nombre))
      print('\nSubgéneros')
      print(tabulate(c.fetchall(), headers=['Género','Subgénero']))

      # TODO: Productos del género

    else:
      print('El comando introducido no es válido')

  conn.close()
