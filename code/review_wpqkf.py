import csv
from mydb__env import *
import pymysql
from emoji import core
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruit_pjt.settings")
django.setup()

from company_info.models import Company_list

f = open('data/company_list_0628.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr)
# com_png 0
# com_rank 1
# com_name 2
# com_in 3
# industry_field 4
# workforce 5
# com_detail_type 6
# est_date 7
# capital 8
# sales 9
# ceo 10
# initial_salary 11
# main_business 12
# insurance 13
# website 14
# com_detail_address 15
# subsidiary 16

for i in rdr:
    print(i)
    i[5] = i[5].replace(',','')
    # print(i[5])
    if '(' in i[5]:
        # print(i[5])
        i[5] = i[5].split(' ')
        i[5] = i[5][0]
        # print(i[5])

    # print(i[16])

    Company_list.objects.create(
        com_name = i[2],
        com_png = i[0],
        com_rank = i[1],
        com_in = i[3],
        ceo = i[10],
        est_date = i[7],
        workforce = i[5],
        industry_field = i[4],
        website = i[14],
        com_detail_type = i[6],
        capital = i[8],
        sales = i[9],
        initial_salary = i[11],
        main_business = i[12],
        insurance = i[13],
        com_detail_address = i[15],
        subsidiary = i[16]
    )
