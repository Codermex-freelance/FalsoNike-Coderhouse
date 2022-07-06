
from django.shortcuts import render,redirect
from Nike.models import indumentarias,calzados,accesorios
from django.views.generic import DetailView, UpdateView, DeleteView,CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from users.models import Usuario
from django.contrib.auth.models import User

class Detalle_User(DetailView):
    model= Usuario
    template_name= 'usr.html'

    def get_success_url(self):
        return reverse ('usr',kwargs={'pk':self.object.pk})

class Editar_User (UpdateView):
    model= Usuario
    template_name= 'users_editar.html'
    fields= ['username','email','nombres','apellidos','linkedin','imagen']

    def get_success_url(self):
        return reverse ('index')

class Eliminar_User(DeleteView):
    model= Usuario
    template_name= 'users_eliminar.html'

    def get_success_url(self):
        return reverse ('index')

#--------------------INFO DE LA WEB Y LOS CREADORES---------------------------
def sobre_nosotros(request):
    return render(request, 'Sobre_mi.html')
#--------------------------------------CRUD DE INDUMENTARIAS--------------------------------------------------------------

class indumentaria_view(ListView):
    model = indumentarias
    print('paso por aca')
    template_name= 'indumentaria.html'
    queryset = indumentarias.objects.filter(is_active = True)

class Crear_indumentaria(LoginRequiredMixin, CreateView):
    model = indumentarias
    template_name = 'create_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('indumentarias-detalle',kwargs={'pk':self.object.pk})

class Editar_indumentarias (UpdateView):
    model= indumentarias
    template_name= 'indumentarias_editar.html'
    fields= '__all__'

    def get_success_url(self):
        return reverse ('index')

class Eliminar_indumentarias(DeleteView):
    model= indumentarias
    template_name= 'indumentarias_eliminar.html'

    def get_success_url(self):
        return reverse ('Indumentarias')

class Detalle_indumentarias(DetailView):
    model= indumentarias
    template_name= 'indumentarias_detalle.html'


def Remeras(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 1)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Pantalones(request):
    print('paso por aca')
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 2)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Camperas(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 3)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

def Buzos(request):
    print(request.method)
    productos = indumentarias.objects.filter(categoria = 4)
    context = {'productos':productos}
    return render(request, 'indumentaria.html', context=context)

#--------------------------------------CRUD DE CALZADOS--------------------------------------------------------------
class crear_productos_calzados(LoginRequiredMixin, CreateView):
    model = calzados
    template_name = 'create_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('calzado-detalle',kwargs={'pk':self.object.pk})

class Editar_calzado (UpdateView):
    model= calzados
    template_name= 'calzado_editar.html'
    fields= '__all__'

    def get_success_url(self):
        return reverse ('index')

class Eliminar_calzado(DeleteView):
    model= calzados
    template_name= 'calzado_eliminar.html'

    def get_success_url(self):
        return reverse ('ZapatillaDeportiva')

class Detalle_calzado(DetailView):
    model= calzados
    template_name= 'calzado_detalle.html'

def ZapatillaDeportiva(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 1)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def ZapatillaComunes(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 2)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def Botines(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 3)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

def Ojotas(request):
    print(request.method)
    productos = calzados.objects.filter(categoria = 4)
    context = {'productos':productos}
    return render(request, 'calzado.html', context=context)

#--------------------------------------CRUD DE ACCEDORIOS--------------------------------------------------------------
class crear_productos_accesorios(LoginRequiredMixin, CreateView):
    model = accesorios
    template_name = 'create_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('accesorios-detalle',kwargs={'pk':self.object.pk})

class Editar_accesorios (UpdateView):
    model= accesorios
    template_name= 'accesorios_editar.html'
    fields= '__all__'

    def get_success_url(self):
        return reverse ('index')

class Eliminar_accesorios(DeleteView):
    model= accesorios
    template_name= 'accesorios_eliminar.html'

    def get_success_url(self):
        return reverse ('Accesorios')

class Detalle_accesorios(DetailView):
    model= accesorios
    template_name= 'accesorios_detalle.html'

def Pelota(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 1)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Pulseras(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 2)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Cantiplora(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 3)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Anteojos(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 4)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Muñequeras(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 5)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Bolsos_Mochilas(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 6)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

def Llaveros(request):
    print(request.method)
    productos = accesorios.objects.filter(categoria = 7)
    context = {'productos':productos}
    return render(request, 'accesorio.html', context=context)

#------------------------------BUSQUEDA GENERAL--------------------------------
def buscar_productos_indumentarias(request):
    productos = []
    producto_search = indumentarias.objects.filter(nombre__contains=request.GET["search"])
    calzado_search = calzados.objects.filter(nombre__contains=request.GET["search"])
    accesorio_search = accesorios.objects.filter(nombre__contains=request.GET["search"])
    for x in producto_search:
        productos.append(x)
    for x in calzado_search:
        productos.append(x)
    for x in accesorio_search:
        productos.append(x)
    if productos:
        context = {"productos": productos}
    else:
        context = {"errors": "No se encontro el producto"}
    return render(request, "search_product.html", context=context)

