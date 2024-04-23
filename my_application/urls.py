from django.urls import path
from . import views

urlpatterns = [
    path('my_application/', views.bienvenida, name='my_application')
]
