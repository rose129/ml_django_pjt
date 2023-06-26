import os
import django
import pymysql
from mydb_env import *
# from recruiting.models import Recruiting_list
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruit_pjt.settings")
django.setup()

from recruiting.models import Recruiting_list 

# DB연결
conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
# 커서생성
cur = conn.cursor()

sql = """

SELECT * FROM recruting_info

"""



cur.execute(sql)

# result_data = cur.fetchall()
result_data = cur.fetchall()

for i in result_data:
    # print(i[0])
    Recruiting_list.objects.create(
        company_name = i[0],
        job = i[1],
        company_intro = i[2],
        main_duties = i[3],
        requirments = i[4],
        stack = i[5],
        desirable_skills = i[6],
        employee_benefits = i[7],
        address = i[8]
    )



# print(result_data)

# DB닫기
conn.close()

