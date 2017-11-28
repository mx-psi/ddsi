## Instalación en GNU/Linux
La instalación requiere aceptar primero la **clave pública** de Cédric
Krier (<cedric.krier@tryton.org>), que está disponible desde los servidores
de claves de GNU.

``` bash
gpg --search-keys B7DA61DEEDF05DCF
```

Una vez añadida, existen paquetes para las distintas distribuciones de GNU/Linux. En particular:

- **Archlinux**: `tryton` para el cliente, `trytond`, el servidor.
- **Ubuntu**: `tryton-client` para el cliente, `tryton-server` para el servidor

``` bash
sudo aura -A install tryton trytond
sudo apt install tryton-client tryton-server
```

## Instalación

Dependiendo del sistema pueden crearse un grupo y un usuario específicos para
`tryton`,

``` bash
Adding tryton group...
Adding tryton user...
```

La configuración de servidor estará disponible en `/etc/trytond.conf` 
y los módulos pueden instalarse usando `pip` o el gestor de paquetes.

``` bash
Note:
- Tryton modules can be installed using pip2,
  e.g. 'pip2 install trytond-party'.
- Configure Tryton using the config file
  /etc/trytond.conf.
- See the Tryton documentation at http://doc.tryton.org
```

## Servidor
La **configuración** del servidor se controla desde `/etc/trytond.conf` y una
completa descripción de la sintaxis posible puede encontrarse en la
[*documentación de tryton*](http://doc.tryton.org/3.8/trytond/doc/topics/configuration.html).

Por ejemplo, puede marcarse sobre qué dirección escuchará el servidor,
nombre del host y qué dirección usará como raíz para sus datos.

``` bash
[jsonrpc]
listen = localhost:8000
hostname =
data = /var/www/localhost/tryton
```

## Cliente
Al arrancar el cliente se nos ofrece elegir a qué servidor y con qué
usuario nos queremos conectar.

![Pantalla de selección de perfil.](Presentacion/tryton-profile.png){width=250px height=250px}

En particular se nos ofrece un servidor de prueba.
