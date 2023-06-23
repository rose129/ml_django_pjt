from django.shortcuts import render


# Create your views here.

def Recruiting(request):
    return render( request, 'recruiting/recruiting.html')

def Stack(request):
    return render( request, 'recruiting/all_stack.html')