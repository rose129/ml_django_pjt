from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import pymysql
from .models import Recruiting_list
from django.core.paginator import Paginator

# Create your views here.

def recruiting(request):
    aa = Recruiting_list.objects.all().order_by('-pk')
    # print(aa[0])
    all_items = Recruiting_list.objects.all()
    paginator = Paginator(all_items, 30)  # Change the number as per your requirement
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    paginate_by = 10
    context = {
        'page_obj' : page_obj
    }
    return render( request, 'recruiting/recruiting.html', context)



def Stack(request):
    return render( request, 'recruiting/all_stack.html')

def StackSub(request):
    return render( request, 'recruiting/all_stack_m1.html')
def StackSub2(request):
    return render( request, 'recruiting/all_stack_m2.html')
def StackSub3(request):
    return render( request, 'recruiting/all_stack_m3.html')


def single_company_page(request, pk):
    post = Recruiting_list.objects.get(pk=pk)
    # post.image = get_random_image_url()
    detail_company = {
        'post' : post
    }

    return render(request,'recruiting/recruit_detail.html',  detail_company)




