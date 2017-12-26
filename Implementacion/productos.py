#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
import auxiliar


# RF-1.1
def add(c):
  """Añade un producto"""
  print('Añadiendo un producto cultural.')
  prod_nombre = auxiliar.lee_no_vacio('Nombre: ')
  prod_fecha  = auxiliar.lee_fecha('Fecha de creación: ')
  prod_tipo   = auxiliar.lee_no_vacio('Tipo: ')

  prod_inspirado = prompt('Inspirado en: ')
  c.execute('INSERT INTO productoCulturalPadre VALUES (?, ?, ?, ?, ?)',
            (12,prod_nombre,prod_fecha,prod_tipo,prod_inspirado))
  # TODO:
# una lista posiblemente vacía de pares compuestos por el nombre de un producto cultural ya existente y la descripción de su asociación con el producto cultural a añadir (una cadena no vacía),
# una lista no vacía de los identificadores de los géneros a las que pertenece,
# una lista no vacía de los nombres de los productos culturales padre y
# una lista no vacía de pares compuestos por el nombre de cada entidad creadora asociada y rol de esa asociación (una cadena no vacía).

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
