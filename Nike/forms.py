from django import forms
from Nike.models import indumentarias,calzados,accesorios

class Indumentarias_form(forms.ModelForm):
    class Meta:
        model = indumentarias
        fields = '__all__'

class Calzados_form(forms.ModelForm):
    class Meta:
        model = calzados
        fields = '__all__'

class Accesorios_form(forms.ModelForm):
    class Meta:
        model = accesorios
        fields = '__all__'