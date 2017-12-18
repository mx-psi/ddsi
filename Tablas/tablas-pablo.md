
### **productoCultural-Padre**

El esquema es:

- productoCultural-Padre(_id_, nombre, fechaPublicacion, tipo, idPadre)

donde *idPadre* es clave externa en `productoCultural-Padre` (puede ser `null`)

Las dependencias funcionales son las generadas por $\operatorname{id} \to R$.

La única clave candidata es _id_ por lo que cualquier atributo no primo depende de forma completa de esta (sólo tiene un elemento). Por tanto **está en 2FN**.

No hay más determinantes aparte de la única clave candidata por lo que **está en FNBC**.

En SQL la creamos con la siguiente sentencia:

```sql
CREATE TABLE productoCulturalPadre(
id int,
nombre varchar(100),
fechaPublicacion date,
tipo varchar(100),
idPadre CONSTRAINT idPadre_ext 
        REFERENCES productoCulturalPadre(id),
        
CONSTRAINT clave_primaria PRIMARY KEY (id)
);
```

### **asociadoA**

- asociadoA(_id1_, _id2_, descripcion)

donde *id1*, *id2* son claves externas en `productoCultural-Padre`

Las dependencias funcionales son las generadas por $\{\operatorname{id}_1, \operatorname{id}_2\} \to R$.

Sólo hay una clave candidata: $\{\operatorname{id}_1, \operatorname{id}_2\}$. El único atributo no primo (descripción) depende de forma completa de la única clave candidata. Por tanto **está en 2FN**. 

No hay más determinantes aparte de la única clave candidata por lo que **está en FNBC**.

En SQL la creamos con la siguiente sentencia:

```sql
CREATE TABLE asociadoA(
id1 CONSTRAINT id1_ext 
    REFERENCES productoCulturalPadre(id),
id2 CONSTRAINT id2_ext 
    REFERENCES productoCulturalPadre(id),
descripcion varchar(100),

CONSTRAINT clave_primaria PRIMARY KEY (id1,id2)
);
```

### **creadoPor**

- creadoPor(_idProducto_, _rol_, _nombreCreador_)

donde *idProducto* es clave externa en `productoCultural-Padre` y *nombreCreador* es clave externa en `entidadCreadora`.

Las dependencias funcionales son las generadas por $\{\operatorname{idProducto}, \operatorname{rol}, \operatorname{nombreCreador}\} \to R$

Como no hay atributos no primos podemos afirmar directamente que **está en 3FN**. No hay más determinantes aparte de la clave primaria por lo que **está en FNBC**.

En SQL la creamos con la siguiente sentencia:

```sql
CREATE TABLE creadoPor(
idProducto CONSTRAINT idProducto_ext 
    REFERENCES productoCulturalPadre(id),
rol varchar(100),
nombreCreador CONSTRAINT nombreCreador_ext 
    REFERENCES entidadCreadora(nombre),

CONSTRAINT clave_primaria PRIMARY KEY (idProducto, rol, nombreCreador)
);
```
