from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pages/', views.page, name="page"),
   
]
