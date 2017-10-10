## Requisitos funcionales

RF-3.1
: **Alta de usuario**: un usuario puede de darse de alta en el sistema.

    - E: RD-3.1
    - A/M: RD-3.2
    - S:
 
RF-3.2
: **Baja de usuario**: un usuario es capaz de darse de baja del sistema.

    - E: RD-3.3
    - A/M: RD-3.2
    - S:
 
RF-3.3
: **Modificar perfil**: los usuarios son capaces de modificar sus datos en el sistema.

    - E: RD-3.4
    - A/M: RD-3.2
    - S:
 
RF-3.4
: **Consultar recomendaciones**: los usuarios son capaces de consultar recomendaciones dadas por el sistema basadas en sus categor�as de inter�s y sus valoraciones en productos culturales similares

    - E: RD-3.5
    - A/M: RD-3.2 {Falta requisito de las valoraciones asociadas al usuario}
    - S: RD-3.6
 
RF-3.5
: **Notificar de productos interesantes**: los usuarios recibir�n notificaciones de la salida de nuevos productos culturales que podr�an interesarles.

    - E:
    - A/M: RD-3.2
    - S: RD-3.7

RF-3.6
: **Log in de usuario**: identificaci�n del usuario en el sistema necesaria para acceder a los requisitos funcionales RF-3.2, RF-3.3, RF-3.4 y RF-3.5.

    - E: RD-3.8
    - A/M:
    - S:

## Requisitos de datos

RD-3.1
: **Datos de entrada de la alta de un usuario**: datos que debe introducir el usuario que quiera darse de alta en el sistema.

 - Nombre de usuario (una cadena de hasta 20 caracteres no vac�a)
 - Nombre real (una cadena de hasta 60 caracteres no vac�a)
 - Localidad de origen (una cadena de hasta 20 caracteres no vac�a)
 - Correo electr�nico (una cadena de hasta 40 caracteres no vac�a)
 - Lista de g�neros de inter�s 
 - Descripci�n del usuario (una cadena de hasta 300 caracteres)
 - Contrase�a (una cadena de al menos 6 caracteres y de hasta 20 como m�ximo)
 
RD-3.2
: **Datos de un usuario en el sistema**: datos que almacenar� el sistema de un usuario.

 - Nombre de usuario (una cadena de hasta 20 caracteres no vac�a)
 - Nombre real (una cadena de hasta 60 caracteres no vac�a)
 - Localidad de origen (una cadena de hasta 20 caracteres no vac�a)
 - Correo electr�nico (una cadena de hasta 40 caracteres no vac�a)
 - Lista de g�neros de inter�s 
 - Descripci�n del usuario (una cadena de hasta 300 caracteres)
 - Contrase�a (una cadena de al menos 6 caracteres y de hasta 20 como m�ximo)
 
RD-3.3
: **Bot�n darse de baja**: bot�n que debe pulsar el usuario para darse de baja del sistema.

 - Bot�n Darse de baja
 
RD-3.4
: **Modificar datos de perfil de usuario**: datos del usuario nuevos.

 - Nombre de usuario (una cadena de hasta 20 caracteres no vac�a)
 - Nombre real (una cadena de hasta 60 caracteres no vac�a)
 - Localidad de origen (una cadena de hasta 20 caracteres no vac�a)
 - Correo electr�nico (una cadena de hasta 40 caracteres no vac�a)
 - Lista de g�neros de inter�s 
 - Descripci�n del usuario (una cadena de hasta 300 caracteres)
 - Contrase�a (una cadena de al menos 6 caracteres y de hasta 20 como m�ximo)
 
 Solo se modificar�n los datos rellenados con las restricciones.

RD-3.5
: **Bot�n consultar recomendaciones**: bot�n que sirve para obtener las recomendaciones basadas en tu perfil de usuario.

 - Bot�n "Recomendaciones"
 
RD-3.6
: **Recomendaciones al usuario**: recomendaciones generadas por el sistema basadas en los datos del usuario.

 - Lista de productos culturales recomendados

RD-3.7
: **Notificaci�n de productos culturales**: aviso de nuevos productos culturales de inter�s.

 - Producto cultural estrenado
 
RD-3.8
: **Nombre de usuario y contrase�a**:

 - Nombre de usuario
 - Contrase�a

## Requisitos sem�nticos

RS-3.1
: El nombre de usuario no podr� ser uno ya registrado en el sistema.

RS-3.2
: El correo electr�nico debe estar en un formato v�lido.

RS-3.3
: La contrase�a deber� contener al menos un car�cter especial y un n�mero.

RS-3.4
: La lista de g�neros debe estar incluida en los g�neros registrados en el sistema.
