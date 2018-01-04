#!/usr/bin/python3

import sqlite3 # Interacción base de datos
from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI
from prompt_toolkit.validation import Validator, ValidationError
from datetime import datetime

def get_pk(c, tabla):
  """Obtiene lista de atributos que forman parte de la clave primaria."""

  c.execute("PRAGMA table_info([{tab}]);".format(tab = tabla))
  rows = c.fetchall()
  pks = []
  for r in rows:
    if r[5] == 1:
      pks.append(r[0])
  return pks


class FieldValidator(Validator):
  """Validación de campos"""

  def __init__(self, c, tabla, campo, vacio):
    super().__init__()
    self.c = c
    self.tabla = tabla
    self.campo = campo
    self.vacio = vacio

  def validate(self, document):
    self.c.execute("SELECT {campo} FROM {tabla} WHERE {campo} = \'{text}\'"
                   .format(campo = self.campo, tabla = self.tabla, text =  document.text))

    if len(self.c.fetchall()) == 0 and not (self.vacio and document.text == ""):
      raise ValidationError(message="No existe en la base de datos: \"{}\"".format(document.text))


class IterValidator(Validator):
  """Validación de iterable"""

  def __init__(self, iterable, mensaje="No es valido"):
    super().__init__()
    self.iterable = iterable
    self.mensaje  = mensaje

  def validate(self, document):
    for x in self.iterable:
      if str(x) == document.text: return None
    raise ValidationError(message=self.mensaje)

def leer(c, tabla, campo, texto, vacio = True):
    """Función auxiliar: lee de la entrada un elemento de la base de datos.

       c → Cursor a la base de datos
       tabla → Nombre de la tabla a consultar
       campo → Campo a autocompletar
       texto → Texto del prompt
       vacio → Si el campo puede estar vacío

       La función pregunta al usuario por un elemento válido de campo en tabla o un valor vacío
       en caso de que pueda estarlo. Resuelve ambigüedades en campos que no son clave primaria con una lista
    """

    c.execute("SELECT {campo} FROM {tabla}".format(campo = campo, tabla = tabla))

    val_campo =  prompt(texto,
                  completer=WordCompleter(set(str(t[0]) for t in c.fetchall()), ignore_case = True),
                  validator=FieldValidator(c, tabla, campo, vacio))
    pks = get_pk(c,tabla)
    if val_campo == "":
      return tuple(None for k in pks)

    c.execute("SELECT * FROM {tabla} WHERE {campo}=\'{val_campo}\'"
              .format(campo = campo, tabla = tabla, val_campo = val_campo))
    opciones = c.fetchall()
    elegido = None

    if len(opciones) == 1:
      elegido = opciones[0]
    else:
      print("Múltiples coincidencias: ")
      headers = ["Nº"] + [d[0] for d in c.description]
      print(tabulate([list((i,) + op) for i,op in enumerate(opciones)],
                     headers = headers))
      n = int(prompt("Indica el número: ",
                     validator = IterValidator(range(len(opciones)))))
      elegido = opciones[n]

    return tuple(elegido[k] for k in pks)



class NonEmptyValidator(Validator):
  """Validación de campos no vacíos"""
  def validate(self, document):
    if len(document.text) == 0:
      raise ValidationError(message="No puede estar vacío")

def lee_no_vacio(texto):
  return prompt(texto, validator=NonEmptyValidator())



FORMATO_FECHA = "%Y/%m/%d"

class DateValidator(Validator):
  """Validación de fechas"""
  def validate(self, document):
    message = "Formato incorrecto (YYYY/MM/DD)"
    text = document.text
    try: datetime.strptime(text, FORMATO_FECHA)
    except ValueError:
      raise ValidationError(message=message)

def lee_fecha(texto='Fecha: '):
  """Lee fecha"""
  return datetime.strptime(prompt(texto, validator=DateValidator()), FORMATO_FECHA).date()



def lee_lista(mensaje, lector):
  """Lee lista con lector"""
  print(mensaje + " (Ctrl+D para terminar): ")
  l = []
  try:
    while True:
      l.append(lector())
  except EOFError:
    return l


def lee_texto(mensaje):
  """Lee texto con posibles saltos de línea"""
  print(mensaje + " (Escape seguido de Intro para terminar):")
  return prompt('> ', multiline=True)


def lee_entero(mensaje):
  """Lee un número entero"""
  return int(input(mensaje))


def leer2(c, tabla, campo, texto):
    """Función auxiliar: lee de la entrada un elemento de la base de datos."""
    c.execute("SELECT " + campo + " FROM " + tabla)
    return prompt(texto, completer=WordCompleter([str(t[0]) for t in c.fetchall()], ignore_case = True))
