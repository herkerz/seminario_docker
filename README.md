
# Proyecto de extracción de y carga de información con Airflow

Este proyecto tiene como objetivo automatizar la extracción de información económica a través de una API que baja información de FRED y luego realizar su carga a una base de datos. 
Para ello se crea un DAG de Airflow, programado para correr el primer dia de cada mes.

El proyecto cuenta con las siguientes etapas:

    *1) A través de una API se accede a la información del sitio web [FRED](https://fred.stlouisfed.org/) y se extrae la información sobre la serie deseada y se resguarda en un archivo CSV.

    *2) La información guardada en el archivo CSV es leída y cargada a una base de datos SQLite, creando la tabla necesaria en el momento en caso de no existir.


# Instalación:

Bajar o clonar la siguiente [URL](https://github.com/herkerz/seminario_docker)

# Ejecución  

Para ejecutar el proceso debe correrse el bash 'contrl_env.sh' el cual en base al 'docker-compose.yml' ejecuta las etapas antes mencionadas.

    *./control_env.sh start --> corre los dockers
    *./control_env.sh stop --> para los dockers