---
title: Sistema de valoración de productos culturales
author: ["Pablo Baeyens", "José Manuel Muñoz", "Mario Román", "Víctor Manuel Cerrato"]
date: DDSI
lang: es
toc: true
toc-depth: 1
fontsize: 12pt
geometry: margin=1.4in
---

\newpage

```include
descripcion.md
```

\newpage

# Requisitos funcionales y de datos

```include
Requisitos/productos.md
Requisitos/entidades.md
Requisitos/usuario.md
Requisitos/valoraciones.md
```


<!--Esquemas-->

```include
Esquemas/general.md
```

\newpage

```include
Esquemas/productos.md
```

\newpage

```include
Esquemas/entidades.md
```

\newpage

```include
Esquemas/usuarios.md
```

\newpage

```include
Esquemas/valoraciones.md
```

<!--Operaciones-->

\newpage

# Operaciones de datos y esquemas de navegación

```include
Operaciones/productos.md
```

\newpage

```include
Operaciones/entidades.md
```

\newpage

```include
Operaciones/usuarios.md
```

\newpage

```include
Operaciones/valoraciones.md
```

\newpage

# Tablas asociadas al esquema entidad-relación

```include
Tablas/tablas-mario.md
```

```include
Tablas/tablas-pablo.md
```

```include
Tablas/tablas-victor.md
```

```include
Tablas/tablas-jose-manuel.md
```

# Implementación de la práctica

El lenguaje utilizado para la implementación ha sido Python 3 mediante la librería `sqlite3`. Se han utilizado además las librerías `prompt_toolkit` y `tabulate`. Los ficheros implementados son:

- `main.py` donde se gestiona la inicialización de la base de datos y el bucle principal de lectura de comandos interactiva
- `auxiliar.py`, donde se implementan funciones auxiliares que son utilizadas por varios subsistemas.
- `populate.py` que añade al inicio del programa algunos datos de ejemplo
- `entidades.py`, `productos.py`, `valoraciones.py` y `usuarios.py`, donde se implementa cada subsistema
- `init.sql` donde se declaran las tablas
- `triggers.sql` donde se implementan los disparadores

El código puede consultarse en los ficheros correspondientes. La implementación de cada requisito funcional está indicada con un comentario.
