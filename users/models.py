from operator import truediv
from turtle import up
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password=None): #y si queremos que no traiga al registrar el apellido le ponemos APELLIDO = NONE O BORRARLO
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email,nombres,apellidos,password):  #y si queremos que no traiga al registrar el apellido le ponemos APELLIDO = NONE O BOORARLO
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario',unique=True,max_length=100)
    email = models.EmailField('Correo Electronico',max_length=254,unique=True)
    nombres = models.CharField('Nombre',max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellido',max_length=200,blank=True,null=True)
    imagen = models.ImageField('Imagen de Perfil',upload_to='perfil/',max_length=200,blank=True, null=True,default='default.jpg')
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default= False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos'] #aca son las cosas que te van a pedir al registrarte

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
