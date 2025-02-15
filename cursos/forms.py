from django import forms
from .models import Contactos

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = '__all__'

