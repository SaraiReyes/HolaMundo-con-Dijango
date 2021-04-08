# DJANGO

## Instalación


### comrobar que se instalo correctamente
python -m django --version

## Creación del proyecto

django-admin startproject nombreDelProyecto

### Para crear su aplicación, asegúrese de que está en el mismo directorio que el archivo manage.py y escriba este comando:

python manage.py startapp nombre2

en nombre2 modificamos:

#### views.py


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.Mi primera app.")

###  cree un archivo llamado urls.py.
###  urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

### modificaciones en la primera carpeta
####urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('nombre2.urls')),
    path('admin/', admin.site.urls),
]


## Prueba de funcionamiento

python manage.py runserver

### Si desea cambiar el puerto del servidor
python manage.py runserver 8080

### Si desea cambiar la IP del servidor, pásela junto con el puerto

python manage.py runserver 0:8000

0 es un atajo para 0.0.0.0

##### si a corrar la app obtienes un error 404
 no hay problema, dirigete a 


 http://localhost:8000/nombre2
