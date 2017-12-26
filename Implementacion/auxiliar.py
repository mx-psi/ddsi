#!/usr/bin/python3

import sqlite3 # Interacción base de datos
from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI
from prompt_toolkit.validation import Validator, ValidationError
from datetime import datetime

def leer(c, tabla, campo, texto):
    """Función auxiliar: lee de la entrada un elemento de la base de datos."""
    c.execute("SELECT " + campo + " FROM " + tabla)
    return prompt(texto, completer=WordCompleter([str(t[0]) for t in c.fetchall()], ignore_case = True))


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
