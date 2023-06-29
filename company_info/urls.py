from django.urls import path
from . import views

# urls.py

urlpatterns = [
    path('', views.company_array, name='companyinfo'),
    path('<str:com_name>/', views.company_info_detail)
    # path('<str:com_name>/', views.company_info_detail)
]