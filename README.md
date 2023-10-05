# MINIBLOG DE AGOS

![Kirby is here](https://i.pinimg.com/564x/3f/78/fd/3f78fd0cd0e8b2ee0b10eeaca003af96.jpg)

Un miniblog que permite a los usuarios crear y compartir sus propios posteos.

## Requisitos

- Docker
- Docker Compose

## Configuración

1. Clona este repositorio: `git clone git@github.com:quevedoagostina/AGOS_MiniBlog.git`
2. Ve al directorio del proyecto: `cd AGOS_MiniBlog`

## Uso

Para ejecutar la aplicación en un contenedor Docker, sigue estos pasos:

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

2. En el directorio del proyecto, ejecuta el siguiente comando para construir y ejecutar los contenedores:

   ```bash
   docker-compose up --build
   ```

   Esto iniciará tu aplicación Flask en un contenedor Docker junto con un servidor MySQL en otro contenedor. La aplicación estará disponible en http://localhost:5000/.

3. Para detener los contenedores, puedes presionar `Ctrl+C` en la terminal o ejecutar:

   ```bash
   docker-compose down
   ```

Con estos pasos, deberías poder ejecutar tu aplicación Flask en Docker utilizando MySQL como base de datos. Asegúrate de que Docker esté instalado en tu sistema antes de ejecutar estos comandos.

## Aclaración importante

Hay un init_db.py para meter las categorías en la base de datos, para agregarlas ejecuta el script init_db.py. Desde la terminal, utiliza el siguiente comando: `docker-compose exec app python init_db.py`. Esto ejecutará el script dentro del contenedor de la aplicación.