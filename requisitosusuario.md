# Requisitos del subsistema de usuarios

## Requisitos funcionales

RF-3.1. Alta de usuario
: un usuario puede de darse de alta en el sistema. Se usan las restricciones RS-3.1, RS-3.2, RS-3.3 y RS-3.4.

 - E: RD-3.1
 - A/M: RD-3.2
 - S: RD-3.9
 
RF-3.2. Baja de usuario
: un usuario es capaz de darse de baja del sistema.

 - E: RD-3.3
 - A/M: RD-3.2
 - S: RD-3.10
 
RF-3.3. Modificar perfil
: los usuarios son capaces de modificar sus datos en el sistema. Se usan las restricciones RS-3.1, RS-3.2, RS-3.3 y RS-3.4.

 - E: RD-3.4
 - A/M: RD-3.2
 - S: RD-3.11
 
RF-3.4. Consultar recomendaciones
: los usuarios son capaces de consultar recomendaciones dadas por el sistema basadas en sus categorías de interés y sus valoraciones en productos culturales similares.

 - E: RD-3.5
 - A/M: RD-3.2 y RD-4.2
 - S: RD-3.6
 
RF-3.5. Notificar de productos interesantes
: los usuarios recibirán notificaciones de la salida de nuevos productos culturales que podrían interesarles.

 - A/M: RD-3.2 y RD-1.2
 - S: RD-3.7

RF-3.6. Log in de usuario
: identificación del usuario en el sistema necesaria para acceder a los requisitos funcionales RF-3.2, RF-3.3, RF-3.4, RF-3.5, RF-3.7 y RF-3.8.

 - E: RD-3.8
 - A/M: RD-3.2
 - S: RD-3.12

RF-3.7. Consulta de perfil de usuario
: el usuario es capaz de consultar sus datos de perfil.

 - E: RD-3.13
 - A/M: RD-3.2
 - S: RD-3.14

RF-3.8. Consula de un perfil de usuario del sistema
: el usuario es capaz de consultar otros perfiles introduciendo el nombre de usuario de éstos.

 - E: RD-3.15
 - A/M: RD-3.2
 - S: RD-3.16

## Requisitos de datos

RD-3.1. Datos de entrada de la alta de un usuario
: datos que debe introducir el usuario que quiera darse de alta en el sistema. Se usan las restricciones RS-3.1, RS-3.2, RS-3.3 y RS-3.4.

 - Nombre de usuario (una cadena de hasta 20 caracteres no vacía).
 - Nombre real (una cadena de hasta 60 caracteres no vacía).
 - Localidad de origen (una cadena de hasta 20 caracteres no vacía).
 - Correo electrónico (una cadena de hasta 40 caracteres no vacía).
 - Lista de géneros de interés.
 - Descripción del usuario (una cadena de hasta 300 caracteres).
 - Contraseña (una cadena de al menos 6 caracteres y de hasta 20 como máximo).
 
RD-3.2. Datos de un usuario en el sistema
: datos que almacenará el sistema de un usuario. Se usan las restricciones RS-3.1, RS-3.2, RS-3.3 y RS-3.4.

 - Nombre de usuario (una cadena de hasta 20 caracteres no vacía).
 - Nombre real (una cadena de hasta 60 caracteres no vacía).
 - Localidad de origen (una cadena de hasta 20 caracteres no vacía).
 - Correo electrónico (una cadena de hasta 40 caracteres no vacía).
 - Lista de géneros de interés.
 - Descripción del usuario (una cadena de hasta 300 caracteres).
 - Contraseña (una cadena de al menos 6 caracteres y de hasta 20 como máximo).
 
RD-3.3. Botón darse de baja
: botón que debe pulsar el usuario para darse de baja del sistema.

 - Botón "Darse de baja".
 
RD-3.4. Modificar datos de perfil de usuario
: datos del usuario nuevos. Se usan las restricciones RS-3.1, RS-3.2, RS-3.3 y RS-3.4.

 - Nombre de usuario (una cadena de hasta 20 caracteres no vacía).
 - Nombre real (una cadena de hasta 60 caracteres no vacía).
 - Localidad de origen (una cadena de hasta 20 caracteres no vacía).
 - Correo electrónico (una cadena de hasta 40 caracteres no vacía).
 - Lista de géneros de interés.
 - Descripción del usuario (una cadena de hasta 300 caracteres).
 - Contraseña (una cadena de al menos 6 caracteres y de hasta 20 como máximo).
 
 Solo se modificarán los datos rellenados con las restricciones.

RD-3.5. Botón consultar recomendaciones
: botón que sirve para obtener las recomendaciones basadas en tu perfil de usuario.

 - Botón "Recomendaciones".
 
RD-3.6. Recomendaciones al usuario
: recomendaciones generadas por el sistema basadas en los datos del usuario.

 - Lista de productos culturales recomendados.

RD-3.7. Notificación de productos culturales
: aviso de nuevos productos culturales de interés.

 - Producto cultural estrenado
 
RD-3.8. Nombre de usuario y contraseña
: Consta de:

 - Nombre de usuario.
 - Contraseña.
 
RD-3.9. Mensaje de confirmación de alta de usuario
: Un mensaje que indique al usuario si su registro en el sistema se hizo correctamente.
 
RD-3.10. Mensaje de confirmación de baja de un usuario
: Se confirma que la baja del usuario en el sistema se realizó correctamente.
 
RD-3.11. Mensaje de confirmación de modificación de datos de un usuario
: con este mensaje indicamos si el usuario modificó sus datos correctamente.
 
RD-3.12. Mensaje de conffirmación de log in correcto del usuario
: este mensaje inicará si el usuario y contraseña introducidos son válidos.

RD-3.13. Botón de consulta de perfil de usuario
: este botón se usa para consultar el perfil de usuario propio.

 - Botón "Mi perfil".
 
RD-3.14. Datos de un usuario en el sistema
: datos que mostrará el sistema a un usuario al intentar consultarlos mediante RF-3.7.

 - Nombre de usuario.
 - Nombre real.
 - Localidad de origen.
 - Correo electrónico.
 - Lista de géneros de interés.
 - Descripción del usuario.
 - Contraseña.
 
RD-3.15. Nombre de usuario
: nombre de usuario que se introduce otro usuario para consultar su perfil.

 - Nombre de usuario.
 
RD-3.16. Datos de perfil de un usuario
: datos que se muestran como salida en el RF-3.8 en caso de que el nombre de usuario de entrada sea correcto.

 - Nombre de usuario
 - Nombre real
 - Localidad de origen
 - Correo electrónico
 - Lista de géneros de interés 
 - Descripción del usuario
 
 Si el nombre de usuario de entrada es incorrecto (no está en el sistema) se mostrara un mensaje que lo indique.

## Requisitos semánticos

RS-3.1
: El nombre de usuario no podrá ser uno ya registrado en el sistema. Este requisito afecta a RF-3.1, RF-3.3, RD-3.1, RD-3.2 y RD-3.4.

RS-3.2
: El correo electrónico debe estar en un formato válido. Este requisito afecta a RF-3.1, RF-3.3, RD-3.1, RD-3.2 y RD-3.4.

RS-3.3
: La contraseña deberá contener al menos un carácter especial y un número. Este requisito afecta a RF-3.1, RF-3.3, RD-3.1, RD-3.2 y RD-3.4.

RS-3.4
: La lista de géneros debe estar incluida en los géneros registrados en el sistema. Este requisito afecta a RF-3.1, RF-3.3, RD-3.1, RD-3.2 y RD-3.4.
