---
title: Descripción del sistema
date: DDSI
lang: es
fontsize: 12pt
geometry: margin=1in
---

# Descripción del problema

El sistema consiste en la implementación de una web que registre valoraciones de productos culturales así como datos que permitan su clasificación y la obtención de recomendaciones a los usuarios.

Los productos culturales constan de un nombre, ediciones o versiones, otros productos culturales asociados y una serie de géneros o categorías a las que pertenece. Cada edición o versión consta de fecha de publicación, identificador y un conjunto de entidades creadoras asociadas. El sistema debe permitir consultar la información asociada a un producto cultural y buscar productos culturales en función de cualquier dato asociado.

Una entidad creadora es una persona, colectivo u organización que ha participado en la creación de un producto cultural. Cada entidad creadora puede estar asociada a cualquier cantidad de productos culturales. Una entidad creadora puede formar parte de otras. Las entidades creadoras constan de nombre, tipo y de un rol asociado a cada producto cultural.

Los géneros se identifican por un nombre y tienen una serie de subgéneros asociados. Pueden consultarse todos los productos culturales asociados a un género o a una combinación de los mismos.

Cada usuario estará representado en el sistema por un nombre de usuario, datos de identificación, géneros o categorías de interés y una descripción. Los usuarios podrán escribir valoraciones y reseñas asociadas a una edición concreta de un producto cultural y estas podrán ser consultadas por otros usuarios individualmente o como datos agregados (por ejemplo consultando una media de las valoraciones o un histograma de las mismas).

<!--Los usuarios podrán añadir productos culturales o versiones de las mismas en el caso de que no existieran ya en el sistema o completar la información asociada en caso de que esta sea incompleta.-->

Una valoración estará compuesta de una puntuación numérica y una reseña en texto opcional que justifique tal puntuación.



