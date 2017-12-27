#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
import auxiliar


n = 5
def get_valid_id():
  """Devuelve una id válida para un producto cultural"""
  global n
  m = n
  n = n + 1
  return m

# RF-1.1
def add(c):
  """Añade un producto"""
  print('Añadiendo un producto cultural.')
  ident  = get_valid_id()
  nombre = auxiliar.lee_no_vacio('Nombre: ')
  fecha  = auxiliar.lee_fecha('Fecha de creación: ')
  tipo   = auxiliar.lee_no_vacio('Tipo: ')
  padre  = auxiliar.lee_no_vacio("id del Padre: ")

  c.execute('INSERT INTO productoCulturalPadre VALUES (?, ?, ?, ?, ?)',
            (ident,nombre,fecha,tipo,padre))

  def lee_creador():
    nombre = auxiliar.leer(c, "entidadCreadora", "nombre", "Nombre: ")
    if nombre == "q":     return None
    rol    = auxiliar.lee_no_vacio("Rol: ")
    if rol == "q":      return None
    return (ident, rol, nombre)

  print("Creadores del producto (\"q\" para terminar): ")
  creadores = auxiliar.lee_list(lee_creador)
  c.executemany('INSERT INTO creadoPor VALUES (?, ?, ?)', creadores)

  print("Géneros asociados al producto (\"q\" para terminar): ")
  generos = auxiliar.lee_list(lambda: leer(c, "generoSupergenero", "nombreGenero", "Género: "))


  # TODO:
# una lista posiblemente vacía de pares compuestos por el nombre de un producto cultural ya existente y la descripción de su asociación con el producto cultural a añadir (una cadena no vacía),
# una lista no vacía de los identificadores de los géneros a las que pertenece,

def list_all(c):
  """Lista todos los productos"""
  c.execute("SELECT * FROM productoCulturalPadre")
  print(tabulate(c.fetchall(), headers=['Id','Título','Fecha','Tipo','Inspirado en']))

def view(c):
  """Muestra la información asociada a un producto"""
  pass

def modify(c):
  """Modifica un producto cultural existente"""
  pass

comandos = {
  'Listar-Productos': list_all,
  'Ver-Producto': view,
  'Modifica-Producto': modify,
  'Añadir-Productos': add
}
