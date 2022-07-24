from django.urls import path
#O . representa nesse mesmo diretório
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("v1/", views.v1, name="View 1"),
]
