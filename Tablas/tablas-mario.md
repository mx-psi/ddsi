### premiadaPor
El esquema de la tabla es

 - premiadaPor(_nombre_, _id_, _nombrepremio_)

donde *nombre* es clave externa en `entidadCreadora` e *id* es una
clave externa en la tabla `productoCulturalPadre`.

Todos los atributos forman parte de la clave candidata y son primos;
por lo tanto, está en **2FN**. Está en **FNBC** porque no hay más
determinantes aparte de la única clave candidata.

```sql
CREATE TABLE premiadaPor(
  nombre varchar(100) CONSTRAINT nombre_ext REFERENCES entidadCreadora(nombre),
  id int CONSTRAINT id_ext REFERENCES productoCulturalPadre(id),
  nombrepremio varchar(100),
  
  CONSTRAINT clave_primaria PRIMARY KEY (nombre,id,nombrepremio)
)
```

## entidadCreadora
El esquema de la tabla es

 - entidadCreadora(_nombre_, tipo)
 
donde las dependencias funcionales son las generadas por `nombre → tipo`.
El único atributo no primo depende de forma completa de `nombre`; por tanto,
la tabla está en **2FN**. Este es el único determinante, así que la tabla
está además en **FNBC**.

```sql
CREATE TABLE entidadCreadora(
  nombre varchar(100),
  tipo varchar(100),
  
  CONSTRAINT clave_primaria PRIMARY KEY (nombre)
)
```


## géneroSupergénero
El esquema de la tabla es
 
 - géneroSupergénero(_identificador_, nombreGénero, supergénero).

donde *supergénero* puede ser `null` y tiene a identificador en esta
misma tabla como clave externa; las dependencias funcionales son las
generadas por `identificador → nombreGénero` y `identificador →
supergénero`.  Nótese que permitimos que pudieran existir dos géneros
con el mismo nombre pero distinto identificador, que podrían tener
supergéneros distintos.  La tabla está en **2FN**, porque cada
atributo no primo depende de forma completa de la única clave
candidata; además, está en **FNBC** porque de nuevo la clave candidata
es el único determinante.

```sql
CREATE TABLE géneroSupergénero(
  identificador varchar(100),
  nombreGenero varchar(100),
  superGenero varchar(100),
  
  CONSTRAINT clave_primaria PRIMARY KEY (identificador)
)
```
