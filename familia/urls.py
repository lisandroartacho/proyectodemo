from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('miembro-de-familia/<str:pk>', views.miembro_de_familia, name='familiar'),
]