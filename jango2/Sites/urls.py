from django.conf.urls import url
from .views import *
from .classed_views import Index, Register, Login

urlpatterns = [
    url(r'^$', index, name="sites-index"),
    url(r'^contacto/$',contacto, name="sites-contacto"),
    url(r'^registro/$',register, name="sites-register"),
    url(r'^login/$',login,name="sites-login"),
    url(r'^profile/$',profile,name="sites-profile"),
    url(r'^logout/$',logout, name="sites-logout"), 
    url(r'^index2/$',Index.as_view(), name="index2"),
    url(r'^registe2/$',Register.as_view(), name="register2"),
    url(r'^login2/$',Login.as_view(), name="sites-login"),
    url(r'^profile2/$',profile, name="profile2"),
]

