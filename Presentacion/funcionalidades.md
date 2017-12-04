## Tablas

![Mostrando una tabla.](Presentacion/tryton-table.png){width=250px height=250px}

## Gestión de usuarios

 * Provee mecanismos de autenticación de usuarios al servidor.
 * Control sobre los datos que accede cada usuario.
 * Permite crear grupos de usuario con datos y control particulares.
 * Permite el acceso concurrente a los recursos.

## Bases de datos

Tryton puede usarse sobre PostgreSQL, MySQL y SQLite. Para ello usa internamente
la librería `python-sql`, que es agnóstica respecto a la base de datos utilizada.

El servidor de pruebas utiliza `SQLite`

## Localización

 * Traducción a numerosos lenguajes (francés, ruso, italiano,
   español...).
 
 * Módulo `currency` con soporte para monedas arbitrarias y ratios de
   cambio.

 * Gestor de contabilidad adaptado a la legislación del país. Por ejemplo,
   `account-es` crea según el *Plan General Contable Español 2008*, y según
   el *Plan Contable para PYMES 2008*.


## Módulos

La funcionalidad puede extenderse con **módulos** instalables desde
Python.


