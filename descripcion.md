# Descripción del problema

El sistema consiste en la implementación de una web que registre valoraciones de productos culturales así como datos que permitan su clasificación y la obtención de recomendaciones a los usuarios. Consta de 4 subsistemas que implementan funcionalidades complementarias: 

- productos culturales,
- entidades creadoras y géneros,
- usuarios y
- valoraciones.

Los **productos culturales** constan de un nombre, tipo, fecha de publicación, identificador, un producto cultural padre, otros productos culturales asociados, una serie de géneros a las que pertenece y un conjunto de entidades creadoras asociadas. El subsistema encargado de los mismos debe permitir:

- añadir la información asociada a productos culturales nuevos o existentes,
- consultar la información asociada a un producto cultural y
- buscar productos culturales en función de cualquier dato asociado.

El subsistema permitirá en concreto añadir películas, libros, series (añadiendo los capítulos individuales) y música (añadiendo obras concretas clasificadas en discos) y consultar la información de los mismos.

Una **entidad creadora** es una persona, colectivo u organización que ha participado en la creación de un producto cultural. Cada entidad creadora puede estar asociada a cualquier cantidad de productos culturales. Una entidad creadora puede formar parte de otras. Las entidades creadoras constan de nombre, tipo y de un rol asociado a cada producto cultural. Una entidad creadora puede haber recibido uno o varios premios o reconocimientos asociados a un producto cultural concreto.

Los **géneros** constan de un nombre y un identificador y tienen una serie de subgéneros asociados. Pueden consultarse todos los productos culturales asociados a un género o a una combinación de los mismos. El subsistema encargado de géneros y entidades creadoras debe permitir:

- añadir la información asociada a géneros o entidades creadoras,
- consultar los productos culturales asociados a un género o entidad creadora,
- mostrar datos agregados sobre las valoraciones de los productos culturales asociados a un género o entidad,
- consultar los premios de una entidad creadora concreta y
- consultar la jerarquía de entidades creadoras.

Cada **usuario** estará representado en el sistema por un nombre de usuario, datos de identificación, géneros o categorías de interés y una descripción. Los usuarios podrán:

- darse de alta o de baja en el sistema,
- modificar sus datos,
- consultar las recomendaciones dadas por el sistema basadas en sus categorías de interés y sus valoraciones en productos culturales similares y
- ser notificado de la salida de nuevos productos culturales que podrían interesarle.

Una **valoración** estará compuesta de una puntuación numérica y una reseña en texto opcional que justifique tal puntuación. Tendrá asociada una puntuación basada en la opinión del resto de usuarios sobre su utilidad. Este subsistema permitirá que los usuarios:

- escriban valoraciones y reseñas asociadas a una edición concreta de un producto cultural, 
- consulten las valoraciones de otros usuarios individualmente o como datos agregados. En concreto permitirá consultar una media de las valoraciones o un histograma de las mismas y clasificar los productos culturales en función de estas
- indiquen si una valoración es útil o no y
- reporten valoraciones inapropiadas.


