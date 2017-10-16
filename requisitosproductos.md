---
title: Requisitos del subsistema de entidades creadoras
---

# Cambios realizados en la descripción durante el establecimiento de los requisitos

Inicialmente la descripción de los productos culturales incluía el concepto de edición, versión o instancia de un producto cultural:

> Los **productos culturales** constan de un nombre, ediciones o versiones, otros productos culturales asociados y una serie de géneros o categorías a las que pertenece. Cada edición, versión o instancia consta de fecha de publicación, identificador y un conjunto de entidades creadoras asociadas.

Esta descripción se ha modificado de tal forma que las ediciones, versiones o instancias ahora son productos culturales, de tal manera que se permita la creación de jerarquías de más de dos niveles (por ejemplo, serie de televisión → temporada → episodio):

> Los **productos culturales** constan de un nombre, fecha de publicación, identificador, productos culturales padre, otros productos culturales asociados, una serie de géneros a las que pertenece y un conjunto de entidades creadoras asociadas.

# Requisitos funcionales

<!--
RF-1.x
: Descripción
- E: RDy
- M: RDz
- S: RDw

- No hay que pensar en la implementación directamente: hay que pensar en el uso que les vamos a dar.
- Los datos de entrada, manejados y de salida son diferentes como requisitos de datos (datos de un contacto/de un contacto almacenado)!

Entrada
: Los que requiere la función para funcionar. Siempre hay.

Manejados
: Los que se almacenan. Incluye uso y solución de almacenamiento. Siempre hay.

Salida
: Cosas tipo "Se ha insertau bien". A veces no hay
-->

RF-1.1. Añadir un producto cultural nuevo
: El sistema permite añadir un producto cultural. Con restricción RS-1.1, RS-1.2 y RS-1.3.

- E: RD-1.1
- M: RD-1.2 
- S: RD-1.3

RF-1.2. Modificar un producto cultural existente
: El sistema permite modificar los datos de un producto cultural ya existente. Con restricción RS-1.1, RS-1.2 y RS-1.3.

- E: RD-1.4
- M: RD-1.5
- S: RD-1.6

RF-1.3. Consultar información de un producto cultural
: El sistema permite consultar los datos asociados a un producto cultural

- E: RD-1.7
- M: RD-1.2
- S: RD-1.8

RF-1.4. Buscar un producto cultural
: El sistema permite buscar los productos culturales que cumplan un cierto criterio. Con restricción RS-1.4

- E: RD-1.9
- M: RD-1.10
- S: RD-1.11


# Requisitos de datos

<!--El único punto donde se repiten los RD es en Almacenamiento. Si Rdx aparece en entrada/salida, nunca puede aparecer en otro sitio.-->

RD-1.1. Datos de un producto cultural
: Proporcionados al introducir un producto cultural al sistema (con restricción RS-1.1, RS-1.2 y RS-1.3):

- Nombre (una cadena no vacía) con restricción RS-1.1
- Identificador (una cadena no vacía) con restricción RS-1.2
- Una lista posiblemente vacía de pares compuestos por el nombre de un producto cultural ya existente y la descripción de su asociación con el producto cultural a añadir (una cadena no vacía).
- Una lista no vacía de los identificadores de los géneros a las que pertenece.
- Una fecha de publicación posiblemente futura
- Una lista no vacía de los nombres de los productos culturales padre
- Una lista no vacía de pares compuestos por el nombre de cada entidad creadora asociada y rol de esa asociación (una cadena no vacía)

RD-1.2. Producto cultural
: Los datos proporcionados en RD-1.1. Con restricción RS-1.1, RS-1.2 y RS-1.3.

RD-1.3. Confirmación de introducción de producto cultural
: Mensaje de salida que indica si los datos se han introducido correctamente y cuáles son los datos almacenados (los de RD-1.2). Con restricción RS-1.1, RS-1.2 y RS-1.3

RD-1.4. Datos a modificar de un producto cultural
: Los datos a modificar son (con restricción RS-1.1, RS-1.2 y RS-1.3):

- Una lista posiblemente vacía de pares compuestos por el nombre de un producto cultural ya existente y la descripción de su asociación con el producto cultural a añadir (una cadena no vacía).
- Una lista no vacía de los identificadores de los géneros a las que pertenece.
- Una lista no vacía de los nombres de los nuevos productos culturales padre
- Una lista posiblemente vacía de pares compuestos por el nombre de un producto cultural ya existente y la descripción de su asociación con el producto cultural a añadir (una cadena no vacía).
- Una lista no vacía de los identificadores de los géneros a las que pertenece.

RD-1.5. Modificados de producto cultural
: Los datos proporcionados en RD-1.4. Con restricción RS-1.1, RS-1.2 y RS-1.3.

RD-1.6. Confirmación de modificación
: Mensaje de salida que indica si los datos se han introducido correctamente y cuáles son los datos almacenados con las modificaciones (los listados en RD-1.1 con las modificaciones de RD-1.4). Con restricción RS-1.1, RS-1.2 y RS-1.3

RD-1.7. Producto a consultar
: Identificador del producto a consultar

RD-1.8. Salida de consulta de productos cultural
: Los datos del producto cultural con el identificador de RD-1.7 incluyendo todos los datos listados de RD-1.1 así como una lista de todos las entidades creadoras que han participado en alguno de los descendientes del producto cultural (describiendo su rol sólo si están directamente relacionados con el producto cultural consultado) y una lista de los géneros de todos los descendientes del producto cultural.

RD-1.9. Datos de búsqueda de productos culturales
: Alguno de los datos del listado de RD-1.1 o una combinación lógica (con operadores OR, AND, NOT) de los datos. Con restricción RS-1.4.

RD-1.10. Búsqueda de productos culturales
: Los datos proporcionados en RD-1.9 así como una lista de los identificadores de los productos culturales que cumplan esos criterios.

RD-1.11. Salida de la búsqueda
: Una lista posiblemente vacía de pares identificador - nombre de los productos culturales que cumplan los criterios de RD-1.9.


# Restricciones semánticas

<!--Para las restricciones semánticas, poner RF y RD asociado-->

RS-1.1
: No habrá dos productos culturales con el mismo identificador. Asociado a: RD-1.1 a RD-1.6, RF-1.1 y RF-1.2

RS-1.2
: Un producto cultural no podrá estar asociado a sí mismo. Asociado a: RD-1.1 a RD-1.6, RF-1.1 y RF-1.2

RS-1.3
: La jerarquía de productos culturales será un árbol (no podrá formar ciclos). Asociado a: RD-1.1 a RD-1.6, RF-1.1 y RF-1.2

RS-1.4
: Debe rellenarse al menos un campo de la búsqueda de productos culturales. Asociado a: RD-1.9 y RF-1.4

