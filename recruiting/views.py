from django.shortcuts import render


# Create your views here.

def Recruiting(request):
    return render( request, 'recruiting/recruiting.html')