from django import forms  
from .models import Denuncia


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia 
        fields = ['titulo', 'descripcion', 'categoria', 'estado']  

    def save(self, commit=True):
        denuncia = super().save(commit=False)  
        if commit:
            denuncia.save() 
        return denuncia