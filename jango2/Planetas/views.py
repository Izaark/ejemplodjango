from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from .models import Planeta,Galaxia,Habitantes
def index(request):
	planetas = Planeta.objects.all().order_by("-name")
	habitantes = Habitantes.objects.all().order_by("-species")
	galaxia = Galaxia.objects.all()
	return render(request,"planetas.html",{"planetas":planetas,"habitantes":habitantes,"galaxias":galaxia})