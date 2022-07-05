from django.db import models


class indumentarias(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    talle = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="indumentaria",null=True)
    categoria = models.ForeignKey('Categoria_Indumentaria', on_delete=models.CASCADE, related_name='Nike')

    class Meta:
        verbose_name = 'indumentaria'
        verbose_name_plural = 'indumentarias'

    def __str__(self):
        return F'Producto {self.nombre} cuesta un total de ${self.precio}'

class calzados(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    talle = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="calzado",null=True)
    categoria = models.ForeignKey('Categoria_Calzado', on_delete=models.CASCADE, related_name='Nike')

    class Meta:
        verbose_name = 'calzado'
        verbose_name_plural = 'calzados'

    def __str__(self):
        return F'Producto {self.nombre} cuesta un total de ${self.precio}'

class accesorios(models.Model):
    codigo_barra = models.CharField(max_length=40, unique = True)
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    color = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="accesorio",null=True)
    categoria = models.ForeignKey('Categoria_Accesorio', on_delete=models.CASCADE, related_name='Nike')#une con la tabla categoria y me muestra un listado

    class Meta:
        verbose_name = 'accesorio'
        verbose_name_plural = 'accesorios'

    def __str__(self):
        return F'Producto {self.nombre} cuesta un total de ${self.precio}'

class Categoria_Indumentaria(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria_Indumentaria'
        verbose_name_plural = 'Categoria_Indumentarias'

    def __str__(self):
        return self.name

class Categoria_Calzado(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria_Calzado'
        verbose_name_plural = 'Categoria_Calzados'

    def __str__(self):
        return self.name

class Categoria_Accesorio(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria_Accesorio'
        verbose_name_plural = 'Categoria_Accesorios'

    def __str__(self):
        return self.name

