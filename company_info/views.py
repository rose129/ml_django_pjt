import csv
from django.shortcuts import render

# Create your views here.



# views.py
def Companyinfo(request):
    return render( request, 'company_info/company_info.html')

