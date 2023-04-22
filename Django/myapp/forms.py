from django import forms


class addForm(forms.Form):
    nombre= forms.CharField(label="nombre", max_length=100)
    email= forms.EmailField(label="email", max_length=100)
    edad = forms.IntegerField(label="edad")
    genero = forms.ChoiceField(label="genero", choices=[("M", "Masculino"), ("F", "Femenino")])
    mensaje = forms.CharField(label="mensaje", max_length=250)
