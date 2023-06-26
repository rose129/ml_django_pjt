import csv
from django.shortcuts import render

# Create your views here.


def Companyinfo(request):
    return render( request, 'company_info/company_info.html')


# views.py

# def csv_to_html(request):
#     with open('파일명.csv', 'r') as file:
#         reader = csv.reader(file)
#         data = list(reader)
    
#     return render(request, 'table.html', {'data': data})   