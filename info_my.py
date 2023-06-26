import os
import django
import pymysql
from mydb_env import *
import csv
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruit_pjt.settings")
django.setup()

from company_info.models import Company_list

f = open('data/startup_300.csv', 'r',encoding='utf-8')
rdr = csv.reader(f)
next(rdr)

for i in rdr:
    # print(i[3])
    Company_list.objects.create(
        com_png = i[0],
        com_rank = i[1],
        com_name = i[2],
        com_in = i[3]
    )

    





