from django.urls import path
from . import views

urlpatterns = [
    path('', views.recruiting, name="recruiting"),
    path('<int:pk>/', views.single_company_page),
    path('all_stack/', views.Stack, name="allstack"),
    path('all_stack_m1/', views.StackSub, name="allstack"),
    path('all_stack_m2/', views.StackSub2, name="allstack"),
    path('all_stack_m3/', views.StackSub3, name="allstack"),
]
