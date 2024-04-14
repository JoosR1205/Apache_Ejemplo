
# Spotify API Integration Project

Este proyecto está diseñado para interactuar con la API de Spotify, permitiendo realizar diversas acciones como autenticación, búsqueda de nuevas lanzamientos y creación de playlist en base a generos de los nuevos lanzamientos.

## Instalación

Para comenzar a usar este proyecto, sigue estos pasos para clonar el repositorio e instalar las dependencias necesarias:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
# Agrega aquí más instrucciones si es necesario instalar dependencias adicionales
```

## Uso

A continuación, se muestran algunos ejemplos de cómo utilizar los scripts del proyecto:

```python
# Ejecuta este comando para autenticarte con la API de Spotify
python spotify_authentication.py

# Una vez autenticado, puedes probar buscar nuevos lanzamientos con:
python New_Release.py

# O puedes ejecutar el archivo principal para ver todas las funcionalidades:
python app.py
```

## Archivos

- `app.py`: Este es el archivo principal del proyecto. Coordina las interacciones entre los usuarios y las funciones disponibles en el proyecto.
- 
- `functions.py`: Este archivo contiene funciones esenciales que facilitan la interacción con la API de Spotify. Las funciones clave incluyen:

  - `check_or_create_playlist()`: Verifica si existe una playlist por su ID y, si no existe, crea una nueva con el nombre especificado. También configura la visibilidad de la playlist (pública o privada).

  - `update_playlist()`: Actualiza la playlist especificada con los nuevos lanzamientos de música basándose en géneros predefinidos. Utiliza un intervalo de tiempo para filtrar lanzamientos recientes y los agrega a la playlist. Las pistas se seleccionan comprobando los géneros de los artistas y asegurándose de que coincidan con los géneros deseados. También maneja la paginación de los resultados de la API para procesar todos los lanzamientos relevantes.

    Las funciones están diseñadas para ser utilizadas dentro de un flujo de trabajo de Apache Airflow, gestionando tareas recurrentes y manteniendo la playlist actualizada con eficiencia y precisión.

- `New_Release.py`: Este script automatiza la gestión de una playlist en Spotify para incluir nuevos lanzamientos. Se utiliza Apache Airflow para orquestar la tarea, definida en el archivo como `manage_playlist_task`. La función `manage_playlist` autentica con Spotify a través de `authenticate_spotify`, verifica la existencia de la playlist (o la crea si no existe) con `check_or_create_playlist`, y luego actualiza la playlist con la función `update_playlist`. El script está configurado para ejecutarse diariamente, asegurando que la playlist contenga siempre las últimas novedades. Este proceso hace que la playlist "New K-Releases" se mantenga actualizada y sea pública para los usuarios de Spotify.

- `spotify_authentication.py`: Maneja la autenticación del usuario con la API de Spotify. Es necesario ejecutar este script antes de realizar cualquier solicitud que requiera autenticación.

## IMAGENES
![image](https://github.com/JoosR1205/Apache_Ejemplo/assets/160549504/5c451e66-57e3-4840-986f-d0fb707dd105)
![image](https://github.com/JoosR1205/Apache_Ejemplo/assets/160549504/e00edad0-980f-4b13-9212-395ae537e73e)
![image](https://github.com/JoosR1205/Apache_Ejemplo/assets/160549504/843bea00-ab05-422a-9af5-d9cab99d3994)
