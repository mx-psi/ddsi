#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from prompt_toolkit.contrib.completers import WordCompleter #CLI

def leer(c, tabla, campo, texto):
    """Función auxiliar: lee de la entrada un elemento de la base de datos."""
    c.execute("SELECT ? FROM ?", (campo, tabla))
    return prompt(texto, completer=WordCompleter([t[0] for t in c.fetchall()], ignore_case = True))
