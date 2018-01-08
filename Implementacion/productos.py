#!/usr/bin/python3
# Autor: Pablo Baeyens

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
import sqlite3
from auxiliar import lee_fecha, lee_lista, lee_no_vacio, leer

def get_valid_id(c):
  """Devuelve una id válida para un producto cultural"""
  c.execute("SELECT max(id) from productoCulturalPadre")
  return c.fetchall()[0][0] + 1


#####################################
# RF-1.1.                           #
# Añadir un producto cultural nuevo #
#####################################

def add(c):
  """Añade un producto"""
  print('Añadiendo un producto cultural.')
  idProd = get_valid_id(c)
  nombre = lee_no_vacio('Nombre: ')
  fecha  = lee_fecha('Fecha de creación: ')
  tipo   = lee_no_vacio('Tipo: ')
  padre  = leer(c, "productoCulturalPadre", "nombre", "Padre: ")

  c.execute('INSERT INTO productoCulturalPadre VALUES (?, ?, ?, ?, ?)',
            (idProd,nombre,fecha,tipo) + padre)

  def lee_creador():
    nombre = leer(c, "entidadCreadora", "nombre", "Nombre: ")
    rol    = lee_no_vacio("Rol: ")
    return (idProd, rol) + nombre
  creadores = lee_lista("Creadores del producto", lee_creador)
  c.executemany('INSERT INTO creadoPor VALUES (?, ?, ?)', creadores)


  generos = lee_lista("Géneros asociados",
                      lambda: (idProd,) + leer(c, "generoSupergenero", "nombreGenero", "Género: "))
  c.executemany('INSERT INTO perteneceA VALUES (?,?)', generos)

  def lee_asociado():
    asociado    = leer(c, "productoCulturalPadre", "nombre", "Producto asociado: ")
    descripcion = lee_no_vacio("Descripción de la asociación: ")
    return (idProd,) + asociado + (descripcion,)
  asociados = lee_lista("Productos asociados", lee_asociado)
  c.executemany('INSERT INTO asociadoA VALUES (?, ?, ?)', asociados)

  print("Datos introducidos correctamente. La id de su producto es {idProd}".format(idProd = idProd))


def list_all(c):
  """Lista todos los productos"""
  c.execute("SELECT * FROM productoCulturalPadre")
  print(tabulate(c.fetchall(), headers=['Id','Título','Fecha','Tipo','Padre'], tablefmt="plain"))


############################################
# RF-1.2                                   #
# Modificar un producto cultural existente #
############################################

def modify(c):
  """Modifica un producto cultural existente"""
  idProd  = leer(c, "productoCulturalPadre", "id", "Id del producto: ")

  def lee_asociado():
    asociado    = leer(c, "productoCulturalPadre", "nombre", "Producto asociado: ")
    descripcion = lee_no_vacio("Descripción de la asociación: ")
    return idProd + asociado + (descripcion,)
  asociados = lee_lista("Nuevos productos asociados", lee_asociado)
  c.executemany('INSERT INTO asociadoA VALUES (?, ?, ?)', asociados)

  generos = lee_lista("Nuevos géneros",
                      lambda: idProd + leer(c, "generoSupergenero", "nombreGenero", "Género: "))
  c.execute('DELETE  FROM perteneceA WHERE idProducto = ?', idProd)
  c.executemany('INSERT INTO perteneceA VALUES (?,?)', generos)
  print("Datos modificados correctamente")


#################################################
# RF-1.3                                        #
# Consultar información de un producto cultural #
#################################################

def view(c):
  """Muestra la información asociada a un producto"""
  idProd  = leer(c, "productoCulturalPadre", "id", "Id del producto: ")
  c.execute("SELECT * FROM productoCulturalPadre WHERE id={idProd}".format(idProd = idProd[0]))

  print("\nDatos básicos:\n")
  print(tabulate(c.fetchall(), headers=['Id','Título','Fecha','Tipo','Padre']))

  c.execute("SELECT id, nombre, tipo, descripcion FROM asociadoA, productoCulturalPadre WHERE (id2={idProd} AND id1=id) OR (id1={idProd} AND id2=id)".format(idProd = idProd[0]))
  asociados = c.fetchall()
  if len(asociados) > 0:
    print("\nProductos asociados: \n")
    print(tabulate(asociados, headers=['Id','Nombre','Tipo', 'Asociación']))

  c.execute("SELECT nombreGenero FROM perteneceA, generoSupergenero WHERE idProducto={idProd} AND perteneceA.identificador=generoSupergenero.identificador".format(idProd = idProd[0]))
  generos = c.fetchall()
  if len(generos) > 0:
    print("\nGéneros: {generos}".format(generos = ", ".join(x[0] for x in generos)))

  c.execute("SELECT nombreCreador, rol FROM creadoPor WHERE idProducto={idProd}".format(idProd = idProd[0]))
  creadores = c.fetchall()
  if len(creadores) > 0:
    print("\nCreadores:\n")
    print(tabulate(creadores, headers=['Nombre','Rol']))


comandos = {
  'Listar-Productos':  list_all,
  'Ver-Producto':      view,
  'Modificar-Producto': modify,
  'Añadir-Productos':  add
}
