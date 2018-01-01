#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from auxiliar import lee_texto, lee_entero, leer2

###################################################
# RF-4.1.                                         #
# Escribir una valoración de un producto cultural #
###################################################

def add_valoracion(c):
  """Añade una valoración de un producto cultural"""
  print('Añadiendo una valoración de un producto cultural.')
  idProd = leer2(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")
  user   = leer2(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ")
  texto  = lee_texto("Valoración")
  puntos = lee_entero("Puntuación: ")

  c.execute('INSERT INTO valoracionValora VALUES (?, ?, ?, ?)',
            (idProd, user, texto, puntos))


##########################
# RF-4.4.                #
# Puntuar una valoración #
##########################

def add_puntuacion(c):
  """Añade una puntuación a una valoración"""
  print('Puntuando una valoración.')
  userP  = leer2(c, "usuario", "nombreusuario", "Nombre del usuario puntuador: ")
  userV  = leer2(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ")
  idProd = leer2(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")
  puntos = lee_entero("Puntuación: ")

  c.execute('INSERT INTO puntua VALUES (?, ?, ?, ?)',
            (userP, userV, idProd, puntos))


###########################
# RF-4.5.                 #
# Reportar una valoración #
###########################

def add_reporte(c):
  """Reporta una valoración"""
  print('Reportando una valoración.')
  userR  = leer2(c, "usuario", "nombreusuario", "Nombre del usuario reportador: ")
  userV  = leer2(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ")
  idProd = leer2(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")

  c.execute('INSERT INTO reporta VALUES (?, ?, ?)',
            (userR, userV, idProd))


comandos = {
  'Añadir-Valoración':  add_valoracion,
  'Puntuar-Valoración':  add_puntuacion,
  'Reportar-Valoración':  add_reporte
}
