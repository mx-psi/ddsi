-- Script para creación de tablas

-- Tablas de productos culturales

CREATE TABLE productoCulturalPadre(
id int AUTOINCREMENT,
nombre varchar(100),
fechaPublicacion date,
tipo varchar(100),
idPadre CONSTRAINT idPadre_ext
        REFERENCES productoCulturalPadre(id),

CONSTRAINT clave_primaria PRIMARY KEY (id)
);

CREATE TABLE asociadoA(
id1 CONSTRAINT id1_ext
    REFERENCES productoCulturalPadre(id),
id2 CONSTRAINT id2_ext
    REFERENCES productoCulturalPadre(id),
descripcion varchar(100),

CONSTRAINT clave_primaria PRIMARY KEY (id1,id2)
);

CREATE TABLE creadoPor(
idProducto CONSTRAINT idProducto_ext
    REFERENCES productoCulturalPadre(id),
rol varchar(100),
nombreCreador CONSTRAINT nombreCreador_ext
    REFERENCES entidadCreadora(nombre),

CONSTRAINT clave_primaria PRIMARY KEY (idProducto, rol, nombreCreador)
);

CREATE TABLE pertenece_a(
  idProducto int NOT NULL FOREIGN KEY REFERENCES productoCultural-Padre(id),
  Identificador varchar(100) NOT NULL FOREIGN KEY REFERENCES géneroSupergénero(identificador),

  CONSTRAINT clave_primaria_puntua PRIMARY KEY (idProducto, Identificador)
);


-- Tablas de géneros y entidades creadoras

CREATE TABLE géneroSupergénero(
  identificador int AUTOINCREMENT,
  nombreGenero varchar(100),
  superGenero varchar(100),
  
  CONSTRAINT clave_primaria PRIMARY KEY (identificador)
);

CREATE TABLE entidadCreadora(
  nombre varchar(100),
  tipo varchar(100),
  
  CONSTRAINT clave_primaria PRIMARY KEY (nombre)
);

CREATE TABLE premiadaPor(
  nombre varchar(100) CONSTRAINT nombre_ext REFERENCES entidadCreadora(nombre),
  id int CONSTRAINT id_ext REFERENCES productoCulturalPadre(id),
  nombrepremio varchar(100),
  
  CONSTRAINT clave_primaria PRIMARY KEY (nombre,id,nombrepremio)
);

-- Tablas de valoraciones

CREATE TABLE valoracion-valora(
  idProducto int NOT NULL FOREIGN KEY REFERENCES productoCultural-Padre(id),
  nombreUsuario varchar(20) NOT NULL FOREIGN KEY REFERENCES usuario(nombreusuario),
  resena varchar(16384) NOT NULL,
  puntuacion int NOT NULL,

  CONSTRAINT clave_primaria_valoracion PRIMARY KEY (idProducto, nombreUsuario),
  CONSTRAINT rango_puntuacion CHECK (puntuacion >= 1 AND puntuacion <= 5)
);

CREATE TABLE puntua(
  nombreUsuarioPuntuador varchar(20) NOT NULL FOREIGN KEY REFERENCES usuario(nombreusuario),
  nombreUsuarioValorador varchar(20) NOT NULL FOREIGN KEY REFERENCES usuario(nombreusuario),
  idProducto int NOT NULL FOREIGN KEY REFERENCES productoCultural-Padre(id),
  puntuacion int NOT NULL,

  CONSTRAINT clave_primaria_puntua PRIMARY KEY (nombreUsuarioPuntuador, nombreUsuarioValorador, idProducto),
  CONSTRAINT rango_puntuacion CHECK (puntuacion >= 0 AND puntuacion <= 1)
);

