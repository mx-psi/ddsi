---
title: Requisitos del subsistema de valoraciones
---

# Requisitos funcionales

RF-4.1. Escribir valoración
: Un usuario valora un producto cultural.

- E: RD-4.1
- M: RD-4.2

RF-4.2. Consultar resumen de valoraciones
: Permite obtener un resumen de las valoraciones de un producto cultural, presentando datos estadísticos fáciles de interpretar para el usuario.

- E: RD-4.3
- M: RD-4.2
- S: RD-4.4

RF-4.3. Consultar valoración
: Un usuario visualiza una valoración particular.

- E: RD-4.5
- M: RD-4.2, RD-4.7
- S: RD-4.6

RF-4.4. Puntuar una valoración
: Permite que el usuario indique si una valoración es útil.

- E: RD-4.7
- M: RD-4.8

RF-4.5. Reportar valoración inapropiada
: Un usuario reporta una valoración que considere inapropiada.

- E: RD-4.9
- M: RD-4.10

 
# Requisitos de datos

RD-4.1. Nueva valoración
: Proporcionada por el usuario, y consta de:

- Producto cultural
- Usuario
- Puntuación numérica
- Reseña

RD-4.2. Valoración
: Almacenada en el sistema. Consta de:

- Producto cultural
- Usuario
- Puntuación numérica
- Reseña

RD-4.3. Producto cultural
: Es proporcionado por el usuario, y se compone de:

- Producto cultural

RD-4.4. Resumen de valoraciones
: Se ofrece al usuario un resumen estadístico de valoraciones, provisionalmente en el siguiente formato:

- Puntuación media
- Histograma
 <!-- TODO: podría haber más datos relevantes o incluso datos más relevantes -->

RD-4.5. Valoración
: Pedida por el usuario, se describe por:

- Valoración

RD-4.6. Valoración
: Presentada al usuario, compuesta por:

- Producto cultural
- Usuario
- Puntuación numérica
- Reseña
- Puntuación de la propia valoración

RD-4.7. Puntuación de valoración
: Indicación de un usuario sobre si cierta valoración es útil, descrita por:

- Valoración
- Usuario que efectúa la valoración
- Útil/no útil

RD-4. Puntuación de valoración
: Se describe por:

- Valoración
- Usuario que efectuó la valoración
- Útil/no útil

RD-4.9. Valoración
: Referida por el usuario con el objetivo de marcarla como inválida. Consta de:

- Valoración
- Usuario denunciante

RD-4.10. Denuncia de valoración
: Se compone de:

- Valoración
- Usuario denunciante


# Restricciones semánticas

RS-4.1
: Un usuario no podrá hacer más de una valoración de un producto cultural. Asociado a: RF-4.1 y RD-4.2

RS-4.2
: Un usuario no podrá puntuar más de una vez una misma valoración. Asociado a: RF-4.4 y RD-4.8

RS-4.3
: Un usuario no podrá reportar una valoración que ya ha sido reportada por el mismo usuario. Asociado a: RF-4.5 y RD-4.10

