#!/usr/bin/python3

import sqlite3 # Interacción base de datos
from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI
from prompt_toolkit.validation import Validator, ValidationError
from datetime import datetime


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
      raise ValidationError(message="Ese valor no existe en la base de datos")


def leer(c, tabla, campo, texto):
    """Función auxiliar: lee de la entrada un elemento de la base de datos."""

    c.execute("SELECT {campo} FROM {tabla}".format(campo = campo, tabla = tabla))
    return prompt(texto,
                  completer=WordCompleter([str(t[0]) for t in c.fetchall()], ignore_case = True),
                  validator=FieldValidator(c, tabla, campo))


class NonEmptyValidator(Validator):
  """Validación de campos no vacíos"""
  def validate(self, document):
    if len(document.text) == 0:
      raise ValidationError(message="No puede estar vacío")

def lee_no_vacio(texto):
  return prompt(texto, validator=NonEmptyValidator())


class DateValidator(Validator):
  """Validación de fechas"""
  def validate(self, document):
    message = "Formato incorrecto (YYYY/MM/DD)"
    text = document.text
    try: datetime.strptime(text, "%Y/%m/%d")
    except ValueError:
      raise ValidationError(message=message)

def lee_fecha(texto='Fecha: '):
  """Lee fecha"""
  return datetime.strptime(prompt(texto, validator=DateValidator()), "%Y/%m/%d").date()

def lee_list(lector):
  """Lee lista con lector"""
  l = []
  while True:
    act = lector()
    if act != None:
      l.append(act)
    else:
      return l
