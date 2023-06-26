from django.shortcuts import render
import pymysql
from .models import Recruiting_list

# Create your views here.

def recruiting(request):
    aa = Recruiting_list.objects.all().order_by('-pk')
    # print(aa[0])
    context = {
        'aa' : aa
    }

    return render( request, 'recruiting/recruiting.html', context)

def Stack(request):
    return render( request, 'recruiting/all_stack.html')


def single_company_page(request, pk):
    post = Recruiting_list.objects.get(pk=pk)
    detail_company = {
        'post' : post
    }

    return render(request,'recruiting/recruit_detail.html',  detail_company)






