#!/usr/bin/python3
from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI


def leerEntidad(c):
  """Auxiliar: lee entidad con autocompletado"""
  c.execute("SELECT nombre FROM entidadCreadora")
  return prompt("Nombre: ", completer=WordCompleter([t[0] for t in c.fetchall()], ignore_case = True))


def add_entidad(c):
  """Añade entidad creadora"""
  # RF-2.1. Añadir entidad creadora.  Esta función registra una
  # entidad creadora dentro del sistema a partir de su nombre y
  # tipo.
  print('Añadiendo una entidad creadora.')
  ent_nombre = prompt("Nombre: ")
  ent_tipo = prompt("Tipo: ")
  c.execute('INSERT INTO entidadCreadora VALUES (?, ?)',
            (ent_nombre,ent_tipo))


def add_premio(c):
  """Añade premio"""
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


def view_entidad(c):
  """Consulta datos de entidad creadora"""
  # RF-2.3. Consultar una entidad creadora.  Dado el nombre de una
  # entidad creadora, esta función muestra el nombre, tipo,
  # productos culturales creados y premios asociados a esas
  # creaciones, si los hubiere.
  ent = leerEntidad(c)
  c.execute('SELECT * FROM entidadCreadora WHERE nombre=?', (ent,))
  print(tabulate(c.fetchall(), headers=['Nombre','Tipo']))
  c.execute(
    """SELECT rol, idProducto, nombre, tipo, fechaPublicacion
    FROM creadoPor, productoCulturalPadre
    WHERE (idProducto=id AND nombreCreador=?)""", (ent,))
  print(tabulate(c.fetchall(), headers=['Rol','ID','Nombre', 'Tipo', 'Fecha']))


def list_all_entidad(c):
  """Lista entidades"""
  c.execute("SELECT * FROM entidadCreadora")
  print(tabulate(c.fetchall(), headers=['Nombre','Tipo']))


comandos = {
  'Ver-Creadores': list_all_entidad,
  'Añadir-Premios': add_premio,
  'Consultar-Creadores': view_entidad
}
