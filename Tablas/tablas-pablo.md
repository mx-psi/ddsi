
- productoCultural-Padre(_id_, nombre, fechaPublicacion, tipo, idPadre)

donde *idPadre* es clave externa en productoCultural-Padre (puede ser `null`)

- asociadoA(_id1_, _id2_, descripcion)

donde *id1*, *id2* son claves externas en productoCultural-Padre

- creadoPor(_idProducto_, _rol_, _nombreCreador_)

donde *idProducto* es clave externa en productoCultural-Padre y *nombreCreador* es clave externa en entidadCreadora.
