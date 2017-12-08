## Tablas

Las tablas permiten la visualización directa de los datos

![Mostrando una tabla.](Presentacion/tryton-table.png){width=250px height=250px}

Se permite el tratamiento individual de entradas de la tabla,
el ejecutar acciones sobre la tabla y añadir notas y adjuntar
archivos a entradas.

## Gestión de usuarios

![Gestión de grupos de usuario.](Presentacion/usuarios.png){width=250px height=250px}

 * Mecanismos de autenticación de usuarios al servidor.
 * Control sobre los datos que accede cada usuario.
 * Creación de grupos de usuario con datos y control particulares.
 * Acceso concurrente a los recursos.

## Bases de datos

Tryton puede usarse sobre PostgreSQL, MySQL y SQLite. Para ello usa internamente
la librería `python-sql`, que es agnóstica respecto a la base de datos utilizada.
La base de datos MySQL que se utilizará se decide al lanzar el servidor.

```
trytond -c /etc/trytond.conf -d <base de datos> --all
```


El servidor de pruebas utiliza `SQLite` y se recomienda para prototipado.

## Localización

 * Traducción a numerosos lenguajes (francés, ruso, italiano,
   español...).
 
 * Módulo `currency` con soporte para monedas arbitrarias y ratios de
   cambio.

 * Gestor de contabilidad adaptado a la legislación del país. Por ejemplo,
   `account-es` crea según el *Plan General Contable Español 2008*, y según
   el *Plan Contable para PYMES 2008*.
   
 * Módulo `country` permitiendo ubicarse con subdivisiones en un país
   (comunidades autónomas, provincias, ...).


## Módulos

La funcionalidad puede extenderse con **módulos** instalables desde
Python; los módulos permiten, por ejemplo,

 * integración con Google Maps;
 * controlar el tiempo de trabajo;
 * control de transportistas;
 * control de cuentas bancarias;
 * gestión en diferentes proyectos;
 * acceso desde interfaz web;
 * guardar contactos y calendarios.
 


