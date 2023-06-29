import csv
from django.shortcuts import render
from .models import Company_list
from .models import Ml_final
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.


def company_array(request):

    array = Company_list.objects.all().order_by('pk')
    paginator = Paginator(array, 48)  # 한 페이지에 10개씩 보여줌
    page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
    page_obj = paginator.get_page(page_number)  # 현재 페이지의 객체 가져오기
    
    context = {
        'page_obj': page_obj
    }

    return render( request, 'company_info/company_info.html', context)

def company_info_detail(request, com_name):
    # info = CompanyDetail.objects.get(pk=pk)
    info = Company_list.objects.get(com_name=com_name)
    try:
        ml_info = Ml_final.objects.get(com_name=com_name)  # Ml_final 모델에서 com_name 필드를 기준으로 해당 회사의 정보 가져오기
    except Ml_final.DoesNotExist:
        ml_info = f"기업리뷰 미제공 기업입니다." 
    
    info_detail = {
        'info': info,
        'ml_info': ml_info
    }
    return render(request, 'company_info/company_info_detail.html', info_detail)

