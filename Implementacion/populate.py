#!/usr/bin/python3
# c.executemany('INSERT INTO productoCulturalPadre VALUES (?,?,?,?)', productos)
from datetime import date

# Productos culturales
#  productoCulturalPadre(_id_, nombre, fechaPublicacion, tipo, idPadre)
productoCulturalPadre = [
  (1, "Harry Potter y la Piedra Filosofal", date(1997,6,30), "Libro", None),               
  (2, "Harry Potter y la Piedra Filosofal", date(2001,11,4), "Película", 1),               
  (3, "El Señor de los Anillos", date(1954,7,24), "Libro", None),                          
  (4, "El Señor de los Anillos: la Comunidad del Anillo", date(2001,12,19), "Película", 3)  
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
  (1, "Ficción", None),
  (2, "Fantasía", "Ficción"),
  (3, "Magia", "Fantasía"),
  (4, "Juvenil", None)
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

# Usuarios
# usuario(nombreusuario,nombrereal,localidadorigen,correoelectrónico,descripciónusuario,password)
usuario = [ 
  ("alba23","Alba Muñoz","Andalucia","alba@correo.es","Amante de la literatura","a_123456"),
  ("cristi23","Cristina Fernandez","Andalucia","cristina@correo.es","Amante del cine","c_123456"),
  ("alicia22","Alicia Quero","Andalucia","alicia@correo.es","Amante del cine y literatura","ali_123456"),
  ("alberto23","Alberto Castro","Andalucia","alberto@correo.es","Amante de la musica","alb_123456"),
  ("nacho23","Ignacio Sanchez","Andalucia","nacho@correo.es","Amante de la musica y el cine","n_123456"),
  ("fede33","Federico Cerrato","Andalucia","fede@correo.es","Amante de la literatura y la musica","f_123456"),
  ("msaracchi","Mauricio Saracchi","Rosario","msaracchi@correo.com.ar","Visionario y exigente, le cae mal a toda la gente","messipechofriomaradonaeselmejor")
]

# leGusta
# leGusta(nombreusuario,identificador)
leGusta = [
  ("alba23","Ficción"),
  ("cristi23","Fantasía"),
  ("alicia22","Magia"),
  ("alberto23","Juvenil"),
  ("nacho23","Magia"),
  ("fede33","Ficción"),
  ("fede33","Fantasía"),
  ("msaracchi","Ficción")
]

# Valoraciones
#  valoracion-valora(_idProducto_, _nombreUsuario_, resena, puntuacion)
valoracion-valora = [
  (1, "alicia22", """[reseña con gran entusiasmo; tal vez demasiado]""", 5),
  (3, "alba23", """[reseña bastante bien hecha]""", 3),
  (3, "fede33", """vaya tocho infumable""", 1),
  (2, "nacho23", """[reseña estándar]""", 4),
  (4, "nacho23", """[reseña con spoilers]""", 4),
  (3, "msaracchi", """[reseña muy larga y detallada que desafía los límites de almacenamiento del sistema, del ancho de banda del sitio web y de la paciencia humana]""", 4)
]

# Puntúa valoración
#  puntua(_nombreUsuarioPuntuador_, _nombreUsuarioValorador_, _idProducto_, puntuacion)
puntua = [
  ("nacho23", "alba23", 3, 1),
  ("alicia22", "nacho23", 2, 1),
  ("alba23", "nacho23", 4, 0),
  ("alberto23", "alba23", 3, 1)
]

# Reporta valoración
#  reporta(_nombreusuarioreportador_, _nombreusuarioreportado_, _idproducto_)
reporta = [
  ("alba23", "fede33", 3),
  ("nacho23", "fede33", 3),
  ("alberto23", "fede33", 3),
  ("cristi23", "fede33", 3),
  ("alba23", "nacho23", 4)
]
