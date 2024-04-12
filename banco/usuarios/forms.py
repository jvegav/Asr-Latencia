from django import forms

from .models import Usuario


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'name',
            'phone',
            'email'
        ]
        labels = {
            'name': 'Nombre',
            'phone': 'Telefono',
            'email': 'Email',
        }