#!/usr/bin/python3

import sqlite3 # Interacción base de datos
from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI
from prompt_toolkit.validation import Validator, ValidationError
from datetime import datetime

class EndInputError(Exception):
  """Error que indica el fin de la entrada."""
  def __init__(self,message):
    self.message = message
  def __str__(self):
    return self.message

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

  def __init__(self, c, tabla, campo):
    super().__init__()
    self.c = c
    self.tabla = tabla
    self.campo = campo

  def validate(self, document):
    self.c.execute("SELECT {campo} FROM {tabla} WHERE {campo} = \'{text}\'"
                   .format(campo = self.campo, tabla = self.tabla, text =  document.text))

    if len(self.c.fetchall()) == 0 and document.text != "q":
      raise ValidationError(message="El valor no existe en la base de datos")


class IterValidator(Validator):
  """Validación de iterable"""

  def __init__(self, iterable):
    super().__init__()
    self.iterable = iterable

  def validate(self, document):
    for x in self.iterable:
      if str(x) == document.text:
        return None
    raise ValidationError(message="El valor no es válido")


def leer(c, tabla, campo, texto):
    """Función auxiliar: lee de la entrada un elemento de la base de datos."""

    c.execute("SELECT {campo} FROM {tabla}".format(campo = campo, tabla = tabla))

    val_campo =  prompt(texto,
                  completer=WordCompleter([str(t[0]) for t in c.fetchall()], ignore_case = True),
                  validator=FieldValidator(c, tabla, campo))

    if val_campo == "q":
      raise EndInputError("Fin de entrada: Leer")

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

    pks = get_pk(c,tabla)
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



def lee_lista(lector):
  """Lee lista con lector"""
  l = []
  try:
    while True:
      l.append(lector())
  except EndInputError:
    return l
