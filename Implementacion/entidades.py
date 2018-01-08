#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI
from auxiliar import *



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
  prm_entidad = leer2(c, "entidadCreadora", "nombre", "Entidad que recibe el premio: ")
  prm_producto = leer2(c, "productoCulturalPadre", "id", "ID del producto por el que recibe el premio: ")
  prm_nombre = prompt("Nombre del premio: ")

  c.execute('INSERT INTO premiadaPor VALUES (?, ?, ?)',
            (prm_entidad, prm_producto, prm_nombre))


def view_entidad(c):
  """Consulta datos de entidad creadora"""
  # RF-2.3. Consultar una entidad creadora.  Dado el nombre de una
  # entidad creadora, esta función muestra el nombre, tipo,
  # productos culturales creados y premios asociados a esas
  # creaciones, si los hubiere.
  ent = leer2(c, "entidadCreadora", "nombre", "Nombre: ")

  # Datos de la entidad creadora
  c.execute('SELECT * FROM entidadCreadora WHERE nombre=?', (ent,))
  print('\n' + tabulate(c.fetchall(), headers=['Nombre','Tipo']))

  # Creaciones culturales
  c.execute(
    """SELECT rol, idProducto, nombre, tipo, fechaPublicacion
    FROM creadoPor, productoCulturalPadre
    WHERE (idProducto=id AND nombreCreador=?)""", (ent,))
  print('\nProductos culturales creados\n'
        + tabulate(c.fetchall(), headers=['Rol','ID','Nombre', 'Tipo', 'Fecha']))

  # Premios
  c.execute(
    """SELECT prem.nombrepremio, prod.nombre
    FROM premiadaPor prem, productoCulturalPadre prod
    WHERE (prem.nombre = ? AND prod.id = prem.id)
    """, (ent,))
  print('\n' + tabulate(c.fetchall(), headers=['Premio','Por']))
  

def list_all_entidad(c):
  """Lista entidades"""
  c.execute("SELECT * FROM entidadCreadora")
  print(tabulate(c.fetchall(), headers=['Nombre','Tipo']))


def add_genero(c):
  """Añade un género"""
  # RF-2.4. Añadir un género
  # Esta función registra un género en el sistema a partir de un nombre,
  # un identificador, y, opcionalmente, un supergénero al que pertenece
  # como subgénero.
  gen_nombre = prompt("Nombre del género: ")
  gen_id = prompt("Identificador de género: ")
  gen_supg = leer2(c, "generoSupergenero", "identificador", "Supergénero: ")

  c.execute('INSERT INTO generoSupergenero VALUES (?, ?, ?)',
            (gen_id, gen_nombre, gen_supg))
  

def view_genero(c):
  """Consulta datos y productos de un género"""
  # RF-2.5. Consultar un género por nombre.  Dado el nombre de un
  # género, esta función muestra todos los géneros con ese nombre,
  # dando identificador, supergénero, subgéneros asociados y productos
  # culturales asociados a ellos.
  gen_nombre = leer2(c, "generoSupergenero", "nombreGenero", "Nombre del género: ")

  # Datos
  c.execute("""
    SELECT genero.identificador, genero.nombreGenero, genero.superGenero
    FROM generoSupergenero genero
    WHERE (genero.nombreGenero = ?)
  """, (gen_nombre,))
  print('\nDatos del género')
  print(tabulate(c.fetchall(), headers=['ID', 'Nombre', 'ID-Sup']))

  # Subgéneros
  c.execute(
    """SELECT subgenero.nombreGenero, subgenero.identificador, genero.identificador
    FROM generoSupergenero genero, generoSupergenero subgenero
    WHERE (subgenero.superGenero = genero.Identificador AND genero.nombreGenero = ?)""",
    (gen_nombre,))
  print('\nSubgéneros')
  print(tabulate(c.fetchall(), headers=['Subgénero','ID-Sub','ID']))

  # Productos del género
  c.execute(
    """SELECT id, nombre, fechaPublicacion, tipo, idPadre
    FROM productoCulturalPadre productos, perteneceA pertenece, generoSupergenero generos
    WHERE (
      generos.nombreGenero = ? AND
      pertenece.Identificador = generos.identificador AND
      pertenece.idProducto = productos.id
    )""", (gen_nombre,))
  print('\nProductos del género')
  print(tabulate(c.fetchall(), headers=['Id','Nombre','Fecha','Tipo','IdPadre']))


def view_genero_id(c):
  """Consulta datos de un ID de género específico"""
  # RF-2.6. Consultar un género por ID. Dado el identificador de un
  # género, esta función muestra su nombre, identificador,
  # supergénero, subgéneros asociados y productos culturales asociados
  # a ese género.
  gen_id = leer2(c, "generoSupergenero", "identificador", "ID del género: ")

  # Datos
  c.execute('SELECT * FROM generoSupergenero WHERE identificador = ?', (str(gen_id),))
  print('\nDatos del género')
  print(tabulate(c.fetchall(), headers=['ID', 'Nombre', 'Supergénero']))

  # Subgéneros
  c.execute(
    """SELECT subgenero.nombreGenero, subgenero.identificador
    FROM generoSupergenero genero, generoSupergenero subgenero
    WHERE (subgenero.superGenero = genero.identificador AND genero.identificador = ?)""",
    (str(gen_id),))
  print('\nSubgéneros')
  print(tabulate(c.fetchall(), headers=['Subgénero', 'ID-Sub']))

  # Productos del género
  c.execute(
    """SELECT id, nombre, fechaPublicacion, tipo, idPadre
    FROM productoCulturalPadre productos, perteneceA pertenece
    WHERE (
      pertenece.Identificador = ? AND
      pertenece.idProducto = productos.id
    )""", (str(gen_id),))
  print('\nProductos del género')
  print(tabulate(c.fetchall(), headers=['Id','Nombre','Fecha','Tipo','IdPadre']))

  # TODO: Restricciones semánticas


comandos = {
  'Añadir-Creadores': add_entidad,
  'Añadir-Premios': add_premio,
  'Consultar-Creadores': view_entidad,
  'Ver-Creadores': list_all_entidad,
  'Añadir-Género': add_genero,
  'Consultar-Género': view_genero,
  'Consultar-Id-Género': view_genero_id,
}
