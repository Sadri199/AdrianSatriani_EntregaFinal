# English
Will translate once the entire readme is finished.

# Español

# Bienvenido a mi proyecto para la Entrega Final

Acá vas a encontrar toda la información sobre este proyecto.

## Instalación

- Podes hacer un git clone o descargar el .zip con el proyecto.
- Luego vas a precisar instalar Python, lo podes descargar desde "https://www.python.org/downloads/" .
- Una vez que lo tengas instalado vas a precisar instalar el modulo de Django, esto lo podes hacer en la terminal con el comando "pip install Django".
- El resto de los módulos / librerías están en "requirements.txt".

## Ejecución

Parandote dentro de tercera_entrega vas a ver un archivo llamado "manage.py". Abris terminal dentro de esta carpeta y ejecutas "python manage.py runserver", luego entras a la URL que aparece en la terminal "http://127.0.0.1:8000/".

La web consiste de 2 partes:

Por un lado está la vista para personas no registradas, ellas podrán ver:

- Home, que es la pantalla inicial.
- "List of Movies" que devuelve toda la base de datos.
- About Me, un poco de información de mi persona.

Por otro lado está la vista para usuarios que inician sesión, ellos podrán ver:

- Home, que es la pantalla inicial.
- "List of Movies", que devuelve toda la base de datos. Los usuarios autenticados pueden editar o borrar películas.
- "Add a Movie", que permite agregar películas a la base de datos.
- "My Profile", devuelve la información del usuario registrado.
- "Edit Profile", permite editar los datos del usuario.
- "Change Password", permite cambiar la contraseña.
- "Log Out", para que puedan cerrar sesión.
- About Me, un poco de información de mi persona.

## Créditos

- Template de la página web lo tome de "https://startbootstrap.com/template/full-width-pics".
- Foto de background la tome de "https://wallpapers.com/images/featured-full/film-reel-png-wkzwgj0y9laly3vs.png".
- Favicon.ico tomado de "https://www.favicon.cc/?action=icon&file_id=1005743".
- Todo lo demás hecho por mí, Adrian Satriani.
