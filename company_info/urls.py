from django.urls import path
from . import views

# urls.py

urlpatterns = [
    path('csv-to-html/', views.csv_to_html, name='csv_to_html'),
]