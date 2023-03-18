from django import forms


class addForm(forms.Form):
    nombre= forms.CharField(label="nombre", max_length=100)
