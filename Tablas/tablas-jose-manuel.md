### **valoración-valora**

- valoración-valora(_idProducto_,_nombreUsuario_,reseña,puntuación)

donde *idProducto* y *nombreUsuario* son clave externa en `productoCultural-Padre` y `usuario` respectivamente.

Las dependencias funcionales son las generadas por $\{\operatorname{idProducto}, \operatorname{nombreUsuario}\} \to R$.

La única clave candidata es la clave primaria *idProducto* *nombreUsuario*. Por ello **está en 2FN** (cualquier atributo no primo depende de forma completa de esta clave candidata).

Solo hay un determinante, que es la clave primaria. Por ello, no hay dependencias transitivas (**está en 3FN**) y todo determinante es clave candidata: **está en FNBC**.

<!-- TODO: sentencia SQL -->

### **puntúa**

- puntúa(_nombreUsuarioPuntuador_,_nombreUsuarioValorador_,_idProducto_,puntuación)

donde *idProducto* es clave externa en `productoCultural-Padre`, y *nombreUsuarioPuntuador* y *nombreUsuarioValorador* son ambos clave externa en `usuario`.

Las dependencias funcionales son las del cierre de $\{\operatorname{nombreUsuarioPuntuador}, \operatorname{nombreUsuarioValorador}, \operatorname{idProducto}\} \to R$.

Solo hay una clave candidata y solo hay un determinante, que es la clave primaria: **está en 2FN** (el único atributo no primo depende de forma completa de la única clave candidata), **está en 3FN** (no hay dependencias transitivas) y **está en FNBC** (el único determinante es clave candidata).

<!-- TODO: sentencia SQL -->

### **pertenece_a**

- pertenece a(_idProducto_,_Identificador_)

donde *idProducto* es clave externa en `productoCultural-Padre` e *Identificador* es clave externa en `géneroSupergénero`.

Las dependencias funcionales son las triviales.

No hay atributos no primos y solo hay un determinante, por lo que **está en FNBC**.

<!-- TODO: sentencia SQL -->
