import os
import django
import pymysql
import csv
from mydb__env import *
# from recruiting.models import Recruiting_list

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruit_pjt.settings")
django.setup()

from company_info.models import Ml_final 

f = open('data/ml_final.csv', 'r',encoding='utf-8')
ml = csv.reader(f)
next(ml)

for i in ml:
    Ml_final.objects.create(
        com_name = i[0],
        rating = i[1]
    )

