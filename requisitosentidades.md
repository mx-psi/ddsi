---
title: Requisitos del subsistema de entidades creadoras
---

## Requisitos funcionales

RF-2.1. Añadir una entidad creadora
: Esta función registra una entidad creadora dentro del sistema a
  partir de su nombre y tipo.
  
    - E: RD-2.1,
    - M: RD-2.2,
    - S: ninguno.

RF-2.2. Registrar un premio asociado a la creación de una entidad creadora
: Esta función añade un premio dada una entidad creadora que lo recibe
  y un producto cultural por el cual lo recibe.
  
    - E: RD-2.3,
    - M: RD-2.4,
    - S: RD-2.10.
  
  Debe cumplirse la restricción semántica especificada en RS2.1.

RF-2.3. Consultar una entidad creadora
: Dado el nombre de una entidad creadora, esta función muestra el
  nombre, tipo, productos culturales creados y premios asociados a
  esas creaciones, si los hubiere.

    - E: RD-2.1;
    - M: RD-2.2, RD-2.4, [productos culturales];
    - S: RD-2.2, RD-2.4, [productos culturales].

RF-2.4. Añadir un género
: Esta función registra un género en el sistema a partir de un nombre,
  un identificador, y, opcionalmente, un supergénero al que pertenece
  como subgénero.
  
    - E: RD-2.5,
    - M: RD-2.6,
    - S: ninguna.

  Debe cumplirse la restricción semántica RS2.2.

RF-2.5. Consultar un género por nombre
: Dado el nombre de un género, esta función muestra su nombre,
  identificador, supergénero, subgéneros asociados y productos
  culturales asociados a ese género.

    - E: RD-2.8;
    - M: RD-2.5, [productos];
    - S: RD-2.5, [productos].
    
RF-2.6. Consultar un género por identificador
: Dado el identificador de un género, esta función muestra su nombre,
  identificador, supergénero, subgéneros asociados y productos
  culturales asociados a ese género.

    - E: RD-2.9;
    - M: RD-2.5, [productos];
    - S: RD-2.5, [productos].


## Requisitos de datos

RD-2.1. Los datos de una entidad creadora
: Constará de los datos

 - *nombre*, una cadena de hasta 80 caracteres no vacía; y
 - *tipo*, una cadena de hasta 80 caracteres no vacía.

RD-2.2. Los datos de una entidad creadora almacenada
: Constará de los datos

 - nombre, una cadena de hasta 80 caracteres no vacía; y
 - tipo, una cadena de hasta 80 caracteres no vacía.

RD-2.3. Los datos de un premio concedido a una entidad por un producto
: Constará de los datos

 - nombre del premio, una cadena de hasta 100 caracteres no vacía;
 - nombre de entidad creadora, una cadena de hasta 80 caracteres no vacía; y
 - nombre del producto cultural, una cadena de hasta 80 caracteres no vacía.

RD-2.4. Los datos almacenados de un premio concedido a una entidad por un producto
: Constará de los datos
  
 - nombre del premio, una cadena de hasta 100 caracteres no vacía;
 - nombre de entidad creadora, una cadena de hasta 80 caracteres no vacía; y
 - nombre del producto cultural, una cadena de hasta 80 caracteres no vacía.

RD-2.5. Los datos de un género
: Constará de los datos

 - nombre, una cadena de hasta 80 caracteres no vacía;
 - identificador, una cadena de hasta 60 caracteres no vacía; y
 - supergénero, una cadena, quizá vacía, de hasta 80 caracteres.

RD-2.6. Los datos de un género almacenado
: Constará de los datos

 - nombre, una cadena de hasta 80 caracteres no vacía;
 - identificador, una cadena de hasta 60 caracteres no vacía; y
 - supergénero, una cadena, quizá vacía, de hasta 80 caracteres.

RD-2.7. Los datos de consulta de una entidad creadora
: Constará del dato

 - nombre, una cadena de hasta 80 caracteres no vacía.

RD-2.8. Los datos de consulta de un género por nombre
: Constará del dato

 - nombre, una cadena de hasta 80 caracteres no vacía.

RD-2.9. Los datos de consulta de un género por identificador
: Constará del dato

 - identificador, una cadena de hasta 60 caracteres no vacía.

RD-2.10. Mensaje de confirmación de registro de premio
: Mensaje que indica que un premio asociado a una entidad creadora por
  un producto cultural se ha añadido correctamente
  
    - mensaje, una cadena no vacía.

## Restricciones semánticas

RS2.1
: La entidad creadora debe estar presente en la lista de entidades
  creadoras del producto cultural. Asociado a: RF-2.2, RD-2.2 y RD-2.4.

RS2.2
: Un género no podrá ser su propio supergénero. Asociado a: RF-2.4, RD-2.5 y RD-2.6.

