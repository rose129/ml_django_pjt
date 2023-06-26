from django.urls import path
from . import views

# urls.py

urlpatterns = [
    path('', views.company_array, name='companyinfo'),
]