
# Playground (Proyecto final): Pugliese Leandro, Juan Siro, Lucas Maciel.
1. Todos los Template Heredan de nuestro template padre "T01-view.html".

2. Las clases en models son: Usuario, Publicación, Comentario.

3. Usuario.
3A. Formulario de creación de Usuario: Ingresar en "Ingrese"/"Crear usuario".
3B. Formulario para iniciar sesión: Ingresar en "Ingrese"(Ingresar username y contraseña). (Login).
Nota: Usuarios para prueba:
    - Username: admin / Contrtaseña: playground (Super Usuario) (Puede publicar y modificar los tipos para otorgar permisos de publicación o denegarlos).
    - Username: Marty / Contrtaseña: playground (Autor) (Puede publicar).
    - Username: Wendy / Contrtaseña: playground (Lector) (No puede publicar).
3C. Formulario de modificación de los datos del usuario: Abrir el menú desplegable haciendo click en el username y elegir la opción "Modificar datos".
Nota: Para optimizar el espacio de guardado de la Base de Datos solo se guarda la imagen del avatar actual, las anteriores se eliminan.
3D. Dentro del menú desplegable mencionado en el punto anterior puede consultar todas las publicaciones y comentarios realizados por el usuario en la opción "Tu actividad"
3E. Para el cerrar sesión la opción se encuentra en el mismo menú desplegable ya mencionado, haciendo click en "Cerrar sesión". (Logout)

4. Publicación.
4A. Sin estar logueado no podras visualizar el contenido de las publicaciones, ni crear una publicación.
4B. Formulario de Publicación: Ingresar en "Noticias"/"Hacer Publicacion".
Nota: Se incorporó la posibilidad de modificar el texto y agregar imagenes dentro del cuerpo de la publicación con el CKEDITOR.
4C. Formulario de Busqueda en la DB: Ingresar a "Noticias"/"Buscar"(Escribir título de la noticia).
Nota: El criterio de busqueda es el título de la publicación (se puede utilizar solo parte del título para la busqueda).
4D. Modificación de la públicacion solo esta permitido para el usuario AUTOR de la misma.
4E. Formulario de edición de la publicación: Ingresar a la publicación que quiera editar y hacer click en "editar noticia".

5. Comentario.
5A. Formulario de Comentario: Ingresar en la publicación en la cual quiera hacer un comentario y hacer click en "Hacer un comentario".
5B. En cada publicación se visualizan los últimos 3 comentarios, en caso de querer ver la totalidad de comentarios hacerca de la publicación hacer click en "Ver comentarios".
5C. La modificación o eliminación del comentario solo esta permitido para el usuario que haya creado dicho comentario. 

6. Sobre Nosotros.
6A. Para ingresar en la sección "sobre nosotros" hacer click en el botón "Sobre nosotros" en la barra de inicio.
6B. En "Sobre nosotros" se cuenta hacerca de quienes somos los desarrolladores del proyecto y contar un poco sobre que trata el Blog.

7. Probar el blog.
7A. En el siguiente link encontrará un video demostrativo de las funcionalidades del Blog. ("link")

8. Grupo.
8A. El proyecto fue desarrollado integramente en equipo. Al no tener mucha experiencia nos pareció conveniente realizar todo en conjunto.
8B. Utilizamos esta metodología de trabajo para todos poder aprender a hacer la totalidad de la aplicación.


