from django.shortcuts import render

# Create your views here.


def Companyinfo(request):
    return render( request, 'company_info/company_info.html')