#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate

def add(c):
  print('Añadiendo un producto cultural.')
  prod_nombre = prompt('Nombre del producto: ')
  prod_fecha = prompt('Fecha de creación: ')
  prod_tipo = prompt('Tipo del producto: ')
  prod_inspirado = prompt('Inspirado en: ')
  c.execute('INSERT INTO productoCulturalPadre VALUES (?, ?, ?, ?, ?)',
            (12,prod_nombre,prod_fecha,prod_tipo,prod_inspirado))

  def list_all(c):
    c.execute("SELECT * FROM productoCulturalPadre")
      print(tabulate(c.fetchall(), headers=['Id','Título','Fecha','Tipo','Inspirado en']))
