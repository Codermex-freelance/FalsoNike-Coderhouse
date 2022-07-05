from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import ListadoUsuario

urlpatterns = [
    path('listado_usuario/',login_required(ListadoUsuario.as_view()),name='listar_usuario'),
]