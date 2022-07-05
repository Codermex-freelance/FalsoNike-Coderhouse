from datetime import datetime
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime  import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from users.forms import FormularioUsuario
from users.models import Usuario
from django.urls import reverse_lazy,reverse



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        print('1')
        if form.is_valid():
            print('2')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print('3')
                login(request, user)
                return redirect('/')#redireccionar mi vista
            else:
                print('4')
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            print('5')
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'index.html', context = context)
    else:
        print('6')
        print(request.method)
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

class RegistrarUsuario(CreateView):
    model =  Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('index')
        else:
            return render(request,self.template_name,{'form':form})

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.user.is_authenticated and request.user.is_superuser:
        print(request.user.username)
        return render(request, 'contact.html')
    else:
        return redirect('login')









