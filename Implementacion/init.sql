-- Script para creación de tablas

-- Tablas de productos culturales

CREATE TABLE productoCulturalPadre(
id int,
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


-- Tablas de géneros y entidades creadoras

CREATE TABLE géneroSupergénero(
  identificador varchar(100),
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
