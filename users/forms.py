from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    """Formulario de Registro de un Usuario en la base de datos

    Variables:

        -password1:     Contraseña
        -password2:     Verificacion de la contraseña

    """

    password1 = forms.CharField(label = 'Contraseña',widget=forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmacion',widget=forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Repita su contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombres','apellidos')
        widgets = {
            'email' : forms.EmailInput (
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Correo Electronico',
                }
            ),
            'nomnbres' : forms.TextInput (
                attrs = {
                        'class' : 'form-control',
                        'placeholder' : 'Ingrese su nombre',
                }
            ),
            'apellidos' : forms.TextInput (
                attrs = {
                        'class' : 'form-control',
                        'placeholder' : 'Ingrese sus apellidos',
                }
            ),
            'username' : forms.TextInput (
                attrs = {
                        'class' : 'form-control',
                        'placeholder' : 'Ingrese su nombre de usuario',
                }
            )
        }

    def clean_password2(self):
        """
        VALIDACION DE CONTRASEÑA

        METODO QUE VALIDA QUE AMBAS CONTRASEÑAS INGRESADAS SEAN IGUALES, ESTO ANTES DE SER ENCRIPTADAS
        Y GUARDADAS EN LA BASE DE DATOS, RETORNAR LA CONTRASEÑA VALIDA

        EXCEPCIONES:
            - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseña no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user