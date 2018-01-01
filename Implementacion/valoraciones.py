#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
#from prompt_toolkit.contrib.completers import WordCompleter #CLI # TODO: ver si hace falta
from auxiliar import lee_texto, lee_entero, leer2

###################################################
# RF-4.1.                                         #
# Escribir una valoración de un producto cultural #
###################################################

def add_valoracion(c):
  """Añade una valoración de un producto cultural"""
  print('Añadiendo una valoración de un producto cultural.')
  idProd = leer2(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ") # TODO: leer identificador de producto cultural
  user   = leer2(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ") # TODO: leer usuario de los disponibles en la DB
  texto  = lee_texto("Valoración") # TODO: leer texto. Debe permitir saltos de línea
  puntos = lee_entero("Puntuación: ") # TODO: leer puntuación

  c.execute('INSERT INTO valoracionValora VALUES (?, ?, ?, ?)',
            (idProd, user, texto, puntos))


comandos = {
  'Añadir-Valoración':  add_valoracion
}
