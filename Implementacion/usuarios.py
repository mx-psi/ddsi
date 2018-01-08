#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from auxiliar import lee_no_vacio


#####################################
# RF-3.1.                           #
# Alta de usuario                   #
#####################################

def add_usuario(c):
  """Añade un usuario"""
  print('Añadiendo un usuario.')
  nombreusuario = lee_no_vacio('Nombre de usuario: ')
  nombrereal = lee_no_vacio('Nombre real: ')
  localidadorigen  = lee_no_vacio('Localidad de origen: ')
  correo   = lee_no_vacio('Correo: ')
  descripcion  = lee_no_vacio('Descripción del usuario: ')
  password = lee_no_vacio('Contraseña: ')

  c.executemany('INSERT INTO usuario VALUES (?,?,?,?,?,?)',
[(nombreusuario,nombrereal,localidadorigen,correo,descripcion,password)])

def lista_usuarios(c):
  """Lista todos los usuarios"""
  c.execute("SELECT * FROM usuario")
  print(tabulate(c.fetchall(), headers=['Nombre de usuario','Nombre real','Localidad de origen','Correo','Descripción del usuario','Contraseña'], tablefmt="plain"))

comandos = {
  'Añadir-Usuario':  add_usuario,
  'Listar-Usuarios': lista_usuarios 
}
