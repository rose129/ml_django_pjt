from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recruiting, name="recruiting"),
]
