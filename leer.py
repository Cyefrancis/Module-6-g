# al correr "python manage.py runserver" va a dar un error 404 en la barra de navegacion debes agregar /my_application/
# al final de la direccion para que se despliege el mensaje

#Identifique los diferentes archivos creados por Django al crear un proyecto y una aplicación. Describa en
#palabras simples la utilidad de cada script.
"""
    el comando python django-admin startproject "nombreDeProjecto" creara 6 archivos y una carpeta con el nombre de tu proyecto
    -manage.py

        este archivo se ocupa mas como una utilidad de la linea de comandos te deja interactuar con el proyecto de varias formas

    -__init__.py

        le dice a python que este directorio deberia considerarse un package
    
    -asgi.py

        un entry-point para los servers web compatibles ASGI para usarlos en tu proyecto 
    
    -settings.py

        es el archivo de configuracion del proyecto 
    
    -urls.py

        las declaraciones de urls para el proyecto django, como una tabla de contenidos de tu sitio
    
    -wsgi.py

        un entry-point para los servers web compatibles WSGI para usarlos en tu proyecto
"""
"""
    el comando python manage.py startapp "nombreDeApp" creara 2 carpetas una del proyecto y la otra de las migraciones ademas 
    de 6 archivos 

    -__init__.py
        
        hace lo mismo que el de arriba

    -admin.py

        en este archivo es donde registras los modelospara hacerlos accesibels en la interfaz de admin de django

    -apps.py

        contiene la cofiguracion de la app, aqui puedes definir los metadatos
    
    -models.py

        aqui defines los modelos de django estos representan la estructura de los datos de la aplicacion

    -tests.py

        en este archivo escribes los test para la aplicacion

    -views.py

        este archivo contiene las funciones de vista(controladores) que manejan las request HTTP y devuelve las HTTP responses
        tambien interactua  con los modelos para manipular datos y renderizar las templates

    -urls.py <-- este archivo lo tuve que agregar manualmente

        contiene los patrones  URL para la aplicacion define el mapeo entre URLs y Views que manejan las HTTP

"""