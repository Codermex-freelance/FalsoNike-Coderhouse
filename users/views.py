from datetime import datetime
from django.http import HttpResponseRedirect,request
from django.shortcuts import render, redirect
from datetime  import datetime

from django.views.generic import CreateView,ListView,UpdateView,DeleteView

from users.forms import FormularioUsuario,FormularioLogin
from users.models import Usuario
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuario.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo = True)


