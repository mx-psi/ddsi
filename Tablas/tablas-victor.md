### Usuario

- usuario(_nombreusuario_, nombrereal, localidadorigen,
         correoelectrónico, descripciónusuario, contraseña)

Las dependencias funcionales son las generadas por *nombreusuario → R*.

La única clave candidata es *nombreusuario*, luego los atributos no primos dependen de forma completa de ésta y por lo tanto está
en **segunda forma normal**.

El único determinante de la relación es la única clave candidata luego **está en FNBC**.

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

Al insertar tuplas en esta tabla se lanza este disparador, que implementa la restricción semántica RS-3.2.

```sql
CREATE TRIGGER inserta_usuario
BEFORE INSERT ON usuario
WHEN NEW.correoelectronico NOT REGEXP
'[(a-z)]+[(a-z0-9\_\-\.)]*@([(a-z)]+\.)*[(a-z)]+\.[(a-z)]{2,15}$'
BEGIN
SELECT RAISE(ABORT, 'El formáto de correo electrónico no es válido.');
END;
```

### leGusta

- leGusta(_nombreusuario_,_identificador_)

donde *nombreusuario* es clave externa de la tabla *usuario* e *identificador* de la tabla *géneroSupergénero*.

Solo hay una clave candidata y primaria que es *nombreusuario* junto *identificador* por lo tanto está en **FNBC**.

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
		
CONSTRAINT clave_primaria PRIMARY KEY 
(nombreusuarioreportador,nombreusuarioreportado,idproducto)
);
```

Al insertar tuplas en esta tabla se lanza este disparador, que implementa la restricción semántica RS-4.5.

```sql
CREATE TRIGGER reportar_propias_valoraciones
BEFORE INSERT ON reporta
WHEN NEW.nombreUsuarioReportador = NEW.nombreUsuarioReportado
BEGIN
SELECT RAISE(ABORT, 'Un usuario no puede reportar sus propias valoraciones');
END;
```
