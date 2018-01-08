### **valoración-valora**

- valoración-valora(_idProducto_,_nombreUsuario_,reseña,puntuación)

donde *idProducto* y *nombreUsuario* son clave externa en `productoCultural-Padre` y `usuario` respectivamente.

Las dependencias funcionales son las generadas por $\{\operatorname{idProducto}, \operatorname{nombreUsuario}\} \to R$.

La única clave candidata es la clave primaria *idProducto* *nombreUsuario*. Por ello **está en 2FN** (cualquier atributo no primo depende de forma completa de esta clave candidata).

Solo hay un determinante, que es la clave primaria. Por ello, no hay dependencias transitivas (**está en 3FN**) y todo determinante es clave candidata: **está en FNBC**.

```sql
CREATE TABLE valoracion-valora(
  idProducto int NOT NULL FOREIGN KEY REFERENCES productoCultural-Padre(id),
  nombreUsuario varchar(100) NOT NULL FOREIGN KEY REFERENCES usuario(nombreusuario),
  resena varchar(16384) NOT NULL,
  puntuacion int NOT NULL,

  CONSTRAINT clave_primaria_valoracion PRIMARY KEY (idProducto, nombreUsuario),
  CONSTRAINT rango_puntuacion CHECK (puntuacion >= 1 AND puntuacion <= 5)
);
```


### **puntúa**

- puntúa(_nombreUsuarioPuntuador_,_nombreUsuarioValorador_,_idProducto_,puntuación)

donde *idProducto* es clave externa en `productoCultural-Padre`, y *nombreUsuarioPuntuador* y *nombreUsuarioValorador* son ambos clave externa en `usuario`.

Las dependencias funcionales son las del cierre de $\{\operatorname{nombreUsuarioPuntuador}, \operatorname{nombreUsuarioValorador}, \operatorname{idProducto}\} \to R$.

Solo hay una clave candidata y solo hay un determinante, que es la clave primaria: **está en 2FN** (el único atributo no primo depende de forma completa de la única clave candidata), **está en 3FN** (no hay dependencias transitivas) y **está en FNBC** (el único determinante es clave candidata).

```sql
CREATE TABLE puntua(
  nombreUsuarioPuntuador varchar(100) NOT NULL FOREIGN KEY REFERENCES usuario(nombreusuario),
  nombreUsuarioValorador varchar(100) NOT NULL FOREIGN KEY REFERENCES usuario(nombreusuario),
  idProducto int NOT NULL FOREIGN KEY REFERENCES productoCultural-Padre(id),
  puntuacion int NOT NULL,

  CONSTRAINT clave_primaria_puntua PRIMARY KEY (nombreUsuarioPuntuador, nombreUsuarioValorador, idProducto),
  CONSTRAINT rango_puntuacion CHECK (puntuacion >= 0 AND puntuacion <= 1)
);
```

La inserción en esta tabla provoca la ejecución del siguiente disparador, que implementa la restricción semántica RS-4.4.

```sql
CREATE TRIGGER puntuar_propias_valoraciones
BEFORE INSERT ON puntua
WHEN NEW.nombreUsuarioPuntuador = NEW.nombreUsuarioValorador
BEGIN
SELECT RAISE(ABORT, 'Un usuario no puede puntuar sus propias valoraciones');
END;
```


### **pertenece_a**

- pertenece_a(_idProducto_,_Identificador_)

donde *idProducto* es clave externa en `productoCultural-Padre` e *Identificador* es clave externa en `géneroSupergénero`.

Las dependencias funcionales son las triviales.

No hay atributos no primos y solo hay un determinante, por lo que **está en FNBC**.

```sql
CREATE TABLE pertenece_a(
  idProducto int NOT NULL FOREIGN KEY REFERENCES productoCultural-Padre(id),
  Identificador varchar(100) NOT NULL FOREIGN KEY REFERENCES generoSupergenero(identificador),

  CONSTRAINT clave_primaria_puntua PRIMARY KEY (idProducto, Identificador)
);
```
