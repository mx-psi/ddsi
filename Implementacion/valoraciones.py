#!/usr/bin/python3

from prompt_toolkit.shortcuts import prompt
from tabulate import tabulate
from auxiliar import lee_texto, lee_entero, lee_usuario, leer

###################################################
# RF-4.1.                                         #
# Escribir una valoración de un producto cultural #
###################################################

def add_valoracion(c):
  """Añade una valoración de un producto cultural"""
  print('Añadiendo una valoración de un producto cultural.')
  idProd = leer(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")[0]
  user   = lee_usuario(c, "Nombre del usuario valorador: ")
  texto  = lee_texto("Reseña")
  puntos = lee_entero("Puntuación: ")

  c.execute('INSERT INTO valoracionValora VALUES (?, ?, ?, ?)',
            (idProd, user, texto, puntos))


#####################################
# RF-4.2                            #
# Consultar resumen de valoraciones #
#####################################

def view_resumen_valoraciones(c):
  """Obtiene un resumen de las valoraciones de un producto cultural"""
  idProd = leer(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")[0]
  c.execute("SELECT puntuacion, COUNT(*) FROM valoracionValora WHERE idProducto = ? GROUP BY puntuacion ORDER BY puntuacion", (idProd, ))
  histograma = c.fetchall()
  if len(histograma) == 0:
    print("\nTodavía no hay valoraciones del producto " + idProd)
    return
  print_histograma(histograma)
  
  c.execute("SELECT ROUND(AVG(puntuacion)*10)/10 FROM valoracionValora WHERE idProducto = ?", (idProd,))
  print("Puntuación media: " + str(c.fetchall()[0][0]).replace(".", ","))

  print("\nAlgunas valoraciones:\n")
  c.execute("SELECT nombreUsuario, v.puntuacion, CASE WHEN LENGTH(resena) > 40 THEN substr(resena, 0, 40) || '...' ELSE resena END,COALESCE(sum(p.puntuacion), 0), -COALESCE(sum(1 - p.puntuacion), 0) FROM valoracionValora v LEFT JOIN puntua p on (p.nombreUsuarioValorador = v.nombreUsuario AND p.idProducto = v.idProducto) WHERE v.idProducto = ? GROUP BY nombreUsuario,v.idProducto ORDER BY COALESCE(sum(2*p.puntuacion-1), 0) DESC LIMIT 3;", (idProd,))
  print(tabulate(c.fetchall(), headers=['Valorador', 'Puntos', 'Reseña', '+', '-']))

def print_histograma(h):
  l = [0]*5
  m = 0
  for t in h:
    l[t[0]-1] = t[1]
    m = max(m, t[1])

  lim = min(40, m)
  print("\n")
  for p in range(1, 6):
    print(str(p) + " | " + "▓"*round(l[p-1]*lim/m))

########################
# RF-4.3               #
# Consultar valoración #
########################

def view_valoracion(c):
  """Visualiza una valoración"""
  idProd = leer(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")[0]
  user   = leer(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ")[0]
  c.execute("SELECT nombre, nombreUsuario, puntuacion, resena FROM valoracionValora JOIN productoCulturalPadre ON (id=? AND idProducto=id AND nombreUsuario=?)", (idProd, user))
  res = c.fetchall()
  if len(res) == 0:
    print("\n" + user + " no ha valorado el producto " + idProd)
    return

  print("\nValoración de {producto} por {usuario}: {pts} puntos\nReseña:\n".format(producto = res[0][0], usuario = res[0][1], pts = res[0][2]))
  print(res[0][3])

  c.execute("SELECT COALESCE(SUM(puntuacion), 0), COALESCE(SUM(1 - puntuacion), 0) FROM puntua WHERE idProducto=? AND nombreUsuarioValorador=?", (idProd, user))
  print("\nPuntuación de esta valoración:\n")
  print(tabulate(c.fetchall(), headers=['A favor', 'En contra']))

##########################
# RF-4.4.                #
# Puntuar una valoración #
##########################

def add_puntuacion(c):
  """Añade una puntuación a una valoración"""
  print('Puntuando una valoración.')
  userP  = lee_usuario(c, "Nombre del usuario puntuador: ")
  userV  = leer(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ")[0]
  idProd = leer(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")[0]
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
  userR  = lee_usuario(c, "Nombre del usuario reportador: ")
  userV  = leer(c, "usuario", "nombreusuario", "Nombre del usuario valorador: ")[0]
  idProd = leer(c, "productoCulturalPadre", "id", "ID del producto cultural valorado: ")[0]

  c.execute('INSERT INTO reporta VALUES (?, ?, ?)',
            (userR, userV, idProd))


comandos = {
  'Añadir-Valoración':  add_valoracion,
  'Ver-Resumen-Valoraciones': view_resumen_valoraciones,
  'Ver-Valoración': view_valoracion,
  'Puntuar-Valoración':  add_puntuacion,
  'Reportar-Valoración':  add_reporte
}
