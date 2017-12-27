#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from auxiliar import lee_fecha, lee_lista, lee_no_vacio, leer

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
  nombre = lee_no_vacio('Nombre: ')
  fecha  = lee_fecha('Fecha de creación: ')
  tipo   = lee_no_vacio('Tipo: ')
  padre  = leer(c, "productoCulturalPadre", "nombre", "Padre: ")

  c.execute('INSERT INTO productoCulturalPadre VALUES (?, ?, ?, ?, ?)',
            (ident,nombre,fecha,tipo) + padre)

  print("Creadores del producto (\"q\" para terminar): ")

  def lee_creador():
    nombre = leer(c, "entidadCreadora", "nombre", "Nombre: ")
    rol    = lee_no_vacio("Rol: ")
    return (ident, rol) + nombre
  creadores = lee_lista(lee_creador)
  c.executemany('INSERT INTO creadoPor VALUES (?, ?, ?)', creadores)

  print("Géneros asociados al producto (\"q\" para terminar): ")
  generos = lee_lista(lambda: (ident,) + leer(c, "generoSupergenero", "nombreGenero", "Género: "))
  c.executemany('INSERT INTO perteneceA VALUES (?,?)', generos)

  print("Productos asociados (\"q\" para terminar): ")
  def lee_asociado():
    asociado    = leer(c, "productoCulturalPadre", "nombre", "Producto asociado: ")
    descripcion = lee_no_vacio("Descripción de la asociación: ")
    return (ident,) + asociado + (descripcion,)
  asociados = lee_lista(lee_asociado)
  c.executemany('INSERT INTO asociadoA VALUES (?, ?, ?)', asociados)



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
