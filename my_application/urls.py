from django.urls import path
from . import views

app_name = 'my_application'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('form/', views.form, name='form'), 
    path('<int:user_id>/', views.detail, name='detail')
]
