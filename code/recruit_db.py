import requests as req
import pymysql
import os
import csv
from mydb__env import *

f = open('data/all_recruit_clean_v3.csv','r', encoding='UTF8')

recruit = csv.reader(f)
next(recruit)
 
# 기업명,직무,회사소개,주요업무,자격요건,스택,우대사항,복리후생,회사주소
total = []
for re in recruit:
    data = []
    # 기업명
    r1 = re[0]
    # print(re[0])
    # 직무
    r2 = re[1]
    # 회사소개
    r3 = re[2]
    # 주요업무
    r4 = re[3]
    # 자격요건
    r5 = re[4]
    # 스택
    r6 = re[5]
    # 우대사항
    r7 = re[6]
    # 복리후생
    r8 = re[7]
    # 회사주소
    r9 = re[8]

    data.append(r1)
    data.append(r2)
    data.append(r3)
    data.append(r4)
    data.append(r5)
    data.append(r6)
    data.append(r7)
    data.append(r8)
    data.append(r9)

    total.append(data)

print(total)

f.close()

def accessDB(total):
    
    # DB연결
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
    # 커서생성
    cur = conn.cursor()

    # daum_movies 테이블이 존재하면 삭제하기
    sql = "DROP TABLE IF EXISTS recruting_info"
    cur.execute(sql)

    # 테이블생성
    # 기업명,직무,회사소개,주요업무,자격요건,스택,우대사항,복리후생,회사주소
    sql = """
    CREATE TABLE IF NOT EXISTS recruting_info (
        company_name VARCHAR(100) NOT NULL,
        job VARCHAR(100) NOT NULL,
        company_intro TEXT NOT NULL,
        main_duties TEXT NOT NULL,
        requirments TEXT NOT NULL,
        stack TEXT NOT NULL,
        desirable_skills TEXT NOT NULL,
        employee_benefits TEXT NOT NULL,
        address VARCHAR(100)  NOT NULL
    )

    """
    cur.execute(sql)
    cur.executemany("""
    INSERT INTO recruting_info(company_name, job, company_intro, main_duties, requirments, stack, desirable_skills, employee_benefits, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, total)

    # db 적용 
    conn.commit()

    result_data = cur.fetchall()

    # DB닫기
    conn.close()
    return result_data

accessDB(total)
