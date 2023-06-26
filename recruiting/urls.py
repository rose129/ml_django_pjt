from django.urls import path
from . import views

urlpatterns = [
    path('', views.recruiting, name="recruiting"),
    path('<int:pk>/', views.single_company_page),
    path('all_stack/', views.Stack, name="allstack"),
]
