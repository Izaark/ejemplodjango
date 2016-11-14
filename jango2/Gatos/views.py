from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.views.generic  import TemplateView, ListView, CreateView, UpdateView, DeleteView,DetailView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import Gato,Comida
from .forms import GatoForm,ComidaForm
import random

class GatoTemplateView(TemplateView):
	template_name = "about.html"

class GatoListView(ListView):
	model = Gato
	context_object_name = "gatos"
	template_name = 'Gatos/gato_list.html'

class GatoDetailView(DetailView):
	model = Gato
	template_name = 'Gatos/gato_detail.html'
	template_name = 'solicitud_list.html'

class GatoDeleteView(DeleteView):
	model = Gato
	template_name = 'Gatos/gato_confirm_delete.html'
	success_url = reverse_lazy('Gatos:lista-gatos')

class GatoUpdateView(UpdateView):
	model = Gato
	fields = ["name", "age"]
	success_url = reverse_lazy('Gatos:lista-gatos')

class GatoCreateView(CreateView):
	model = Gato
	fields = ["name","age","callejero", "sexo", "comida"]
	success_url = reverse_lazy('Gatos:lista-gatos')

def index(request):
	gatos = Gato.objects.all().order_by("-name")#filter(name="garfield")| Gato.objects.filter(callejero=False)
	cachorros = gatos.filter(age__lte = 10)
	comidas = 	Comida.objects.all()

	return render(request,"Gatos.html",{"gatos":gatos,"comidas":comidas,"cachorros":cachorros})

def saludo(request,saludo):
	return HttpResponse("Soy un gato y me llamo "+ saludo)
def suma(request):
	n1 = random.randint(1,4)
	n2 = random.randint(5,9)
	s = n1 +n2
	return HttpResponse(s)
def resta(request,x,y):
	parte1 = int(x)
	parte2 = int(y)

	resta = parte1 - parte2
	return HttpResponse(resta)
def nuevo(request):

	if request.method == "POST":
		form = GatoForm(request.POST)

		if form.is_valid():
			gato = Gato(name=form.cleaned_data["name"],age=form.cleaned_data["age"])
			gato.name = form.cleaned_data["name"]
			gato.age = form.cleaned_data["age"]
			gato.sexo = form.cleaned_data["sexo"]
			gato.callejero = form.cleaned_data["callejero"]
			gato.comida = form.cleaned_data["comida"]

			gato.save()
	
			return redirect('gatos-index')
		return redirect('sites-index')

	else:
		form = GatoForm()

		return render(request,'nuevo_gato.html',{"form":form})

def comida(request):

	if request.method == "POST":
		comida = ComidaForm(request.POST)

		if comida.is_valid():

			comida.save()
			
		return redirect('gatos-index')
	else:

		form = ComidaForm()
		return render(request,'nueva_comida.html',{"form":form})

