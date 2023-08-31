# Challenge interno
Solución creada para el desafío interno de SCM Latam. 

Consiste en una API que generera reportes de marcas, los cuales podrán ser consultados y posteriormente descargados en formato PDF.

## Tabla de Contenidos
- [Requisitos previos](#requisitos-previos)
- [Estrcutura del proyecto](#estructura-del-proyecto)
- [Configuración de Docker Compose](#configuración-de-docker-compose)
- [Variables de entorno](#variables-de-entorno)
- [Instrucciones de instalación ](#instrucciones-de-instalación)
- [Uso](#uso)

## Requisitos previos
Para la utilización de esta solución asegurate de tener instalado docker en tu sistema.

https://www.docker.com/products/docker-desktop/

## Estructura del proyecto

Una vez que nos posicionemos en el directorio del proyecto, nos prodremos encontrar la siguiente estructura:
  ```
   interChallenge/
    ├── api/
    │   ├── Dockerfile
    │   ├── crud.py
    │   ├── database.py
    │   ├── main.py
    │   ├── models.py
    │   ├── requirement.txt
    │   ├── shcemas.py
    │
    ├── backend/
    │   ├── Dockerfile
    │   ├── database.py
    │   ├── main.py
    │   ├── models.py
    │   ├── requirement.txt
    │
    ├── docker-compose.yml
    ├── init.sql
    ├── README.md
    └── .gitignore
   ```
   - api: Es un aplicación desarrollada en FastAPI y SQLAlchemy para la generación de endpoints, los cuales se utilizan para las principales funcionalidades de esta solución.
     - Dockerfile: Podremos encontrar las principales instrucciones para la construcción de la imagen de este componente. Indicamos el directorio de trabajo, instalamos la dependecias necesarias,
       exponemos el puerto y damos accesos.
     - crud.py: Archivo python que cuenta con las funcionalidades de los endpoints.
     - database.py: En este archivo es el encargado de conectarnos con la base de datos.
     - main.py: Archivo que maneja los endpoints para generación, consulta y descarga de los reportes.
     - models.py: Contiene los modelos de SQLAlchemy para la interación con la base de datos.
     - requirement.txt: Archivo que contiene las depencias que necesitamos.
   - backend: Es un script el cual se encarga de consultar los estados de los reportes, para luego generer el documento PDF con Reportlab.
     - Dockerfile: Podremos encontrar las principales instrucciones para la construcción de la imagen de este componente. Indicamos el directorio de trabajo, instalamos la dependecias necesarias y damos accesos.
     - database.py: En este archivo es el encargado de conectarnos con la base de datos.
     - main.py: Script principal que consulta la base de datos para la generación de los reportes.
     - models.py: Contiene los modelos de SQLAlchemy para la interación con la base de datos.
     - requirement.txt: Archivo que contiene las depencias que necesitamos.
   - init.sql: Script inicial para la inicialización de la base de datos MySQL.
   - docker-compose: Archivo para orquestar nuestros contenedores en Docker.

## Configuración de Docker Compose
Nuestro archivo docker-compose.yml será el encargado de orquestar nuestros contenedores para que nuestra aplicación funcione.

A contuación se dará una explicación de la configuraciones dentro del docker-compose de cada uno de los servicios.

  1. mysql:
     - Descargamos una imagen oficial de mysql desde DockerHub, en este caso, estaremos utilizando la versión 8.0.26 y expondremos el puerto
      por defecto de mysql 3306.
      - Aquí indicamos las variables de entorno para las configuraciones iniciales, como lo son la contraseña
      del usuario root, usuario no root, su respectiva contraseña y la base de datos inicial.
      - Tambien haremos uso del script de inicialización antes mencionado, que nos creará las tablas de nuestro proyecto. Esto lo montamos como un volumen dentro 
      de nuestro contenedor. Además, de igual manera, indicaremos otro volumen para que nuestros datos persistan en la base de datos si es que el contenedor
      se apaga.
      - Por otra parte, y como configuración adicional, se le indicó una red para que pueda interactuar con los demás componentes de la aplicación.
      - Finalmente, indicamos un healthcheck para que sepamos cuando la base de datos este lista para ser utilizada.
        
  2. api:
     - Para la creación de la imagen de api, utilizaremos el Dockerfile ubicado dentro del directorio. Esto lo realizamos indicando el contexto al docker-compose
     - Indicamos que este componente depende de que el componente de la base de datos este en funcionamiento.
     - Al igual que la base de datos, indicamos el puerto que utilizaremos, la red y sus respectivas variables de entorno.
     - Además indicamos un volumen, el cual es compartido con el componente backend, esto para el manejo de los archivos generados para los reportes.
       
  3. backend:
       - Para la creación de la imagen, de igual menera que con api, utilizaremos el Dockerfile ubicado en su respectivo directorio e indicamos su contexto.
       - Este componente igual depende de que la base de datos este funcionando, pero en este caso se asegura de que el servicio este "saludable".
       - Tambien indicamos la red, el volumen compartido y sus variables de entorno.
         
## Variables de entorno
Debemos crear un archivo .env en la raiz del proyecto para que docker-compose sepa de donde sacar las varibles de entorno.

```
# mysql
MYSQL_ROOT_PASSWORD=contraseña_usuario_root
MYSQL_DATABASE=bd_inicial
MYSQL_USER=usuario_no_root
MYSQL_PASSWORD=contraseña_usuario_no_root

#api and backend
db_user=usuario_no_root
db_password=constraseña_usuario_no_root
db_host=mysql
db_port=3306
db_name=bd_inicial
```

Es importante que el db_host sea "mysql" ya que hace referencia al servicio de nuestra base de datos dentro de la red que se configuró. 

## Instrucciones de instalación 

1. Debemos clonar el repositorio con el siguiente comando:
   ```
   git clone https://github.com/nicolastve/internChallenge.git
   ```
2. Crear el archivo de las variables de entorno:
   ```
    interChallenge/
      ├── api/
      ├── backend/
      ├── .env
      ├── docker-compose.yml
      ├── init.sql
      ├── README.md
      └── .gitignore
   ```
3. Levantar los contenedores con docker compose:
   ```docker
   docker-compose up
   ```
4. Bajar los contenedores:
   ```docker
   docker-compose down
   ```
## Uso
Para la generación de reportes, debemos tener información en nuestra base de datos. Por lo que es importante cargar información a las 3 tablas.

- Tabla de usuarios:
  
  ![image](https://github.com/nicolastve/internChallenge/assets/108106098/1af07fcb-7a3b-4b3e-aadb-0d26f240af2a)

- Tabla de entrys:
  
  ![image](https://github.com/nicolastve/internChallenge/assets/108106098/0a0b8cdd-248c-4091-b842-a8e699209262)

- Tabla de exits:
  
  ![image](https://github.com/nicolastve/internChallenge/assets/108106098/e3d19066-2171-4d74-9a61-205423135b40)

Luego podemos hacer una petición post al endpoint de generación de reportes (/generate). Donde debemos indicar el rango de fechas del reporte:

![image](https://github.com/nicolastve/internChallenge/assets/108106098/d8deec80-1582-486d-ad89-5a61ddaef1d1)

Nos dará como resultado, los datos del reporte generado:
```json
  {
    "id": 1,
    "start_date": "2023-08-01",
    "end_date": "2023-08-02",
    "status": "Generated"
  }
```
Una vez hecha la petición, el backend tomará esta solicitud y al ver que el reporte tiene el estado de "Generated", cambiará el estado a "Proccesing"
y se pondrá a generar el reporte con reportlab, para posteriomente dejar el documento en el volumen compartido que mencionamos antes. Posterior a esto,
cambiará el estado a "Finalized" e indicará a la base de datos la ruta en donde se encuentra el reporte, el cual, ya puede ser descargado.

![image](https://github.com/nicolastve/internChallenge/assets/108106098/f1273efe-22f6-480f-a338-0e6056b17ded)

Para verificar que el reporte esta finalizado, podemos hacer una petición get al endpoint de consulta de reportes (/all_reports)

![image](https://github.com/nicolastve/internChallenge/assets/108106098/7eb4c53c-f946-49ad-a38b-10469c225aa7)

que nos dará una lista de todos los reportes generados y sus estados:

```json
  [
    {
      "id": 1,
      "start_date": "2023-08-01",
      "end_date": "2023-08-02",
      "status": "Finalized"
    }
  ]
```

Para descargar, debemos utilizar el id del reporte que queremos descargar y hacer una petición get al endpoint /download

![image](https://github.com/nicolastve/internChallenge/assets/108106098/55f33266-4e4e-47dc-b998-ada5cb4e9005)

Como resultado:

![image](https://github.com/nicolastve/internChallenge/assets/108106098/5c254cee-4dd2-4ae2-9c8e-613271e703e3)



