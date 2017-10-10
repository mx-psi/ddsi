## Requisitos de datos

RD4.1. Nueva valoración
: Proporcionada por el usuario, y consta de:

 - Producto cultural
 - Usuario
 - Puntuación numérica
 - Reseña

RD4.2. Valoración
: Almacenada en el sistema. Consta de:

 - Producto cultural
 - Usuario
 - Puntuación numérica
 - Reseña

RD4.3. Producto cultural
: Es proporcionado por el usuario, y se compone de:

 - Producto cultural

RD4.4. Resumen de valoraciones
: Se ofrece al usuario un resumen estadístico de valoraciones, provisionalmente en el siguiente formato:

 - Puntuación media
 - Histograma
 <!-- TODO: podría haber más datos relevantes o incluso datos más relevantes -->

RD4.5. Valoración
: Pedida por el usuario, se describe por:

 - Valoración

RD4.6. Valoración
: Presentada al usuario, compuesta por:

 - Producto cultural
 - Usuario
 - Puntuación numérica
 - Reseña
 - Puntuación de la propia valoración

RD4.7. Puntuación de valoración
: Indicación de un usuario sobre si cierta valoración es útil, descrita por:

 - Valoración
 - Usuario que efectúa la valoración
 - Útil/no útil

RD4. Puntuación de valoración
: Se describe por:

 - Valoración
 - Usuario que efectuó la valoración
 - Útil/no útil

RD4.9. Valoración
: Referida por el usuario con el objetivo de marcarla como inválida. Consta de:

 - Valoración
 - Usuario denunciante

RD4.10. Denuncia de valoración
: Se compone de:

 - Valoración
 - Usuario denunciante

 
## Requisitos funcionales

RF4.1. Escribir valoración
: Un usuario valora un producto cultural, proporcionando:

  - RD4.1

El sistema almacenará:

  - RD4.2

RF4.2. Consultar resumen de valoraciones
: Permite obtener un resumen de las valoraciones de un producto cultural, presentando datos estadísticos fáciles de interpretar para el usuario. El usuario proporciona:

 - RD4.3

El sistema consultará:

 - RD4.2

El sistema devolverá al usuario:

 - RD4.4

RF4.3. Consultar valoración
: Un usuario visualiza una valoración particular, proporcionando para ello:

 - RD4.5

El sistema consultará:

 - RD4.2
 - RD4.7

Y responderá presentando:

 - RD4.6

RF4.4. Puntuar una valoración
: Permite que el usuario indique si una valoración es útil. El usuario proporciona:

 - RD4.7

El sistema actualizará, consecuentemente:

 - RD4.8

RF4.5. Reportar valoración inapropiada
: Un usuario reporta una valoración que considere inapropiada. El usuario indica:

 - RD4.9

Y el sistema actualiza:

 - RD4.10

 
## Restricciones semánticas

RS4.1
: Un usuario no podrá hacer más de una valoración de un producto cultural.

RS4.2
: Un usuario no podrá puntuar más de una vez una misma valoración.

RS4.3
: Un usuario no podrá reportar una valoración que ya ha sido reportada por el mismo usuario.
