from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^hola/', index, name="gatos-index"),
    url(r'^saludo/(?P<saludo>\w+)',saludo),
    url(r'^suma/', suma),
    url(r'^resta/(?P<x>[0-9]+)/(?P<y>[0-9]+)', resta),
    url(r'^nuevo/', nuevo , name="gatos-nuevo"),
    url(r'^comida/', comida , name="gatos-comida"),

]
