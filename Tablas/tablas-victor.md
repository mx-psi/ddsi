### Usuario

- usuario(_nombreusuario_,nombrereal,localidadorigen,correoelectrónico,descripciónusuario,contraseña)

La única clave candidata es _nombreusuario_, luego cualquier atributo no primo depende de forma completa de ésta y por lo tanto está
en **segunda forma normal**.

El determinante de la relación es la única clave candidata luego **está en FNBC**.

Sentencia de creación de la tabla en SQL:
```sql
CREATE TABLE usuario(
nombreusuario varchar(20),
nombrereal varchar(60),
localidadorigen varchar(20),
correoelectronico varchar(40),
descripcionusuario varchar(300),
password varchar(20),
        
CONSTRAINT clave_primaria PRIMARY KEY (nombreusuario)
);
```

### leGusta

- leGusta(_nombreusuario_,_identificador_)

donde *nombreusuario* es clave externa de la tabla *usuario* e *identificador* de la tabla *géneroSupergénero*.

Solo hay una clave candidata y primaria que es nombreusuario junto identificador por lo tanto está en **FNBC**.

Sentencia de creación de la tabla en SQL:
```sql
CREATE TABLE leGusta(
nombreusuario varchar(20),
identificador varchar(100),

nombreusuario CONSTRAINT nombreusuario_ext 
        REFERENCES usuario(nombreusuario),
		
identificador CONSTRAINT identificador_ext 
        REFERENCES géneroSupergénero(identificador),
        
CONSTRAINT clave_primaria PRIMARY KEY (nombreusuario,identificador)
);
```

### reporta

- reporta(_nombreusuarioreportador_,_nombreusuarioreportado_,_idproducto_)

donde *nombreusuarioreportador* es clave externa de la tabla *usuario*, *nombreusuarioreportado* *idproducto* es clave externa de la tabla *valoración-valora*.

Solo hay una clave candidata y primaria que es _nombreusuarioreportador_ _nombreusuarioreportado_ _idproducto_ por lo tanto está en **FNBC**.

Sentencia de creación de la tabla en SQL:
```sql
CREATE TABLE reporta(
nombreusuarioreportador varchar(20),
nombreusuarioreportado varchar(20).
idproducto int,

nombreusuarioreportador CONSTRAINT nombreusuarioreportador_ext 
        REFERENCES usuario(nombreusuario),

idproducto CONSTRAINT idproducto_ext 
        REFERENCES productoCulturalPadre(id),
		
nombreusuarioreportado CONSTRAINT nombreusuarioreportado_ext 
        REFERENCES valoracion-valora(nombreUsuario),
		
CONSTRAINT clave_primaria PRIMARY KEY (nombreusuarioreportador,nombreusuarioreportado,idproducto)
);
```
