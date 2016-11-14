from django.forms import ModelForm
from django.contrib.auth.models import User,AbstractUser
from django import forms
'''
    first_name
    last_name
    username
    password
    email
    is_active
    is_staff
    is_superuser
'''
class RegistrarForm(ModelForm):

    class Meta:
        model=User
        fields = ["first_name","last_name","username","password","email"]
        widgets = {
        "password":forms.PasswordInput(attrs={"type":"password"})

        }


class EntrarForm(forms.Form):
	username = forms.CharField(max_length=100,
		widget=forms.TextInput(attrs={'placeholder':"ingreasa user"}))

	password = forms.CharField(max_length=100,
		widget=forms.PasswordInput(attrs={"type":"password"}))


'''class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    cinta = models.CharField(max_length=30, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)'''