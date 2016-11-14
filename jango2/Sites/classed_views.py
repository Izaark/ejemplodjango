from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from .functions import authenticated
from django.contrib.auth import logout as lg

class Index(View):
	
	template = "index.html"

	def get(self,request,*args, **kargs):
		batch = "Batch 12 este es otro view"
		cinta = "<p>Negra</p>"
		lista = ["cuchufleto", "gertrudis","garfield", "peje", "filomeno", "casimiro"]
		datos = {"name":"fido", "raza": "labrador", "edad": "4"}
		

		return render(request, self.template,{
			"variable":batch, 
			"cinta":cinta, "lista":lista,
			"datos" : datos,
		})

	def post(self, request, *args, **kargs):
		pass 

class Register(View):
	form = RegisterForm()
	template = "registro.html"

	def get(self,request,*args, **kargs):
		return render(request, self.template, {"form":self.form})

	def post(self,request, *args, **kargs):
		
		self.form = RegisterForm(request.POST)
		if (self.form.is_valid()):
			User.objects.create_user(
				first_name=self.form.cleaned_data["first_name"],
				last_name=self.form.cleaned_data["last_name"],
				username=self.form.cleaned_data["username"],
				password=self.form.cleaned_data["password"],
				email=self.form.cleaned_data["email"])

			return redirect("index2")

class Login(View):
	form = LoginForm()
	template = "login.html"
	def get(self,request,*args, **kargs):
		return render(request, self.template, {"form":self.form})


	def post(self,request,*args, **kargs):
		self.form = LoginForm(request.POST)

		if self.form.is_valid():
			auth = authenticated(
				request,
				self.form.cleaned_data["username"],
				self.form.cleaned_data["password"]
				)

			log = 'profile2' if auth else 'sites-login'

			return redirect(log)

class Profile(View):

	def get(self,request,*args, **kargs):
		template = "profile.html"
		if request.user.is_authenticated():

			user = User.objects.get(id=request.user.id)

			return render(request,self.template,{"user":user})


		else:
			return redirect('sites-login')
	# def put()
	# def delete
	# def dispatch()
	# def head()
	# def options()
	# def update()
