from django import forms 

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True)
    email = forms.CharField(label= 'Email', required= True, widget=forms.EmailInput)
    contenido = forms.CharField(label= 'Contenido', widget=forms.Textarea)
