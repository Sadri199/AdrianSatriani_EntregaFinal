# Español

## Bienvenido a mi proyecto para la Entrega Final

Acá vas a encontrar toda la información sobre este proyecto. Si queres ver una demo, poder verla en este video "https://youtu.be/ZCeyivfGOUA".

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
- "Let´s Chat", un pequeño chat grupal async, si todos se van se borran los mensajes.
- "Log Out", para que puedan cerrar sesión.
- About Me, un poco de información de mi persona.

## Créditos

- Template de la página web lo tome de "https://startbootstrap.com/template/full-width-pics".
- Foto de background la tome de "https://wallpapers.com/images/featured-full/film-reel-png-wkzwgj0y9laly3vs.png".
- Favicon.ico tomado de "https://www.favicon.cc/?action=icon&file_id=1005743".
- Todo lo demás hecho por mí, Adrian Satriani.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
# English

## Welcome to my Final Test project

Here you will find all the information regarding this project. If you want to see a demo, you can check out this video "https://youtu.be/ZCeyivfGOUA".

## Installation

- You can either "git clone" or download the ".zip" with the project.
- Then you are going to need to install Python, you can get it from "https://www.python.org/downloads/".
- Once you have it installed you are going to need the "Django" module, you can install it by typing on the terminal "pip install Django".
- The rest of the modules / libraries are in "requirements.txt".

## Execution

Inside "tercera_entrega" you are going to see a file called "manage.py". Open the terminal inside that folder and type "python manage.py runserver", then you enter the URL that will appear in the terminal "http://127.0.0.1:8000/".

This page consists of 2 parts:

On one side, there is the view for an unregistered person, they can only see:

- Home, which is the landing page.
- "List of Movies" that returns the entire Database.
- About Me, which has a bit of information regarding myself.

On the other side, there is the view for logged in users, they can see:

- Home, which is the landing page.
- "List of Movies" that returns the entire Database. Authenticated users can Edit and Delete Movies.
- "Add a Movie", which lets you add a Movie to the Database.
- "My Profile", returns information of the currently logged user.
- "Edit Profile", lets the user edits its information.
- "Change Password", lets the user change their Password.
- "Let´s Chat", a small async group chat, if everybody leaves the messages disappear.
- "Log Out", so they can log out.
- About Me, which has a bit of information regarding myself.

## Credits

- Template for the entire webpage taken from "https://startbootstrap.com/template/full-width-pics".
- Background pic from "https://wallpapers.com/images/featured-full/film-reel-png-wkzwgj0y9laly3vs.png".
- Favicon.ico taken from "https://www.favicon.cc/?action=icon&file_id=1005743".
- Everything else made by me, Adrian Satriani.