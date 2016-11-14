from django import forms
from .models import Comida
from django.forms import ModelForm

class GatoForm(forms.Form):
	SEXO_CHOISES = (
		('M',"Masculino"),
		('F',"Femenino")
	)


	name = forms.CharField(label='El nombre del gato:', max_length=100, widget=forms.TextInput(attrs={'class':'name'}))
	age = forms.IntegerField(label='Edad del perro')
	callejero = forms.BooleanField(label='Es callejero')
	sexo = forms.ChoiceField(choices=SEXO_CHOISES)
	comida = forms.ModelChoiceField(queryset=Comida.objects.all())

class ComidaForm(ModelForm):
	class meta:
		model =Comida
		#field = ["tipo","compra","caducidad"]
		exclude	= ["compra"]
		widget={
				'tipo':forms.TextInput(attrs={'class':'tipo'})
		}	
    
    