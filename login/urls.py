from django.urls import path
from login.views import index, cadastro

urlpatterns = [
    path('', index, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro')
]