from django.urls import path
from login.views import index, cadastro

urlpatterns = [
    path('', index),
    path('cadastro/', cadastro)
]