import csv
from django.shortcuts import render
from .models import Company_list
# Create your views here.


def company_array(request):

    array = Company_list.objects.all()
    context = {
        'array' : array
    }
    

    return render( request, 'company_info/company_info.html', context)


# views.py

# def csv_to_html(request):
#     with open('파일명.csv', 'r') as file:
#         reader = csv.reader(file)
#         data = list(reader)
    
#     return render(request, 'table.html', {'data': data})   