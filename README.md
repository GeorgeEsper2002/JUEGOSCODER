# Proyecto final de coderhouse de Rachid Esper
# "Pagina de reseña de videojuegos"

## Acerca de la pagina:
<p>
Music blog es el nombre de la pagina web que se hizo como proyecto final para el curso de Python en Coderhouse. Esta pagina es un blog sobre musica.
</p>

<p>
Para la creacion de esta pagina, se utilizo el framework de python Django junto con algunas herramientas de html, css y javascript.<br>
Ademas, se utilizaron plantillas html que se descargaron de la pagina "Bootstra" y se modificaron para adaptarlas a las necesidades de la web.
</p>


<p>
Asimismo, para realizar pruebas, se puede usar el usuario 'jorge' cuya contraseña es:BlackPearl2023 igual al usuario para entrar al panel de administracion de django y crear o modificar objetos en la base de datos.
</p>

## Funcionamiento:

<p>
Al ejecutar el comando <strong>manage.py runserver</strong> se inicia el servidor en el localhost de la pc, en el puerto 8000 por defecto. <br>
Una vez que el servidor esta corriendo, la pagina nos redigira a la URL '/' que es el inicio, en donde se puede observar la pagina de inicio de la web.
</p>
<p>
Para movernos entre las diferentes vistas de la pagina, se puede usar la barra de navegacion situada en la parte superior de la web, teniendo en cuenta que para muchas de las vistas hace falta estar logueado. <br>
Se puede usar a modo de prueba el usuario <strong>Hola123</strong> cuya contraseña es <strong>##Rachid123</strong><br>
De ser necesario, se puede crear un nuevo usuario desde la opcion en la barra de navegacion llamada "register" que solo sera visible si no se esta logueado.
</p>
<p>
La pagina en si esta compuesta de una sola aplicacion
<strong>misjuegos</strong>:

Para poder hacer posteos sobre los juegos debemos estar logueados o en caso contrario registrar un usuario.
Los campos al rellenar para hacer un post son:
<li> Titulo
<li> Estudio
<li> Tematica
<li> Fecha de lanzamiento
<li> Descripcion
<li> Imagen (del juego)    
</p>
