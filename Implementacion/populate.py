#!/usr/bin/python3
# c.executemany('INSERT INTO productoCulturalPadre VALUES (?,?,?,?)', productos)
from datetime import date

# Productos culturales
#  productoCulturalPadre(_id_, nombre, fechaPublicacion, tipo, idPadre)
productosCulturalPadre = [
  ("Harry Potter y la Piedra Filosofal", date(1997,6,30), "Libro", None),                # 1
  ("Harry Potter y la Piedra Filosofal", date(2001,11,4), "Película", 1),                # 2
  ("El Señor de los Anillos", date(1954,7,24), "Libro", None),                           # 3
  ("El Señor de los Anillos: la Comunidad del Anillo", date(2001,12,19), "Película", 3)  # 4
]

# Entidades creadoras
#  entidadCreadora(_nombre_, tipo)
entidadCreadora = [
  ("J.K. Rowling", "Persona"),
  ("Mary GrandPré", "Persona"),
  ("Chris Columbus", "Persona"),
  ("J.R.R. Tolkien", "Persona"),
  ("Peter Jackson", "Persona"),
  ("Warner Bros. Pictures", "Compañía")
]

# Creado por
#  creadoPor(_idProducto_, _rol_, _nombreCreador_)
creadoPor = [
  (1, "Autor", "J.K. Rowling"),
  (1, "Ilustrador", "Mary GrandPré"),
  (2, "Director", "Chris Columbus"),
  (2, "Distribuidora", "Warner Bros. Pictures"),
  (3, "Autor", "J.R.R. Tolkien"),
  (4, "Director", "Peter Jackson")
]


# Asociado a
#  asociadoA(_id1_, _id2_, descripcion)
asociadoA = []


# Géneros
# géneroSupergénero(_identificador_, nombreGénero, supergénero)
generoSupergenero = [
  ("Ficción", None),
  ("Fantasía", "Ficción"),
  ("Magia", "Fantasía"),
  ("Juvenil", None)
]

# Pertenece a género
#  pertenece_a(_idProducto_,_Identificador_)
perteneceA = [
  (1, 3), # Harry Potter - Magia
  (1, 4), # Harry Potter - Juvenil
  (2, 3), # Harry Potter (película) - Magia
  (2, 4), # Harry Potter (película) - Juvenil
  (3, 2), # Señor de los Anillos - Fantasía
  (4, 2)  # Señor de los Anillos (película) - Fantasía
]

# Premios
#  premiadaPor(_nombre_, _id_, _nombrepremio_)
premiadaPor = [
  ("J.R.R. Tolkien", 3, "International Fantasy Award (1957)"),
  ("J.K. Rowling", 1, "National Book Award")
] 
